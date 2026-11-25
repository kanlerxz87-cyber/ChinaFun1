"""
Cluster proximity model — reproducible, no invented values.

Method
------
1. Take only restaurants with coordinates published by the MICHELIN Guide itself
   (guide.michelin.com restaurant pages embed a lat/lon in the "Maps" link).
2. Take only hotels with coordinates from OpenStreetMap (via Photon geocoder).
3. Compute great-circle (haversine) distance hotel -> restaurant.
4. Convert to a modelled door-to-door transit estimate using a single declared
   assumption (see TRANSIT_MODEL). This is an ESTIMATE, not a Google/AMap
   routing result, and is labelled as such everywhere it appears.
5. Count restaurants inside 1 hour, weighted by star level.

Run:  python3 tools/proximity_model.py
"""

import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Declared model constants -------------------------------------------------
TRANSIT_MODEL = {
    "walk_to_station_min": 6,          # assumed walk from hotel to metro entrance
    "avg_metro_speed_kmh": 30.0,       # Shanghai Metro Metro average incl. stops (assumed)
    "transfer_penalty_min": 6,         # assumed penalty if a change of line is needed
    "transfer_distance_threshold_km": 4.0,  # >4 km straight-line assumed to need 1 transfer
    "street_detour_factor": 1.25,      # straight-line -> rail-path factor (assumed)
    "one_hour_budget_min": 60,
}

# Restaurants with MICHELIN-published coordinates (lat, lon) and star level.
# Source for every coordinate: the restaurant's own page on guide.michelin.com
# (the "Maps" link contains ll=<lat>,<lon> for the venue pin).
RESTAURANTS = [
    {"id": "R01", "name": "Taian Table", "stars": 3, "lat": 31.22205,  "lon": 121.43291},
    {"id": "R02", "name": "8 ½ Otto e Mezzo Bombana", "stars": 2, "lat": 31.242347, "lon": 121.487921},
    {"id": "R03", "name": "Fu He Hui", "stars": 2, "lat": 31.21875, "lon": 121.42979},
    {"id": "R05", "name": "T'ang Court", "stars": 2, "lat": 31.2217958, "lon": 121.4742971},
    {"id": "R07", "name": "Ji Pin Court", "stars": 2, "lat": 31.20628, "lon": 121.44867},
]

# Hotels with OSM-verified coordinates.
HOTELS = [
    {"id": "H01", "name": "Radisson Blu Hotel Shanghai New World", "lat": 31.2364079, "lon": 121.4684659},
    {"id": "H02", "name": "Grand Central Hotel Shanghai", "lat": 31.2370564, "lon": 121.4769667},
    {"id": "H04", "name": "The Langham, Shanghai, Xintiandi", "lat": 31.2237257, "lon": 121.4698926},
    {"id": "H05", "name": "Waldorf Astoria Shanghai on the Bund", "lat": 31.2357915, "lon": 121.4865459},
    {"id": "H06", "name": "The Peninsula Shanghai", "lat": 31.2432569, "lon": 121.4847583},
]


def haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def modelled_transit_minutes(dist_km):
    rail_km = dist_km * TRANSIT_MODEL["street_detour_factor"]
    ride = rail_km / TRANSIT_MODEL["avg_metro_speed_kmh"] * 60
    transfers = 1 if dist_km > TRANSIT_MODEL["transfer_distance_threshold_km"] else 0
    return (
        TRANSIT_MODEL["walk_to_station_min"]
        + ride
        + transfers * TRANSIT_MODEL["transfer_penalty_min"]
    ), transfers


def main():
    out = []
    for h in HOTELS:
        rows = []
        for r in RESTAURANTS:
            d = haversine_km(h["lat"], h["lon"], r["lat"], r["lon"])
            mins, transfers = modelled_transit_minutes(d)
            rows.append(
                {
                    "restaurant_id": r["id"],
                    "restaurant": r["name"],
                    "stars": r["stars"],
                    "distance_km": round(d, 2),
                    "modelled_transit_min": round(mins),
                    "assumed_transfers": transfers,
                    "within_1h": mins <= TRANSIT_MODEL["one_hour_budget_min"],
                }
            )
        within = [x for x in rows if x["within_1h"]]
        out.append(
            {
                "hotel_id": h["id"],
                "hotel": h["name"],
                "restaurant_count_1h": len(within),
                "star_weight_1h": sum(x["stars"] for x in within),
                "mean_transit_min_all": round(sum(x["modelled_transit_min"] for x in rows) / len(rows), 1),
                "mean_transit_min_1h": round(sum(x["modelled_transit_min"] for x in within) / len(within), 1) if within else None,
                "nearest": min(rows, key=lambda x: x["distance_km"])["restaurant"],
                "nearest_distance_km": min(x["distance_km"] for x in rows),
                "rows": sorted(rows, key=lambda x: x["distance_km"]),
            }
        )
    # Primary: total MICHELIN star weight reachable within 1 hour.
    # Secondary: number of starred restaurants within 1 hour.
    # Tie-break: lower mean modelled transit time across the whole verified set.
    out.sort(
        key=lambda x: (
            -x["star_weight_1h"],
            -x["restaurant_count_1h"],
            x["mean_transit_min_all"],
        )
    )
    for i, h in enumerate(out, 1):
        h["rank"] = i

    result = {"model": TRANSIT_MODEL, "results": out}
    dest = os.path.join(ROOT, "data", "hotel-ranking.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

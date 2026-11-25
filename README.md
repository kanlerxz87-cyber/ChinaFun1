# China 2027 — Shanghai couple's trip plan

A research-backed trip planner for **2 adults, 15–22 February 2027** (within the wider
2027-02-15 → 2027-03-23 window). Built to answer one question honestly: what can actually be
verified about a Shanghai trip, and what can't?

Live site: **https://kanlerxz87-cyber.github.io/ChinaFun1/**

## Pages

| Page | What it answers |
|------|-----------------|
| `index.html` | Executive summary, headline recommendation, price windows |
| `itinerary.html` | Day-by-day plan built around verified opening hours |
| `hotels.html` | 7 hotels compared on verified 7-night totals, beds, bathrooms |
| `restaurants.html` | 50 starred venues, shortlist of 14, star vs Guide distinction |
| `activities.html` | Hours, closures and official links for each activity |
| `ranking.html` | Hotels ranked by MICHELIN access, with the method disclosed |
| `questions.html` | 14 open questions, each with a way to resolve it |
| `suggestions.html` | 10 proposals awaiting a decision — none implemented |
| `flagged.html` | Irregularities, conflicts and dead ends |
| `sources.html` | Every source, what it proved, what it couldn't |

## Data

- `data/hotels.json` — 7 hotels, 7-night totals, bed/bathroom specs, price ladder
- `data/michelin-restaurants.json` — 14 shortlisted restaurants with star level and source
- `data/activities.json` — activities with hours, exceptions, official and social links
- `data/price-windows.json` — 5 date windows sampled for the best time to book
- `data/hotel-ranking.json` — proximity model output

## Model

```bash
python3 tools/proximity_model.py
```

Standard library only. Applies declared constants (walk 6 min, 30 km/h rail, ×1.25 detour, +6 min
line change beyond 4 km) to MICHELIN-published restaurant coordinates and OpenStreetMap hotel
coordinates, then writes `data/hotel-ranking.json`.

**These are modelled estimates, not routed transit times** — no routing API was reachable. The
disclosed model ranks hotels reliably against each other; it does not predict a single journey well.

## Ground rules this repo follows

1. Never infer a value. If an official source does not state it, the cell is blank and flagged.
2. Cite an official source for every row, or mark it unverified.
3. Distinguish *MICHELIN Guide listed* from *currently holds a star*.
4. Show hotel costs as a 7-night total on real dates, and restaurant costs as a total for 2.
5. Publish what could **not** be found — see `flagged.html` and `questions.html`.

## What is still missing

No restaurant publishes a menu price; 10 of 12 shortlist venues publish no hours; the Pullman
Jing'an and Capella could not be geocoded, so the ranking excludes the cheapest option. Details and
resolutions: `questions.html`.

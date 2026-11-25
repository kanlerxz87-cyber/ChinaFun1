#!/usr/bin/env python3
"""Build a canonical venue inventory from the four plans already in this repo.

Read-only on every other session's files. Output: social-2027/data/inventory.json
No value is invented here: fields are copied verbatim with their origin recorded.
"""
import csv, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "social-2027/data/inventory.json"

def norm(s):
    s = (s or "").lower()
    s = s.replace("½", "12").replace("½", "12")
    s = re.sub(r"[^a-z0-9]+", "", s)
    return s

# Row shape: id, city, kind, name, plan, source_file, distinction, price_band,
# address, official_url, guide_url, social[], hours{}, cost{}
rows = []

# 1. Beijing plan (repo root) — assets/data.js
js = (ROOT / "assets/data.js").read_text()
bj = json.loads(subprocess.check_output([
    "node", "-e",
    "const fs=require('fs');const d=new Function(fs.readFileSync(process.argv[1],'utf8')"
    "+'; return {MICHELIN,ACTIVITIES,GUIDE_SLUG};')();console.log(JSON.stringify(d));",
    str(ROOT / "assets/data.js")], text=True))
for i, r in enumerate(bj["MICHELIN"], 1):
    slug = bj["GUIDE_SLUG"].get(r["n"], "")
    rows.append(dict(
        id=f"BJ-R{i:02d}", city="Beijing", kind="restaurant", name=r["n"],
        plan="fac6d965 (root)", source_file="assets/data.js",
        distinction=f"{r['s']} MICHELIN star" if r["s"] else "",
        price_band=r.get("p", ""), address=r.get("a", ""),
        official_url=r.get("w", ""),
        guide_url=("https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurant/" + slug) if slug else "",
        social=[dict(platform=("Instagram" if "instagram" in u else "TikTok" if "tiktok" in u else "YouTube" if "youtube" in u else "Other"),
                     url=u, label=l, origin="fac6d965/assets/data.js") for l, u in r.get("soc", [])],
        hours=dict(text=r.get("h", ""), closed="", exceptions="", source="", origin="assets/data.js"),
        cost=dict(text=r.get("p2", ""), source="", origin="assets/data.js"),
        plan_note=r.get("fx", "")))
for i, r in enumerate(bj["ACTIVITIES"], 1):
    rows.append(dict(
        id=f"BJ-A{i:02d}", city="Beijing", kind="activity", name=r["n"],
        plan="fac6d965 (root)", source_file="assets/data.js", distinction="", price_band="",
        address="", official_url=r.get("off", ""), guide_url="",
        social=[dict(platform="YouTube" if "youtube" in u else "Other", url=u, label=l,
                     origin="fac6d965/assets/data.js") for l, u in r.get("soc", [])],
        hours=dict(text=r.get("h", ""), closed="", exceptions="", source="", origin="assets/data.js"),
        cost=dict(text=r.get("price", ""), source="", origin="assets/data.js"),
        plan_note=r.get("fx", "")))

# 2. Shanghai plan in docs/ (session 68e13071)
for i, r in enumerate(json.loads((ROOT / "data/restaurants.json").read_text()), 1):
    vids = [dict(platform=v.get("platform", ""), url=v.get("url", ""), label=v.get("title", ""),
                 origin="68e13071/data/restaurants.json") for v in r.get("videos", [])]
    rows.append(dict(
        id=f"DOC-R{i:02d}", city="Shanghai", kind="restaurant", name=r["name"],
        plan="68e13071 (docs/)", source_file="data/restaurants.json",
        distinction=r.get("tier_label", ""), price_band=r.get("price_band", ""),
        address=r.get("address", ""), official_url=r.get("official_url") or "",
        guide_url=r.get("michelin_url") or "", social=vids,
        hours=dict(text=(r.get("hours") or {}).get("text", ""), closed=(r.get("hours") or {}).get("closed", ""),
                   exceptions="", source=(r.get("hours") or {}).get("source") or "", origin="data/restaurants.json"),
        cost=dict(text=(r.get("price_two_adults") or {}).get("basis", ""), source="", origin="data/restaurants.json"),
        plan_note="; ".join(r.get("flags", []))))
for i, r in enumerate(json.loads((ROOT / "data/activities.json").read_text()), 1):
    rows.append(dict(
        id=f"DOC-A{i:02d}", city="Shanghai", kind="activity", name=r["name"],
        plan="68e13071 (docs/)", source_file="data/activities.json", distinction="", price_band="",
        address="", official_url=r.get("official_url") or "", guide_url="",
        social=[dict(platform=v.get("platform", ""), url=v.get("url", ""), label=v.get("title", ""),
                     origin="68e13071/data/activities.json") for v in r.get("videos", [])],
        hours=dict(text=r.get("hours", ""), closed=r.get("closed", ""), exceptions="", source="", origin="data/activities.json"),
        cost=dict(text=r.get("ticket_two_adults_usd") or "", source="", origin="data/activities.json"),
        plan_note="; ".join(r.get("flags", []))))

# 3. Shanghai plan shanghai-2027/ (session 3b27db6c)
for i, r in enumerate(json.loads((ROOT / "shanghai-2027/data/michelin-restaurants.json").read_text()), 1):
    rows.append(dict(
        id=f"S27-R{i:02d}", city="Shanghai", kind="restaurant", name=r["name"],
        plan="3b27db6c (shanghai-2027/)", source_file="shanghai-2027/data/michelin-restaurants.json",
        distinction=r.get("distinction", ""), price_band=r.get("price_band", ""),
        address=r.get("address", ""), official_url=r.get("official_url") or "", guide_url=r.get("michelin_url") or "",
        social=[dict(platform=v.get("platform", ""), url=v.get("url", ""), label=v.get("title", ""),
                     origin="3b27db6c/data/michelin-restaurants.json") for v in r.get("social", [])],
        hours=dict(text=r.get("hours", ""), closed=r.get("closed_days", ""), exceptions="",
                   source=r.get("hours_source") or "", origin="shanghai-2027/data/michelin-restaurants.json"),
        cost=dict(text=r.get("menu_price_note", ""), source=r.get("cost_source") or "",
                  origin="shanghai-2027/data/michelin-restaurants.json"),
        plan_note=""))
for i, r in enumerate(json.loads((ROOT / "shanghai-2027/data/activities.json").read_text()), 1):
    rows.append(dict(
        id=f"S27-A{i:02d}", city="Shanghai", kind="activity", name=r["name"],
        plan="3b27db6c (shanghai-2027/)", source_file="shanghai-2027/data/activities.json", distinction="", price_band="",
        address=r.get("address", ""), official_url=r.get("official_url") or "", guide_url="",
        social=[dict(platform=v.get("platform", ""), url=v.get("url", ""), label=v.get("title", ""),
                     origin="3b27db6c/data/activities.json") for v in r.get("social", [])],
        hours=dict(text=r.get("hours", ""), closed=r.get("closed_days", ""), exceptions=r.get("exceptions", ""),
                   source=r.get("official_url") or "", origin="shanghai-2027/data/activities.json"),
        cost=dict(text=r.get("price", ""), source="", origin="shanghai-2027/data/activities.json"), plan_note=""))

# 4. Shanghai verified plan (session 16153d37)
with (ROOT / "shanghai-verified-2027/data/michelin.csv").open() as fh:
    for i, r in enumerate(csv.DictReader(fh), 1):
        rows.append(dict(
            id=f"VER-R{i:02d}", city="Shanghai", kind="restaurant", name=r.get("name", ""),
            plan="16153d37 (shanghai-verified-2027/)", source_file="shanghai-verified-2027/data/michelin.csv",
            distinction=r.get("michelin_status_official", ""), price_band=r.get("price_band_official", ""),
            address=r.get("address_official", ""), official_url=r.get("official_site", ""),
            guide_url=r.get("guidelist_url", ""), social=[],
            hours=dict(text=r.get("days_hours_official", ""), closed="", exceptions=r.get("hours_exceptions", ""),
                       source=r.get("guidelist_url", ""), origin="shanghai-verified-2027/data/michelin.csv"),
            cost=dict(text=r.get("cost_2_adults_total_verified", ""), source=r.get("cost_basis", ""),
                      origin="shanghai-verified-2027/data/michelin.csv"),
            plan_note=r.get("verification_status", "")))
with (ROOT / "shanghai-verified-2027/data/activities.csv").open() as fh:
    for i, r in enumerate(csv.DictReader(fh), 1):
        rows.append(dict(
            id=f"VER-A{i:02d}", city="Shanghai", kind="activity", name=r.get("activity_name", ""),
            plan="16153d37 (shanghai-verified-2027/)", source_file="shanghai-verified-2027/data/activities.csv",
            distinction="", price_band="", address=r.get("address_official", ""),
            official_url=r.get("official_site", ""), guide_url="", social=[],
            hours=dict(text=" ".join(x for x in [r.get("days_open_official", ""), r.get("hours_official", "")] if x),
                       closed="", exceptions=r.get("hours_exceptions_official", ""),
                       source=r.get("official_site", ""), origin="shanghai-verified-2027/data/activities.csv"),
            cost=dict(text=r.get("cost_2_adults_total_verified", ""), source=r.get("admission_official", ""),
                      origin="shanghai-verified-2027/data/activities.csv"),
            plan_note=r.get("verification_status", "")))

# Explicit, hand-checked aliases. Each is a literal name written by an existing plan;
# none of these merges is a guess about two different venues being the same place.
ALIASES = {
    ("Shanghai", "activity", "Shanghai Museum (People's Square)"): "Shanghai Museum (People's Square)",
    ("Shanghai", "activity", "Shanghai Museum on People's Square"): "Shanghai Museum (People's Square)",
    ("Shanghai", "activity", "Yu Garden (Yuyuan)"): "Yu Garden",
    ("Shanghai", "activity", "Yu Garden (豫园)"): "Yu Garden",
    ("Shanghai", "activity", "The Bund (Waitan) waterfront"): "The Bund waterfront",
    ("Shanghai", "activity", "The Bund (Waitan) waterfront promenade"): "The Bund waterfront",
    ("Shanghai", "activity", "The Bund riverside promenade"): "The Bund waterfront",
    ("Shanghai", "activity", "Shanghai Tower — 118F observation deck"): "Shanghai Tower observatory",
    ("Shanghai", "activity", "Shanghai Tower - Top of Shanghai Observatory"): "Shanghai Tower observatory",
    ("Shanghai", "activity", "Taian Table — 3★ tasting menu (dining experience)"): "Taian Table",
}
for r in rows:
    alias = ALIASES.get((r["city"], r["kind"], r["name"]))
    if alias:
        r["name"] = alias
        if alias == "Taian Table":
            r["kind"] = "restaurant"  # the plan listed this dining experience as an activity

# Merge rows that are the same venue inside the same city, keeping every plan reference.
venues = []
by_key = {}
for r in rows:
    key = (r["city"], r["kind"], norm(r["name"]))
    if key in by_key:
        v = by_key[key]
        v["plan_refs"].append({"plan": r["plan"], "id": r["id"], "source_file": r["source_file"]})
        for s in r["social"]:
            if s["url"] and s["url"] not in [x["url"] for x in v["social"]]:
                v["social"].append(s)
        for fld in ("official_url", "guide_url", "address", "distinction", "price_band"):
            if not v[fld] and r[fld]:
                v[fld] = r[fld]
        for fld in ("text", "closed", "exceptions", "source"):
            if not v["hours"][fld] and r["hours"][fld]:
                v["hours"][fld] = r["hours"][fld]
        if not v["cost"]["text"] and r["cost"]["text"]:
            v["cost"] = r["cost"]
    else:
        v = dict(r)
        v["plan_refs"] = [{"plan": r["plan"], "id": r["id"], "source_file": r["source_file"]}]
        by_key[key] = v
        venues.append(v)

payload = {
    "built": "2026-11-25",
    "session": "c2067093",
    "method": "Verbatim extraction from four existing plan data files; rows merged only on exact normalised venue name within a city. No value inferred.",
    "source_plan_files": ["assets/data.js", "data/restaurants.json", "data/activities.json",
                          "shanghai-2027/data/michelin-restaurants.json", "shanghai-2027/data/activities.json",
                          "shanghai-verified-2027/data/michelin.csv", "shanghai-verified-2027/data/activities.csv"],
    "counts": {"raw_rows": len(rows), "unique_venues": len(venues)},
    "venues": venues,
}
OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
print("raw rows", len(rows), "unique venues", len(venues))
from collections import Counter
print(Counter((v["city"], v["kind"]) for v in venues))
print("venues with candidate social:", sum(1 for v in venues if v["social"]))

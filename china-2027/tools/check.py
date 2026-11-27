#!/usr/bin/env python3
"""Automated QA & integrity validator for china-2027/ (Python 3 stdlib only)."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

EXPECTED_PAGES = [
    "index.html",
    "hotels.html",
    "restaurants.html",
    "activities.html",
    "itineraries.html",
    "questions.html",
    "suggestions.html",
    "flagged.html",
    "sources.html",
]

BANNED_URL_FRAGMENTS = [
    "example.com",
    "results?search_query=",
    "Sy0Df7KVfJk",  # private YouTube video audited in repo root
]


class LinkAndMetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.external_assets: list[str] = []
        self.has_viewport = False
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = dict(attrs)
        if d.get("id"):
            self.ids.add(d["id"])
        if tag == "meta" and d.get("name") == "viewport":
            self.has_viewport = True
        if tag == "a" and d.get("href"):
            self.links.append(d["href"])
        if tag == "link" and d.get("href"):
            href = d["href"]
            self.links.append(href)
            if href.startswith("http"):
                self.external_assets.append(href)
        if tag == "script" and d.get("src"):
            src = d["src"]
            self.links.append(src)
            if src.startswith("http"):
                self.external_assets.append(src)


def check_url(url: str, ctx: str, errors: list[str]) -> None:
    if not url:
        return
    if not url.startswith("https://"):
        errors.append(f"{ctx}: external URL must use https:// -> {url}")
    for bad in BANNED_URL_FRAGMENTS:
        if bad in url:
            errors.append(f"{ctx}: banned/invalid URL fragment '{bad}' -> {url}")


def main() -> int:
    errors: list[str] = []

    # 1. Load all JSON files
    data_files = [
        "meta.json",
        "hotels.json",
        "restaurants.json",
        "activities.json",
        "itineraries.json",
        "audit_and_planning.json",
        "sources.json",
    ]
    loaded = {}
    for df in data_files:
        p = DATA_DIR / df
        if not p.exists():
            errors.append(f"Missing required data file: {p}")
            continue
        try:
            loaded[df] = json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid JSON in {df}: {exc}")

    if errors:
        for err in errors:
            print("FAIL:", err)
        return 1

    # 2. Validate Beijing 33/33 MICHELIN invariants + all restaurant rows
    rests = loaded["restaurants.json"]["items"]
    seen_rids: set[str] = set()
    bj_starred = []
    for r in rests:
        rid = r["id"]
        if rid in seen_rids:
            errors.append(f"Duplicate restaurant ID: {rid}")
        seen_rids.add(rid)
        check_url(r.get("michelin_url", ""), f"restaurant {rid} michelin_url", errors)
        check_url(r.get("official_url", ""), f"restaurant {rid} official_url", errors)
        check_url(r.get("cost_source", ""), f"restaurant {rid} cost_source", errors)
        for s in r.get("social", []):
            check_url(s.get("url", ""), f"restaurant {rid} social", errors)
        if r["city"] == "Beijing" and r["stars"] > 0:
            bj_starred.append(r)
            for req in ("district", "address", "phone", "michelin_url"):
                if not r.get(req):
                    errors.append(f"Beijing starred {rid} ({r['name']}) missing {req}")

    if len(bj_starred) != 33:
        errors.append(f"Expected 33 Beijing starred restaurants, found {len(bj_starred)}")
    star_hist = {3: 0, 2: 0, 1: 0}
    dist_hist: dict[str, int] = {}
    for r in bj_starred:
        star_hist[r["stars"]] = star_hist.get(r["stars"], 0) + 1
        dist_hist[r["district"]] = dist_hist.get(r["district"], 0) + 1
    if star_hist != {3: 2, 2: 5, 1: 26}:
        errors.append(f"Unexpected Beijing star distribution: {star_hist}")
    if dist_hist != {"Chaoyang": 20, "Dongcheng": 9, "Xicheng": 3, "Shunyi": 1}:
        errors.append(f"Unexpected Beijing district distribution: {dist_hist}")

    # 3. Validate hotel room filters, exact-date rate snapshots, and offer totals
    hotels = loaded["hotels.json"]
    seen_hids: set[str] = set()
    expected_windows = {w["dates"] for w in hotels.get("comparison_windows", [])}
    all_observed_dates: set[str] = set()
    for city_key in ("beijing", "shanghai"):
        for h in hotels[city_key]:
            hid = h["id"]
            if hid in seen_hids:
                errors.append(f"Duplicate hotel ID: {hid}")
            seen_hids.add(hid)
            if not str(h.get("bed_verified", "")).startswith("PASS"):
                errors.append(f"Hotel {hid} failed bed_verified check")
            if not str(h.get("bathroom_verified", "")).startswith("PASS"):
                errors.append(f"Hotel {hid} failed bathroom_verified check")
            lowest = h.get("lowest_observed_7n_usd")
            if isinstance(lowest, bool) or not isinstance(lowest, (int, float)) or lowest <= 0:
                errors.append(f"Hotel {hid} invalid lowest_observed_7n_usd")
            check_url(h.get("booking_url", ""), f"hotel {hid}", errors)
            observed = []
            for w in h.get("windows", []):
                all_observed_dates.add(w.get("dates"))
                source_url = w.get("source_url", "")
                check_url(source_url, f"hotel {hid} rate window {w.get('dates')}", errors)
                try:
                    checkin, checkout = w["dates"].split(" -> ")
                    query = parse_qs(urlparse(source_url).query)
                    if query.get("checkin") != [checkin] or query.get("checkout") != [checkout]:
                        errors.append(f"Hotel {hid} rate URL does not match its stated dates {w.get('dates')}")
                except (KeyError, ValueError):
                    errors.append(f"Hotel {hid} rate window has malformed date range: {w.get('dates')}")
                if w.get("checked") != hotels.get("verified_on"):
                    errors.append(f"Hotel {hid} rate window {w.get('dates')} has stale/missing checked date")
                if w.get("status") == "available":
                    offers = w.get("offers", [])
                    if not offers:
                        errors.append(f"Hotel {hid} rate window {w.get('dates')} has no offers")
                    qualifying = [o for o in offers if o.get("qualifies", True) is True]
                    if not qualifying:
                        errors.append(f"Hotel {hid} rate window {w.get('dates')} has no qualifying queen/king offer")
                    for offer in offers:
                        amount = offer.get("total_usd")
                        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
                            errors.append(f"Hotel {hid} rate window {w.get('dates')} has invalid offer total")
                        elif offer.get("qualifies", True) is True:
                            observed.append((float(amount), w.get("dates")))
                        if "qualifies" in offer and not isinstance(offer["qualifies"], bool):
                            errors.append(f"Hotel {hid} rate window {w.get('dates')} has non-boolean qualifies flag")
                        if offer.get("qualifies") is False and not offer.get("room"):
                            errors.append(f"Hotel {hid} rate window {w.get('dates')} has an excluded offer without a room label")
                elif w.get("status") != "no_qualifying_room_captured":
                    errors.append(f"Hotel {hid} rate window {w.get('dates')} has unknown status {w.get('status')}")
                for bucket in ("other_observed_rates", "unattributed_observed_rates"):
                    for offer in w.get(bucket, []):
                        amount = offer.get("total_usd")
                        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
                            errors.append(f"Hotel {hid} rate window {w.get('dates')} has invalid {bucket} total")
            if observed:
                expected_low, expected_date = min(observed)
                if (
                    isinstance(lowest, bool)
                    or not isinstance(lowest, (int, float))
                    or abs(float(lowest) - expected_low) > 0.01
                ):
                    errors.append(f"Hotel {hid} lowest observed total does not match its offers")
                if h.get("lowest_observed_window") != expected_date:
                    errors.append(f"Hotel {hid} lowest observed window does not match its offers")
                note_prefix = f"${expected_low:,.2f} total including taxes and fees on {expected_date}"
                if not str(h.get("lowest_observed_note", "")).startswith(note_prefix):
                    errors.append(f"Hotel {hid} lowest observed note does not match its total/window")
                winning_window = next((w for w in h.get("windows", []) if w.get("dates") == expected_date), None)
                if winning_window and h.get("booking_url") != winning_window.get("source_url"):
                    errors.append(f"Hotel {hid} booking_url does not point to its lowest observed date capture")
            elif lowest:
                errors.append(f"Hotel {hid} has a lowest observed value but no qualifying offers")
    if not expected_windows.issubset(all_observed_dates):
        missing = sorted(expected_windows - all_observed_dates)
        errors.append(f"Hotel dataset does not contain captures for comparison windows: {missing}")

    # 4. Validate activities
    acts = loaded["activities.json"]["items"]
    if len(acts) < 16:
        errors.append(f"Expected >=16 activities, found {len(acts)}")
    for a in acts:
        check_url(a.get("official_url", ""), f"activity {a['id']} official_url", errors)
        check_url(a.get("booking_url", ""), f"activity {a['id']} booking_url", errors)
        if not a.get("social"):
            errors.append(f"Activity {a['id']} missing verified social links")
        for s in a.get("social", []):
            check_url(s.get("url", ""), f"activity {a['id']} social", errors)

    # 5. Validate sources and ensure every hotel capture is registered exactly
    registered_rate_urls: set[str] = set()
    for cat in loaded["sources.json"]["categories"]:
        for it in cat["items"]:
            check_url(it.get("url", ""), f"source {it.get('title')}", errors)
            if "Booking.com" in it.get("title", "") and "rate capture" in it.get("title", ""):
                registered_rate_urls.add(it.get("url", ""))
    hotel_rate_urls = {
        w.get("source_url", "")
        for city_key in ("beijing", "shanghai")
        for h in hotels[city_key]
        for w in h.get("windows", [])
        if w.get("source_url")
    }
    if hotel_rate_urls != registered_rate_urls:
        missing = sorted(hotel_rate_urls - registered_rate_urls)
        extra = sorted(registered_rate_urls - hotel_rate_urls)
        errors.append(f"Booking.com rate capture register mismatch (missing={missing}, extra={extra})")

    # 6. Validate all 9 HTML pages, local links, anchors, viewport, and zero external CDNs
    parsed_ids: dict[str, set[str]] = {}
    page_parsers: dict[str, LinkAndMetaParser] = {}
    for page in EXPECTED_PAGES:
        p = ROOT / page
        if not p.exists():
            errors.append(f"Missing generated HTML page: {page}")
            continue
        text = p.read_text(encoding="utf-8")
        if re.search(r"\bundefined\b|>None<", text):
            errors.append(f"{page}: contains literal undefined/None text")
        if re.search(r'youtube\.com/[^"]+"[^>]*>IG:', text):
            errors.append(f"{page}: YouTube URL mislabeled as IG:")
        parser = LinkAndMetaParser()
        parser.feed(text)
        if not parser.has_viewport:
            errors.append(f"{page}: missing responsive viewport meta tag")
        if parser.external_assets:
            errors.append(f"{page}: external CDN assets disallowed -> {parser.external_assets}")
        parsed_ids[page] = parser.ids
        page_parsers[page] = parser

    for page, parser in page_parsers.items():
        for href in parser.links:
            if href.startswith(("mailto:", "tel:", "javascript:")):
                continue
            if href.startswith("http"):
                check_url(href, f"{page} link", errors)
                continue
            if href.startswith("#"):
                frag = href[1:]
                if frag and frag not in parsed_ids.get(page, set()):
                    errors.append(f"{page}: broken in-page anchor #{frag}")
                continue
            path_part, _, frag = href.partition("#")
            target = (ROOT / path_part).resolve()
            if not target.exists():
                errors.append(f"{page}: broken relative link '{href}' -> {target}")
            elif frag and target.parent == ROOT and target.name in parsed_ids:
                if frag not in parsed_ids[target.name]:
                    errors.append(f"{page}: broken target anchor '{href}'")

    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for err in errors:
            print(" -", err)
        return 1

    print(
        f"PASS: china-2027 validated ({len(EXPECTED_PAGES)} HTML pages, "
        f"{len(hotels['beijing']) + len(hotels['shanghai'])} hotels, "
        f"{len(rests)} restaurants [33/33 BJ starred], {len(acts)} activities, "
        f"0 broken links, 0 external CDNs)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

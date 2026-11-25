#!/usr/bin/env python3
"""Checks for the social-2027 sub-site: JSON integrity, row sourcing, internal links."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def fail(msg):
    errors.append(msg)


def main():
    venues = json.loads((ROOT / "data/venues.json").read_text(encoding="utf-8"))["venues"]
    social = json.loads((ROOT / "data/social.json").read_text(encoding="utf-8"))["videos"]
    content = json.loads((ROOT / "data/content.json").read_text(encoding="utf-8"))
    ids = {v["id"] for v in venues}

    if len(venues) != 43:
        fail(f"expected 43 venues, got {len(venues)}")
    for v in venues:
        for field in ("id", "name", "flag"):
            if not v.get(field):
                fail(f"venue {v.get('id')} missing {field}")
        if v["type"] == "Restaurant" and not v["official"]:
            fail(f"restaurant {v['id']} has no official guide URL")

    seen = set()
    for v in social:
        if v["id"] in seen:
            fail(f"duplicate video id {v['id']}")
        seen.add(v["id"])
        if v["venue"] not in ids:
            fail(f"video {v['id']} points at unknown venue {v['venue']}")
        m = re.search(r"[?&]v=([\w-]{11})", v["verify"])
        if not m:
            fail(f"video {v['id']} has no verifiable video ID")
        else:
            vid = m.group(1)
            if vid not in v["url"]:
                fail(f"video {v['id']} URL does not match its proof ID {vid}")
        if "www.youtube.com" not in v["url"] and "youtube.com" not in v["url"]:
            fail(f"video {v['id']} is not a YouTube URL")

    counts = {}
    for v in social:
        counts[v["platform"]] = counts.get(v["platform"], 0) + 1
    if len(social) != content["coverage"]["social_links"]:
        fail("coverage count does not match social.json")

    pages = sorted(p.name for p in ROOT.glob("*.html"))
    expected = ["activities.html", "flagged.html", "index.html", "questions.html",
                "restaurants.html", "sources.html", "suggestions.html", "videos.html"]
    if pages != expected:
        fail(f"page set mismatch: {pages}")
    for page in ROOT.glob("*.html"):
        text = page.read_text(encoding="utf-8")
        if "<title>" not in text or 'name="viewport"' not in text:
            fail(f"{page.name}: missing title or viewport")
        for target in re.findall(r'href="([^"#][^"#]*)"', text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (ROOT / target).exists():
                fail(f"{page.name}: broken local link {target}")
        # Every data row on every page must carry an outbound source link.
        body_only = re.sub(r"<thead>.*?</thead>", "", text, flags=re.S)
        for row in re.findall(r"<tr>(.*?)</tr>", body_only, flags=re.S):
            if 'rel="noopener noreferrer"' not in row:
                fail(f"{page.name}: a table row has no source link")

    print(f"venues={len(venues)} videos={len(social)} pages={len(pages)} platforms={counts}")
    if errors:
        print("FAIL:")
        for e in errors[:40]:
            print(" -", e)
        sys.exit(1)
    print("PASS: data, row sourcing and internal links are consistent")


if __name__ == "__main__":
    main()

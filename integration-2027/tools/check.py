#!/usr/bin/env python3
"""Post-build checks for the integration site. Standard library only."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []
warnings = []

for page in sorted(ROOT.glob("*.html")):
    text = page.read_text(encoding="utf-8")
    if "<title>" not in text or 'name="viewport"' not in text:
        errors.append(f"{page.name}: missing title or viewport")
    for href in re.findall(r'href="([^"]*)"', text):
        if not href:
            errors.append(f"{page.name}: empty href")
            continue
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        target = (page.parent / href.split("#")[0]).resolve()
        if not target.exists():
            errors.append(f"{page.name}: broken local link {href}")

for name in ("plans.json", "price_windows.json", "social.json", "questions.json",
             "suggestions.json", "flags.json", "sources.json"):
    data = json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))
    rows = data["rows"] if "rows" in data else data.get(name.split(".")[0], [])
    if not rows:
        errors.append(f"{name}: empty dataset")
    for row in rows:
        keys = [k for k in ("source", "official_url", "source_page", "url") if k in row]
        if not keys:
            errors.append(f"{name}: row without any source field: {row.get('id', row.get('q', '?'))}")
        elif all(not row.get(k) for k in keys):
            errors.append(f"{name}: row with empty source: {row.get('id', row.get('q', '?'))}")

social = json.loads((ROOT / "data" / "social.json").read_text(encoding="utf-8"))
sources = {s["url"] for s in json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8"))["sources"]}
for row in social["rows"]:
    for video in row["social"]:
        if not video.get("evidence"):
            errors.append(f"social.json: {video['url']} has no read evidence")
    if not row.get("official_url"):
        errors.append(f"social.json: {row['venue']} has no official source")

for err in errors:
    print("ERROR", err)
for warn in warnings:
    print("WARN", warn)
print(f"checked {len(list(ROOT.glob('*.html')))} pages; {len(errors)} errors")
sys.exit(1 if errors else 0)

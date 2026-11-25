#!/usr/bin/env python3
"""Static checks for the generated docs/ site: broken internal links, bad hrefs, empty tables."""
import os, re, sys, glob

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
problems, stats = [], []
href_re = re.compile(r'href="([^"]*)"')

def strip_hash(u):
    return u.split("#")[0]

for f in sorted(glob.glob(os.path.join(OUT, "*.html"))):
    html = open(f, encoding="utf-8").read()
    name = os.path.basename(f)
    local = 0
    for href in href_re.findall(html):
        if href.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        if href in ("", "#"):
            problems.append(f"{name}: empty href")
            continue
        target = strip_hash(href)
        if not target:
            continue
        p = os.path.join(OUT, target)
        if not os.path.exists(p):
            problems.append(f"{name}: broken link -> {href}")
        else:
            local += 1
    tables = html.count("<table")
    rows = html.count("<tr>")
    unv = html.count('class="unv"')
    stats.append((name, tables, rows, unv, local))
    if "<title>" not in html:
        problems.append(f"{name}: missing <title>")
    if 'name="viewport"' not in html:
        problems.append(f"{name}: missing viewport meta")

print(f"{'page':22} {'tables':>7} {'rows':>6} {'unverified cells':>17} {'internal links':>15}")
for n, t, r, u, l in stats:
    print(f"{n:22} {t:7} {r:6} {u:17} {l:15}")

total_rows = sum(r for _, _, r, _, _ in stats)
print(f"\nTotal table rows rendered: {total_rows}")
if problems:
    print("\nPROBLEMS:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("\nOK — no broken internal links, no empty hrefs, all pages have title + viewport.")

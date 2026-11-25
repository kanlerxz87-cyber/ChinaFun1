"""Shared page generator for the ChinaFun1 static site.

The published site is plain static HTML/CSS/JS committed at the repo root, so
GitHub Pages needs no build step. This module exists only so the pages stay
consistent and can be regenerated; it is not required to serve the site.

All content values passed in here come from the verified research in /data.
"""

NAV = [
    ("index.html", "Overview"),
    ("executive-summary.html", "Executive Summary"),
    ("dates.html", "Dates &amp; Entry"),
    ("hotels.html", "Hotels"),
    ("michelin.html", "MICHELIN Dining"),
    ("activities.html", "Activities"),
    ("costs.html", "Costs &amp; Booking"),
    ("questions.html", "Open Questions"),
    ("suggestions.html", "Suggestions"),
    ("flagged.html", "Flagged for Review"),
    ("sources.html", "Sources"),
]

FETCHED = "2026-11-25"

CSS = '<link rel="stylesheet" href="assets/style.css">'


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Trip Planning China</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0f1720">
{CSS}
</head>
<body>
"""


def header(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return f"""<header class="hdr">
  <div class="hdr-in">
    <a class="brandmark" href="index.html"><span class="dot">CF</span>
      <span><b>Trip Planning China</b><span>Shanghai · Feb–Mar 2027 · 2 adults</span></span></a>
    <button class="navtoggle" type="button" aria-controls="nav-list">Menu</button>
  </div>
  <nav class="nav" aria-label="Site"><ul id="nav-list" class="hidden">{''.join(items)}</ul></nav>
</header>
<main>
"""


def footer():
    return f"""</main>
<footer class="ftr">
  <p><b>Verification rule applied to every table on this site:</b> each row carries a link to the official
  source that was actually fetched. Where a value could not be confirmed from an official source it is left
  <span class="b blist">blank</span> and flagged <span class="b bwarn">unverified</span> — no value is ever
  inferred, estimated or filled in.</p>
  <p>All live prices are timestamped snapshots fetched <b>{FETCHED} (UTC)</b> for 2 adults, 1 room, 7 nights,
  USD, total-price display. Hotel and restaurant rates change; re-check the linked page before booking.</p>
  <p>Data layer: <code>/data</code> (CSV + notes). Task board and verification log:
  <a href="https://github.com/kanlerxz87-cyber/ChinaFun1/blob/main/COORDINATION.md">COORDINATION.md</a>.
  Repo: <a href="https://github.com/kanlerxz87-cyber/ChinaFun1">kanlerxz87-cyber/ChinaFun1</a>.</p>
</footer>
<script src="assets/app.js" defer></script>
</body>
</html>
"""


def page(filename, title, desc, body):
    return head(title, desc) + header(filename) + body + footer()


def hero(h1, lead, stamp=None):
    s = stamp or (f"Every figure on this page was read from an official source on {FETCHED}. "
                  "Unconfirmed values are left blank and flagged rather than estimated.")
    return f'<div class="hero"><h1>{h1}</h1><p>{lead}</p><div class="stamp">{s}</div></div>'


def metrics(items):
    """items: list of (klass, key, value, sub)"""
    cells = "".join(
        f'<div class="metric {k}"><div class="k">{key}</div><div class="v">{val}</div>'
        f'<div class="s">{sub}</div></div>' for k, key, val, sub in items)
    return f'<div class="grid g4">{cells}</div>'


def tablewrap(caption, head_cells, rows, footnote=None, filterable=True, sortable=True, tfoot=None):
    th = "".join(
        f'<th data-sort data-sort-col="{i}">{c}</th>' if sortable else f"<th>{c}</th>"
        for i, c in enumerate(head_cells))
    body = "".join("<tr>" + "".join(c for c in r) + "</tr>" for r in rows)
    tf = f"<tfoot><tr>{tfoot}</tr></tfoot>" if tfoot else ""
    attrs = ' data-filterable' if filterable else ''
    sattrs = ' data-sortable' if sortable else ''
    tools = ""
    if filterable:
        tools = ('<div class="toolbar"><input type="search" data-search '
                 'placeholder="Filter rows (type a name, district, price, status…)" '
                 'aria-label="Filter table rows"><span class="count"></span></div>')
    fn = f'<p class="hint">{footnote}</p>' if footnote else ""
    return (f'<div data-tablewrap>{tools}<div class="tw"><table{sattrs}{attrs}>'
            f'<caption>{caption}</caption><thead><tr>{th}</tr></thead>'
            f'<tbody>{body}</tbody>{tf}</table></div>{fn}</div>')


def td(v, cls=""):
    c = f' class="{cls}"' if cls else ""
    if v is None or v == "":
        return '<td class="blank">— blank / unverified</td>'
    return f"<td{c}>{v}</td>"


def num(v):
    return f'<td class="num">{v}</td>'


def link(href, label):
    return f'<a href="{href}" rel="noopener">{label}</a>'

#!/usr/bin/env python3
"""Deterministic static site generator for china-2027/ (Python 3 stdlib only).

Reads china-2027/data/*.json and outputs 9 executive, mobile-friendly HTML pages
inside china-2027/ with zero external CDN dependencies.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

NAV_ITEMS = [
    ("index.html", "Overview"),
    ("hotels.html", "Hotels"),
    ("restaurants.html", "MICHELIN"),
    ("activities.html", "Activities"),
    ("itineraries.html", "Itineraries"),
    ("questions.html", "Decisions"),
    ("suggestions.html", "Suggestions"),
    ("flagged.html", "Audit & Flags"),
    ("sources.html", "Sources"),
]


def e(val: Any) -> str:
    return html.escape("" if val is None else str(val), quote=True)


def booking_url_for_dates(base_url: str, check_in: str, check_out: str) -> str:
    """Return the listed Booking.com property URL with the table row dates."""
    parts = urlsplit(base_url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query["checkin"] = check_in
    query["checkout"] = check_out
    query.setdefault("group_adults", "2")
    query.setdefault("no_rooms", "1")
    query.setdefault("selected_currency", "USD")
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def external_source_links(urls: list[str], label: str = "Source") -> str:
    return "<br>".join(
        f'<a href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(label)} {idx} ↗</a>'
        for idx, url in enumerate(urls, 1)
    )


def load_json(name: str) -> Any:
    with (DATA_DIR / name).open(encoding="utf-8") as fh:
        return json.load(fh)


def page_shell(filename: str, title: str, subtitle: str, meta: dict, body_html: str) -> str:
    nav_links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == filename else ""
        nav_links.append(f'<a href="{e(href)}"{cls}>{e(label)}</a>')
    nav_html = "\n        ".join(nav_links)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)} — China 2027 Verified Planner</title>
  <meta name="description" content="{e(subtitle)}">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="index.html">
        <span class="brand-mark">CN</span>
        <span>
          China 2027 Verified Planner
          <span class="brand-sub">Beijing &amp; Shanghai · Sources checked {e(meta['source_check_window'])}</span>
        </span>
      </a>
      <button id="navToggle" class="nav-toggle" type="button" aria-expanded="false" aria-controls="siteNav">Menu</button>
      <nav id="siteNav" class="site-nav" aria-label="Primary">
        {nav_html}
      </nav>
    </div>
  </header>

  <main id="main" class="container">
{body_html}
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div><strong>China 2027 Verified Trip Planner</strong> · Dated source checks: {e(meta['source_check_window'])} · Individual rates and facts are dated by row · <a href="../index.html">Repo Root Dashboard</a></div>
      <div><a href="sources.html">Official Sources</a> · <a href="flagged.html">Audit &amp; Flagged Items</a> · <a href="questions.html">Open Decisions</a></div>
    </div>
  </footer>
  <script src="assets/app.js"></script>
</body>
</html>
"""


def render_social_pills(social: list[dict], max_inline: int = 8) -> str:
    if not social:
        return '<span class="blank-cell">None verified (blank — never fabricated)</span>'
    parts = []
    for s in social[:max_inline]:
        plat = s.get("platform", "Link")
        if plat.startswith("YouTube"):
            p_cls = "social-yt"
            short_plat = "YT Short" if "Short" in plat else "YT"
        elif plat == "TikTok":
            p_cls = "social-tt"
            short_plat = "TikTok"
        else:
            p_cls = "social-ig"
            short_plat = "IG"
        creator = s.get("creator", "")
        title = s.get("title", plat)
        label = f"{short_plat}: {creator}" if creator and creator not in ("YouTube Review", "YouTube Guide") else f"{short_plat}: {title[:36]}"
        if len(label) > 42:
            label = label[:39] + "..."
        parts.append(
            f'<a class="social-pill {p_cls}" href="{e(s["url"])}" target="_blank" rel="noopener noreferrer" '
            f'title="{e(title)} ({e(s.get("verification", ""))})">{e(label)}</a>'
        )
    if len(social) > max_inline:
        parts.append(f'<span class="badge badge-neutral">+{len(social) - max_inline} more</span>')
    return '<div class="social-list">' + "".join(parts) + "</div>"


def render_tier_badge(tier: str) -> str:
    if "Star" in tier:
        return f'<span class="badge badge-star">{e(tier)}</span>'
    if "Bib" in tier:
        return f'<span class="badge badge-bib">{e(tier)}</span>'
    return f'<span class="badge badge-sel">MICHELIN {e(tier)}</span>'


def build_index(meta: dict, hotels: dict, restaurants: dict, activities: dict, audit: dict) -> str:
    r_items = restaurants["items"]
    bj_starred = [r for r in r_items if r["city"] == "Beijing" and r["stars"] > 0]
    bj_hours = sum(1 for r in bj_starred if r["hours"])
    bj_prices = sum(1 for r in bj_starred if r["published_cost_2_adults"])
    sh_verified = [r for r in r_items if r["city"] == "Shanghai"]
    social_total = sum(len(r["social"]) for r in r_items) + sum(len(a["social"]) for a in activities["items"])
    dist_counts: dict[str, int] = {}
    for r in bj_starred:
        dist_counts[r["district"]] = dist_counts.get(r["district"], 0) + 1
    dist_sorted = sorted(dist_counts.items(), key=lambda kv: (-kv[1], kv[0]))

    bar_rows = []
    for d, cnt in dist_sorted:
        pct = round(cnt / len(bj_starred) * 100, 1)
        bar_rows.append(
            f'<div class="bar-row">'
            f'<div class="bar-label"><span>{e(d)}</span><span>{cnt} / {len(bj_starred)} ({pct}%)</span></div>'
            f'<div class="bar-track"><div class="bar-fill" style="width:{pct}%"></div></div>'
            f"</div>"
        )

    bj_top = hotels["beijing"][:3]
    sh_top = hotels["shanghai"][:3]
    hotel_capture_dates = sorted({
        w["checked"] for city in ("beijing", "shanghai") for h in hotels[city] for w in h.get("windows", []) if w.get("checked")
    })
    hotel_capture_label = "–".join(hotel_capture_dates)
    hotel_rows = []
    for city_lbl, group in [("Beijing", bj_top), ("Shanghai", sh_top)]:
        for h in group:
            hotel_rows.append(
                f"<tr>"
                f"<td><strong>{e(city_lbl)} · Provisional #{h['rank']}</strong></td>"
                f"<td><a href=\"hotels.html#{e(h['id'])}\"><strong>{e(h['name'])}</strong></a><br><small>{e(h['district'])}<br><a href=\"{e(h['booking_url'])}\" target=\"_blank\" rel=\"noopener noreferrer\">Booking.com quote source ↗</a></small></td>"
                f"<td><strong style=\"color:var(--jade)\">${h['cheapest_7n_usd']:,}</strong><br><small>Lowest shown capture: {e(h['cheapest_window'])}</small></td>"
                f"<td><span class=\"badge badge-pass\">Matched in dated capture: queen/king + private bath</span></td>"
                f"<td>{e(h['tier'])}</td>"
                f"</tr>"
            )

    p1_qs = [q for q in audit["traveler_questions"] if q.get("priority", "").startswith("P1")]
    q_cards = []
    for q in p1_qs:
        reference_links = external_source_links(q.get("source_urls", []), "Reference")
        reference_html = f'<p style="font-size:12px;margin:8px 0 0">{reference_links}</p>' if reference_links else ""
        q_cards.append(
            f'<div class="card">'
            f'<span class="badge badge-flag">{e(q["priority"])}</span>'
            f'<h3 style="margin-top:8px">{e(q["question"])}</h3>'
            f'<p style="margin:0;color:var(--muted);font-size:13.5px">{e(q["why_it_matters"])}</p>'
            f"{reference_html}"
            f"</div>"
        )

    cal = meta["calendar_2027"]
    transit = meta["transit_official"]
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Executive Trip Brief · Dual-City Primary-Source Edition</span>
      <h1>China 2027 Verified Travel Dashboard: Beijing &amp; Shanghai</h1>
      <p>For 2 adults, the requested trip length is <strong>1–2 weeks</strong> inside <strong>2027-02-15 to 2027-03-23</strong>. If Feb 15 is check-in and Feb 18 is checkout, that preferred interval is <strong>3 nights</strong> and conflicts with the minimum; whether it means a start preference or the whole trip remains unresolved, and no flexible-start interpretation is inferred. Hotel rates are dated Booking.com captures; unconfirmed values stay blank or flagged. <strong>No hotel is certified for the requested ≤60-minute hotel-to-venue transit limit.</strong></p>
      <div class="hero-meta">
        <span>2 Adults · 1 Room (Queen/King + Private Bath)</span>
        <span>No statutory public holidays Feb 15 – Mar 23, 2027</span>
        <span>{len(bj_starred)}/33 Beijing Stars + {len(sh_verified)} Shanghai Venues Verified</span>
        <span>{len(activities['items'])} Gov-Verified Activities</span>
        <span>{social_total} Verified YT / TikTok / IG Links</span>
      </div>
    </section>

    <section class="kpi-grid" aria-label="Headline Findings">
      <div class="kpi-card">
        <div class="kpi-label">Dated 7-Night Stay-Price Sample</div>
        <div class="kpi-value">Varies by hotel</div>
        <div class="kpi-sub">Selected stay dates only (captures {e(hotel_capture_label)}). Stay-date rates vary: Grand Millennium Beijing was captured at $783 for Mar 1–8 and $838 for Feb 15–22, while some Feb 15–22 quotes were below Mar 16–23 captures. This does not identify when to purchase.</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Best Time to Purchase</div>
        <div class="kpi-value">Not established</div>
        <div class="kpi-sub">One dated price capture cannot prove a historical low or forecast the cheapest booking date.</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">MICHELIN Coverage Verified</div>
        <div class="kpi-value">{len(r_items)} Venues</div>
        <div class="kpi-sub"><strong>33/33</strong> Beijing starred ({bj_hours} w/ hours, {bj_prices} w/ menu PDFs) + 8 BJ Bib/Sel + 15 SH highlights (live SH total: <strong>50 starred / 153 guide</strong>).</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Activities &amp; Multi-Platform Reviews</div>
        <div class="kpi-value">{len(activities['items'])} / {len(activities['items'])} Verified</div>
        <div class="kpi-sub">10 Beijing + 6 Shanghai official schedules · <strong>{social_total}</strong> verified YouTube, TikTok &amp; Instagram links.</div>
      </div>
    </section>

    <section class="callout callout-jade">
      <strong class="label">Official 2027 Holidays &amp; Date-Window Context</strong>
      <p style="margin:4px 0 8px">The official 2027 schedule lists Spring Festival from <strong>Feb 5–13</strong>; an official Beijing notice confirms makeup workdays Jan 31 and Feb 14. The Hong Kong Observatory's 2027 Gregorian–lunar table places the Lantern Festival (lunar day 15) on Sat Feb 20. No statutory public-holiday dates in the official schedule fall within Feb 15–Mar 23. Selected hotel snapshots vary by property and stay date; some Feb 15–22 quotes are below some mid-March quotes, while other sampled dates are not. That comparison does not establish the best date to purchase. <a href="{e(cal['source_url'])}" target="_blank" rel="noopener noreferrer">Official State Council Release &rarr;</a> · <a href="{e(cal['makeup_workdays_source_url'])}" target="_blank" rel="noopener noreferrer">Beijing holiday notice &rarr;</a> · <a href="{e(cal['lantern_festival_source_url'])}" target="_blank" rel="noopener noreferrer">Hong Kong Observatory lunar calendar &rarr;</a></p>
      <a class="btn btn-primary" href="hotels.html">View Dated 7-Night Hotel Quotes</a>
      <a class="btn" href="itineraries.html">Compare 7-night / 14-day options</a>
    </section>

    <section>
      <h2>Hotel Quote Shortlist (Provisional Order; Not Route-Validated)</h2>
      <p class="lead">The dated room captures matched the private-bathroom and queen/king filters shown in each row; quote dates vary by property. Ordering is provisional and does not certify the requested ≤60-minute hotel-to-venue rule. <a href="hotels.html">View all {len(hotels['beijing']) + len(hotels['shanghai'])} hotel snapshots &amp; date comparisons &rarr;</a></p>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Provisional Position</th><th>Hotel &amp; District (Booking.com quote)</th><th>Lowest Listed 7-Night Capture</th><th>Room Check (at capture)</th><th>Snapshot Note</th></tr>
          </thead>
          <tbody>
            {''.join(hotel_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <section class="grid-2">
      <div class="card">
        <h3>Verified 33/33 Beijing MICHELIN Starred District Split</h3>
        <p style="font-size:13.5px;color:var(--muted);margin-top:0">Direct 2026-11-26 verification of all 33/33 official MICHELIN 2027 Beijing pages shows <strong>Chaoyang has 20/33 stars (60.6%)</strong>. <a href="https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred" target="_blank" rel="noopener noreferrer">MICHELIN Guide source &rarr;</a></p>
        {''.join(bar_rows)}
        <p style="font-size:13px;margin:10px 0 0"><a href="restaurants.html">Explore all {len(r_items)} verified restaurants &amp; reviews &rarr;</a></p>
      </div>
      <div class="card">
        <h3>Beijing &harr; Shanghai Rail &amp; Transit Snapshot</h3>
        <ul class="clean" style="font-size:13.5px">
          <li><strong>Fuxing High-Speed Rail (~1,300 km):</strong> 4.5–5.5 hr Beijing South &harr; Shanghai Hongqiao. Official 2nd Class <strong>CNY 550–670/adult</strong> (CNY 1,100–1,340 for 2 one-way); 1st Class ~CNY 1,035; Business ~CNY 2,318 (<a href="https://www.12306.cn/en/index.html" target="_blank" rel="noopener noreferrer">12306.cn</a>).</li>
          <li><strong>Beijing Subway:</strong> {transit['beijing_subway']['fares']}</li>
          <li><strong>Shanghai Metro:</strong> {transit['shanghai_metro']['fares']} <em>Recheck the fare and contactless-card rules before travel; a final 2027 schedule is not established here.</em></li>
          <li><strong>Visitor payments:</strong> Official Shanghai guidance describes international-card setup for Alipay / Weixin Pay and overseas-card acceptance at participating merchants; card, issuer, app, account limits, and fees vary. <a href="https://english.shanghai.gov.cn/en-Individuals-BankingandPayments-Payments/20260920/4fc94c2f0e6b47e7939969415e5feb04.html" target="_blank" rel="noopener noreferrer">Mobile payment guide</a> · <a href="https://english.shanghai.gov.cn/en-Individuals-BankingandPayments-Payments/20260921/c2c94d06a0454c8fa05386b80d0ae865.html" target="_blank" rel="noopener noreferrer">Overseas bank-card guide</a>.</li>
          <li><strong>Dual-City Synergy:</strong> Shanghai Museum East is <strong>OPEN Mondays</strong> (hosting the Met Museum's <em>Jewelry: The Body Transformed</em> show through May 5, 2027!) — solving classic Monday museum closures.</li>
        </ul>
      </div>
    </section>

    <section>
      <h2>Open Decisions &amp; Missing Information</h2>
      <p class="lead">The examples stay within the 1–2-week request while trip dates, city mix, hotel budget, dining preferences, and flight/passport details remain open. Nothing is assumed; these questions do not block publication of the documented options. <a href="questions.html">See full Knowns/Unknowns &amp; Discovery Plan &rarr;</a></p>
      <div class="grid-2">
        {''.join(q_cards)}
      </div>
    </section>

    <section class="callout callout-navy">
      <strong class="label">Historical Cross-Directory Audit (2026-11-26)</strong>
      <p style="margin:4px 0 8px;font-size:13.5px">The linked audit is a dated read-only snapshot of repository files as they appeared on <code>main @ 179e24c</code>; it is not a current-status statement for later commits. Check the coordination log and each linked source before acting on historical findings.</p>
      <a class="btn" href="flagged.html">Read Full Line-by-Line Audit &amp; Flagged Items &rarr;</a>
      <a class="btn" href="suggestions.html">Review Optional Suggestions &rarr;</a>
    </section>
    """
    return page_shell("index.html", "Executive Overview", meta["subtitle"], meta, body)


def build_hotels(meta: dict, hotels: dict) -> str:
    hotel_capture_dates = sorted({
        w["checked"] for city in ("beijing", "shanghai") for h in hotels[city] for w in h.get("windows", []) if w.get("checked")
    })
    hotel_capture_label = "–".join(hotel_capture_dates)

    def render_city_section(city_name: str, items: list[dict]) -> str:
        cards = []
        matrix_rows = []
        for h in items:
            win_map = {w["dates"]: w for w in h["windows"]}
            def cell(d: str) -> str:
                w = win_map.get(d)
                if not w:
                    return '<span class="blank-cell">Not queried</span>'
                check_in, _, check_out = d.partition(" -> ")
                source_url = booking_url_for_dates(h["booking_url"], check_in, check_out)
                checked = e(w.get("checked", ""))
                return (
                    f"<strong>${w['total_usd']:,}</strong><br>"
                    f"<small>${w['per_night_usd']}/nt · {e(w['terms'][:48])} · captured {checked}</small><br>"
                    f'<a href="{e(source_url)}" target="_blank" rel="noopener noreferrer">Booking.com quote source ↗</a>'
                )

            matrix_rows.append(
                f"<tr>"
                f"<td><strong>Provisional #{h['rank']}</strong> <a href=\"#{e(h['id'])}\">{e(h['name'])}</a><br><small>{e(h['district'])}</small></td>"
                f"<td>{cell('2027-02-15 -> 2027-02-22')}</td>"
                f"<td>{cell('2027-03-01 -> 2027-03-08')}</td>"
                f"<td>{cell('2027-03-16 -> 2027-03-23')}</td>"
                f"</tr>"
            )
            amen_html = "".join(f'<span class="badge badge-neutral">{e(a)}</span>' for a in h["amenities"])
            reach_html = (
                e(h["michelin_reach_summary"])
                if h.get("michelin_reach_summary")
                else '<span class="blank-cell">Not verified — no official ≤60-minute hotel-to-venue route result; see <a href="flagged.html#GAP-08">Flagged for Review</a>.</span>'
            )
            flag_html = "".join(f'<div class="callout callout-amber" style="margin:10px 0 0;padding:10px 12px;font-size:13px"><strong>Flag:</strong> {e(fl)}</div>' for fl in h["flags"])
            cards.append(
                f'<article class="card" id="{e(h["id"])}">'
                f'<div class="card-header">'
                f'<div><span class="badge badge-sel">Provisional shortlist #{h["rank"]} · {e(h["tier"])}</span><h3 style="margin-top:6px">{e(h["name"])}</h3>'
                f'<div style="font-size:13px;color:var(--muted)">{e(h["district"])} · {e(h["address"])} · Rating: <strong>{e(h["rating"])}</strong> (Location: {e(h["location_score"])})</div></div>'
                f'<div class="price-tag">${h["cheapest_7n_usd"]:,}<small>Lowest captured 7N ({e(h["cheapest_window"])})</small></div>'
                f"</div>"
                f'<div class="badges">'
                f'<span class="badge badge-pass">{e(h["bed_verified"])}</span>'
                f'<span class="badge badge-pass">{e(h["bathroom_verified"])}</span>'
                f"</div>"
                f'<p style="font-size:13.5px;margin:8px 0"><strong>Captured Quote Terms:</strong> {e(h["cheapest_note"])}</p>'
                f'<p style="font-size:13.5px;margin:8px 0"><strong>Reported station access:</strong> {e(h["subway_access"])}</p>'
                f'<p style="font-size:13.5px;margin:8px 0"><strong>≤60-minute hotel-to-venue test:</strong> {reach_html}</p>'
                f'<div class="badges" style="margin-top:8px">{amen_html}</div>'
                f'{flag_html}'
                f'<p style="margin:12px 0 0"><a class="btn btn-primary" href="{e(h["booking_url"])}" target="_blank" rel="noopener noreferrer">Check Live 2027 Booking.com Rate &rarr;</a></p>'
                f"</article>"
            )

        return (
            f"<section><h2>{e(city_name)} Dated 7-Night Quote Matrix (USD, 2 Adults, 1 Room)</h2>"
            f'<div class="table-wrap"><table><thead><tr>'
            f"<th>Provisional Shortlist</th><th>Feb 15–22, 2027</th><th>Mar 1–8, 2027</th><th>Mar 16–23, 2027</th>"
            f"</tr></thead><tbody>{''.join(matrix_rows)}</tbody></table></div>"
            f'<div class="grid-2">{"".join(cards)}</div></section>'
        )

    bt = hotels["booking_timing_finding"]
    ev_lis = "".join(f"<li>{e(x)}</li>" for x in bt["evidence"])
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Booking.com Quote Snapshots · Captured {e(hotel_capture_label)}</span>
      <h1>Hotel Price Snapshots &amp; Stay-Date Comparison (Beijing &amp; Shanghai)</h1>
      <p>The listed room types matched the requested <strong>private/attached bathroom</strong> and <strong>queen/king bed</strong> filters in their dated Booking.com captures. These are selected <strong>7-night quotes for 2 adults</strong>, not guaranteed live offers. Some properties have only one captured date window; every quote row shows its capture date and Booking.com source.</p>
    </section>

    <section class="callout callout-jade">
      <strong class="label">Dated Stay-Price Comparison — Not a Booking-Time Forecast</strong>
      <h3 style="margin:4px 0 6px">{e(bt['headline'])}</h3>
      <ul class="clean" style="font-size:13.5px">{ev_lis}</ul>
      <p style="margin:10px 0 0;font-size:13.5px"><strong>Recommended Action:</strong> {e(bt['action'])}</p>
    </section>

    <section class="callout callout-navy">
      <strong class="label">Price Snapshot &amp; Requested ≤60-Minute Transit Test (Strict Honesty)</strong>
      <p style="margin:4px 0 6px;font-size:13.5px">{e(hotels['pricing_notes'])}</p>
      <p style="margin:0;font-size:13.5px">{e(hotels['proximity_methodology'])}</p>
    </section>

    {render_city_section("Beijing", hotels["beijing"])}
    {render_city_section("Shanghai", hotels["shanghai"])}
    """
    return page_shell("hotels.html", "Hotel Rate Snapshots & Stay Dates", "Dated 7-night Booking.com quotes for Beijing and Shanghai; hotel-to-venue route times remain unverified.", meta, body)


def build_restaurants(meta: dict, restaurants: dict) -> str:
    items = restaurants["items"]
    districts = sorted({r["district"] for r in items if r["district"]})
    dist_opts = "".join(f'<option value="{e(d)}">{e(d)}</option>' for d in districts)

    rows = []
    for r in items:
        hrs_html = (
            f'<strong>{e(r["hours"])}</strong><br><small style="color:var(--muted)">{e(r["hours_source"])}</small>'
            if r["hours"]
            else '<span class="blank-cell">Not published — confirm directly</span>'
        )
        price_html = (
            f'<strong>{e(r["published_cost_2_adults"])}</strong>'
            + (f'<br><a href="{e(r["cost_source"])}" target="_blank" rel="noopener noreferrer">Official menu &rarr;</a>' if r["cost_source"] else "")
            if r["published_cost_2_adults"]
            else f'<span class="blank-cell">Band {e(r["price_band"])} only (2-adult total not published)</span>'
        )
        links = [f'<a href="{e(r["michelin_url"])}" target="_blank" rel="noopener noreferrer">MICHELIN</a>']
        if r["official_url"]:
            links.append(f'<a href="{e(r["official_url"])}" target="_blank" rel="noopener noreferrer">Official Site</a>')
        search_blob = " ".join([
            r["name"], r["city"], r["tier"], r["cuisine"], r["district"],
            r["address"], r["price_band"], r["notes"]
        ])
        has_hours = "yes" if r["hours"] and "CONFLICT" not in r["hours"] else "no"
        has_price = "yes" if r["published_cost_2_adults"] else "no"
        has_social = "yes" if r["social"] else "no"

        rows.append(
            f'<tr data-filter-item '
            f'data-city="{e(r["city"])}" '
            f'data-tier="{e(r["tier"])}" '
            f'data-district="{e(r["district"])}" '
            f'data-band="{e(r["price_band"])}" '
            f'data-hours="{has_hours}" '
            f'data-price="{has_price}" '
            f'data-social="{has_social}" '
            f'data-search="{e(search_blob)}">'
            f'<td><strong>{e(r["name"])}</strong><br>'
            f'<div class="badges" style="margin:4px 0">{render_tier_badge(r["tier"])} '
            f'<span class="badge badge-neutral">{e(r["city"])} · {e(r["district"])}</span> '
            f'<span class="badge badge-neutral">{e(r["cuisine"])} · {e(r["price_band"])}</span></div>'
            f'<small style="color:var(--muted)">{e(r["address"])}<br>Tel: {e(r["phone"])} · {" · ".join(links)}</small></td>'
            f"<td>{hrs_html}</td>"
            f"<td>{price_html}</td>"
            f'<td>{render_social_pills(r["social"])}'
            f'<div style="margin-top:6px;font-size:12px;color:var(--muted)">{e(r["notes"])}</div></td>'
            f"</tr>"
        )

    bj_s = meta["michelin_summary"]["beijing_2027"]
    sh_s = meta["michelin_summary"]["shanghai_live"]
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">MICHELIN Guide Primary-Source Audit · Verified {e(restaurants['verified_on'])}</span>
      <h1>MICHELIN Restaurants &amp; Multi-Platform Reviews</h1>
      <p>{e(restaurants['coverage_note'])}</p>
    </section>

    <section class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">Beijing 2027 Starred (100%)</div>
        <div class="kpi-value">{bj_s['total_starred']} / 33</div>
        <div class="kpi-sub">{bj_s['three_star']}×3★ · {bj_s['two_star']}×2★ · {bj_s['one_star']}×1★ · Chaoyang {bj_s['district_breakdown_starred']['Chaoyang']}, Dongcheng {bj_s['district_breakdown_starred']['Dongcheng']}, Xicheng {bj_s['district_breakdown_starred']['Xicheng']}, Shunyi {bj_s['district_breakdown_starred']['Shunyi']}.</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Shanghai Live Guide Totals</div>
        <div class="kpi-value">{sh_s['total_starred']} Starred</div>
        <div class="kpi-sub">{sh_s['three_star']}×3★ · {sh_s['two_star']}×2★ · {sh_s['one_star']}×1★ · {sh_s['bib_gourmand']} Bib · {sh_s['selected']} Selected ({sh_s['total_guide']} total; {sh_s['directly_verified_sample']} verified below).</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Verified Hours &amp; Menu Totals</div>
        <div class="kpi-value">{sum(1 for r in items if r['hours'])} Hours · {sum(1 for r in items if r['published_cost_2_adults'])} Menus</div>
        <div class="kpi-sub">10/33 Beijing starred hours verified (up from 2/33 in repo root); Mio Mon-closure conflict flagged.</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Multi-Platform Review Links</div>
        <div class="kpi-value">{sum(len(r['social']) for r in items)} Verified</div>
        <div class="kpi-sub">YouTube oEmbed 200, direct TikTok clips &amp; official Instagram profiles — zero broken/private links.</div>
      </div>
    </section>

    <div class="filter-bar" data-filter-root>
      <input type="search" data-filter-search placeholder="Search restaurant, cuisine, hutong, hotel..." aria-label="Search restaurants">
      <select data-filter-key="city" aria-label="Filter by city">
        <option value="">All Cities</option>
        <option value="Beijing">Beijing</option>
        <option value="Shanghai">Shanghai</option>
      </select>
      <select data-filter-key="tier" aria-label="Filter by MICHELIN tier">
        <option value="">All Tiers</option>
        <option value="3 Stars">3 Stars</option>
        <option value="2 Stars">2 Stars</option>
        <option value="1 Star">1 Star</option>
        <option value="Bib Gourmand">Bib Gourmand</option>
        <option value="Selected">Selected</option>
      </select>
      <select data-filter-key="district" aria-label="Filter by district">
        <option value="">All Districts</option>
        {dist_opts}
      </select>
      <select data-filter-key="hours" aria-label="Filter by verified hours">
        <option value="">Hours: Any</option>
        <option value="yes">Verified Hours Only</option>
      </select>
      <select data-filter-key="social" aria-label="Filter by social reviews">
        <option value="">Reviews: Any</option>
        <option value="yes">Has Verified YT/TikTok/IG</option>
      </select>
      <button type="button" class="btn" data-filter-reset>Reset</button>
      <span class="filter-count" data-filter-count>Showing {len(items)} of {len(items)}</span>
    </div>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th style="min-width:260px">Restaurant, District &amp; Contact</th>
            <th style="min-width:170px">Official Operating Hours</th>
            <th style="min-width:190px">Published 2-Adult Menu Cost</th>
            <th style="min-width:250px">Verified Reviews (YT / TikTok / IG) &amp; Notes</th>
          </tr>
        </thead>
        <tbody>
          {''.join(rows)}
        </tbody>
      </table>
    </div>
    """
    return page_shell("restaurants.html", "MICHELIN Restaurants & Reviews", "All 33/33 Beijing 2027 starred restaurants plus verified Shanghai MICHELIN highlights and social reviews.", meta, body)


def build_activities(meta: dict, activities: dict) -> str:
    items = activities["items"]
    cards = []
    for a in items:
        flags_html = "".join(
            f'<div style="margin-top:8px;padding:8px 10px;border-radius:8px;background:var(--amber-soft);color:var(--amber);font-size:12.5px"><strong>Note / Flag:</strong> {e(fl)}</div>'
            for fl in a["flags"]
        )
        book_link = (
            f' · <a href="{e(a["booking_url"])}" target="_blank" rel="noopener noreferrer">Booking / Night Portal &rarr;</a>'
            if a["booking_url"] and a["booking_url"] != a["official_url"]
            else ""
        )
        search_blob = " ".join([a["name"], a["city"], a["district"], a["category"], a["hours"], a["closed_days"], a["transit"]])
        closed_tag = "Monday" if "CLOSED Mondays" in a["closed_days"] or "Closed Mondays" in a["closed_days"] else ("Tuesday" if "CLOSED Tuesdays" in a["closed_days"] else "OpenDaily")

        cards.append(
            f'<article class="card" data-filter-item data-city="{e(a["city"])}" data-closed="{closed_tag}" data-search="{e(search_blob)}">'
            f'<div class="card-header">'
            f'<div><div class="badges" style="margin:0 0 6px">'
            f'<span class="badge badge-sel">{e(a["city"])} · {e(a["district"])}</span>'
            f'<span class="badge badge-neutral">{e(a["category"])}</span>'
            f'<span class="badge badge-pass">Official Source Verified</span>'
            f'</div><h3>{e(a["name"])}</h3></div>'
            f'<div class="price-tag" style="font-size:15px;max-width:210px;text-align:right;white-space:normal">{e(a["cost_2_adults"])}<small>2 Adults Base</small></div>'
            f"</div>"
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Hours (Feb–Mar 2027):</strong> {e(a["hours"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Closed Days / Exceptions:</strong> {e(a["closed_days"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Per-Adult Tariff:</strong> {e(a["cost_1_adult"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Booking Rules:</strong> {e(a["booking_rules"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Subway / Access:</strong> {e(a["transit"])}</p>'
            f'<div style="margin-top:8px"><strong style="font-size:12.5px;color:var(--muted)">Verified Video Guides &amp; Reviews:</strong>{render_social_pills(a["social"], max_inline=6)}</div>'
            f'{flags_html}'
            f'<p style="margin:10px 0 0;font-size:12.5px;color:var(--muted)">Source: <a href="{e(a["official_url"])}" target="_blank" rel="noopener noreferrer">{e(a["source_note"])} &rarr;</a>{book_link}</p>'
            f"</article>"
        )

    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Official Municipal &amp; Operator Schedules · Verified {e(activities['verified_on'])}</span>
      <h1>Beijing &amp; Shanghai Activities, Hours &amp; Costs</h1>
      <p>{e(activities['coverage_note'])}</p>
    </section>

    <section class="callout callout-amber">
      <strong class="label">Critical Monday &amp; Tuesday Closure Cheat Sheet (Avoid Wasted Trips!)</strong>
      <p style="margin:4px 0 0;font-size:13.5px"><strong>Closed Mondays:</strong> Palace Museum (Forbidden City), National Museum of China, Temple of Heaven interior halls, Summer Palace interior halls, Tian'anmen Rostrum, Shanghai Museum West (People's Square), Yu Garden, and Da Vittorio / Mio / Sir Elly's.<br>
      <strong>OPEN Mondays (Use as Monday Anchors!):</strong> Nanluoguxiang, Jingshan Park, Yonghe Temple, Mutianyu Great Wall, <strong>Shanghai Museum East (Pudong — closes Tuesdays instead!)</strong>, The Bund (lights 17:00–21:00 winter), Shanghai Tower, and Yuyuan Bazaar.</p>
    </section>

    <div class="filter-bar" data-filter-root>
      <input type="search" data-filter-search placeholder="Search attraction, subway line, museum..." aria-label="Search activities">
      <select data-filter-key="city" aria-label="Filter by city">
        <option value="">All Cities (16)</option>
        <option value="Beijing">Beijing (10)</option>
        <option value="Shanghai">Shanghai (6)</option>
      </select>
      <select data-filter-key="closed" aria-label="Filter by closure day">
        <option value="">Closure Schedule: Any</option>
        <option value="OpenDaily">Open Daily (No Closure)</option>
        <option value="Monday">Closed Mondays</option>
        <option value="Tuesday">Closed Tuesdays (Open Mon!)</option>
      </select>
      <button type="button" class="btn" data-filter-reset>Reset</button>
      <span class="filter-count" data-filter-count>Showing {len(items)} of {len(items)}</span>
    </div>

    <div class="grid-2">
      {''.join(cards)}
    </div>
    """
    return page_shell("activities.html", "Activities & Official Hours", "10 Beijing + 6 Shanghai officially verified attractions with winter hours, CNY costs, and video guides.", meta, body)


def build_itineraries(meta: dict, itineraries: dict) -> str:
    rules_html = "".join(f"<li>{e(r)}</li>" for r in itineraries["scheduling_rules_enforced"])
    tab_btns = []
    tab_panels = []
    for idx, opt in enumerate(itineraries["options"]):
        act = " active" if idx == 1 else ""  # default open the 14-day / 13-night dual-city option
        tab_btns.append(
            f'<button type="button" class="tab-btn{act}" data-tab-target="{e(opt["id"])}">{e(opt["duration_band"])}</button>'
        )
        day_cards = []
        for d in opt["days"]:
            slots = []
            if d.get("morning"):
                slots.append(f"<li><strong>Morning:</strong> {e(d['morning'])}</li>")
            if d.get("afternoon"):
                slots.append(f"<li><strong>Afternoon:</strong> {e(d['afternoon'])}</li>")
            if d.get("evening"):
                slots.append(f"<li><strong>Evening:</strong> {e(d['evening'])}</li>")
            day_cards.append(
                f'<div class="day-card">'
                f'<div class="day-head"><span class="day-tag">{e(d["day"])}</span><span class="day-theme">{e(d["theme"])}</span></div>'
                f'<ul class="day-slots">{"".join(slots)}</ul>'
                f"</div>"
            )
        tab_panels.append(
            f'<div class="tab-panel{act}" data-tab-panel="{e(opt["id"])}">'
            f'<div class="card" style="margin-bottom:16px">'
            f'<span class="badge badge-sel">{e(opt["duration_band"])}</span>'
            f'<h2 style="margin-top:8px;border:none;padding:0">{e(opt["title"])}</h2>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Anchored Dates:</strong> {e(opt["dates"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Recommended Hotel Base:</strong> {e(opt["recommended_base"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Verified Cost Breakdown:</strong> {e(opt["verified_cost_summary"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0 0;color:var(--muted)"><strong>Best For:</strong> {e(opt["ideal_for"])}</p>'
            f"</div>"
            f'<div class="day-list">{"".join(day_cards)}</div>'
            f"</div>"
        )

    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">In-Scope Examples · 7 Nights or 14 Days / 13 Nights</span>
      <h1>Verified Itineraries (Starting Mon Feb 15, 2027)</h1>
      <p>Compare a <strong>7-night Beijing plan</strong> with a <strong>14-day / 13-night Beijing + Shanghai plan</strong> (7 Beijing nights + 6 Shanghai nights). If Feb 15 is check-in and Feb 18 checkout, the preferred interval is only 3 nights; its meaning remains unresolved and is not treated as a flexible-start window. No quote was captured for the six-night Shanghai stay (check-in Feb 22, checkout Feb 28). Restaurant/attraction hours, prices, and source/social links are listed on the <a href="restaurants.html">MICHELIN</a> and <a href="activities.html">Activities</a> pages.</p>
    </section>

    <section class="callout callout-jade">
      <strong class="label">Scheduling Rules Enforced Across Both In-Scope Itineraries</strong>
      <ul class="clean" style="font-size:13.5px">{rules_html}</ul>
    </section>

    <div class="tab-bar" role="tablist" aria-label="Itinerary options">
      {''.join(tab_btns)}
    </div>

    {''.join(tab_panels)}
    """
    return page_shell("itineraries.html", "Itineraries (1–2 Weeks)", "A 7-night Beijing example and a 14-day / 13-night Beijing–Shanghai example.", meta, body)


def build_questions(meta: dict, audit: dict) -> str:
    known_lis = "".join(f"<li>{e(k)}</li>" for k in audit["knowns"])
    unk_lis = "".join(f"<li>{e(u)}</li>" for u in audit["unknowns"])
    q_cards = []
    for idx, q in enumerate(audit["traveler_questions"], 1):
        opts = "".join(f"<li>{e(o)}</li>" for o in q["options"])
        reference_links = external_source_links(q.get("source_urls", []), "Reference")
        reference_html = f'<p style="font-size:12px;margin:8px 0 0">{reference_links}</p>' if reference_links else ""
        q_cards.append(
            f'<div class="card">'
            f'<span class="badge badge-high">Q{idx} · {e(q["priority"])}</span>'
            f'<h3 style="margin-top:8px">{e(q["question"])}</h3>'
            f'<p style="font-size:13.5px;color:var(--muted);margin:6px 0">{e(q["why_it_matters"])}</p>'
            f'<strong style="font-size:12.5px">Choices to confirm:</strong>'
            f'<ul class="clean" style="font-size:13.5px">{opts}</ul>'
            f"{reference_html}"
            f"</div>"
        )
    step_rows = "".join(
        f"<tr><td><strong>{e(s['phase'])}</strong></td><td>{e(s['owner'])}</td><td>{e(s['action'])}</td>"
        f"<td>{external_source_links(s.get('source_urls', []), 'Source') or 'No source link recorded'}</td></tr>"
        for s in audit["discovery_plan"]
    )
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Decisions &amp; Research Roadmap</span>
      <h1>Traveler Questions, Knowns vs. Unknowns &amp; Discovery Plan</h1>
      <p>Clear separation between source-backed facts, unknowns, and traveler decisions. Hotel quote captures span 2026-11-25–26; exact travel dates and live room terms still require a booking-time check. Hotel-to-venue ≤60-minute travel remains unverified.</p>
    </section>

    <section class="grid-2">
      <div class="card" style="border-top:4px solid var(--jade)">
        <h3>Verified Knowns ({len(audit['knowns'])})</h3>
        <ul class="clean" style="font-size:13.5px">{known_lis}</ul>
      </div>
      <div class="card" style="border-top:4px solid var(--amber)">
        <h3>Open Unknowns ({len(audit['unknowns'])})</h3>
        <ul class="clean" style="font-size:13.5px">{unk_lis}</ul>
      </div>
    </section>

    <section>
      <h2>Prioritized Questions for the Traveler</h2>
      <div class="grid-2">{''.join(q_cards)}</div>
    </section>

    <section>
      <h2>Chronological Discovery &amp; Booking Timeline</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Window</th><th>Owner</th><th>Concrete Action</th><th>Sources</th></tr></thead>
          <tbody>{step_rows}</tbody>
        </table>
      </div>
    </section>
    """
    return page_shell("questions.html", "Decisions, Knowns & Discovery Plan", "Traveler questions, verified knowns vs unknowns, and booking timeline.", meta, body)


def build_suggestions(meta: dict, audit: dict) -> str:
    cards = []
    for s in audit["suggestions"]:
        source_html = external_source_links(s.get("source_urls", []), "Source")
        source_paragraph = f'<p style="font-size:12px;margin:8px 0 0">{source_html}</p>' if source_html else ""
        cards.append(
            f'<article class="card">'
            f'<div class="badges" style="margin:0 0 8px"><span class="badge badge-sel">{e(s["id"])}</span><span class="badge badge-neutral">{e(s["category"])}</span><span class="badge badge-flag">Optional Idea — Not Assumed</span></div>'
            f'<h3>{e(s["title"])}</h3>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Idea:</strong> {e(s["idea"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0 0;color:var(--muted)"><strong>Trade-off:</strong> {e(s["tradeoff"])}</p>'
            f"{source_paragraph}"
            f"</article>"
        )
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Ideas for Traveler Approval · Strictly Separated from Verified Decisions</span>
      <h1>Suggestions &amp; Strategic Trade-Offs</h1>
      <p>Every item below is an <strong>optional idea</strong> grounded in our verified findings — nothing here is treated as a locked assumption until you approve it.</p>
    </section>

    <div class="grid-2">{''.join(cards)}</div>
    """
    return page_shell("suggestions.html", "Suggestions for Review", "Optional strategic ideas and trade-offs for traveler approval.", meta, body)


def build_flagged(meta: dict, audit: dict) -> str:
    gap_rows = "".join(
        f"<tr id=\"{e(g['id'])}\"><td><strong>{e(g['id'])}</strong><br><small>{e(g['area'])}</small></td>"
        f"<td><strong>{e(g['item'])}</strong></td>"
        f"<td><span class=\"badge badge-flag\">{e(g['status'])}</span></td>"
        f"<td>{e(g['detail'])}</td>"
        f"<td>{external_source_links(g.get('source_urls', []), 'Source') or e(g.get('source_note', 'No external source — remains unverified.'))}</td></tr>"
        for g in audit["flagged_own_gaps"]
    )
    aud_rows = []
    for a in audit["repo_audit_findings"]:
        sev_cls = (
            "badge-high" if a["severity"] == "HIGH"
            else ("badge-pass" if a["severity"] == "RESOLVED"
            else ("badge-flag" if a["severity"] == "MEDIUM" else "badge-neutral"))
        )
        aud_rows.append(
            f"<tr>"
            f"<td><strong>{e(a['id'])}</strong><br><span class=\"badge {sev_cls}\">{e(a['severity'])}</span></td>"
            f"<td><code>{e(a['file'])}</code></td>"
            f"<td>{e(a['finding'])}</td>"
            f"<td>{e(a['verified_truth'])}</td>"
            f"<td>{external_source_links(a.get('source_urls', []), 'Repository / official source') or 'No external source recorded'}</td>"
            f"</tr>"
        )
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Radical Transparency &amp; Line-by-Line Repo QA</span>
      <h1>Flagged for Review &amp; Repository-Wide Audit</h1>
      <p>Two distinct ledgers below: (1) every remaining unverified blank or official conflict inside <code>china-2027/</code>, and (2) every factual, structural, or CSV defect uncovered during our read-only line-by-line audit of existing repository files.</p>
    </section>

    <section>
      <h2>1. Flagged Gaps &amp; Official Conflicts Inside This Plan ({len(audit['flagged_own_gaps'])})</h2>
      <p class="lead">Where primary sources omit hours, prices, or future 2027 policy outcomes, we leave cells blank and list them explicitly below rather than fabricating numbers.</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>ID &amp; Area</th><th>Item</th><th>Status</th><th>Verification Detail</th><th>Source / Note</th></tr></thead>
          <tbody>{gap_rows}</tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>2. Line-by-Line Audit of Pre-Existing Repository Files ({len(audit['repo_audit_findings'])})</h2>
      <p class="lead">The rows below preserve findings from a read-only audit snapshot of <code>main @ 179e24c</code> on 2026-11-26. They are historical, not a statement of current status after later merges; use the cited repository and official pages to review each item.</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Audit ID</th><th>Repo File(s)</th><th>Defect Found</th><th>Audit Finding / Verified Truth</th><th>Source(s)</th></tr></thead>
          <tbody>{''.join(aud_rows)}</tbody>
        </table>
      </div>
    </section>
    """
    return page_shell("flagged.html", "Flagged Items & Repo Audit", "Remaining unverified items plus complete line-by-line repository QA audit.", meta, body)


def build_sources(meta: dict, sources: dict) -> str:
    sections = []
    for cat in sources["categories"]:
        rows = "".join(
            f'<tr><td><a href="{e(it["url"])}" target="_blank" rel="noopener noreferrer">{e(it["title"])} &rarr;</a></td>'
            f'<td style="white-space:nowrap">{e(it["checked"])}</td></tr>'
            for it in cat["items"]
        )
        sections.append(
            f"<section><h2>{e(cat['name'])} ({len(cat['items'])})</h2>"
            f'<div class="table-wrap"><table><thead><tr><th>Source</th><th>Checked On</th></tr></thead>'
            f"<tbody>{rows}</tbody></table></div></section>"
        )
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Source Register · Checked {e(meta['source_check_window'])}</span>
      <h1>Sources &amp; Verification Register</h1>
      <p>Official and primary sources are listed for government, museum, restaurant, and transit facts. Hotel prices are third-party Booking.com snapshots; review links are social-platform sources. Capture dates are shown per row, and venue-specific sources are linked on their MICHELIN and Activities rows.</p>
    </section>
    {''.join(sections)}
    """
    return page_shell("sources.html", "Sources & Verification Register", "Official sources, third-party hotel snapshots, and per-row verification dates.", meta, body)


def main() -> None:
    meta = load_json("meta.json")
    hotels = load_json("hotels.json")
    restaurants = load_json("restaurants.json")
    activities = load_json("activities.json")
    itineraries = load_json("itineraries.json")
    audit = load_json("audit_and_planning.json")
    sources = load_json("sources.json")

    pages = {
        "index.html": build_index(meta, hotels, restaurants, activities, audit),
        "hotels.html": build_hotels(meta, hotels),
        "restaurants.html": build_restaurants(meta, restaurants),
        "activities.html": build_activities(meta, activities),
        "itineraries.html": build_itineraries(meta, itineraries),
        "questions.html": build_questions(meta, audit),
        "suggestions.html": build_suggestions(meta, audit),
        "flagged.html": build_flagged(meta, audit),
        "sources.html": build_sources(meta, sources),
    }
    for fname, html_text in pages.items():
        (ROOT / fname).write_text(html_text, encoding="utf-8")
    print(f"Built {len(pages)} HTML pages in {ROOT}")


if __name__ == "__main__":
    main()

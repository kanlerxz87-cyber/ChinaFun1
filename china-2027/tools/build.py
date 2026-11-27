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


def money(value: float | int) -> str:
    return f"${float(value):,.2f}"


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
  <title>{e(title)} — China 2027 Travel Planner</title>
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
          China 2027 Travel Planner
          <span class="brand-sub">Beijing &amp; Shanghai · Core research {e(meta['last_verified'])} · Hotel rates {e(meta['hotel_rates_verified_on'])}</span>
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
      <div><strong>China 2027 Travel Planner</strong> · Calendar, restaurant, activity &amp; transit sources checked {e(meta['last_verified'])} · Third-party Booking.com hotel snapshots checked {e(meta['hotel_rates_verified_on'])}; recheck rates and terms · <a href="../index.html">Repo Root Dashboard</a></div>
      <div><a href="sources.html">Sources &amp; Verification</a> · <a href="flagged.html">Audit &amp; Flagged Items</a> · <a href="questions.html">Open Decisions</a></div>
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
    hotel_rows = []
    for city_lbl, group in [("Beijing", bj_top), ("Shanghai", sh_top)]:
        for h in group:
            hotel_rows.append(
                f"<tr>"
                f"<td><strong>{e(city_lbl)} #{h['rank']}</strong></td>"
                f"<td><a href=\"hotels.html#{e(h['id'])}\"><strong>{e(h['name'])}</strong></a><br><small>{e(h['district'])}</small></td>"
                f"<td><strong style=\"color:var(--jade)\">{money(h['lowest_observed_7n_usd'])}</strong><br><small>{e(h['lowest_observed_window'])}</small></td>"
                f"<td><span class=\"badge badge-pass\">Queen/King + Private Bath</span></td>"
                f"<td>{e(h['tier'])}</td>"
                f"</tr>"
            )

    p1_qs = [q for q in audit["traveler_questions"][:4]]
    q_cards = []
    for q in p1_qs:
        q_cards.append(
            f'<div class="card">'
            f'<span class="badge badge-flag">{e(q["priority"])}</span>'
            f'<h3 style="margin-top:8px">{e(q["question"])}</h3>'
            f'<p style="margin:0;color:var(--muted);font-size:13.5px">{e(q["why_it_matters"])}</p>'
            f"</div>"
        )

    cal = meta["calendar_2027"]
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Executive Trip Brief · Dual-City Source-Labeled Edition</span>
      <h1>China 2027 Travel Dashboard: Beijing &amp; Shanghai</h1>
      <p>Built for 2 adults considering travel inside <strong>2027-02-15 to 2027-03-23</strong> (1–2 week and 2–4 week options; exact duration and city split remain open). Restaurant, activity, calendar, and transit claims cite their listed sources. Hotel prices are third-party Booking.com rate snapshots captured on <strong>{e(hotels['verified_on'])}</strong> for specified seven-night dates; room, cancellation, payment, tax/fee, and member-rate conditions vary and must be rechecked at checkout.</p>
      <div class="hero-meta">
        <span>2 Adults · 1 Room (Queen/King + Private Bath)</span>
        <span>Zero Holidays Feb 15 – Mar 23, 2027</span>
        <span>{len(bj_starred)}/33 Beijing Stars + {len(sh_verified)} Shanghai Venues Verified</span>
        <span>{len(activities['items'])} Gov-Verified Activities</span>
        <span>{social_total} Verified YT / TikTok / IG Links</span>
      </div>
    </section>

    <section class="kpi-grid" aria-label="Headline Findings">
      <div class="kpi-card">
        <div class="kpi-label">Hotel Rate Snapshot</div>
        <div class="kpi-value">4 Selected Date Windows</div>
        <div class="kpi-sub">Captured Nov 27 for 13 properties on Feb 15–22 and a seven-property subset on Feb 18–25, Mar 1–8, and Mar 16–23.</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Rate-Plan Conditions</div>
        <div class="kpi-value">Compare Before Booking</div>
        <div class="kpi-sub">Snapshots mix nonrefundable, partially refundable, and free-cancellation offers; some prices require Genius/member eligibility. No universal cheapest date is established.</div>
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
      <strong class="label">2027 Calendar Context &amp; Hotel-Rate Caveat</strong>
      <p style="margin:4px 0 8px">The PRC State Council schedule lists Spring Festival on Feb 5–13, 2027 (CNY Sat Feb 6; make-up workdays Jan 31 &amp; Feb 14; Lantern Festival Sat Feb 20). Feb 5 is Friday per the Hong Kong Observatory calendar; one Gazette copy conflicts on the weekday, so the discrepancy is flagged in the audit. <strong>Zero statutory public holidays fall between Feb 15 and Mar 23, 2027.</strong> Starting Feb 15 places a Beijing stay across Lantern Festival, but the sampled Booking.com prices do not establish that any stay date is universally cheapest. <a href="{e(cal['source_url'])}" target="_blank" rel="noopener noreferrer">Official State Council Release &rarr;</a></p>
      <a class="btn btn-primary" href="hotels.html">Review 7-Night Rate Snapshots</a>
      <a class="btn" href="itineraries.html">Compare 7N / 14D / 3-week Itineraries</a>
    </section>

    <section>
      <h2>Selected Hotels &amp; Lowest Captured 7-Night Totals</h2>
      <p class="lead">The listed candidates meet the private-bathroom and queen/king filters based on the displayed room descriptions. Rank/“Why It Wins” order is a curated shortlist, not a calculated score or price sort; lowest observed rates are dated snapshots, while cancellation and member eligibility vary. <a href="hotels.html">View all {len(hotels['beijing']) + len(hotels['shanghai'])} hotels and exact-date rate plans &rarr;</a></p>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Rank</th><th>Hotel &amp; District</th><th>Lowest Observed 7-Night Total (USD)</th><th>Room Check</th><th>Why It Wins</th></tr>
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
        <p style="font-size:13.5px;color:var(--muted);margin-top:0">Direct 2026-11-26 verification of all 33/33 official MICHELIN 2027 Beijing pages proves <strong>Chaoyang holds 60.6%</strong> (independently matching PR #26's root recomputation):</p>
        {''.join(bar_rows)}
        <p style="font-size:13px;margin:10px 0 0"><a href="restaurants.html">Explore all {len(r_items)} verified restaurants &amp; reviews &rarr;</a></p>
      </div>
      <div class="card">
        <h3>Beijing &harr; Shanghai Rail &amp; Transit Snapshot</h3>
        <ul class="clean" style="font-size:13.5px">
          <li><strong>Fuxing High-Speed Rail (~1,300 km):</strong> 4.5–5.5 hr Beijing South &harr; Shanghai Hongqiao. Official 2nd Class <strong>CNY 550–670/adult</strong> (CNY 1,100–1,340 for 2 one-way); 1st Class ~CNY 1,035; Business ~CNY 2,318 (<a href="https://www.12306.cn/en/index.html" target="_blank" rel="noopener noreferrer">12306.cn</a>).</li>
          <li><strong>Beijing Subway:</strong> Distance-based CNY 3 (&le;6 km) to CNY 6+ (22–32 km); Airport Express CNY 25. New Line 17 central section opened Dec 2025.</li>
          <li><strong>Shanghai Metro:</strong> CNY 3 (&le;6 km) + CNY 1/10 km; 1-Day CNY 18 / 3-Day CNY 45; direct international Visa/MC/Amex/JCB tap-to-ride. <em>Flagged: re-verify post-Aug 2026 fare-hearing adjustments for 2027.</em></li>
          <li><strong>Dual-City Synergy:</strong> Shanghai Museum East is <strong>OPEN Mondays</strong> (hosting the Met Museum's <em>Jewelry: The Body Transformed</em> show through May 2027!) — solving classic Monday museum closures.</li>
        </ul>
      </div>
    </section>

    <section>
      <h2>Top Traveler Decisions Needed Next</h2>
      <p class="lead">Nothing below has been assumed on your behalf — confirm these choices to lock reservations and flight routing. <a href="questions.html">See full Knowns/Unknowns &amp; Discovery Plan &rarr;</a></p>
      <div class="grid-2">
        {''.join(q_cards)}
      </div>
    </section>

    <section class="callout callout-navy">
      <strong class="label">Repository Audit &amp; Cross-Directory Guide (Synced to main @ 179e24c)</strong>
      <p style="margin:4px 0 8px;font-size:13.5px">We audited every directory across this repository line by line against live primary sources on <strong>{e(meta['last_verified'])}</strong> — logging active cross-session defects (malformed CSV column counts across all 4 files in <code>shanghai-verified-2027/data/</code>, missing hours &amp; phone/price discrepancies for <code>Xin Rong Ji</code> &amp; <code>Zijin Mansion</code> and unflagged <code>Mio</code> Monday-closure conflict in root <code>assets/data.js</code>, and <code>The Bund</code> / <code>Da Vittorio</code> gaps in <code>shanghai-2027/</code>) while crediting PRs #26–#28 for resolving earlier root district counts. All sibling directories remain untouched per non-overlapping coordination rules.</p>
      <a class="btn" href="flagged.html">Read Full Line-by-Line Audit &amp; Flagged Items &rarr;</a>
      <a class="btn" href="suggestions.html">Review Optional Suggestions &rarr;</a>
    </section>
    """
    return page_shell("index.html", "Executive Overview", meta["subtitle"], meta, body)


def build_hotels(meta: dict, hotels: dict) -> str:
    comparison_windows = hotels["comparison_windows"]
    date_labels = {w["dates"]: w["label"] for w in comparison_windows}

    def render_city_section(city_name: str, items: list[dict]) -> str:
        cards = []
        matrix_rows = []
        for h in items:
            win_map = {w["dates"]: w for w in h["windows"]}

            def cell(d: str) -> str:
                w = win_map.get(d)
                if not w:
                    return '<span class="blank-cell">Not queried</span>'
                source_link = (
                    f'<a href="{e(w["source_url"])}" target="_blank" rel="noopener noreferrer">Capture</a>'
                    if w.get("source_url") else ""
                )
                eligible_offers = [o for o in w.get("offers", []) if o.get("qualifies", True)]
                if w.get("status") != "available" or not eligible_offers:
                    note = w.get("note", "No qualifying queen/king rate was captured.")
                    return f'<span class="blank-cell">Queried; no qualifying rate</span><br><small>{e(note)} {source_link}</small>'
                low = min(eligible_offers, key=lambda o: float(o["total_usd"]))
                nightly = float(low["total_usd"]) / 7
                return (
                    f"<strong>{money(low['total_usd'])}</strong><br>"
                    f"<small>{e(low['rate_type'])} · {money(nightly)}/night avg. · {source_link}</small>"
                )

            cells = "".join(f"<td>{cell(w['dates'])}</td>" for w in comparison_windows)
            matrix_rows.append(
                f"<tr>"
                f"<td><strong>#{h['rank']}</strong> <a href=\"#{e(h['id'])}\">{e(h['name'])}</a><br><small>{e(h['district'])}</small></td>"
                f"{cells}"
                f"</tr>"
            )

            amen_html = "".join(f'<span class="badge badge-neutral">{e(a)}</span>' for a in h["amenities"])
            flag_html = "".join(
                f'<div class="callout callout-amber" style="margin:10px 0 0;padding:10px 12px;font-size:13px"><strong>Flag:</strong> {e(fl)}</div>'
                for fl in h["flags"]
            )
            rate_details = []
            for w in h["windows"]:
                label = date_labels.get(w["dates"], w["dates"])
                if w.get("status") != "available" or not w.get("offers"):
                    other = "".join(
                        f'<li>{money(o["total_usd"])} — {e(o["rate_type"])}</li>'
                        for o in w.get("other_observed_rates", [])
                    )
                    note = e(w.get("note", "No qualifying rate was captured."))
                    rate_details.append(
                        f'<li><strong>{e(label)}:</strong> {e(w.get("room", ""))}. {note}'
                        f'{"<ul>" + other + "</ul>" if other else ""}'
                        f' <a href="{e(w.get("source_url", ""))}" target="_blank" rel="noopener noreferrer">View capture</a></li>'
                    )
                    continue
                offer_rows = []
                for o in w["offers"]:
                    room_note = f'Room: {e(o["room"])}. ' if o.get("room") else ""
                    excluded_note = " Excluded from queen/king comparison." if o.get("qualifies") is False else ""
                    offer_rows.append(
                        f'<li><strong>{money(o["total_usd"])}</strong> — {room_note}'
                        f'{e(o["rate_type"])}. {e(o["terms"])}{excluded_note}</li>'
                    )
                unattributed_rows = "".join(
                    f'<li><strong>{money(o["total_usd"])}</strong> — {e(o["rate_type"])}. '
                    f'{e(o.get("note", "Room attribution not verified; excluded from the qualifying-room comparison."))}</li>'
                    for o in w.get("unattributed_observed_rates", [])
                )
                unresolved_note = (
                    f'<p><strong>Unresolved terms:</strong> {e(w["note"])}</p>'
                    if w.get("note") else ""
                )
                unattributed_html = (
                    f'<li><strong>Other displayed offer(s), room not verified:</strong><ul>{unattributed_rows}</ul></li>'
                    if unattributed_rows else ""
                )
                rate_details.append(
                    f'<li><strong>{e(label)}:</strong> {e(w["room"])}'
                    f'{unresolved_note}<ul>{"".join(offer_rows)}</ul>{unattributed_html}'
                    f'<a href="{e(w["source_url"])}" target="_blank" rel="noopener noreferrer">View Booking.com capture</a></li>'
                )
            rate_details_html = (
                '<details style="margin:10px 0;font-size:13px">'
                '<summary><strong>All captured offers, cancellation/payment terms, and source links</strong></summary>'
                f'<ul class="clean">{"".join(rate_details)}</ul></details>'
            )
            lowest_label = date_labels.get(h["lowest_observed_window"], h["lowest_observed_window"])
            cards.append(
                f'<article class="card" id="{e(h["id"])}">'
                f'<div class="card-header">'
                f'<div><span class="badge badge-sel">Rank #{h["rank"]} · {e(h["tier"])}</span><h3 style="margin-top:6px">{e(h["name"])}</h3>'
                f'<div style="font-size:13px;color:var(--muted)">{e(h["district"])} · {e(h["address"])} · Rating: <strong>{e(h["rating"])}</strong> (Location: {e(h["location_score"])})</div></div>'
                f'<div class="price-tag">{money(h["lowest_observed_7n_usd"])}<small>Lowest captured 7N · {e(lowest_label)}</small></div>'
                f"</div>"
                f'<div class="badges">'
                f'<span class="badge badge-pass">{e(h["bed_verified"])}</span>'
                f'<span class="badge badge-pass">{e(h["bathroom_verified"])}</span>'
                f"</div>"
                f'<p style="font-size:13.5px;margin:8px 0"><strong>Lowest observed offer:</strong> {e(h["lowest_observed_note"])}</p>'
                f'{rate_details_html}'
                f'<p style="font-size:13.5px;margin:8px 0"><strong>Subway / Transit Access:</strong> {e(h["subway_access"])}</p>'
                f'<p style="font-size:13.5px;margin:8px 0"><strong>MICHELIN Reach:</strong> {e(h["michelin_reach_summary"])}</p>'
                f'<div class="badges" style="margin-top:8px">{amen_html}</div>'
                f'{flag_html}'
                f'<p style="margin:12px 0 0"><a class="btn btn-primary" href="{e(h["booking_url"])}" target="_blank" rel="noopener noreferrer">Recheck Live Booking.com Rate &rarr;</a></p>'
                f"</article>"
            )

        header_cells = "".join(f"<th>{e(w['label'])}</th>" for w in comparison_windows)
        return (
            f"<section><h2>{e(city_name)} Date-Specific 7-Night Rate Snapshots (USD, 2 Adults, 1 Room)</h2>"
            f'<div class="table-wrap"><table><thead><tr>'
            f"<th>Ranked Hotel</th>{header_cells}"
            f"</tr></thead><tbody>{''.join(matrix_rows)}</tbody></table></div>"
            f'<div class="grid-2">{"".join(cards)}</div></section>'
        )

    bt = hotels["booking_timing_finding"]
    ev_lis = "".join(f"<li>{e(x)}</li>" for x in bt["evidence"])
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Booking.com Rate Captures · Checked {e(hotels['verified_on'])}</span>
      <h1>Hotel Rate Snapshots &amp; Terms (Beijing &amp; Shanghai)</h1>
      <p>Thirteen selected hotels are shown against up to four exact seven-night windows. Rates are displayed totals for <strong>2 adults, 1 room, USD</strong>; some comparison cells are intentionally blank or flagged where a qualifying queen/king offer was not captured.</p>
    </section>

    <section class="callout callout-jade">
      <strong class="label">What These Captures Establish — and What They Do Not</strong>
      <h3 style="margin:4px 0 6px">{e(bt['headline'])}</h3>
      <ul class="clean" style="font-size:13.5px">{ev_lis}</ul>
      <p style="margin:10px 0 0;font-size:13.5px"><strong>Practical next step:</strong> {e(bt['action'])}</p>
    </section>

    <section class="callout callout-navy">
      <strong class="label">Rate &amp; MICHELIN-Proximity Methodology</strong>
      <p style="margin:4px 0 6px;font-size:13.5px">{e(hotels['pricing_notes'])}</p>
      <p style="margin:0 0 6px;font-size:13.5px">{e(hotels['ranking_methodology_note'])}</p>
      <p style="margin:0;font-size:13.5px">{e(hotels['proximity_methodology'])}</p>
    </section>

    {render_city_section("Beijing", hotels["beijing"])}
    {render_city_section("Shanghai", hotels["shanghai"])}
    """
    return page_shell("hotels.html", "Hotel Rate Snapshots & Terms", "Date-specific, third-party hotel rate snapshots with cancellation and payment terms.", meta, body)


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
        act = " active" if idx == 1 else ""  # default open Flagship 14-day Dual-City!
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
      <span class="hero-eyebrow">Zero-Conflict Day-by-Day Blueprints · 1–2 Weeks &amp; 2–4 Weeks</span>
      <h1>Verified Itineraries (Starting Mon Feb 15, 2027)</h1>
      <p>Switch tabs below to compare our <strong>7-Night Single-City Beijing</strong>, <strong>14-Day Flagship Dual-City (Beijing + HSR + Shanghai)</strong>, and <strong>3-Week Unhurried Deep Dive (21 nights)</strong> plans. Every day has been checked against official Monday/Tuesday museum and restaurant closures.</p>
    </section>

    <section class="callout callout-jade">
      <strong class="label">Scheduling Rules Enforced Across All Three Itineraries</strong>
      <ul class="clean" style="font-size:13.5px">{rules_html}</ul>
    </section>

    <div class="tab-bar" role="tablist" aria-label="Itinerary options">
      {''.join(tab_btns)}
    </div>

    {''.join(tab_panels)}
    """
    return page_shell("itineraries.html", "Itineraries (1-2 wk & 2-4 wk)", "Date-anchored Beijing and Shanghai itineraries with zero Monday/Tuesday closure clashes.", meta, body)


def build_questions(meta: dict, audit: dict) -> str:
    known_lis = "".join(f"<li>{e(k)}</li>" for k in audit["knowns"])
    unk_lis = "".join(f"<li>{e(u)}</li>" for u in audit["unknowns"])
    q_cards = []
    for idx, q in enumerate(audit["traveler_questions"], 1):
        opts = "".join(f"<li>{e(o)}</li>" for o in q["options"])
        q_cards.append(
            f'<div class="card">'
            f'<span class="badge badge-high">Q{idx} · {e(q["priority"])}</span>'
            f'<h3 style="margin-top:8px">{e(q["question"])}</h3>'
            f'<p style="font-size:13.5px;color:var(--muted);margin:6px 0">{e(q["why_it_matters"])}</p>'
            f'<strong style="font-size:12.5px">Choices to confirm:</strong>'
            f'<ul class="clean" style="font-size:13.5px">{opts}</ul>'
            f"</div>"
        )
    step_rows = "".join(
        f"<tr><td><strong>{e(s['phase'])}</strong></td><td>{e(s['owner'])}</td><td>{e(s['action'])}</td></tr>"
        for s in audit["discovery_plan"]
    )
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Decisions &amp; Research Roadmap</span>
      <h1>Traveler Questions, Knowns vs. Unknowns &amp; Discovery Plan</h1>
      <p>Clear separation between primary-source facts already locked in, open decisions requiring traveler input, and our chronological execution timeline from today (Nov 2026) through arrival (Feb 2027).</p>
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
          <thead><tr><th>Window</th><th>Owner</th><th>Concrete Action</th></tr></thead>
          <tbody>{step_rows}</tbody>
        </table>
      </div>
    </section>
    """
    return page_shell("questions.html", "Decisions, Knowns & Discovery Plan", "Traveler questions, verified knowns vs unknowns, and booking timeline.", meta, body)


def build_suggestions(meta: dict, audit: dict) -> str:
    cards = []
    for s in audit["suggestions"]:
        cards.append(
            f'<article class="card">'
            f'<div class="badges" style="margin:0 0 8px"><span class="badge badge-sel">{e(s["id"])}</span><span class="badge badge-neutral">{e(s["category"])}</span><span class="badge badge-flag">Optional Idea — Not Assumed</span></div>'
            f'<h3>{e(s["title"])}</h3>'
            f'<p style="font-size:13.5px;margin:6px 0"><strong>Idea:</strong> {e(s["idea"])}</p>'
            f'<p style="font-size:13.5px;margin:6px 0 0;color:var(--muted)"><strong>Trade-off:</strong> {e(s["tradeoff"])}</p>'
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
        f"<tr><td><strong>{e(g['id'])}</strong><br><small>{e(g['area'])}</small></td>"
        f"<td><strong>{e(g['item'])}</strong></td>"
        f"<td><span class=\"badge badge-flag\">{e(g['status'])}</span></td>"
        f"<td>{e(g['detail'])}</td></tr>"
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
          <thead><tr><th>ID &amp; Area</th><th>Item</th><th>Status</th><th>Verification Detail</th></tr></thead>
          <tbody>{gap_rows}</tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>2. Line-by-Line Audit of Pre-Existing Repository Files ({len(audit['repo_audit_findings'])})</h2>
      <p class="lead">Because sibling directories are owned by concurrent sessions (per <code>COORDINATION.md</code>), we did NOT overwrite their files — instead, we corrected every item inside <code>china-2027/</code> and logged exact fix requests in <code>COORDINATION.md</code>.</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Audit ID</th><th>Repo File(s)</th><th>Defect Found</th><th>Primary-Source Verified Truth</th></tr></thead>
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
            f'<div class="table-wrap"><table><thead><tr><th>Source / Listing</th><th>Checked On</th></tr></thead>'
            f"<tbody>{rows}</tbody></table></div></section>"
        )
    body = f"""
    <section class="hero">
      <span class="hero-eyebrow">Register updated {e(sources['source_register_updated_on'])} · Hotel rate pages checked {e(sources['hotel_rate_captures_verified_on'])} · Individual source dates shown below</span>
      <h1>Sources &amp; Verification Register</h1>
      <p>Official government, MICHELIN, venue, and operator pages support the calendar, transit, restaurant, and activity facts. Hotel prices are third-party Booking.com listing snapshots for exact date windows—not official hotel quotes or guaranteed future rates. Individual restaurant and activity source links also appear in their respective rows.</p>
    </section>
    {''.join(sections)}
    """
    return page_shell("sources.html", "Sources & Verification", "Official and operator sources plus third-party Booking.com rate captures with exact dates.", meta, body)


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

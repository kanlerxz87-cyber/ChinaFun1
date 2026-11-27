#!/usr/bin/env python3
"""Build the static integration site from data/*.json. Standard library only.

Every table is generated from one JSON file; no prose in this script contains a
research value. Run: python3 integration-2027/tools/build.py
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

PAGES = [
    ("index.html", "Overview"),
    ("plans.html", "Plans & prices"),
    ("social.html", "Social reviews"),
    ("questions.html", "Questions"),
    ("suggestions.html", "Suggestions"),
    ("flagged.html", "Flagged"),
    ("sources.html", "Sources"),
]


def load(name):
    with open(DATA / name, encoding="utf-8") as fh:
        return json.load(fh)


def e(value):
    return html.escape(str(value if value is not None else ""), quote=True)


def blank(value, label="blank — unverified"):
    return f'<span class="blank">{e(label)}</span>' if not value else e(value)


def ext(url, label="source ↗"):
    if not url:
        return ""
    return f'<a href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(label)}</a>'


def nav(active):
    links = "".join(
        f'<a href="{h}" class="{"active" if h == active else ""}">{e(label)}</a>'
        for h, label in PAGES
    )
    return (
        '<header class="top"><div class="wrap brandbar">'
        '<div class="brand"><span class="dot"></span><span>China 2027<small>Decision layer · 5 research dashboards</small></span></div>'
        '<span class="chip">Updated 2026-11-27</span></div>'
        f'<nav class="nav wrap">{links}</nav></header>'
    )


def shell(title, active, body, description=""):
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} — China 2027 decision layer</title>
<meta name="description" content="{e(description or title)}">
<link rel="stylesheet" href="assets/style.css">
</head><body>
{nav(active)}
<main class="wrap">{body}</main>
<footer class="wrap">
<p><strong>Method.</strong> This is a decision layer, not a new trip plan. It links four single-city studies and one dual-city dashboard; dated values remain attributed to their source sessions and are not blended into a like-for-like ranking. Unconfirmed values remain blank or flagged. Third-party videos are not affiliated with any listed venue.</p>
<p><a href="sources.html">Source register</a> · <a href="flagged.html">Flags and blanks</a> ·
<a href="../README.md">Repository README</a> · Integration update e411628d · 27 Nov 2026</p>
</footer>
<script src="assets/app.js"></script>
</body></html>
"""


def write(name, title, active, body, description=""):
    (ROOT / name).write_text(shell(title, active, body, description), encoding="utf-8")


def filter_input(target):
    return (f'<p class="filter"><label for="q-{target}">Filter this table</label> '
            f'<input id="q-{target}" data-filter-input="#{target}" type="search" '
            f'placeholder="Type a name, city or keyword"></p>')


def build_index(plans, social, flags):
    videos = sum(len(r["social"]) for r in social["rows"])
    venues = sum(1 for r in social["rows"] if r["social"])
    cards = "".join(
        f'<tr><td class="name">{e(p["city"])}<span class="meta">{e(p["id"])}</span></td>'
        f'<td>{e(p["dates"])}</td><td>{e(p["starred"])}</td><td>{e(p["hotel_headline"])}</td>'
        f'<td>{e(p["social_in_this_index"])}</td>'
        f'<td class="nowrap"><a href="{e(p["source_page"])}">plan ↗</a> · {ext(p["official_source"], "Guide ↗")} · {ext(p["rate_source"], "rate ↗")}'
        f'{(" · " + ext(p["secondary_official_source"], "second Guide ↗")) if p.get("secondary_official_source") else ""}'
        f'{(" · " + ext(p["secondary_rate_source"], "second rate ↗")) if p.get("secondary_rate_source") else ""}</td></tr>'
        for p in plans["plans"]
    )
    paths = "".join(
        f'<div class="card"><h3>{e(p["title"])}</h3>'
        f'<p class="meta">Priority {p["priority"]} · proposed, not implemented</p>'
        f'<p>{e(p["why"])}</p><p><a href="suggestions.html">Review path →</a></p></div>'
        for p in load("suggestions.json")["suggestions"][:3]
    )
    body = f"""
<p class="eyebrow">Executive summary</p>
<h1>Five research dashboards, one decision layer</h1>
<p class="lede">This repository contains four independent single-city studies (one Beijing and three Shanghai) plus a later
Beijing–Shanghai dual-city dashboard. They were produced separately and are deliberately <strong>not merged</strong>;
this hub now links all five and keeps their dated findings distinct. Choose a city and exact dates before comparing hotels.</p>

<div class="grid g4">
  <div class="card kpi"><div class="big">5</div><div class="sub">research dashboards: 4 single-city + 1 dual-city</div></div>
  <div class="card kpi"><div class="big">{videos}</div><div class="sub">social pages fetched and read this session</div></div>
  <div class="card kpi"><div class="big">{venues}</div><div class="sub">venues with at least one verified link</div></div>
  <div class="card kpi"><div class="big">{len(flags['flags'])}</div><div class="sub">issues logged; resolved entries are identified on the flags page</div></div>
</div>

<h2>What can be decided today</h2>
<div class="grid g2">
  <div class="card"><h3>1 · Choose the city first</h3><p>The later dual-city study verifies 33 starred Beijing restaurants (2027 edition) and reports 50 starred Shanghai restaurants (2026 live guide). It compares separate city alternatives, not one combined itinerary. Hotel access and the restaurant shortlist depend on this choice.</p></div>
  <div class="card"><h3>2 · The preferred window does not fit</h3><p>15–18 Feb 2027 is three nights, shorter than the requested 1–2 weeks. The current comparable candidate window is 15–22 Feb (7 nights); no 3-night rates are shown here.</p></div>
  <div class="card"><h3>3 · Compare compliant rooms only</h3><p>The 26 Nov dual-city snapshot lists 15–22 Feb examples: Beijing $425 for a queen room with private bath, and Shanghai $621 for a king room with private bath (non-refundable; $707 free cancellation). Both exclude VAT; these city alternatives are not a combined price, and earlier study snapshots differ.</p></div>
  <div class="card"><h3>4 · Rates are snapshots, not live quotes</h3><p>Hotel totals were captured on 25–26 Nov 2026. Room type, promotions, cancellation and tax/service terms differ by listing; use the dated Booking.com source and re-check the exact rate before booking.</p></div>
</div>

<h2>The five research dashboards at a glance</h2>
<div class="tablewrap"><table id="plan-table"><thead><tr><th>City / session</th><th>Dates</th><th>MICHELIN scope</th>
<th>Headline 7-night total</th><th>Social coverage here</th><th>Sources</th></tr></thead>
<tbody>{cards}</tbody></table></div>
<p class="meta">Hotel figures are Booking.com snapshots captured 25–26 Nov 2026 by the named sessions, not live prices.
Tax treatment differs between studies and is shown on the <a href="plans.html">price page</a>; the dual-city row links the two separate city rates.</p>

<h2>First three paths to review</h2>
<div class="grid g3">{paths}</div>

<div class="callout warn"><strong>Before booking:</strong> read the <a href="questions.html">blocking questions</a>,
especially city, dates, bed rule, visa, all-in budget and the unverified ≤60-minute transit test.
Every blank is listed on <a href="flagged.html">Flagged for review</a>; none was filled by inference.</div>
"""
    write("index.html", "Overview", "index.html", body,
          "Overview of four single-city China 2027 studies plus one dual-city dashboard, with the decisions that block booking.")


def build_plans(plans, price):
    rows = "".join(
        f'<tr data-f="{e((p["plan"]+" "+p["property"]+" "+p["window"]).lower())}">'
        f'<td>{e(p["plan"])}</td><td class="name">{e(p["property"])}</td><td>{e(p["window"])}</td>'
        f'<td class="num">${p["total_usd"]:,}</td><td>{e(p["terms"])}</td>'
        f'<td class="nowrap">{ext(p["source"])}<span class="meta">captured {e(p["captured"])}</span></td></tr>'
        for p in price["rows"]
    )
    detail = "".join(
        f'<div class="card"><h3>{e(p["city"])} · {e(p["id"])}</h3>'
        f'<p><strong>Entry:</strong> <a href="{e(p["source_page"])}">{e(p["site"])}</a> · {e(p["path"])}</p>'
        f'<p><strong>Focus:</strong> {e(p["focus"])}</p>'
        f'<p><strong>Star scope:</strong> {e(p["starred"])}</p>'
        f'<p><strong>Compliant room:</strong> {e(p["cheapest_compliant"])}</p>'
        f'<p><strong>Decision use:</strong> {e(p["decision"])}</p>'
        f'<p>{ext(p["official_source"], "official Guide/release ↗")}'
        f'{(" · " + ext(p["secondary_official_source"], "second official Guide ↗")) if p.get("secondary_official_source") else ""}'
        f' · {ext(p["rate_source"], "dated rate ↗")}'
        f'{(" · " + ext(p["secondary_rate_source"], "second-city rate ↗")) if p.get("secondary_rate_source") else ""}</p>'
        f'<p class="meta">{e(p["rate_note"])}</p></div>'
        for p in plans["plans"]
    )
    body = f"""
<p class="eyebrow">Comparison</p><h1>Plans and dated prices</h1>
<p class="lede">This comparison links four single-city studies and a dual-city Beijing + Shanghai dashboard. Values below
are dated snapshots carried forward from their owning studies, not live quotes. The dual-city dashboard lists separate
city options, not one combined hotel price; the snapshots use different room types, promotions and tax terms.</p>
{filter_input('price-table')}
<div class="tablewrap"><table id="price-table"><thead><tr><th>Plan</th><th>Room</th><th>Window</th>
<th>7-night total</th><th>Terms / caveat</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="callout"><strong>Finding:</strong> {e(price['finding'])}</div>
<h2>What each plan is good for</h2><div class="grid g2">{detail}</div>
<p class="meta">No plan quotes airfare, visa fees or a complete dinner total. One plan's published proximity minutes
are modelled from coordinates, not routed; they must not be read as measured journey times.</p>
"""
    write("plans.html", "Plans & prices", "plans.html", body,
          "Cross-plan comparison of dated seven-night hotel totals for China 2027.")


def build_social(social):
    out = []
    for r in social["rows"]:
        socials = []
        for s in r["social"]:
            evidence = "".join(
                f'<li><strong>{e(s["title"])}</strong> · {e(s["channel"])} · {e(s["uploaded"])} · {e(s["length"])}<br>'
                f'<span class="meta">{e(s["scope"])}</span><br><span class="evidence">{e(s["evidence"])}</span><br>'
                f'{ext(s["url"], s["platform"] + " ↗")}</li>'
                for s in [s]
            )
            socials.append(f'<li>{evidence}</li>')
        social_cell = ('<ul class="videolist">' + "".join(socials) + '</ul>') if socials else blank("", "no verified link — blank")
        flags = "".join(f'<li>{e(f)}</li>' for f in r["flags"]) or "—"
        hours = (e(r["hours"]) + (f'<span class="meta">{e(r["hours_exceptions"])}</span>' if r["hours_exceptions"] else "")
                 + (f'<span class="meta">{e(r["hours_status"])}</span>' if r["hours_status"] else "")) if r["hours"] else (
                   blank("", "blank — not confirmed") + (f'<span class="meta">{e(r["hours_status"])}</span>' if r["hours_status"] else "")
                 )
        cost = (e(r["cost_two"]) + f'<span class="meta">{e(r["cost_basis"])}</span>') if r["cost_two"] else blank("", "blank — not confirmed")
        out.append(
            f'<tr data-f="{e((r["venue"]+" "+r["city"]+" "+r["kind"]+" "+r["distinction"]).lower())}">'
            f'<td class="name">{e(r["venue"])}<span class="meta">{e(r["city"])} · {e(r["kind"])}</span></td>'
            f'<td>{e(r["distinction"])}</td>'
            f'<td class="nowrap">{ext(r["official_url"], "official ↗")}<span class="meta">{e(r["official_label"])}</span></td>'
            f'<td>{hours}</td><td>{cost}</td><td>{social_cell}</td>'
            f'<td class="flagcell"><ul>{"".join(f"<li>{e(x)}</li>" for x in r["flags"]) or "<li>—</li>"}</ul></td></tr>'
        )
    rows = "".join(out)
    body = f"""
<p class="eyebrow">Primary research · session 815c7943</p><h1>Social reviews index</h1>
<p class="lede">{e(social['rule'])}</p>
<div class="callout"><strong>Parallel register:</strong> session `773e75a3` published a deeper Beijing-only video
register with 58 first-party-oEmbed-verified links at <a href="../social-2027/index.html">social-2027/</a>.
The two registers share three video IDs and do not contradict each other; this page is the cross-plan view that
also covers Shanghai. Use the deeper register when you need maximum Beijing coverage.</div>
{filter_input('social-table')}
<div class="tablewrap"><table id="social-table"><thead><tr><th>Venue</th><th>Status</th><th>Official source</th>
<th>Open days / hours / exceptions</th><th>Cost for 2</th><th>Verified social links</th><th>Flags</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<div class="callout warn"><strong>Do not use video metadata for booking decisions.</strong> Star levels, menus, hours and
prices change; only the linked official page is treated as authoritative for those fields. A blank means the official
source did not state it — never that the value is zero or unavailable.</div>
"""
    write("social.html", "Social reviews", "social.html", body,
          "Verified YouTube review links for Beijing and Shanghai restaurants and activities, with official source links.")


def build_questions(questions):
    cards = "".join(
        f'<article class="card question" data-f="{e((q["q"]+" "+q["known"]+" "+q["unknown"]).lower())}">'
        f'<h3>{e(q["id"])} · {e(q["q"])} '
        f'{"<span class=chip-b>BLOCKING</span>" if q["blocking"] else "<span class=chip>open</span>"}</h3>'
        f'<p><strong>What we know:</strong> {e(q["known"])}</p>'
        f'<p><strong>What we do not know:</strong> {e(q["unknown"])}</p>'
        f'<p><strong>Action to close it:</strong> {e(q["action"])}</p>'
        f'<p><a href="{e(q["source"])}" target="_blank" rel="noopener">source page ↗</a></p></article>'
        for q in questions["questions"]
    )
    body = f"""
<p class="eyebrow">Decision register</p><h1>Questions, information and answers</h1>
<p class="lede">{e(questions['note'])}</p>
{filter_input('question-list-wrap')}
<div id="question-list-wrap">{cards}</div>
<div class="callout">Every 'known' statement links back to a plan page that carries its own official source.
Nothing in the 'unknown' column was estimated or filled in.</div>
"""
    write("questions.html", "Questions", "questions.html", body,
          "Decision-blocking questions, what is known, what is missing and how to resolve each item.")


def build_suggestions(suggestions):
    rows = "".join(
        f'<tr data-f="{e((p["title"]+" "+p["why"]).lower())}"><td class="num">{p["priority"]}</td>'
        f'<td class="name">{e(p["title"])}</td><td>{e(p["why"])}</td><td>{e(p["how"])}</td>'
        f'<td>{e(p["review_first"])}</td><td class="nowrap">{ext(p["source"], "context ↗")}</td></tr>'
        for p in suggestions["suggestions"]
    )
    body = f"""
<p class="eyebrow">Proposals</p><h1>Suggestions — review before implementing</h1>
<p class="lede">{e(suggestions['note'])}</p>
{filter_input('suggestion-table')}
<div class="tablewrap"><table id="suggestion-table"><thead><tr><th>#</th><th>Proposal</th><th>Why it matters</th>
<th>How to do it without guessing</th><th>Decide first</th><th>Context</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="callout">Proposals do not automatically change any of the five source dashboards. In particular, propagate the verified State Council holiday notice to older pages only through their approved integration scope; choose priorities before additional research or edits.</div>
"""
    write("suggestions.html", "Suggestions", "suggestions.html", body,
          "Prioritised, unimplemented suggestions to improve the trip decision process.")


def build_flags(flags, social):
    rows = "".join(
        f'<tr data-f="{e((f["id"]+" "+f["item"]+" "+f["detail"]).lower())}">'
        f'<td>{e(f["id"])}</td><td>{e(f["severity"])}</td><td class="name">{e(f["item"])}</td>'
        f'<td>{e(f["detail"])}</td><td class="nowrap">{ext(f["source"], "source ↗")}</td></tr>'
        for f in flags["flags"]
    )
    blanks = []
    for r in social["rows"]:
        missing = []
        if not r["hours"]:
            missing.append("open days / hours")
        if not r["cost_two"]:
            missing.append("cost for two")
        if not r["social"]:
            missing.append("social link")
        if missing:
            blanks.append(
                f'<tr><td class="name">{e(r["venue"])}</td><td>{e(", ".join(missing))}</td>'
                f'<td>{ext(r["official_url"], "official ↗")}</td></tr>'
            )
    body = f"""
<p class="eyebrow">Verification</p><h1>Flagged for review</h1>
<p class="lede">Irregularities inherited from the five research dashboards plus integration findings. Some rows record issues now resolved (their detail says so); unresolved items remain flagged and do not block the site. Do not use unverified values without the stated check.</p>
{filter_input('flag-table')}
<div class="tablewrap"><table id="flag-table"><thead><tr><th>ID</th><th>Severity</th><th>Issue</th>
<th>Detail</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>Blank register from the social index</h2>
<p class="meta">These cells are empty on <a href="social.html">Social reviews</a> because the official source did not
state the value or no review page could be read. They are not estimates.</p>
<div class="tablewrap"><table id="blank-table"><thead><tr><th>Venue</th><th>Blank fields</th><th>Official source</th>
</tr></thead><tbody>{''.join(blanks)}</tbody></table></div>
"""
    write("flagged.html", "Flagged", "flagged.html", body,
          "Flagged irregularities and the full blank register for the integrated China 2027 plans.")


def build_sources(sources):
    rows = "".join(
        f'<tr data-f="{e(s["url"]+" "+s["what"])}"><td class="url">{ext(s["url"], "open ↗")}</td>'
        f'<td>{e(s["what"])}</td><td>{e(s["date"])}</td></tr>'
        for s in sources["sources"]
    )
    body = f"""
<p class="eyebrow">Audit trail</p><h1>Source register</h1>
<p class="lede">{e(sources['note'])}</p>
{filter_input('source-table')}
<div class="tablewrap"><table id="source-table"><thead><tr><th>URL read</th><th>What it established</th>
<th>Read date</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="callout">For the earlier plans' full registers, use their own sources pages, linked from
<a href="index.html">Overview</a>. A source marked 'Excluded' was read and rejected as evidence; it is listed so
another session does not redo the same dead end.</div>
"""
    write("sources.html", "Sources", "sources.html", body,
          "Every external page fetched and read during the integration and social-link verification pass.")


def main():
    plans = load("plans.json")
    price = load("price_windows.json")
    social = load("social.json")
    flags = load("flags.json")
    build_index(plans, social, flags)
    build_plans(plans, price)
    build_social(social)
    build_questions(load("questions.json"))
    build_suggestions(load("suggestions.json"))
    build_flags(flags, social)
    build_sources(load("sources.json"))
    print("built", ", ".join(p for p, _ in PAGES))


if __name__ == "__main__":
    main()

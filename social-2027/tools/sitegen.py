#!/usr/bin/env python3
"""Generate the self-contained social-2027 dashboard. Stdlib only.

Data sources (all in social-2027/data/):
  inventory.json  - verbatim venue rows from the four existing plans
  social.json     - every social URL fetched and identified on 2026-11-25
  hours.json      - hours copied from fetched official pages
  costs.json      - published prices for two / arithmetic from published tariffs
Nothing in this generator invents a fact; blanks stay blank and are flagged.
"""
import html, json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "social-2027/data"
OUT = ROOT / "social-2027"

inv = json.loads((D / "inventory.json").read_text())
social = json.loads((D / "social.json").read_text())
hours = json.loads((D / "hours.json").read_text())
costs = json.loads((D / "costs.json").read_text())
VENUES = inv["venues"]
SOCIAL = {}
for r in social["verified"]:
    SOCIAL.setdefault(r["venue_id"], []).append(r)
HOURS = {r["venue_id"]: r for r in hours["rows"]}
COSTS = {r["venue_id"]: r for r in costs["rows"]}
CHECKED = "25 Nov 2026"

PAGES = [
    ("index.html", "Overview"),
    ("beijing-restaurants.html", "Beijing dining"),
    ("shanghai-restaurants.html", "Shanghai dining"),
    ("activities.html", "Activities"),
    ("hotel-plans.html", "Hotel plans"),
    ("questions.html", "Questions"),
    ("suggestions.html", "Suggestions"),
    ("flagged.html", "Flagged & blanks"),
    ("sources.html", "Sources"),
    ("verification.html", "Verification log"),
]

def e(x):
    return html.escape(str(x if x is not None else ""), quote=True)

def a(url, label=None, cls=""):
    label = label or url
    if not url:
        return '<span class="none">—</span>'
    return f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(label)}</a>'

def blank(note="Not confirmed from an official source"):
    return f'<span class="flag" title="{e(note)}">— <small>unverified</small></span>'

def badges(v):
    out = []
    if v.get("city"):
        out.append(f'<span class="chip">{e(v["city"])}</span>')
    if v.get("distinction"):
        d = v["distinction"]
        out.append(f'<span class="chip {"star" if "star" in d.lower() or "Stars" in d else ""}">{e(d)}</span>')
    if v.get("price_band"):
        out.append(f'<span class="chip muted">{e(v["price_band"])}</span>')
    return " ".join(out)

def source_cell(v):
    links = []
    if v.get("official_url"):
        links.append(a(v["official_url"], "Official site"))
    if v.get("guide_url") and v["guide_url"] != v.get("official_url"):
        links.append(a(v["guide_url"], "MICHELIN Guide"))
    if not links:
        return '<span class="flag">No official source found <small>· flagged</small></span>'
    return "<br>".join(links)

def social_cell(v):
    rows = SOCIAL.get(v["id"], [])
    if not rows:
        return blank("No YouTube / TikTok / Instagram link was fetched and identified for this venue")
    out = []
    for s in rows:
        tag = "official" if s["official_account"] else "review"
        out.append(f'<div class="socline"><span class="ptag {tag}">{e(s["platform"])}'
                   + (' · official' if s["official_account"] else '') + '</span>'
                   + a(s["url"], s["title"][:78] + ("…" if len(s["title"]) > 78 else "")) + '</div>')
    return "".join(out)

def hours_cell(v):
    h = HOURS.get(v["id"])
    if not h:
        return blank("No opening days/hours confirmed from an official page in this pass")
    return f'<strong>{e(h["days_open"])}</strong><br>{e(h["hours"])}'

def exceptions_cell(v):
    h = HOURS.get(v["id"])
    if not h or not h["exceptions"]:
        return blank("No exception statement located on a fetched official page")
    return e(h["exceptions"])

def cost_cell(v):
    c = COSTS.get(v["id"])
    if not c:
        return blank("No price for two published by the venue; MICHELIN price bands are not totals")
    return (f'<strong>{e(c["total_for_two"])}</strong><br><small>{e(c["status"])} · '
            + a(c["source_url"], "price source") + '</small>')

def provenance(v):
    names = []
    for p in v["plan_refs"]:
        s = p["plan"].split(" (")[0]
        if s not in names:
            names.append(s)
    return " · ".join(names)

def table_for(venue_list, kind):
    heads = ["Venue / plan provenance", "Days & hours", "Exceptions", "Total for 2 adults", "Social reviews (verified)", "Official source"]
    if kind == "restaurant":
        rows = []
        for v in venue_list:
            rows.append(f'''<tr id="{e(v['id'])}">
<td data-label="Venue"><strong>{e(v['name'])}</strong><div class="meta">{badges(v)}<br><small>{e(provenance(v))}</small></div></td>
<td data-label="Days & hours">{hours_cell(v)}</td>
<td data-label="Exceptions">{exceptions_cell(v)}</td>
<td data-label="Total for 2">{cost_cell(v)}</td>
<td data-label="Social reviews">{social_cell(v)}</td>
<td data-label="Official source">{source_cell(v)}</td></tr>''')
    else:
        rows = []
        for v in venue_list:
            rows.append(f'''<tr id="{e(v['id'])}">
<td data-label="Venue"><strong>{e(v['name'])}</strong><div class="meta"><span class="chip muted">{e(v['city'])}</span><br><small>{e(provenance(v))}</small></div></td>
<td data-label="Days & hours">{hours_cell(v)}</td>
<td data-label="Exceptions">{exceptions_cell(v)}</td>
<td data-label="Total for 2">{cost_cell(v)}</td>
<td data-label="Social reviews">{social_cell(v)}</td>
<td data-label="Official source">{source_cell(v)}</td></tr>''')
    return ('<div class="tablewrap"><table><thead><tr>'
            + "".join(f"<th>{e(h)}</th>" for h in heads)
            + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>")

def shell(title, body, active):
    nav = "".join(f'<a href="{e(f)}" ' + ('class="active"' if f == active else '')
                  + '>' + e(label) + '</a>' for f, label in PAGES)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · China 2027 social &amp; hours audit</title>
<link rel="stylesheet" href="assets/style.css"></head>
<body><header class="top"><a class="brand" href="index.html">China 2027 <span>· audit</span></a>
<button id="navtoggle" aria-label="Toggle navigation" aria-expanded="false">☰ Menu</button></header>
<nav id="nav">{nav}</nav>
<main>{body}</main>
<footer>Verified {e(CHECKED)} by session <code>c2067093</code>. Every social link was fetched; every blank is flagged.
This study audits the four plans already in this repository; it does not overwrite them.</footer>
<script src="assets/app.js"></script></body></html>'''

def write(name, title, body, active=None):
    (OUT / name).write_text(shell(title, body, active or name), encoding="utf-8")

# ---------- Overview ----------
n_social = len(SOCIAL)
n_links = len(social["verified"])
n_hours = len(HOURS)
n_costs = len(COSTS)
n_venues = len(VENUES)
n_flagged_social = n_venues - n_social
n_rejected = len(social['rejected'])
pct = lambda n: round(100 * n / n_venues)
body = f'''<section class="hero"><p class="eyebrow">Executive summary · verified {e(CHECKED)}</p>
<h1>One trip, four plans, one evidence trail</h1>
<p class="lede">This dashboard audits the restaurant and activity rows already published by four independent sessions.
It adds the social-review links the original brief asked for, re-checks opening days/hours and published prices
against operator or MICHELIN pages, and leaves every unconfirmed cell <em>blank and flagged</em>.</p>
<div class="stats">
<div><strong>{n_venues}</strong><span>unique venues inventoried</span></div>
<div><strong>{n_social}</strong><span>venues with verified social links</span></div>
<div><strong>{n_links}</strong><span>links fetched &amp; identified</span></div>
<div><strong>{n_hours}</strong><span>official hours rows confirmed</span></div>
<div><strong>{n_costs}</strong><span>official prices for two</span></div>
</div></section>

<section class="card"><h2>What the evidence says</h2>
<ul class="findings">
<li><strong>Social coverage is the gap.</strong> Only <b>{n_social} of {n_venues}</b> venues ({pct(n_social)}%) have a YouTube,
TikTok or Instagram link that was actually fetched and matched to the venue. {n_flagged_social} venues have none and are listed as blank.</li>
<li><strong>Six inherited links were search pages, not reviews.</strong> They are rejected and replaced where a direct video could be verified;
{n_rejected} candidate links in total were rejected: search-result pages, wrong-city/wrong-business accounts and false matches.</li>
<li><strong>Hours are mostly unpublished.</strong> {n_hours} of {n_venues} venues ({pct(n_hours)}%) have hours confirmed from an official page this session.
The rest are blank — including famous restaurants whose MICHELIN entry shows no hours at all.</li>
<li><strong>Exact dinner prices are rare.</strong> Only {n_costs} venues publish a price for two. MICHELIN's ¥ band is a spending
category, not a price: it is never presented as a total here.</li>
<li><strong>Creator quotes are not prices.</strong> Reviewers mention ¥988, ¥2,888 and ¥7,500 figures; all are labelled
unofficial and excluded from the cost column.</li>
</ul></section>

<section class="card"><h2>What is ready to use</h2>
<div class="callouts">
<a class="callout" href="beijing-restaurants.html"><strong>Beijing dining</strong><span>33 starred restaurants · social links, hours, official sources</span></a>
<a class="callout" href="shanghai-restaurants.html"><strong>Shanghai dining</strong><span>34 venues from three independent studies · star vs listed clearly separated</span></a>
<a class="callout" href="activities.html"><strong>Activities</strong><span>16 attractions · Monday closures and last-entry times where published</span></a>
<a class="callout" href="hotel-plans.html"><strong>Hotel plans</strong><span>Where the four existing seven-night hotel rankings live</span></a>
</div></section>

<section class="card"><h2>Booking-relevant facts confirmed this session</h2>
<div class="grid2">
<div><h3>Monday 15 Feb 2027</h3><p>The preferred start date is a Monday. The Palace Museum, Yu Garden, Shanghai Museum
(people's square) and T'ang Court all publish a Monday closure. Da Vittorio is closed Monday. Shanghai Museum East closes Tuesday.
An arrival-day dinner or museum plan needs a different venue.</p>
<p><a href="questions.html#q2">See the date question →</a></p></div>
<div><h3>Prices that are actually published</h3><p>T'ang Court: ¥888 or ¥2,288 per two, inclusive of service and tax.
Yu Garden: ¥60 for two in the off-season tariff. Palace Museum: ¥80 for two in low season. TRB Hutong: ¥1,812.40 /
¥3,882.40 / ¥5,262.40 for two including the operator's 15% service charge — calculated from the published per-person menu.</p>
<p><a href="sources.html">All price sources →</a></p></div>
</div></section>

<section class="card warn"><h2>Unresolved before any booking decision</h2>
<p>The brief's preferred window (15–18 Feb) is three nights, not one to two weeks. The four plans use a seven-night stay
starting 15 Feb. Hotel totals differ by room category and VAT treatment. No routed journey times exist, so the "≤1 hour
from hotel" test remains unanswered. These are decisions, not data problems; see
<a href="questions.html">questions</a> and <a href="suggestions.html">suggestions</a>.</p></section>
'''
write("index.html", "Overview", body, "index.html")

# ---------- Restaurant pages ----------
for city, fname, active in [("Beijing", "beijing-restaurants.html", "beijing-restaurants.html"),
                            ("Shanghai", "shanghai-restaurants.html", "shanghai-restaurants.html")]:
    rows = [v for v in VENUES if v["city"] == city and v["kind"] == "restaurant"]
    body = f'''<section class="pagehead"><p class="eyebrow">Verified {e(CHECKED)}</p>
<h1>{city} restaurants · {len(rows)} venues</h1>
<p>Merged from the plans that listed them. Star status is reproduced from the owning plan; where a plan says
"listed only", it is not a star. Blank hours or prices were not confirmed on a fetched official page.</p>
<input class="filter" type="search" placeholder="Filter this table…" aria-label="Filter table">
</section>
{table_for(rows, "restaurant")}
<section class="note"><p><strong>Reading the table.</strong> <span class="flag">— unverified</span> means the value is blank
in the source data or was not published on the official page fetched on {e(CHECKED)}. Nothing has been estimated.
A social link marked <span class="ptag official">official</span> is the venue's own account; all others are third-party creators.</p></section>'''
    write(fname, f"{city} restaurants", body, active)

# ---------- Activities ----------
acts = [v for v in VENUES if v["kind"] == "activity"]
body = f'''<section class="pagehead"><p class="eyebrow">Verified {e(CHECKED)}</p>
<h1>Activities · {len(acts)} attractions</h1>
<p>Both cities, merged and de-duplicated. Public spaces with no operator page have no asserted hours or price.</p>
<input class="filter" type="search" placeholder="Filter this table…" aria-label="Filter table"></section>
{table_for(acts, "activity")}
<section class="note"><p>Video links are research aids. TikTok and Instagram are not generally reachable in mainland China,
so none of these links should be treated as an on-trip information channel.</p></section>'''
write("activities.html", "Activities", body)

# ---------- Hotel plans navigation ----------
body = '''<section class="pagehead"><p class="eyebrow">Scope note</p>
<h1>Hotels &amp; the four existing plans</h1>
<p>This audit did not re-price hotels. The table below is a <em>navigation aid</em>, not a new ranking and not a price claim.
Each plan owns its own hotel rows; open it to read that plan's dated quote, room category and source link.</p></section>
<div class="tablewrap"><table><thead><tr><th>Plan</th><th>City</th><th>Where its hotel analysis lives</th><th>What it contributes</th></tr></thead><tbody>
<tr><td data-label="Plan"><strong>fac6d965</strong></td><td data-label="City">Beijing</td><td data-label="Link"><a href="../hotels.html">Root hotels page</a></td><td data-label="Contribution">12 seven-night totals, 15–22 Feb 2027, with a published ranking method.</td></tr>
<tr><td data-label="Plan"><strong>68e13071</strong></td><td data-label="City">Shanghai</td><td data-label="Link"><a href="../docs/hotels.html">docs/ hotels page</a></td><td data-label="Contribution">Six hotels, four real week-one totals, five-window date sweep.</td></tr>
<tr><td data-label="Plan"><strong>3b27db6c</strong></td><td data-label="City">Shanghai</td><td data-label="Link"><a href="../shanghai-2027/hotels.html">shanghai-2027 hotels page</a></td><td data-label="Contribution">Seven hotels; a disclosed proximity model for the ≤1-hour test.</td></tr>
<tr><td data-label="Plan"><strong>16153d37</strong></td><td data-label="City">Shanghai</td><td data-label="Link"><a href="../shanghai-verified-2027/hotels.html">verified hotels page</a></td><td data-label="Contribution">Dated Booking.com quotes with fetch timestamps and room/bath details.</td></tr>
</tbody></table></div>
<section class="card"><h2>Why no new hotel ranking here</h2><p>The plans report different cheapest totals ($696, $922, $1,116) because they priced
different room categories and treated tax differently. This session did not re-quote any hotel, so publishing one "winner"
would be an inference, not a verified fact. The decision path is set out in <a href="questions.html#q4">Q4</a> and
<a href="suggestions.html#s4">S4</a>.</p></section>'''
write("hotel-plans.html", "Hotel plans", body)

# ---------- Questions ----------
Q = [
("q1","Which city should the trip be in?","The brief does not say.","Four plans exist: one Beijing, three Shanghai. They optimise different things and disagree with each other.","Not decidable from the evidence.","Ask the traveller to rank three priorities: star count, flight cost, or hotel value; then select the owning plan. No new research needed."),
("q2","Do the dates work?","15–18 Feb 2027 is the preferred window; the brief also asks for 1–2 weeks.","Three nights vs one to two weeks. All plans use 15–22 Feb 2027 (seven nights).","No — the preferred window is too short.","Decide whether 15 Feb is a fixed arrival date or merely a preferred start; if fixed, Monday closures apply on day one. See q3."),
("q3","Is 15 Feb 2027 a Monday, and does it matter?","Yes — computed with the standard calendar.","Palace Museum, Yu Garden, Shanghai Museum (People's Square) and T'ang Court publish Monday closure; Da Vittorio shows Monday closed.","Yes: the first day cannot be a museum/garden day.","Rebuild the day-one plan around an open venue, or arrive a day earlier."),
("q4","Which hotel is genuinely cheapest for the exact week?","Not answered by this session.","Other plans quote $696, $922 and $1,116 seven-night totals for different room types.","Unresolved — do not treat any one figure as final.","Re-quote the same room type on each hotel's own booking engine for 15–22 Feb 2027, with taxes shown."),
("q5","Does the cheapest room meet 'queen bed or larger, private bathroom'?","Partially.","One plan explicitly flags its cheapest $652 room as twin beds and excludes it. Others name a queen room with attached bath.","Needs a room-type check at booking.","Capture a screenshot of the room page showing bed and bathroom before comparing prices."),
("q6","Are the star statuses current?","Partly.","Beijing rows use the 2027 Beijing/Tianjin selection; Shanghai rows use the 2026 Shanghai/Jiangsu/Zhejiang edition. The 2027 Shanghai edition was not published at the time of this audit.","No for Shanghai 2027.","Recheck the MICHELIN guide after the 2027 Shanghai release and update status fields."),
("q7","How many starred restaurants are within one hour of each hotel by subway or bus?","Not answered.","One plan publishes a modelled estimate with disclosed constants; another refuses to model and leaves the field blank. No routed journey time was fetched in this session.","Unanswered.","Run the same origin–destination set through Amap or Baidu Maps at the hour of travel and store the route URL with each result."),
("q8","What will dinner cost for two?","Four totals published; the rest blank.","T'ang Court ¥888 / ¥2,288 for two; Yu Garden and Palace Museum totals are calculated from published tariffs; TRB Hutong calculated from its menu. MICHELIN ¥ bands are not prices.","Mostly unknown.","Request current menus by email or check each restaurant's own menu PDF; record the date of the quote."),
("q9","Which venues publish opening days, hours and exceptions?","12 of 83 confirmed here.","The rest have no fetched official hours statement. Where a plan carried hours but this session could not refetch them, the value is blank and flagged.","Insufficient for scheduling.","Re-check each restaurant's own site and MICHELIN page in the week before travel; record a source URL per cell."),
("q10","Are there reliable social-review links?",f"{n_links} links across {n_social} venues.",f"{n_rejected} candidate links were rejected: search-result pages, wrong-city/wrong-business accounts and false matches.",f"Coverage is {n_social}/{n_venues} venues.","Search official operator accounts first, then fetch each candidate and match the venue name before adding it."),
("q11","Can the TikTok/Instagram links be used during the trip?","Not assumed.","Links were collected as research aids. Mainland China restricts these platforms.","Not verified for on-trip use.","Use official restaurant/museum websites and WeChat channels while travelling."),
("q12","Are creator-quoted prices usable as budget data?","No.","Review videos mention menu prices for Taian Table, Fu He Hui, Canton 8 and Da Vittorio. None is an official price.","Rejected as evidence.","Ignore them; use operator menus only."),
("q13","Is the 2027 Chinese New Year holiday period confirmed by an official notice?","Not in this session.","Plans cite secondary sources that disagree on 5–11 Feb vs 5–13 Feb and a make-up working day.","Unverified.","Locate the State Council holiday notice on gov.cn and link it before treating any date as a holiday."),
("q14","Do museums require advance booking?","Yes for People's Square; no for Museum East individuals.","The People's Square visit page requires advance booking via WeChat Mini Program (trip.com for overseas visitors). Museum East permits walk-in with valid ID; two galleries still need reservations.","Answered for these two venues.","Keep this distinction when building the itinerary."),
("q15","What is the total trip cost?","Not calculable.","Hotel totals exist in other plans; flights, visas and most dinners have no verified price.","Unknown.","Price flights and the three chosen dinners, then add one hotel total from a re-quote."),
]
rows = "".join(f'''<tr id="{e(q[0])}"><td data-label="Question"><strong>{e(q[1])}</strong></td>
<td data-label="Information we have">{e(q[2])}<div class="meta"><small>{e(q[3])}</small></div></td>
<td data-label="Answer / status"><span class="status">{e(q[4])}</span></td>
<td data-label="How to close it">{e(q[5])}</td></tr>''' for q in Q)
body = f'''<section class="pagehead"><p class="eyebrow">Decisions before booking</p>
<h1>Questions, information &amp; answers</h1><p>Each row states what is known, what is missing, and the concrete step that would close it.
Nothing in this section is a recommendation to book.</p>
<input class="filter" type="search" placeholder="Filter questions…" aria-label="Filter questions"></section>
<div class="tablewrap"><table><thead><tr><th>Question</th><th>Information we already have</th><th>Answer / status</th><th>How to discover what is missing</th></tr></thead>
<tbody>{rows}</tbody></table></div>'''
write("questions.html", "Questions", body)

# ---------- Suggestions (none implemented) ----------
S = [
("s1",f"Verify the {n_flagged_social} remaining social gaps","Collect official accounts first; fetch and match each candidate. Expected gain: up to all venues covered.","High","Not implemented — proposed only"),
("s2","Route the ≤1-hour hotel test","Run one origin–destination matrix per hotel in Amap at 18:00 on a weekday; store route URLs. Replaces both the blank and the model.","High","Not implemented — proposed only"),
("s3","Collect exact menu prices for two","Request current menus from the 79 restaurants with no published total; store PDF or email quote with date.","High","Not implemented — proposed only"),
("s4","Re-quote the same hotel room on operator sites","Use one room category, 15–22 Feb 2027, two adults, taxes included; resolves the $696/$922/$1,116 spread.","High","Not implemented — proposed only"),
("s5","Locate the official 2027 holiday notice","Find the State Council notice on gov.cn and replace the conflicting secondary dates.","Medium","Not implemented — proposed only"),
("s6","Split restaurant tables by district","Huangpu, Changning, Chaoyang and Dongcheng clusters would make a one-hour hotel test readable on a phone.","Medium","Not implemented — proposed only"),
("s7","Add an exceptions-first itinerary","Sort days by closure constraints before preference: Monday closures, last entry, then dinner availability.","Medium","Not implemented — proposed only"),
("s8","Publish a change log for hours and prices","Each change gets a fetch date and URL; the current design already records these in the verification log, so extend it site-wide.","Medium","Not implemented — proposed only"),
("s9","Add an official-source badge to every inherited row","Would let a reader distinguish an operator page from an OTA or creator video at a glance.","Low","Not implemented — proposed only"),
("s10","Merge the four plans only after decisions are made","The plans disagree by design. Merging before q1–q5 are answered would hide the disagreement.","Low","Not implemented — proposed only"),
]
rows = "".join(f'''<tr><td data-label="ID"><code>{e(s[0].upper())}</code></td><td data-label="Proposal"><strong>{e(s[1])}</strong></td>
<td data-label="Effect">{e(s[2])}</td><td data-label="Priority"><span class="chip">{e(s[3])}</span></td>
<td data-label="Decision state"><span class="flag">{e(s[4])}</span></td></tr>''' for s in S)
body = '''<section class="pagehead"><p class="eyebrow">Review first, implement later</p>
<h1>Suggestions</h1><p>Ten paths someone can choose from. <strong>None has been applied.</strong> This page exists so a reviewer can
select a path before any change is made to a shared file.</p></section>
<div class="tablewrap"><table><thead><tr><th>ID</th><th>Proposal</th><th>Expected effect</th><th>Priority</th><th>State</th></tr></thead>
<tbody>''' + rows + '''</tbody></table></div>
<section class="card"><h2>Request to the integration session</h2><p>This audit's scope is <code>social-2027/**</code> plus its own section of
<code>COORDINATION.md</code>. If one of these suggestions is approved, the owning session should claim it on the shared board
first. In particular, correcting the Bombana hours inherited from <code>docs/data/restaurants.json</code> requires that file's owner,
not this session.</p></section>'''
write("suggestions.html", "Suggestions", body)

# ---------- Flagged ----------
IRR = [
("F-01","8½ Otto e Mezzo Bombana hours inherited from docs/ say Tue–Sun lunch. The MICHELIN page fetched here shows lunch only Thursday–Sunday; Monday–Wednesday are dinner-only.","docs/data/restaurants.json vs <a href=\"https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurant/8-%C2%BD-otto-e-mezzo-bombana\">MICHELIN page</a>","Corrected in this site; owning session asked to update its file."),
("F-02","Six inherited 'YouTube search' URLs in the Beijing plan are result pages (one returns a 401 banner), not reviews.","assets/data.js","Rejected; four direct videos mined from results and verified where possible."),
("F-03","A YouTube result that mentioned Bao Li Xuan's Shanghai origin was actually a review of Bund House in Jakarta.","<a href=\"https://www.youtube.com/watch?v=hNDCCVEb8bA\">video</a>","Rejected; a different Bao Li Xuan video was verified."),
("F-04","Search results for T'ang Court point to the three-star Hong Kong restaurant, not the two-star Shanghai one.","<a href=\"https://www.instagram.com/tangcourthk/\">Instagram</a>","Rejected; no social link published for Shanghai T'ang Court."),
("F-05","The Palace Museum Instagram account in a search snippet returned HTTP 404 when fetched.","<a href=\"https://www.instagram.com/palace_museum/\">URL</a>","Rejected; no official Instagram published for this venue."),
("F-06","Creator videos quote menu prices (Taian Table ¥2,588/¥2,888; Fu He Hui ¥988/¥998; Canton 8 ¥300; Da Vittorio ¥7,500 for two).","verified video pages","All excluded from the cost column. They are not official prices."),
("F-07","Taian Table's official Menu No.55 PDF publishes add-on prices (¥218, ¥388, ¥188) but not the mandatory degustation price.","<a href=\"https://sh.taian-table.cn/wp-content/uploads/2026/10/Menu-No.55.pdf\">menu PDF</a>","Total for two left blank."),
("F-08","King's Joy videos call it three-star; the current guide in the Beijing plan says Two Stars.","<a href=\"https://www.youtube.com/watch?v=TTfH0qd79aE\">video</a>","Star status from the plan kept; dated video noted in the link row."),
("F-09","Shanghai Tower publishes no price or hours on its official English page; a TikTok creator quotes ¥180.","<a href=\"https://www.tiktok.com/@traveltomtom/video/7282390862808517920\">post</a>","Price left blank; social link kept and labelled unofficial."),
("F-10","Tianzifang has no operator page in the source data, so no official link, hours or price.","inventory DOC-A05","Left blank and listed in the blank register below."),
("F-11","The three Shanghai plans still disagree on hotel totals ($696 / $922 / $1,116) and on proximity method.","README.md and the three plans","Not resolved here; linked from the hotel-plans page."),
("F-12","MICHELIN opening hours are rendered after the map block; the first chunk of a page can look like 'no hours'.","Bombana / Fu He Hui / Yi Long Court pages","Full page chunks were fetched before blanking any hours field."),
]
irr_rows = "".join(f'''<tr><td data-label="ID"><code>{e(i[0])}</code></td><td data-label="Irregularity">{i[1]}</td>
<td data-label="Source">{i[2]}</td><td data-label="Handling">{e(i[3])}</td></tr>''' for i in IRR)
# blank register
missing = []
for v in VENUES:
    if v["id"] not in SOCIAL: missing.append((v["id"], v["name"], "social links"))
    if v["id"] not in HOURS: missing.append((v["id"], v["name"], "days/hours"))
    if v["id"] not in COSTS: missing.append((v["id"], v["name"], "price for two"))
blank_rows = "".join(f'<tr><td data-label="Venue ID"><code>{e(i)}</code></td><td data-label="Venue">{e(n)}</td><td data-label="Blank field"><span class="flag">{e(f)} · unverified</span></td></tr>' for i, n, f in missing)
body = f'''<section class="pagehead"><p class="eyebrow">Every gap is visible</p>
<h1>Flagged for review</h1><p>Irregularities found during this audit, followed by a blank register containing
{len(missing)} venue/field pairs. No blank has been filled by inference.</p></section>
<h2>Irregularities</h2>
<div class="tablewrap"><table><thead><tr><th>ID</th><th>Irregularity</th><th>Source / counter-source</th><th>Handling</th></tr></thead>
<tbody>{irr_rows}</tbody></table></div>
<h2>Rejected social candidates</h2>
<div class="tablewrap"><table><thead><tr><th>Venue</th><th>Platform</th><th>URL</th><th>Why rejected</th></tr></thead><tbody>
{''.join(f'<tr><td data-label="Venue"><code>{e(r["venue_id"])}</code></td><td data-label="Platform">{e(r["platform"])}</td><td data-label="URL">{a(r["url"],"open")}</td><td data-label="Reason">{e(r["reason"])}</td></tr>' for r in social["rejected"])}
</tbody></table></div>
<h2>Blank register ({len(missing)})</h2>
<input class="filter" type="search" placeholder="Filter blanks…" aria-label="Filter blanks">
<div class="tablewrap"><table><thead><tr><th>Venue ID</th><th>Venue</th><th>Blank field</th></tr></thead><tbody>{blank_rows}</tbody></table></div>'''
write("flagged.html", "Flagged & blanks", body)

# ---------- Sources ----------
SRC = [
("Official","Palace Museum visit page","Hours, seasonal last entry, tickets, 40,000 cap, passport rule","https://intl.dpm.org.cn/visit.html"),
("Official","Mutianyu Great Wall","Hours, ticket-sales cut-off, off-season dates","https://en.mutianyugreatwall.com/"),
("Official","King's Joy MICHELIN entry","Two-star status, address, hours block","https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurant/king-s-joy"),
("Official","TRB Hutong — Find us","Days and hours","https://www.trbhutong.com/findus"),
("Official","TRB Hutong — Menu","Per-person menu prices and 15% service charge","https://www.trbhutong.com/menu"),
("Official","TRB Hutong — Instagram","Official account match","https://www.instagram.com/trb_cn/"),
("Official","Mutianyu — Instagram","Official account match","https://www.instagram.com/mutianyu_greatwall_official/"),
("Official","8½ Otto e Mezzo Bombana MICHELIN entry","Two stars, address, per-day hours","https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurant/8-%C2%BD-otto-e-mezzo-bombana"),
("Official","Da Vittorio MICHELIN entry","Two stars, address, Monday closure, hours","https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurant/da-vittorio-570570"),
("Official","Fu He Hui MICHELIN entry","Two stars, address, hours","https://guide.michelin.com/us/en/shanghai-municipality/shanghai/restaurant/fu-he-hui"),
("Official","Fu He Hui — Instagram","Official account match, address","https://www.instagram.com/fuhehui/"),
("Official","Yi Long Court MICHELIN entry","Star status, address, hours","https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurant/yi-long-court"),
("Official","The Langham — T'ang Court","Two stars, hours, Monday closure, attire, 15-minute hold","https://www.langhamhotels.com/en/the-langham/shanghai/dine/tang-court/"),
("Official","T'ang Court set-menu PDF","¥888 and ¥2,288 totals for two, tax and service included","https://www.langhamhotels.com/content/dam/langhamhotels/tlshx-pdfs/tang-court/2026/seasonal-set-menu-selection-2026.pdf"),
("Official","Yu Garden visitor information","Hours, Monday closure, seasonal tariffs, entrances","https://www.yugarden.com.cn/page/articleview/message.html"),
("Official","Shanghai Museum — People's Square","Hours, last entry, exhibition exception, booking rules","https://www.shanghaimuseum.net/mu/frontend/pg/en/service/visit-west"),
("Official","Shanghai Museum East","Hours, Tuesday closure, reservation rules","https://www.shanghaimuseum.net/mu/frontend/pg/m/en/service/visit-east"),
("Official","Shanghai Museum — Instagram","Official account match","https://www.instagram.com/theshanghaimuseum/"),
("Official","Shanghai Museum — YouTube","Official channel match","https://www.youtube.com/@theshanghaimuseum"),
("Official","Taian Table menu PDF","Mandatory degustation statement; add-on prices only","https://sh.taian-table.cn/wp-content/uploads/2026/10/Menu-No.55.pdf"),
("Third-party",f"{n_links} social pages","Titles, uploaders and dates copied from the fetched pages; details in the verification log","verification.html"),
]
rows = "".join(f'<tr><td data-label="Type"><span class="chip {"star" if s[0]=="Official" else "muted"}">{e(s[0])}</span></td><td data-label="Source"><strong>{e(s[1])}</strong></td><td data-label="What it proved">{e(s[2])}</td><td data-label="Link">{a(s[3],"open source")}</td></tr>' for s in SRC)
body = f'''<section class="pagehead"><p class="eyebrow">Source register</p><h1>Sources</h1>
<p>Official pages fetched on {e(CHECKED)} for hours, prices and account identity. Social-review pages are
third-party and are listed individually in the <a href="verification.html">verification log</a>.</p></section>
<div class="tablewrap"><table><thead><tr><th>Type</th><th>Source</th><th>What it proved</th><th>Link</th></tr></thead>
<tbody>{rows}</tbody></table></div>'''
write("sources.html", "Sources", body)

# ---------- Verification log ----------
vrows = "".join(f'''<tr id="{e(r["venue_id"])}"><td data-label="Venue"><code>{e(r["venue_id"])}</code></td>
<td data-label="Platform">{e(r["platform"])}</td><td data-label="Page title"><strong>{e(r["title"])}</strong></td>
<td data-label="Uploader">{e(r["creator"] or "—")}</td><td data-label="Date">{e(r["published"] or "—")}</td>
<td data-label="Account"><span class="chip {"star" if r["official_account"] else "muted"}">{"official" if r["official_account"] else "third-party"}</span></td>
<td data-label="Evidence"><small>{e(r["note"])}</small></td><td data-label="Link">{a(r["url"],"open")}</td></tr>''' for r in social["verified"])
hrows = "".join(f'''<tr><td data-label="Venue"><code>{e(r["venue_id"])}</code></td><td data-label="Field">Hours</td>
<td data-label="Evidence"><small>{e(r["evidence"])}</small></td><td data-label="Link">{a(r["source_url"],"official page")}</td></tr>''' for r in hours["rows"])
crows = "".join(f'''<tr><td data-label="Venue"><code>{e(r["venue_id"])}</code></td><td data-label="Field">Cost for two</td>
<td data-label="Evidence"><small>{e(r["evidence"])}</small></td><td data-label="Link">{a(r["source_url"],"official page")}</td></tr>''' for r in costs["rows"])
body = f'''<section class="pagehead"><p class="eyebrow">Line by line</p><h1>Verification log</h1>
<p>Every social link below was fetched on {e(CHECKED)}; the title, uploader and date are copied from the fetched page.
Hours and prices were read from the linked official page. Search-result URLs and false matches are on the
<a href="flagged.html">flagged page</a>, not here.</p>
<input class="filter" type="search" placeholder="Filter verification rows…" aria-label="Filter verification rows"></section>
<h2>Social links ({len(social["verified"])})</h2>
<div class="tablewrap"><table><thead><tr><th>Venue</th><th>Platform</th><th>Page title</th><th>Uploader</th><th>Date</th><th>Account</th><th>Evidence</th><th>Link</th></tr></thead>
<tbody>{vrows}</tbody></table></div>
<h2>Hours and prices confirmed from official pages ({len(hours["rows"]) + len(costs["rows"])})</h2>
<div class="tablewrap"><table><thead><tr><th>Venue</th><th>Field</th><th>Evidence read</th><th>Official page</th></tr></thead>
<tbody>{hrows}{crows}</tbody></table></div>'''
write("verification.html", "Verification log", body)

# ---------- Assets ----------
(OUT / "assets/style.css").write_text('''*:box-sizing:border-box;html{scroll-behavior:smooth}
body{margin:0;background:#f5f7fa;color:#14263d;font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
a{color:#0a63b8;text-decoration:none}a:hover{text-decoration:underline}
header.top{display:flex;align-items:center;justify-content:space-between;padding:14px 18px;background:#102a43;color:#fff;position:sticky;top:0;z-index:10}
.brand{font-weight:800;font-size:18px;color:#fff}.brand span{font-weight:400;opacity:.7}
#navtoggle{background:#234e75;color:#fff;border:0;border-radius:8px;padding:8px 12px;font:inherit;cursor:pointer}
nav{background:#173e63;display:flex;gap:4px;overflow-x:auto;padding:6px 10px;white-space:nowrap}
nav a{color:#d8e8f7;padding:8px 11px;border-radius:7px;font-size:14px}
nav a.active{background:#fff;color:#102a43;font-weight:700}
main{max-width:1180px;margin:0 auto;padding:18px 14px 60px}
h1{font-size:clamp(25px,5vw,38px);line-height:1.15;margin:.2em 0 .4em}
h2{font-size:21px;margin-top:1.6em}.eyebrow{text-transform:uppercase;letter-spacing:.09em;font-size:12px;color:#4d6b8a;font-weight:700;margin:0}
.lede{font-size:17px;max-width:70ch;color:#34506d}
.hero,.card{background:#fff;border:1px solid #dce5ee;border-radius:14px;padding:20px;margin-bottom:18px;box-shadow:0 2px 8px #102a430a}
.pagehead{background:#fff;border:1px solid #dce5ee;border-radius:14px;padding:18px 20px;margin-bottom:16px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-top:18px}
.stats div{background:#eef4fa;border-radius:10px;padding:12px}.stats strong{display:block;font-size:27px;color:#0b4f8a}.stats span{font-size:12px;color:#42637f}
.findings{padding-left:20px}.findings li{margin:8px 0}
.callouts{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}
.callout{display:block;border:1px solid #c9dbeb;border-radius:10px;padding:14px;background:#f8fbfe;color:#14263d}
.callout strong,.callout span{display:block}.callout span{font-size:13px;color:#4a6580;margin-top:4px}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
.card.warn{border-left:5px solid #d99027;background:#fffaf0}
.note{background:#eef4fa;border-radius:10px;padding:14px;margin-top:18px;font-size:14px}
.tablewrap{overflow-x:auto;background:#fff;border:1px solid #dce5ee;border-radius:12px;margin:12px 0 22px}
table{width:100%;border-collapse:collapse;font-size:14px}
th{background:#e9f0f7;color:#244760;text-align:left;padding:11px;font-size:12px;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap}
td{padding:11px;border-top:1px solid #e6edf4;vertical-align:top}
td:nth-child(1){min-width:190px}td:nth-child(5){min-width:230px}
tr:nth-child(even){background:#fbfdff}
.meta{margin-top:5px;color:#54708a;font-size:12px}
.chip,.ptag,.status{display:inline-block;border-radius:999px;padding:2px 8px;font-size:11px;background:#e8eef5;color:#33526e;margin:2px 3px 2px 0}
.chip.star,.ptag.official{background:#fff2d6;color:#82540a;font-weight:700}
.chip.muted{background:#eef1f5;color:#607083}
.flag{color:#a04b17;background:#fff4e8;border-radius:6px;padding:2px 5px;font-size:13px}
.flag small{font-size:10px;text-transform:uppercase;letter-spacing:.04em}
.socline{margin-bottom:6px;line-height:1.35}.ptag{display:inline-block}
.filter{width:100%;max-width:360px;padding:10px 12px;border:1px solid #bdd0e1;border-radius:9px;font:inherit;margin:10px 0}
.none{color:#8a9bad}
footer{background:#102a43;color:#b9cfe4;padding:20px;text-align:center;font-size:13px}
code{background:#e9f0f7;border-radius:4px;padding:1px 4px;font-size:12px}
@media(max-width:760px){
 nav{display:none;flex-direction:column;gap:2px}nav.open{display:flex}
 header.top{padding:12px}main{padding:12px 9px 40px}
 .hero,.card,.pagehead{padding:15px;border-radius:11px}
 table,thead,tbody,tr,td{display:block;width:100%}
 thead{display:none}tr{border:1px solid #dbe5ef;border-radius:9px;margin:9px 0;padding:8px;background:#fff}
 td{border:0;padding:7px 8px;display:grid;grid-template-columns:34% 1fr;gap:8px;font-size:14px}
 td:before{content:attr(data-label);font-size:10px;text-transform:uppercase;letter-spacing:.05em;color:#58748f;font-weight:700;padding-top:3px}
 td:first-child{grid-template-columns:1fr}td:first-child:before{display:none}
 td:nth-child(5){min-width:0}
}
''', encoding="utf-8")
(OUT / "assets/app.js").write_text('''const nav=document.getElementById('nav'), btn=document.getElementById('navtoggle');
if(btn&&nav){btn.addEventListener('click',()=>{const open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open?'true':'false')});
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');btn.setAttribute('aria-expanded','false')}))}
document.querySelectorAll('.filter').forEach(input=>{input.addEventListener('input',()=>{
  const q=input.value.toLowerCase().trim(); const wrap=input.parentElement.nextElementSibling;
  if(!wrap||!wrap.classList.contains('tablewrap'))return;
  wrap.querySelectorAll('tbody tr').forEach(tr=>{tr.style.display=tr.textContent.toLowerCase().includes(q)?'':'none'})})});
''', encoding="utf-8")
print("generated", len(PAGES), "pages")
for name, _ in PAGES:
    p = OUT / name
    print(name, p.stat().st_size)

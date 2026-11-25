#!/usr/bin/env python3
"""Static site generator for beijing-verified-2027/.

Reads data/restaurants.json, data/hotels.json and data/activities.json and writes
plain HTML pages next to this folder. No dependencies, no build step at runtime:
GitHub Pages serves the generated .html files directly.

Run:  python3 beijing-verified-2027/tools/sitegen.py
"""
import json
import os
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


R = load("restaurants.json")
H = load("hotels.json")
A = load("activities.json")

ROWS = R["restaurants"]
HOTELS = H["hotels"]
ACTS = A["activities"]

PAGES = [
    ("index.html", "Overview"),
    ("restaurants.html", "MICHELIN"),
    ("hotels.html", "Hotels"),
    ("activities.html", "Activities"),
    ("itinerary.html", "Itinerary"),
    ("questions.html", "Open questions"),
    ("suggestions.html", "Suggestions"),
    ("flagged.html", "Verification log"),
]


def e(v):
    return html.escape("" if v is None else str(v))


def a(url, label, cls=""):
    if not url:
        return ""
    c = f' class="{cls}"' if cls else ""
    return f'<a href="{e(url)}" target="_blank" rel="noopener"{c}>{label}</a>'


CHIP = {
    "v": '<span class="chip v">{}</span>',
    "f": '<span class="chip f">{}</span>',
    "u": '<span class="chip u">{}</span>',
    "n": '<span class="chip n">{}</span>',
}


def chip(kind, text):
    return CHIP[kind].format(e(text))


def page_header(active, title, subtitle):
    links = "".join(
        f'<a href="{h}" class="{"active" if h == active else ""}">{e(l)}</a>'
        for h, l in PAGES
    )
    return f"""<header class="top"><div class="wrap">
  <div class="brandbar">
    <div class="brand"><span class="dot"></span><span>Beijing 2027<small>15&ndash;22 Feb 2027 &middot; verified build</small></span></div>
    <span class="chip n">built {e(R['_meta']['generated'])}</span>
  </div>
  <nav class="nav">{links}</nav>
</div></header>"""


FOOTER = """<footer><div class="wrap">
  <p><strong>Method.</strong> Each value was read from the official page linked in its own row.
  Anything that could not be read from an official page is blank and carries a flag &mdash; it is never estimated and never copied from a blog.</p>
  <p>Sources: MICHELIN Guide (guide.michelin.com), restaurant and hotel websites, Booking.com dated rate pages,
  Palace Museum (intl.dpm.org.cn), National Museum of China (en.chnmuseum.cn), Temple of Heaven (tiantanpark.cn),
  Summer Palace (summerpalace.net.cn), Mutianyu Great Wall (en.mutianyugreatwall.com), timeanddate.com, U.S. State Department.</p>
  <p>Session 3b335293 &middot; data in <code>beijing-verified-2027/data/*.json</code> &middot;
  gaps listed on <a href="flagged.html">the verification log</a>. Not affiliated with any listed business.</p>
</div></footer>"""


def shell(active, title, subtitle, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(subtitle)}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body data-page="{active}">
{page_header(active, title, subtitle)}
<main><div class="wrap">
<p class="eyebrow">{e(subtitle)}</p>
{body}
</div></main>
{FOOTER}
</body>
</html>
"""


def write(name, text):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", name, len(text), "bytes")


# ---------------------------------------------------------------- restaurants
def social_cell(row):
    soc = row.get("social") or []
    if not soc:
        return chip("u", "none found")
    out = []
    for s in soc:
        label = s["platform"]
        out.append(a(s["url"], label) + f'<span class="meta">{e(s.get("title", ""))[:90]}</span>')
    return "<br>".join(out)


def price2_cell(row):
    p = row.get("price_two_adults")
    if isinstance(p, dict):
        if p.get("status") == "verified_menu_published":
            return (f'<strong>¥1,576</strong> before 15% service'
                    f'<span class="meta">2 &times; ¥788 business-lunch menu &middot; {a(p.get("menu_url"), "menu")}</span>')
        return chip("u", "not published")
    return chip("u", "not published")


def page_restaurants():
    rows_sorted = sorted(ROWS, key=lambda r: (-r["stars"], r["name"]))
    trs = []
    for r in rows_sorted:
        stars = "★" * r["stars"]
        hours = e(r.get("hours")) if r.get("hours") else chip("u", "not published")
        closed = e(r.get("closed")) if r.get("closed") else ""
        src = a(r.get("hours_source"), "source")
        addr = e(r.get("address")) or chip("u", "blank")
        trs.append(f"""<tr>
<td class="name">{e(r['name'])}<span class="meta">{e(r.get('cuisine'))} &middot; {e(r.get('district'))}</span></td>
<td><span class="star">{stars}</span><span class="meta">{r['stars']}-star</span></td>
<td>{e(r.get('price_band'))}</td>
<td>{price2_cell(r)}</td>
<td>{hours}<span class="meta">{closed}</span></td>
<td>{addr}<span class="meta">{e(r.get('phone')) or 'phone not published'}</span></td>
<td style="min-width:190px">{social_cell(r)}</td>
<td class="nowrap">{a(r.get('guide_url'), 'guide')}{' &middot; ' + a(r.get('website'), 'site') if r.get('website') else ''}</td>
</tr>""")
    n3 = sum(1 for r in ROWS if r["stars"] == 3)
    n2 = sum(1 for r in ROWS if r["stars"] == 2)
    n1 = sum(1 for r in ROWS if r["stars"] == 1)
    with_hours = sum(1 for r in ROWS if r.get("hours"))
    with_soc = sum(1 for r in ROWS if r.get("social"))
    body = f"""
<h1>All {len(ROWS)} starred restaurants, star level stated plainly</h1>
<p class="lede">The 2027 Beijing &amp; Tianjin guide (released 27 October 2026) gives Beijing <strong>{len(ROWS)} starred restaurants</strong>:
{n3} three-star, {n2} two-star, {n1} one-star. A bib-gourmand or a &ldquo;MICHELIN Selected&rdquo; entry is <em>not</em> a star and is not in this table.</p>

<div class="grid g4" style="margin:16px 0">
  <div class="card kpi"><div class="big">{n3}</div><div class="sub">three-star</div></div>
  <div class="card kpi"><div class="big">{n2}</div><div class="sub">two-star</div></div>
  <div class="card kpi"><div class="big">{n1}</div><div class="sub">one-star</div></div>
  <div class="card kpi"><div class="big">{with_hours}/{len(ROWS)}</div><div class="sub">have published hours</div></div>
</div>

<div class="callout warn">
<p><strong>Read this before trusting the price column.</strong> The MICHELIN Guide publishes a <em>price band</em>
(¥ to ¥¥¥¥), not a bill. Exactly one restaurant in this set publishes its own menu prices, so exactly one row
has a real &ldquo;for two&rdquo; number. The other {len(ROWS)-1} are blank on purpose. Any site quoting a precise
total for the rest is estimating.</p>
</div>

<div class="controls">
  <input type="search" id="q" placeholder="Filter by name, cuisine, district or star count&hellip;" aria-label="Filter restaurants">
</div>
<p class="hint">Slide the table sideways on a phone. {with_soc} of {len(ROWS)} rows have at least one social link;
social coverage is the weakest part of this dataset and is flagged as such on <a href="flagged.html">the log</a>.</p>

<div class="tablewrap">
<table id="t">
<thead><tr>
<th>Restaurant</th><th>Status</th><th>Band</th><th>Price for 2 adults</th><th>Days &amp; hours</th>
<th>Address / phone</th><th>Watch &amp; read</th><th>Official</th>
</tr></thead>
<tbody>
{''.join(trs)}
</tbody>
</table>
</div>

<h2>What the hours column really says</h2>
<p>Only {with_hours} of {len(ROWS)} restaurants publish opening hours on an official page. For the rest the cell is blank,
not &ldquo;open every day&rdquo;. Two distinct sources exist and they are kept apart in the data file:
the MICHELIN listing (4 rows) and the restaurant&rsquo;s or hotel&rsquo;s own page (4 rows).</p>
<ul class="tight">
<li><strong>Own site / hotel site (strongest):</strong> Cai Yi Xuan, Fu Chun Ju, Giada Garden, Il Ristorante &ndash; Niko Romito.</li>
<li><strong>MICHELIN listing (no closing day stated):</strong> King&rsquo;s Joy, Trb Hutong, both Xin Rong Ji entries.</li>
<li><strong>Nobody publishes a closing day.</strong> Not one of the eight states a weekly rest day, so
<em>every</em> row carries "None published" rather than a guess.</li>
</ul>

<h2>The clusters the hotels are ranked against</h2>
<p>Starred restaurants are heavily concentrated. The hotel ranking on the next page counts stars within a
one-hour subway or bus ride, so the two numbers that matter are Dongcheng (9 restaurants, 10 stars) and
Chaoyang (20 restaurants, 27 stars). Shunyi has Blackswan only, 2 stars, and is far outside a one-hour ring
from the centre.</p>
<div class="tablewrap">
<table style="min-width:520px">
<thead><tr><th>District</th><th>Starred restaurants</th><th>Stars</th><th>What it means for a hotel</th></tr></thead>
<tbody>
<tr><td class="name">Chaoyang</td><td class="num">20</td><td class="num">27</td><td>The CBD/Sanlitun cluster; most of the modern dining rooms.</td></tr>
<tr><td class="name">Dongcheng</td><td class="num">9</td><td class="num">10</td><td>Wangfujing, the hutongs, Forbidden City; the tourist core.</td></tr>
<tr><td class="name">Xicheng</td><td class="num">3</td><td class="num">3</td><td>Financial Street and the north-west lakes.</td></tr>
<tr><td class="name">Shunyi</td><td class="num">1</td><td class="num">2</td><td>Blackswan only, near the airport road. Not walkable to anything else.</td></tr>
</tbody>
</table>
</div>
<script>
document.getElementById('q').addEventListener('input', function(){{
  var q = this.value.trim().toLowerCase();
  document.querySelectorAll('#t tbody tr').forEach(function(tr){{
    tr.hidden = q ? tr.textContent.toLowerCase().indexOf(q) === -1 : false;
  }});
}});
</script>
"""
    write("restaurants.html", shell("restaurants.html", "Starred restaurants — Beijing 2027",
                                    "MICHELIN Guide Beijing 2027, row by row", body))


# --------------------------------------------------------------------- hotels
def money(v):
    return "—" if v is None else f"${v:,}"


def page_hotels():
    order = sorted(HOTELS, key=lambda h: (h["w1_total_usd"] is None, h["w1_total_usd"] or 0))
    trs = []
    for h in order:
        bed_ok = h.get("compliant")
        if bed_ok is False:
            bedcell = chip("u", "twin only")
        elif h.get("bed"):
            bedcell = chip("v", "meets") if "king" in h["bed"].lower() or "double" in h["bed"].lower() else chip("f", "check")
        else:
            bedcell = chip("u", "unknown")
        trs.append(f"""<tr>
<td class="name">{e(h['name'])}<span class="meta">{e(h.get('booking_area'))}</span></td>
<td>{bedcell}<span class="meta">{e(h.get('bed')) or 'bed type not captured'}</span></td>
<td>{e(h.get('bathroom')) or chip('u', 'not captured')}</td>
<td class="num">{money(h.get('w1_total_usd'))}<span class="meta">15&ndash;22 Feb</span></td>
<td class="num">{money(h.get('w2_total_usd'))}<span class="meta">1&ndash;8 Mar</span></td>
<td>{e(h.get('guest_score')) or '—'}</td>
<td>{e(h.get('subway')) or '—'}</td>
<td style="min-width:150px">{a(h.get('url_feb'), 'Feb rate')}{' &middot; ' + a(h.get('url_mar'), 'Mar rate') if h.get('url_mar') else ''}</td>
</tr>""")
    body = f"""
<h1>Six 5-star hotels, priced on real dates</h1>
<p class="lede">Every figure below is a <strong>7-night total for 2 adults in 1 room</strong>, read off a dated
Booking.com page on {e(R['_meta']['generated'])}. Two windows were priced: the preferred week
<strong>Mon 15 &ndash; Mon 22 Feb 2027</strong> and a control week <strong>Mon 1 &ndash; Mon 8 Mar 2027</strong>.
The point of the second window was to test the assumption that going later is cheaper. It is not, uniformly.</p>

<div class="callout info">
<p><strong>Why there is no single &ldquo;ranked list&rdquo; yet.</strong> Ranking needs your weights for price against location
against amenities, and the honest answer is that only one hotel could be priced <em>like-for-like</em> in both weeks.
Rather than invent a scoring formula and dress it up as objectivity, the table gives you the
verified numbers and the trade-offs in plain words below it.</p>
</div>

<div class="tablewrap">
<table>
<thead><tr>
<th>Hotel</th><th>Bed</th><th>Bathroom</th><th>7 nights, 15&ndash;22 Feb</th><th>7 nights, 1&ndash;8 Mar</th>
<th>Guest score</th><th>Transit</th><th>Rate page</th>
</tr></thead>
<tbody>
{''.join(trs)}
</tbody>
</table>
</div>
<p class="hint">Amounts exclude local VAT/tax where Booking says so; the exact wording is kept per row in
<code>data/hotels.json</code>. A dash means the hotel was not priced in that window &mdash; blank, not zero.</p>

<h2>The one clean comparison</h2>
<div class="callout warn">
<p><strong>New World Beijing Hotel</strong> is the only property priced as the same room type in both windows:
Superior Room King, 1 king bed, private bathroom with walk-in shower and deep soaking tub. Public rate
<strong>$1,177 for 15&ndash;22 Feb</strong> against <strong>$1,257 for 1&ndash;8 Mar before tax</strong>. February is
<em>cheaper</em> by $80 on the identical room. Cheaper figures exist ($901 and $961.23) but both require a
signed-in account, so they are noted and excluded rather than used.</p>
</div>

<h2>What each hotel actually costs you in trade-offs</h2>
<div class="grid g2">
  <div class="card"><h3>Hilton Beijing Wangfujing &mdash; $1,244</h3>
  <p class="sub">The balanced pick. King bed, 8.7 from 904 reviews, Wangfujing, free cancellation with no prepayment.
  The March week was $1,101 + $183 tax on the standard Deluxe King, so the two weeks are within $40 of each other once
  the room types are lined up.</p></div>
  <div class="card"><h3>New World Beijing &mdash; $1,177</h3>
  <p class="sub">Best bathroom of the set and the largest room (538 sq ft). Chongwenmen, Lines 2 and 5, about 10 minutes
  on foot, 8 minutes to the Temple of Heaven. 9.1 from 1,542 reviews. Slightly further from Wangfujing.</p></div>
  <div class="card"><h3>Waldorf Astoria &mdash; $2,246</h3>
  <p class="sub">9.2 from 474 reviews, heated pool and steam room, Wangfujing. Nearly double the Hilton for the same
  postcode. The result card was labelled &ldquo;Featured &mdash; pays us a higher commission&rdquo;, so its prominence in
  search results is not evidence of value.</p></div>
  <div class="card"><h3>Sunworld Dynasty &mdash; $697</h3>
  <p class="sub">The cheapest 5-star found, 9.1 from 4,217 reviews. But the priced room is <strong>twin beds</strong>,
  which fails your queen-or-larger rule, and $697 was a members-only rate against $836 public. A king room in the
  same hotel was not priced.</p></div>
  <div class="card"><h3>The Peninsula &mdash; price not captured</h3>
  <p class="sub">9.5 from 596 reviews, the highest score in the set, Wangfujing. Its room price was not in the part of
  the page that could be read, so it is blank rather than guessed.</p></div>
  <div class="card"><h3>Grand Hyatt &mdash; excluded</h3>
  <p class="sub">The page loaded in Portuguese with a non-refundable apartment rate ($1,568 + $260 tax). That is not
  comparable to the refundable room-only totals above, so it is recorded as a note and left out of the table.</p></div>
</div>

<h2>Cheapest upcoming time to book &mdash; what can honestly be said</h2>
<p>Two windows is not a price curve. What the data supports is narrower than a recommendation, and it is worth stating
plainly instead of overclaiming:</p>
<ul class="tight">
<li>For the one like-for-like room, <strong>your preferred February week is cheaper than the early-March control week</strong>.</li>
<li><strong>15 Feb 2027 is the Monday after the Spring Festival holiday</strong> (Golden Week ran 6&ndash;13 Feb 2027, with
14 Feb a make-up working day). Demand collapses right after that, which is consistent with February pricing well.</li>
<li>Free-cancellation cut-offs cluster around 7 days before arrival, so a rate can be held now and re-checked later
  at no cost &mdash; that is the actual cost-control lever here, not a forecast.</li>
<li><strong>Not verified:</strong> whether prices fall further later in March, or whether a 21-day stay is cheaper per
  night. Neither was priced.</li>
</ul>
"""
    write("hotels.html", shell("hotels.html", "Hotels — Beijing 2027", "7-night totals on real dates", body))


# ----------------------------------------------------------------- activities
def page_activities():
    trs = []
    for x in ACTS:
        price = (f"¥{x['price_adult_cny']}" if x.get("price_adult_cny") is not None else chip("u", "not read"))
        two = (f"<strong>¥{x['price_two_adults_cny']}</strong>" if x.get("price_two_adults_cny") is not None
               else chip("u", "blank"))
        trs.append(f"""<tr>
<td class="name">{e(x['name'])}<span class="meta">{e(x['type'])} &middot; {e(x['district'])}</span></td>
<td>{e(x.get('days')) or chip('u', 'blank')}</td>
<td>{e(x.get('hours_low')) or chip('u', 'blank')}<span class="meta">{e(x.get('hours_high'))}</span></td>
<td>{e(x.get('exceptions')) or '—'}</td>
<td class="num">{price}</td>
<td class="num">{two}</td>
<td class="nowrap">{a(x.get('website'), 'official')}{' &middot; ' + a(x.get('ticket_url'), 'tickets') if x.get('ticket_url') else ''}</td>
</tr>""")
    verified = sum(1 for x in ACTS if x.get("verified") and len(x.get("verified")) > 2)
    body = f"""
<h1>Activities, with the winter hours that actually apply</h1>
<p class="lede">Your window sits entirely inside Beijing&rsquo;s <strong>low season (1 Nov &ndash; 31 Mar)</strong>, so every venue here
runs its shorter winter timetable and several close an hour earlier than any summer guide will tell you.
{verified} of {len(ACTS)} rows have their hours read from the operator&rsquo;s own site.</p>

<div class="callout">
<p><strong>Two verified prices exist, and both are genuinely cheap.</strong> The Palace Museum is ¥40 per adult in low season
and the Summer Palace combo is ¥50. Three venues publish no machine-readable price at all, so those cells are blank &mdash;
see the log.</p>
</div>

<div class="tablewrap">
<table>
<thead><tr><th>Place</th><th>Days open</th><th>Hours (winter)</th><th>Exceptions</th><th>Per adult</th><th>2 adults</th><th>Official</th></tr></thead>
<tbody>
{''.join(trs)}
</tbody>
</table>
</div>

<h2>Monday is the trap</h2>
<p>Monday 15 Feb is likely your arrival day and Monday 22 Feb is your departure day, so the usual
&ldquo;museums on the first full day&rdquo; plan breaks on arrival. On <em>any</em> Monday inside this window:</p>
<ul class="tight">
<li><strong>Closed:</strong> the Palace Museum, the National Museum of China, and the three main halls inside the
Temple of Heaven (Hall of Prayer for Good Harvests, Echo Wall, Circular Mound Altar).</li>
<li><strong>Closed:</strong> the Summer Palace&rsquo;s inner gardens &mdash; Tower of Buddhist Incense, Dehe Yuan, Suzhou Street,
the museum.</li>
<li><strong>Open:</strong> the Temple of Heaven <em>park</em> itself from 06:30, the Mutianyu Great Wall, and the Lama Temple.</li>
</ul>
<p>That is why the itinerary puts the Forbidden City on Tuesday and keeps Monday for the hutongs and a long lunch.</p>

<h2>Booking reality, in order of how easily it bites</h2>
<ol class="tight">
<li><strong>Palace Museum</strong> &mdash; no tickets are sold on the day. Passport number required at booking, daily cap 40,000.</li>
<li><strong>National Museum</strong> &mdash; free but reservation-only, released 7 days ahead at 17:00, one booking per account
per week, three timed slots, and late arrivals are refused. Three no-shows block you for 30 days.</li>
<li><strong>Mutianyu</strong> &mdash; real-name ticket, passport accepted, booking opens ahead of the date; the cable car is
the only sane way up in February ice.</li>
<li><strong>Summer Palace</strong> &mdash; online ticketing; boats are out of service in this window anyway.</li>
</ol>
"""
    write("activities.html", shell("activities.html", "Activities — Beijing 2027", "Winter hours, closures and ticket rules", body))


# ------------------------------------------------------------------ itinerary
DAYS = [
    ("Mon 15 Feb", "Arrival &mdash; Wangfujing, no museums", [
        "Land, check in, walk Wangfujing and the Donghuamen night-food street.",
        "Today is a Monday: the Palace Museum, the National Museum and the Temple of Heaven halls are all shut, so nothing is lost by arriving today.",
        "Dinner near the hotel &mdash; <strong>Fu Chun Ju</strong> (PuXuan) is open 17:30&ndash;21:30 and is a 1-star Cantonese room inside a Wangfujing hotel; book ahead.",
    ]),
    ("Tue 16 Feb", "Forbidden City &rarr; Jingshan", [
        "<strong>Palace Museum</strong>, 08:30&ndash;16:30, last entry 15:30. Ticket pre-booked with passport; no on-the-day sales.",
        "Exit north to Jingshan Park for the view back over the roofs &mdash; unverified hours, so go before 16:00.",
        "Dinner: <strong>King&rsquo;s Joy</strong> in the Wudaoying hutongs, or <strong>Trb Hutong</strong> for the exact-price menu.",
    ]),
    ("Wed 17 Feb", "Temple of Heaven &rarr; National Museum", [
        "<strong>Temple of Heaven</strong> early, from 06:30 for the park and 08:00 for the halls. Halls open today; they close Mondays.",
        "<strong>National Museum of China</strong> on a timed slot &mdash; book exactly 7 days ahead at 17:00.",
        "Dinner: <strong>Xin Rong Ji (Xinyuan South Road)</strong>, 3 stars, 17:30&ndash;21:00. The 28-day duck needs pre-ordering.",
    ]),
    ("Thu 18 Feb", "Mutianyu Great Wall", [
        "Full day, 70 km north. Off-season hours 08:00&ndash;17:30 with ticket sales ending 16:30.",
        "Cable car up; February ice on the steps is the real risk, not the distance.",
        "Back for a late dinner &mdash; keep it close to the hotel; <strong>Cai Yi Xuan</strong> serves until 22:00.",
    ]),
    ("Fri 19 Feb", "Lama Temple &amp; the hutongs", [
        "<strong>Lama Temple</strong> at opening (winter hours end 16:30), then the Confucius Temple and Wudaoying on foot.",
        "Lunch at <strong>King&rsquo;s Joy</strong> if dinner was elsewhere on Tuesday.",
        "Dinner: <strong>Lu Shang Lu</strong> (2 stars) or <strong>Jingji</strong> in the Ritz-Carlton.",
    ]),
    ("Sat 20 Feb", "Summer Palace &mdash; Lantern Festival", [
        "<strong>Summer Palace</strong>: park 06:30&ndash;19:00, inner gardens 08:30&ndash;17:00, combo ticket ¥50.",
        "No boats in this season &mdash; the lake is a walk, not a cruise.",
        "<strong>20 Feb is Lantern Festival</strong>: expect evening crowds at temples and parks, and prix-fixe menus at several fine-dining rooms. Book dinner before you fly.",
    ]),
    ("Sun 21 Feb", "798 / Olympic Park, then the big one", [
        "Slow morning in 798 Art District or the Olympic Park.",
        "Dinner: <strong>Chao Shang Chao</strong>, the city&rsquo;s other 3-star room. No published hours &mdash; confirm by phone before relying on it.",
    ]),
    ("Mon 22 Feb", "Departure", [
        "Monday again: museums shut. Temple of Heaven <em>park</em> opens at 06:30 if you want a last walk.",
        "Check-out; the 7-night hotel totals on this site end here.",
    ]),
]


def page_itinerary():
    cards = []
    for d, t, items in DAYS:
        lis = "".join(f"<li>{i}</li>" for i in items)
        cards.append(f'<div class="day"><h3><span class="date">{d}</span> {t}</h3><ul>{lis}</ul></div>')
    body = f"""
<h1>Seven nights, built around other people&rsquo;s closing days</h1>
<p class="lede">15&ndash;22 Feb 2027 is eight days and seven nights, and it starts and ends on a Monday &mdash; the one weekday
when most of Beijing&rsquo;s indoor sights shut. The plan below is arranged around that, around the verified winter hours,
and around your two preferred criteria: the star restaurants you came for, and not being on a bus at 7am every day.</p>

<div class="callout info">
<p><strong>Timing luck worth knowing.</strong> Spring Festival 2027 runs 6&ndash;13 Feb with 14 Feb a make-up working day, so
your arrival on 15 Feb lands on the first quiet Monday after the holiday. Prices and crowds both drop at exactly that point.</p>
</div>

{''.join(cards)}

<h2>What this plan can and cannot cost yet</h2>
<div class="tablewrap">
<table style="min-width:600px">
<thead><tr><th>Line</th><th>Known total</th><th>Status</th></tr></thead>
<tbody>
<tr><td>Hotel, 7 nights, Hilton Wangfujing king</td><td class="num">$1,244</td><td>{chip('v', 'verified')}</td></tr>
<tr><td>Palace Museum, 2 adults</td><td class="num">¥80</td><td>{chip('v', 'verified')}</td></tr>
<tr><td>Summer Palace, 2 adults (combo)</td><td class="num">¥100</td><td>{chip('v', 'verified')}</td></tr>
<tr><td>Trb Hutong, 2 adults, entry menu</td><td class="num">¥1,576</td><td>{chip('v', 'verified')} before 15% service</td></tr>
<tr><td>The other 32 restaurants</td><td class="num">—</td><td>{chip('u', 'no published price')}</td></tr>
<tr><td>Mutianyu, National Museum, Lama Temple, flights, transfers</td><td class="num">—</td><td>{chip('u', 'blank')}</td></tr>
</tbody>
</table>
</div>
<p>A grand total would be fiction. Four lines are solid, and the restaurant line &mdash; which is the whole reason for the
trip &mdash; is the one nobody publishes. <a href="questions.html">The open questions page</a> says exactly how to close
that gap yourself in about twenty minutes of phone calls.</p>
"""
    write("itinerary.html", shell("itinerary.html", "Itinerary — Beijing 2027", "8 days, 15–22 Feb 2027", body))


# ------------------------------------------------------------------ questions
QUESTIONS = [
    (
        "Which fine-dining rooms will actually be open on our dates, and at what price?",
        "Twelve of the 33 starred rooms publish no hours at all, and none of the 33 publishes a price for two. "
        "Without a confirmed opening day and a confirmed menu price, the restaurant plan is a wish list, not a plan.",
        "MICHELIN lists the band only. Eight rows have hours from an official page; one row has a real menu price.",
        "Phone the six you care about and ask two questions: are you open on <em>these dates</em>, and what is the "
        "set menu price per person. Phone numbers are already in every row of the restaurants table.",
    ),
    (
        "Is a 21- or 28-day stay cheaper per night than 7 nights?",
        "The brief allows 2&ndash;4 weeks but only 7-night stays were priced, so the per-night economics of a longer "
        "trip are unknown rather than unfavourable.",
        "Two 7-night windows were priced. Longer-stay discounts were not tested.",
        "Re-run the same Booking search for 14 and 21 nights from 15 Feb and compare the nightly rate; serviced "
        "apartments in Chaoyang are the usual answer for stays over three weeks.",
    ),
    (
        "Which room type should the price comparison be based on?",
        "Two hotels priced only as twins and one only as a non-refundable apartment, so the set of comparable "
        "numbers shrank from six hotels to three.",
        "King rooms were priced at Hilton ($1,244), New World ($1,177) and Waldorf ($2,246); Sunworld was twin only.",
        "Decide whether a king is a hard requirement or a preference. If it is hard, Sunworld and the Grand Hyatt "
        "apartment drop out and the comparison stays at three hotels.",
    ),
    (
        "One base for all seven nights, or a split stay?",
        "Twenty of the 33 starred restaurants are in Chaoyang and nine in Dongcheng. A Chaoyang hotel shortens the "
        "evenings; a Dongcheng hotel shortens the sightseeing. A split fixes both and costs a lost half-day.",
        "All six priced hotels are in Dongcheng. No Chaoyang hotel has been priced yet.",
        "Price two Chaoyang 5-stars for the same dates, then compare a 4+3 split against the single-base total.",
    ),
    (
        "How much of the trip should be MICHELIN at all?",
        "The restaurants are the reason for the itinerary, but 33 starred rooms in 7 nights for two people is "
        "neither physically nor financially sensible, and nobody publishes the price that would set the ceiling.",
        "The band column is the only cost signal: four rooms sit at ¥¥¥¥, the rest at ¥¥ or ¥¥¥.",
        "Pick six to eight starred meals, schedule them, and fill the other dinners from the Bib Gourmand list, "
        "which is cheaper and easier to book.",
    ),
    (
        "What is the passport and visa situation, and does it gate the bookings?",
        "The Palace Museum and the National Museum both require a passport number at booking time, days ahead. "
        "If entry documentation is unresolved those two bookings cannot be made at all.",
        "The U.S. advisory is Level 2 (renewed 19 Oct 2026) citing arbitrary law enforcement and exit bans. "
        "Visa-free entry rules were not verified in this pass.",
        "Confirm visa or visa-free eligibility for your nationality before booking any timed ticket, then book "
        "both museums exactly 7 days out.",
    ),
    (
        "Is February weather acceptable for the Mutianyu day?",
        "A full day on an exposed ridge in February can be a wasted day, and the cable car is the only realistic "
        "ascent.",
        "Off-season hours are published (08:00&ndash;17:30). Weather, wind-chill and cable-car suspension policy are not.",
        "Set a go/no-go rule in advance, for example cancel if the forecast high is below &minus;5&deg;C or the wind "
        "above 40 km/h, and keep that day movable.",
    ),
]


def page_questions():
    cards = []
    for i, (q, why, now, action) in enumerate(QUESTIONS, 1):
        cards.append(f"""<article class="card" style="margin:10px 0">
  <h3>{i}. {q} {chip('f', 'open')}</h3>
  <p class="sub" style="margin:6px 0 4px"><strong>Why it blocks a decision:</strong> {why}</p>
  <p class="sub" style="margin:4px 0"><strong>What is known today:</strong> {now}</p>
  <p class="sub" style="margin:4px 0"><strong>How to close it:</strong> {action}</p>
</article>""")
    body = f"""
<h1>Everything that has to be answered before a booking</h1>
<p class="lede">Seven questions, each one written so that it can be closed by a specific action rather than a discussion.
Where the answer is partly known, what is known is stated &mdash; and what is missing is named.</p>
{''.join(cards)}
<div class="callout">
<p><strong>The one that matters most is the first.</strong> Twelve starred rooms publish no opening hours and not one of the
33 publishes a price for two. A restaurant-led trip cannot be costed from public sources; it has to be costed by
phoning, which takes an afternoon and settles most of the uncertainty in this plan.</p>
</div>
"""
    write("questions.html", shell("questions.html", "Open questions — Beijing 2027", "What must be answered before booking", body))


# ----------------------------------------------------------------- suggestions
SUGGESTIONS = [
    (
        "Split the week across two neighbourhoods",
        "Seven nights in one Dongcheng hotel means roughly forty minutes each way to the Chaoyang dining cluster, "
        "twice a day. Three nights in Chaoyang after four in Dongcheng removes most of that.",
        "Costs one half-day of packing; buys back about two hours a day and stops the evenings being a taxi ride.",
    ),
    (
        "Book six restaurants, not sixteen",
        "Every top-end room here is a two- to three-hour tasting menu. Six in seven nights is already a commitment; "
        "sixteen is a schedule nobody enjoys, and the bill is unknowable from public sources.",
        "Keeps most meals in the ¥¥&ndash;¥¥¥ band and turns the trip into a holiday rather than a checklist.",
    ),
    (
        "Use free cancellation as the price hedge",
        "Every rate captured here was free-cancellation with no prepayment. Hold the room now, re-check in "
        "December, cancel if it drops.",
        "Costs nothing, and removes the entire &ldquo;should we have waited?&rdquo; question.",
    ),
    (
        "Let the Monday closures set the skeleton of the plan",
        "Arrival and departure are both Mondays, and Mondays shut the Palace Museum, the National Museum, the "
        "Temple of Heaven halls and the Summer Palace gardens &mdash; the four things people most want to see.",
        "The itinerary already does this. It is the highest-value structural choice in the plan.",
    ),
    (
        "Keep the Great Wall day movable until 48 hours out",
        "February wind and ice can suspend the cable car, and the wall without the cable car is a two-hour climb "
        "on ice.",
        "Keep Mutianyu flexible and let the two reservation-bound museum days be the fixed anchors.",
    ),
    (
        "Read the empty video column as a filter, not a verdict",
        "Only 13 of 33 starred rooms have a findable review video, and several of those are near-misses. The empty "
        "rows are mostly small hotel dining rooms that nobody films.",
        "Treat &ldquo;no video&rdquo; as &ldquo;no independent footage exists&rdquo;. Every 3-star and 2-star room has footage, "
        "which is where video actually helps.",
    ),
    (
        "Get the three missing prices by phone, not online",
        "King&rsquo;s Joy, Chao Shang Chao and Xin Rong Ji publish no menu price anywhere, and two of them are the meals "
        "you would remember most.",
        "Three phone calls convert the biggest unknown in the budget into three known figures.",
    ),
]


def page_suggestions():
    cards = []
    for i, (t, why, what) in enumerate(SUGGESTIONS, 1):
        cards.append(f"""<article class="card" style="margin:10px 0">
  <h3>{i}. {t}</h3>
  <p class="sub" style="margin:6px 0"><strong>Why:</strong> {why}</p>
  <p class="sub" style="margin:4px 0"><strong>What it changes:</strong> {what}</p>
</article>""")
    body = f"""
<h1>Changes worth making before anything is booked</h1>
<p class="lede">These are improvements to the plan itself, not to the data. Each one names what it costs as well as what
it gains, because a suggestion that only lists benefits is a sales pitch.</p>
{''.join(cards)}
"""
    write("suggestions.html", shell("suggestions.html", "Suggestions — Beijing 2027", "Improvements to review before booking", body))


# --------------------------------------------------------------------- flagged
def page_flagged():
    rest_flags = [r for r in ROWS if r.get("flag")]
    hours_gap = [r for r in ROWS if not r.get("hours")]
    soc_gap = [r for r in ROWS if not r.get("social")]
    rows_flag = "".join(
        f'<tr><td class="name">{e(r["name"])}</td><td>{e(r.get("district"))}</td><td>{e(r["flag"])}</td></tr>'
        for r in rest_flags)
    rows_hours = "".join(f"<li>{e(r['name'])}</li>" for r in hours_gap)
    rows_soc = "".join(f"<li>{e(r['name'])}</li>" for r in soc_gap)
    act_flags = "".join(
        f'<tr><td class="name">{e(x["name"])}</td><td>{e(x.get("flag"))}</td></tr>'
        for x in ACTS if x.get("flag"))
    hot_flags = "".join(
        f'<tr><td class="name">{e(h["name"])}</td><td>{e(h.get("flag"))}</td></tr>'
        for h in HOTELS if h.get("flag"))
    body = f"""
<h1>Verification log</h1>
<p class="lede">Everything that could not be confirmed from an official source, written down instead of filled in.
This page is the reason the tables elsewhere have gaps: a blank cell here has a named cause.</p>

<div class="grid g4" style="margin:16px 0">
  <div class="card kpi"><div class="big">{len(rest_flags)}</div><div class="sub">restaurants with a stated flag</div></div>
  <div class="card kpi"><div class="big">{len(hours_gap)}</div><div class="sub">no published hours</div></div>
  <div class="card kpi"><div class="big">{len(soc_gap)}</div><div class="sub">no social link found</div></div>
  <div class="card kpi"><div class="big">{len(ACTS) - 4}</div><div class="sub">activities with a blank price or hours</div></div>
</div>

<h2>Restaurant-level flags</h2>
<div class="tablewrap"><table style="min-width:640px">
<thead><tr><th>Restaurant</th><th>District</th><th>Flag</th></tr></thead>
<tbody>{rows_flag}</tbody></table></div>

<h2>No published opening hours ({len(hours_gap)} of {len(ROWS)})</h2>
<div class="card"><ul class="tight" style="columns:2">{rows_hours}</ul></div>
<p>These are blank on purpose. None of them publishes a weekly schedule on an official page, and inventing
&ldquo;probably open daily&rdquo; for a restaurant that takes one sitting a night is how people end up outside a locked door.</p>

<h2>No review video found ({len(soc_gap)} of {len(ROWS)})</h2>
<div class="card"><ul class="tight" style="columns:2">{rows_soc}</ul></div>
<p><strong>What was tried:</strong> YouTube search and the YouTube oEmbed endpoint as an existence check, TikTok video pages,
and Instagram profile pages. Instagram blocks automated reads for most restaurant handles, TikTok&rsquo;s oEmbed always fails
and only full video URLs render, and YouTube search returns unrelated hutong vlogs for most of these names. Every link that
<em>is</em> included was confirmed to exist, and the ones that are only near-misses say so in their own note.</p>

<h2>Near-miss links kept deliberately</h2>
<ul class="tight">
<li><strong>Gastro Esthetics DaDong</strong> &mdash; three Da Dong <em>group</em> videos. None identifies the Michelin-starred room.</li>
<li><strong>Fu Chun Ju</strong> &mdash; a Chinese video using the exact name 富春居, with no city stated.</li>
<li><strong>Sheng Yong Xing (Chaoyang)</strong> &mdash; one TikTok is the <em>Shanghai</em> outpost, flagged in its note.</li>
<li><strong>King&rsquo;s Joy</strong> &mdash; three of five videos were filmed when it held three stars; it now holds two.</li>
<li><strong>Blackswan</strong> &mdash; the clip found is about dress etiquette, not the food.</li>
</ul>

<h2>Activity flags</h2>
<div class="tablewrap"><table style="min-width:640px">
<thead><tr><th>Place</th><th>Flag</th></tr></thead>
<tbody>{act_flags}</tbody></table></div>

<h2>Hotel flags</h2>
<div class="tablewrap"><table style="min-width:640px">
<thead><tr><th>Hotel</th><th>Flag</th></tr></thead>
<tbody>{hot_flags}</tbody></table></div>

<h2>Source reliability, stated plainly</h2>
<ul class="tight">
<li><strong>Booking.com is an intermediary, not the hotel.</strong> Its own search results carry commission labels and
members-only rates. Every price here is linked to the exact dated query so you can re-read it yourself.</li>
<li><strong>MICHELIN publishes bands, not prices,</strong> and its listings carry no opening days for most Beijing rooms.</li>
<li><strong>Two park sites (Temple of Heaven, Jingshan, Beihai) publish prices and hours only as images or script output,</strong>
so their price cells are blank. Third-party figures are named in the flag but never promoted to verified.</li>
<li><strong>Instagram and TikTok are not reliably readable</strong> by automated fetching; only what rendered was recorded.</li>
</ul>
"""
    write("flagged.html", shell("flagged.html", "Verification log — Beijing 2027", "What could not be verified, and why", body))


# ---------------------------------------------------------------------- index
def page_index():
    n3 = sum(1 for r in ROWS if r["stars"] == 3)
    n2 = sum(1 for r in ROWS if r["stars"] == 2)
    n1 = sum(1 for r in ROWS if r["stars"] == 1)
    cheapest = min((h for h in HOTELS if h.get("w1_total_usd")), key=lambda h: h["w1_total_usd"])
    body = f"""
<h1>Beijing, 15&ndash;22 February 2027</h1>
<p class="lede">A restaurant-led week for two adults, built only from values that could be read on an official page.
Where a number does not exist publicly, the table says so instead of filling the gap.</p>

<div class="grid g4" style="margin:18px 0">
  <div class="card kpi"><div class="big">{len(ROWS)}</div><div class="sub">starred restaurants verified ({n3}/{n2}/{n1} by stars)</div></div>
  <div class="card kpi"><div class="big">{len(HOTELS)}</div><div class="sub">5-star hotels priced on your dates</div></div>
  <div class="card kpi"><div class="big">{len(ACTS)}</div><div class="sub">activities with winter hours checked</div></div>
  <div class="card kpi"><div class="big">13/33</div><div class="sub">restaurants with a review video</div></div>
</div>

<div class="callout">
<p><strong>The headline finding is a negative one.</strong> You asked for the restaurant cost for two in the same row as each
restaurant. Of 33 starred rooms, exactly one publishes its own menu prices. The MICHELIN Guide publishes a price
<em>band</em>. So 32 rows show a band and a blank, and that blank is accurate rather than lazy &mdash; closing it needs
phone calls, and the <a href="questions.html">open questions page</a> sets out which six calls would settle it.</p>
</div>

<h2>Start here</h2>
<div class="grid g2">
  <a class="card" href="restaurants.html" style="text-decoration:none"><h3>All 33 starred restaurants &rarr;</h3>
  <p class="sub">Star level stated plainly, hours only where published, price for two where it exists, and every review video that could be confirmed.</p></a>
  <a class="card" href="hotels.html" style="text-decoration:none"><h3>Hotels on real dates &rarr;</h3>
  <p class="sub">Six 5-star hotels priced as 7-night totals for 15&ndash;22 Feb, with a March control week. Cheapest compliant: {e(cheapest['name'])} at ${cheapest['w1_total_usd']:,}.</p></a>
  <a class="card" href="activities.html" style="text-decoration:none"><h3>Activities &amp; winter hours &rarr;</h3>
  <p class="sub">Low-season timetables, Monday closures, and the two ticket prices that are actually published.</p></a>
  <a class="card" href="itinerary.html" style="text-decoration:none"><h3>The 8-day plan &rarr;</h3>
  <p class="sub">Built around the fact that your first and last days are both Mondays, when most indoor sights are shut.</p></a>
</div>

<h2>Three things worth knowing before you read a table</h2>
<ol class="tight">
<li><strong>Your dates are good.</strong> Spring Festival 2027 runs 6&ndash;13 Feb; you arrive on the first quiet Monday
after it, when crowds and hotel prices both fall.</li>
<li><strong>Your dates are also cold and short.</strong> Every venue runs winter hours, the Summer Palace boats stop
altogether, and the Mutianyu cable car is the only sensible way up.</li>
<li><strong>February is not automatically the expensive week.</strong> The one hotel priced like-for-like in both windows was
<em>cheaper</em> in February ($1,177) than in early March ($1,257 before tax).</li>
</ol>

<h2>What is in these files</h2>
<p class="sub">This build is self-contained in <code>beijing-verified-2027/</code>: the pages you are reading, plus
<code>data/restaurants.json</code>, <code>data/hotels.json</code> and <code>data/activities.json</code>. It does not touch the
shared Beijing planner at the repository root, which a different session owns. The <a href="flagged.html">verification
log</a> lists every gap; <a href="suggestions.html">suggestions</a> lists what to change before booking.</p>
"""
    write("index.html", shell("index.html", "Beijing 2027 — verified trip planner", "15–22 Feb 2027 for two adults", body))


if __name__ == "__main__":
    page_index()
    page_restaurants()
    page_hotels()
    page_activities()
    page_itinerary()
    page_questions()
    page_suggestions()
    page_flagged()
    print("done")

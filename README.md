# ChinaFun1 — four China 2027 trip planners

This repository holds **four independent, source-verified plans** for the same brief (2 adults, 7 nights,
15 Feb – 23 Mar 2027), produced by four parallel sessions that answered the question differently:

| Plan | City | Where it lives | Entry point |
|---|---|---|---|
| `fac6d965` | **Beijing** | repo root | [`index.html`](index.html) |
| `68e13071` | **Shanghai** | `docs/` | [`docs/index.html`](docs/index.html) |
| `3b27db6c` | **Shanghai** | `shanghai-2027/` | [`shanghai-2027/index.html`](shanghai-2027/index.html) |
| `16153d37` | **Shanghai** | `shanghai-verified-2027/` | [`shanghai-verified-2027/index.html`](shanghai-verified-2027/index.html) |

Both follow the same rules: every row links to the official source it came from, unconfirmed values are left
blank and flagged, hotels are priced as a 7-night total for two, and MICHELIN "starred" is never confused with
"listed". Read all four before deciding — the honest answer to "which city" is that the brief did not say, and the
plans optimise different things (Beijing: 33 starred restaurants and a capital-city itinerary; Shanghai:
two independent studies, below).

## The two Shanghai plans disagree, and that is worth knowing

`docs/` and `shanghai-2027/` researched the same city independently and reached **different numbers from
the same Booking.com source**. Neither is wrong; they priced different room categories, which the Beijing
study identifies as the real cost driver.

| | `docs/` (`68e13071`) | `shanghai-2027/` (`3b27db6c`) |
|---|---|---|
| Recommended hotel | Radisson Blu New World, **Junior Suite** | Radisson Blu New World, **queen room** |
| 7-night total | **$1,116** (before 6.6% VAT) | **$922** (Genius member rate; list $1,025) |
| Starred rows itemised | 12 | 14 |
| Hotel ranking | Geocoded hotels, 60-min band on 2★+ only | 5 hotels, published transit model with declared constants |
| Restaurant cost column | not attempted | present, `null` + flagged for all 12 |

**Where they agree — and this is the finding that matters:** once you require "starred, reachable inside
an hour", *every* central hotel passes. Shanghai's MICHELIN density does not discriminate between hotels on
this brief, so **price and room quality should decide, not proximity.** `shanghai-2027/` quantifies the
spread as 6.6 minutes of modelled transit across all five hotels; `docs/` reaches it by a different route.

**Where they differ:** the $194 gap between $922 and $1,116. It reflects room type and VAT treatment, not a
data error. Confirm which room category you are actually being quoted before treating either as the price.

> **Note on the brief's dates:** the preferred window 15–18 Feb 2027 is 3 nights, which does not fit a 1–2 week
> trip. Both plans therefore price and schedule a 7-night stay starting 15 Feb. This is flagged, not hidden.

---

# Beijing plan (`fac6d965`) — repo root


A static, mobile-first planning dashboard for a **7-night Beijing trip for two adults, 15–22 February 2027**
(inside the 15 Feb – 23 Mar 2027 window), built around the MICHELIN Guide rather than around sightseeing.

**Live site:** published from the repository root via GitHub Pages.

## What is in here

| Path | What it is |
|---|---|
| `index.html` | Executive summary and the dashboard landing page |
| `hotels.html` | 12 Beijing hotels priced for the exact week, ranked on a published, auditable score |
| `michelin.html` | All 33 MICHELIN-starred restaurants in Beijing 2027 with star level, price band, hours, links |
| `activities.html` | Activities with verified/unverified flags on hours and ticket prices |
| `itinerary.html` | 7-night day-by-day plan that respects closing days |
| `decisions.html` | The 10 questions that block a booking, plus what is known vs unknown |
| `suggestions.html` | Improvement proposals awaiting review — nothing applied yet |
| `flagged.html` | Verification log, every blank field, irregularities, repository review |
| `assets/data.js` | The single source of truth for all rows |
| `assets/style.css`, `assets/app.js` | Design system and table renderers (no dependencies, no build step) |
| `COORDINATION.md` | Shared task board for parallel agent sessions |

## Editorial rules

1. Every value in every row links to the official source it came from.
2. If a value cannot be confirmed from an official source it is **left blank and flagged** — never estimated, never inferred.
3. Star status is stated explicitly: starred (with count) vs MICHELIN Selected vs Bib Gourmand.
4. Hotel prices are shown as the **total for a 7-night stay**, with the room type and bed type that price actually buys.
5. Every change is committed to a session branch and logged in `COORDINATION.md`.

## Run locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

No build step, no package manager, no external requests at runtime.

## Verification status

See [`flagged.html`](flagged.html) for the source-by-source log, the full list of blank fields and the known
irregularities. Headline caveats:

- Hotel totals are Booking.com "from" rates read on **25 Nov 2026**, not a locked contract.
- Michelin density counts cover **10 of 33** starred restaurants, so they are a lower bound.
- Transit times are deliberately **not** estimated; the ≤1-hour rule still needs a routing pass in Amap.


---

# Shanghai plan (`68e13071`) — `docs/`

**Live path:** `docs/index.html` · **Session branch:** `arena/68e13071-chinafun1`

A generated dashboard, not hand-written HTML: `data/*.json` → `build.py` → `docs/`.

**Recommendation:** Shanghai only, 7 nights Mon 15 Feb → Mon 22 Feb 2027, **Radisson Blu New World Junior Suite**
(1 queen bed, attached private bathroom) at **US$1,116 total for 7 nights** for 2 adults — the cheapest of the five
7-night windows priced, and the best of the hotels that could be geolocated.

**Headline finding:** the ≤60-minute MICHELIN-density test asked for in the brief does not separate central hotels —
all four geocodable hotels reach 10–11 of the 11 geocodable 2★/3★ restaurants. Price and room quality decide.

| Path | What it is |
|---|---|
| `data/*.json` | 14 datasets: hotels, restaurants, activities, itinerary, budget, windows, five-window sweep, flags, questions, suggestions S1–S12, verification log, source register, methodology |
| `build.py` | Renders `docs/` from `data/`. No dependencies. |
| `check.py` | Post-build checks: broken internal links, empty `href`s, missing `<title>`/viewport |
| `src/assets/` | Mobile-first CSS + tiny JS (menu, per-table filter). *Moved out of `assets/` so the Beijing plan keeps the repo-root assets.* |
| `docs/` | The generated Shanghai site |

Rebuild:

```bash
python3 build.py && python3 check.py
```

Pages: 11 — Overview · Hotels & Ranking · Michelin · Activities · Itinerary · Budget · Verification Log ·
Flagged for Review · Open Questions · Suggestions · Sources & Method.

**What is deliberately blank:** menu prices for two at every starred restaurant (MICHELIN publishes only a ¥ band),
hours for 9 of 12 restaurants, all attraction ticket prices/hours, live journey times, flights. Each is on
`docs/flagged.html` with the exact next step to close it.

---

# Shanghai plan (`3b27db6c`) — `shanghai-2027/`

A separate Shanghai study, kept in its own directory because it arrived after the other two plans were
already published to the repo root and `docs/`. It is self-contained: its own `assets/`, its own `data/`,
its own model.

**Entry point:** [`shanghai-2027/index.html`](shanghai-2027/index.html)

| Path | What it is |
|---|---|
| `shanghai-2027/index.html` | Executive summary, recommendation, price-window ladder |
| `shanghai-2027/itinerary.html` | Day-by-day 15–22 Feb 2027, built around verified Monday closures |
| `shanghai-2027/hotels.html` | 7 hotels, verified 7-night totals, bed and bathroom specs |
| `shanghai-2027/restaurants.html` | 50 starred venues, 14-row shortlist, ★ vs Guide-Selected distinction |
| `shanghai-2027/activities.html` | Hours, closures, official and social links |
| `shanghai-2027/ranking.html` | Hotels ranked by MICHELIN access, method disclosed in full |
| `shanghai-2027/questions.html` | 14 open questions, each with a resolution path |
| `shanghai-2027/suggestions.html` | 10 proposals awaiting decision — none implemented |
| `shanghai-2027/flagged.html` | Irregularities F-01…F-09 and dead ends |
| `shanghai-2027/sources.html` | Every source, what it proved and what it could not |
| `shanghai-2027/data/*.json` | Hotels, restaurants, activities, price windows, ranking output |
| `shanghai-2027/tools/proximity_model.py` | Stdlib-only proximity model, re-runnable |

### Its distinctive contribution: a disclosed transit model

No routing API was reachable, so rather than quietly guessing travel times this study publishes the
assumptions and the code that applies them — 6-minute walk to a station, 30 km/h average rail speed,
×1.25 detour factor, +6 minutes for a line change beyond 4 km. Anyone can change a constant and re-run:

```bash
python3 shanghai-2027/tools/proximity_model.py
```

The result is honest about its own limits: the minutes are **modelled, not routed** (±10 min), so the
*ranking* is trustworthy while the individual numbers are not. It also has a floor — a restaurant 0.32 km
away still scores 7 minutes — which is disclosed on the page rather than hidden.

### What it still cannot tell you

- **No menu price from any of the 12 shortlisted restaurants.** Every restaurant cost cell is `null`.
- Only 2 of 12 venues publish opening hours, so 7 dinner slots read "TBC".
- The **Pullman Jing'an at $708** — cheaper than the recommendation — is excluded from the ranking because
  its coordinates could not be verified; geocoding returned a district centroid.
- No total trip cost exists: airfare, visas and dinner prices were never sourced.

---

# Shanghai plan (`16153d37`) — `shanghai-verified-2027/`

**Entry point:** [`shanghai-verified-2027/index.html`](shanghai-verified-2027/index.html)
**Live path:** https://kanlerxz87-cyber.github.io/ChinaFun1/shanghai-verified-2027/
**Session branch:** `arena/16153d37-chinafun1`

A fourth independent Shanghai study, kept in its own directory because it started against the same
`8c3c56c` README-only commit as the others and arrived after all three were already published. The repo
root holds the Beijing plan and `docs/` was occupied, so nothing here was written over another session's
work. Self-contained: its own `assets/`, `data/` and `tools/`.

11 pages, 34 tables, 449 rows, 207 external links across 31 hosts. Pages are generated from
`shanghai-verified-2027/tools/sitegen.py`; `data/` is the source of truth.

| Path | What it is |
|---|---|
| `shanghai-verified-2027/index.html` | Landing page — verified answers, metric tiles, page index |
| `shanghai-verified-2027/executive-summary.html` | The full decision brief on one page |
| `shanghai-verified-2027/dates.html` | 2027 weekday map, CNY and Lantern Festival, entry rules, a 37-row day-by-day closure calendar |
| `shanghai-verified-2027/hotels.html` | Requirement compliance with verbatim room text, 21-row three-window rate matrix, cluster ranking |
| `shanghai-verified-2027/michelin.html` | 23 entries — star vs listed, band, address, cost for two, booking channels |
| `shanghai-verified-2027/activities.html` | Official hours and exceptions, the one-hour test, operator-published journey times |
| `shanghai-verified-2027/costs.html` | 7-night totals, both answers to "when is cheapest", three budget scenarios |
| `shanghai-verified-2027/questions.html` | 17 open questions, each with the verified position and a discovery route |
| `shanghai-verified-2027/suggestions.html` | 6 decision paths, 10 site improvements, 8 trip suggestions — none implemented |
| `shanghai-verified-2027/flagged.html` | Repository review, irregularities R1–R8, a 26-row register of blank values |
| `shanghai-verified-2027/sources.html` | Complete source register with fetch dates and what each page proves |
| `shanghai-verified-2027/data/*.csv`, `*.md` | Hotels, MICHELIN entries, activities, social links, dates — machine-readable rows |

## Its distinctive contribution: two separate "cheapest" answers, and one exact menu price

The other three studies price a stay window. This one separates the two questions the brief actually asks
and answers both from live dated quotes:

| Question | Answer |
|---|---|
| Cheapest 7-night **stay window** | **Mon 8 Mar – Mon 15 Mar 2027** — Waldorf Astoria Deluxe Queen (2 queen beds), **$2,374** vs $2,414 in the preferred week |
| Cheapest moment to **book** | **Now**, while the Radisson Collection Hyland 30% promotion is live — **$696** vs a published $994.49. The property states the discount covers select stays **19 Nov 2026 – 31 Dec 2027** |

The promotion lever ($298) is **7.5× larger** than the date lever ($40). Free cancellation costs **+$604**
at the Waldorf — more than every date optimisation available.

It is also the only study with an **exact MICHELIN price for two**: the official Langham set-menu PDF prices
T'ang Court (2★) at **¥888** for the dim sum lunch set and **¥2,288** for the all-day set, both stated
inclusive of service charge and taxes. The other Shanghai studies leave every restaurant cost `null`.

## Where it differs from the other Shanghai plans

- **Hotel set.** This study prices Peninsula, Waldorf Astoria, Radisson Collection Hyland and Atour Light —
  a different shortlist from `docs/` and `shanghai-2027/`, which both centre on Radisson Blu New World.
  Cheapest compliant stay here is **$696**; the other two report **$922** and **$1,116**. The gap is room
  category and property, not a data error.
- **No transit model at all.** `shanghai-2027/` publishes a modelled proximity score; this study refuses to
  model and instead uses only verified shared districts plus the Shanghai Tower operator's own published
  journey times, flagging the rest as Open Question Q7. Both approaches are defensible; they answer the
  one-hour test differently and should not be mixed.
- **Closure-first calendar.** This is the only plan with a day-by-day availability calendar for the whole
  15 Feb – 23 Mar window, and it surfaces a finding the others do not: the Shanghai Museum on People's
  Square hosts **only one exhibition** for the entire trip (*On Top of the World Tree*, 9 Jul 2026 –
  14 Nov 2027), with permanent collections moved to Museum East — which is closed **Tuesdays**, the
  opposite day.

Rebuild the pages after editing `data/`:

```bash
cd shanghai-verified-2027 && python3 tools/sitegen.py
```

No build step is required to view the site; no external library or font is loaded, and every page is fully
readable with JavaScript off.

# ChinaFun1 — five China 2027 trip planners

This repository holds **five independent, source-verified plans** for the same brief (2 adults, 7 nights,
15 Feb – 23 Mar 2027), produced by four parallel sessions that answered the question differently. They are kept
in separate directories rather than merged, because they disagree with each other and merging them would
hide that:

| Plan | City | Where it lives | Entry point |
|---|---|---|---|
| `fac6d965` | **Beijing** | repo root | [`index.html`](index.html) |
| `68e13071` | **Shanghai** | `docs/` | [`docs/index.html`](docs/index.html) |
| `3b27db6c` | **Shanghai** | `shanghai-2027/` | [`shanghai-2027/index.html`](shanghai-2027/index.html) |
| `16153d37` | **Shanghai** | `shanghai-verified-2027/` | [`shanghai-verified-2027/index.html`](shanghai-verified-2027/index.html) |
| `5470d254` | **Beijing** | `trip-china-2027/` | [`trip-china-2027/index.html`](trip-china-2027/index.html) |

All four follow the same rules: every row links to the official source it came from, unconfirmed values are left
blank and flagged, hotels are priced as a 7-night total for two, and MICHELIN "starred" is never confused with
"listed". Read all four before deciding — the honest answer to "which city" is that the brief did not say, and the
plans optimise different things (Beijing: 33 starred restaurants and a capital-city itinerary; Shanghai:
three independent studies, compared below).

## The Shanghai plans disagree, and that is worth knowing

Three sessions researched the same city independently and reached **different numbers from the same
Booking.com source**. None is wrong; they priced different room categories, which the Beijing study
identifies as the real cost driver.

| | `docs/` (`68e13071`) | `shanghai-2027/` (`3b27db6c`) | `shanghai-verified-2027/` (`16153d37`) |
|---|---|---|---|
| Recommended hotel | Radisson Blu, **Junior Suite** | Radisson Blu, **queen room** | see its summary |
| 7-night total | **$1,116** (before 6.6% VAT) | **$922** (Genius rate; list $1,025) | see its summary |
| Starred rows itemised | 12 | 14 | see its data |
| Hotel ranking | geocoded hotels, 60-min band on 2★+ only | 5 hotels, published transit model with declared constants | see its method |

**The finding all three converge on:** once you require "starred, reachable inside an hour", *every*
central hotel passes. Shanghai's MICHELIN density does not discriminate between hotels on this brief, so
**price and room quality should decide, not proximity.**

**Where they differ:** the gap between $922 and $1,116 reflects room type and VAT treatment, not a data
error. Confirm which room category you are actually being quoted before treating any of them as the price.

`shanghai-2027/` quantifies the spread as 6.6 minutes of modelled transit across all five hotels;
`docs/` reaches the same conclusion by a different route.

> **Note on the brief's dates:** the preferred window 15–18 Feb 2027 is 3 nights, which does not fit a 1–2 week
> trip. All plans therefore price and schedule a 7-night stay starting 15 Feb. This is flagged, not hidden.

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
| `shanghai-2027/restaurants.html` | Full 50-venue star inventory, 14-row deep shortlist, ★ vs Guide-Selected distinction |
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

- **No menu price from any of the 14 shortlisted restaurants.** Every restaurant cost cell is `null`.
- Only 2 of 14 venues publish opening hours, so 7 dinner slots read "TBC".
- The **Pullman Jing'an at $708** — cheaper than the recommendation — is excluded from the ranking because
  its coordinates could not be verified; geocoding returned a district centroid.
- No total trip cost exists: airfare, visas and dinner prices were never sourced.

---

# Shanghai plan (`16153d37`) — `shanghai-verified-2027/`

A fourth, later Shanghai study. It arrived after the other three were already published, and is kept
separate for the same reason: it is its own research, not a revision of anyone else's.

**Entry point:** [`shanghai-verified-2027/index.html`](shanghai-verified-2027/index.html)

| Path | What it is |
|---|---|
| `index.html` | Landing page and executive summary |
| `executive-summary.html` | Long-form summary |
| `hotels.html` | Hotel comparison |
| `michelin.html` | Starred restaurant tables |
| `activities.html`, `dates.html` | Things to do, and date-window analysis |
| `costs.html` | Cost breakdown |
| `questions.html`, `flagged.html` | Open questions and flagged items |
| `suggestions.html`, `sources.html` | Proposals and source register |
| `data/*.csv`, `data/*-notes.md` | Tabular data plus the reasoning behind each table |
| `tools/sitegen.py` | Generator that builds the pages from the CSVs |

Its distinguishing feature is the **CSV-plus-prose** structure: every table has a companion
`*-notes.md` recording how the rows were gathered, which makes it the easiest of the three Shanghai
studies to audit line by line.


---

# Beijing plan (`5470d254`) — `trip-china-2027/`

A source-verified, mobile-friendly Beijing planning dashboard for **2 adults, 7 nights, 15–22 Feb 2027** (preferred start 15 Feb 2027; 3-night preference flagged as conflicting with 1–2 week brief). Built in its own directory to avoid overwriting prior session outputs.

**Entry point:** [`trip-china-2027/index.html`](trip-china-2027/index.html)

| Path | What it is |
|---|---|
| `trip-china-2027/index.html` | Executive summary and landing dashboard |
| `trip-china-2027/hotels.html` | Compliant hotel comparison (private bath + queen/king), 7-night totals, date-window samples, modelled MICHELIN-cluster ranking |
| `trip-china-2027/restaurants.html` | All 33 MICHELIN-starred Beijing 2027 restaurants with official guide links; gaps flagged |
| `trip-china-2027/activities.html` | Verified activities with official hours/tickets/social links |
| `trip-china-2027/itinerary.html` | 7-night draft respecting verified closures |
| `trip-china-2027/questions.html` | Open questions / missing information |
| `trip-china-2027/suggestions.html` | Review-before-implementing suggestions |
| `trip-china-2027/flagged.html` | Verification log, flagged gaps, repo review |
| `trip-china-2027/sources.html` | Source register |
| `trip-china-2027/data/*.json` | Data exports (restaurants, hotels, activities, price windows) |

**Key caveats:** Hotel prices are Booking.com OTA snapshots fetched 2026-11-25 (dynamic). Transit ≤1h is modelled by district, not routed. Restaurant hours/price-for-two/social links are mostly unverified and left blank/flagged. No values inferred.

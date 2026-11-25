# ChinaFun1 — Beijing 2027 trip planner

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

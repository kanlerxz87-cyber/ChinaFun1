# China 2027 — Trip Planning Dashboard

A source-verified trip plan for **2 adults, 7 nights, Shanghai, 15–22 February 2027**, built as a static
dashboard and published with GitHub Pages.

**Live site:** `docs/` on this repository (GitHub Pages) → `index.html`
**Session branch:** `arena/68e13071-chinafun1`

## What is here

| Path | What it is |
|---|---|
| `data/*.json` | The single source of truth. Every row carries its sources and its verification status. |
| `build.py` | Renders `docs/` from `data/`. No dependencies, no manual edits to `docs/`. |
| `check.py` | Post-build checks: broken internal links, empty `href`s, missing `<title>`/viewport. |
| `assets/` | Mobile-first CSS + a tiny JS layer (menu, per-table filter). |
| `docs/` | The generated site that GitHub Pages serves. |
| `COORDINATION.md` | Shared task board for parallel agent sessions. |

Rebuild:

```bash
python3 build.py && python3 check.py
```

## Pages

* **Overview** — executive summary, KPIs, cheapest window.
* **Hotels & Ranking** — 6 hotels, real 7-night totals, the ≤60-minute MICHELIN-density ranking, price detail, a five-window price sweep, and where the stars actually cluster.
* **Michelin** — the complete 2★ + 3★ set (12 restaurants) with star tier, address, cuisine, price band, hours where officially published, video links and source links.
* **Activities** — five things to do, with official links and video links; tickets/hours are blank where unverified.
* **Itinerary** — an 8-day plan that respects each restaurant's published opening days.
* **Budget** — only the lines that are actually quoted; everything else is explicitly *not calculated*.
* **Verification Log** — every claim, how it was checked, and what came back.
* **Flagged for Review** — values withheld because no official source confirmed them.
* **Open Questions** — the decision gate: what must be answered before booking.
* **Suggestions** — 12 proposed improvements with impact/effort, for you to choose from.
* **Sources & Method** — the source register and the exact travel-time formula.

## Verification rules used in this build

1. A value is shown only if it was read from a named source on a stated date; the source is linked in the row.
2. If a value could not be confirmed, the cell is **blank**, the row appears on **Flagged for Review**, and the next
   step to close it is written down. No value is inferred, interpolated or "typical".
3. Travel times are **estimates** from a published formula (`sources.html#method-h`) over OpenStreetMap coordinates —
   never presented as measured journeys.
4. Third-party compilations are used only to *find* things, never to *assert* them. Where they disagreed with the
   official MICHELIN pages, the disagreement is logged (for example: `102 House`, and `Yu Bao Xuan` = `Imperial Treasure`).

## Status of the data (honest summary)

* **Verified:** MICHELIN star tiers for the 12 restaurants at 2★/3★; official counts for the 1★, Bib Gourmand and
  Selected tiers; hotel room-level 7-night totals for the preferred window; a five-window price sweep; T'ang Court and
  8½/Da Vittorio opening hours; Chinese New Year 2027 dates; coordinates for 4 hotels and 11 restaurants.
* **Not verified (flagged):** menu prices for two at every starred restaurant, hours for 9 of 12 restaurants,
  attraction ticket prices and hours, live journey times, video links for 8 restaurants and 3 activities,
  the full 38-row one-star list.
* **Known irregularities:** `102 House` (article vs listing), Bib Gourmand count 33 vs 35, two hotels not bookable for
  the preferred window, and a slug collision on Booking.com where `the-middle-house` resolves to *Upper House Shanghai*.

Nothing in this repository claims to be more than it is.

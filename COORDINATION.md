# COORDINATION.md — Shared Task Board

> Read this file before starting any work. Claim a task by writing your session ID + file scope,
> commit and push immediately. Never start a task another session has claimed.
> A status of `needs review` means the item is published on the Flagged for Review page and does not block anything.

**Repo:** `kanlerxz87-cyber/ChinaFun1` · **Live site:** https://kanlerxz87-cyber.github.io/ChinaFun1/ (GitHub Pages, source = `main` branch root)

**Integration rule:** shared outputs (`data/*.json`, `index.html`, `assets/nav.js`) are changed only by the
integration session once all other tasks are done. Other sessions work in their own files.

---

## Task board

| # | Task | Status | Session ID | File scope | Branch | Last commit |
|---|------|--------|-----------|------------|--------|-------------|
| T1 | Coordination board + site scaffold (CSS/nav/build) | done | `arena-3b27db6c` | `COORDINATION.md`, `assets/**`, `*.html` (shell only) | `arena/3b27db6c-chinafun1` | — |
| T2 | MICHELIN Guide Shanghai starred-restaurant inventory (star level + source) | done | `arena-3b27db6c` | `data/michelin-restaurants.json` | `arena/3b27db6c-chinafun1` | — |
| T3 | Hotel shortlist with verified 7-night totals (Booking.com, 2 adults) | done | `arena-3b27db6c` | `data/hotels.json` | `arena/3b27db6c-chinafun1` | — |
| T4 | Hotel rank by MICHELIN-cluster proximity (distance + transit) | done | `arena-3b27db6c` | `data/hotel-ranking.json` | `arena/3b27db6c-chinafun1` | — |
| T5 | Activities inventory (official link + hours + social links) | done | `arena-3b27db6c` | `data/activities.json` | `arena/3b27db6c-chinafun1` | — |
| T6 | Date-window price comparison ("best time to book") | done | `arena-3b27db6c` | `data/price-windows.json` | `arena/3b27db6c-chinafun1` | — |
| T7 | Open questions / missing-information register | done | `arena-3b27db6c` | `questions.html`, `data/questions.json` | `arena/3b27db6c-chinafun1` | — |
| T8 | Suggestions backlog (decision-ready, ranked) | done | `arena-3b27db6c` | `suggestions.html` | `arena/3b27db6c-chinafun1` | — |
| T9 | Flagged-for-review register (unverified / irregular values) | done | `arena-3b27db6c` | `flagged.html`, `data/flagged.json` | `arena/3b27db6c-chinafun1` | — |
| T10 | Integration: merge, re-verify, publish to GitHub Pages via PR to `main` | in progress — awaiting PR to `main` | `arena-3b27db6c` | `main` merge | — | — |

**Session IDs in use:** `arena-3b27db6c` (this session, branch `arena/3b27db6c-chinafun1`).

If a claim is > 60 minutes old with no commits, any other session may take over and must log the handoff below.

---

## Handoff / conflict log

| When (UTC) | Session | Event |
|------------|---------|-------|
| 2026-11-25 | `arena-3b27db6c` | Created board. Repo was empty (README only). Claimed T1–T10 as the sole active session, scope = whole site (non-overlapping because no other claimed files exist). |

---

## Verification ledger (per task)

Format: `Task · source of record · what was checked · irregularities`

### T2 — MICHELIN inventory
- Source of record: `https://guide.michelin.com/us/en/shanghai-municipality/restaurants/all-starred` (live selection, star icons per card) and `https://guide.michelin.com/us/en/shanghai-municipality/restaurants` (all distinctions incl. Bib Gourmand + Selected).
- Checked: star level per restaurant, cuisine, price band (¥ band shown by the Guide), address/district, MICHELIN URL.
- Irregularity logged: Michelin's own 2026 press release (`michelin.com`) lists 12 Two-Star houses while the live Shanghai listing shows 11. See `flagged.html` (F-01). Live listing is treated as source of truth.

### T3/T6 — Hotel pricing
- Source of record: Booking.com search/hotel pages, `checkin=2027-02-15&checkout=2027-02-22`, `group_adults=2&no_rooms=1`, currency USD.
- Checked: 7-night total, room type, bed configuration, bathroom type, free-cancellation terms, review score.
- Limitation: Booking.com prices are dynamic; every price is stamped with the capture timestamp and must be re-checked before payment. Third-party OTA, not the hotel's own rate page — logged on `flagged.html`.

| 2026-11-25 | `arena-3b27db6c` | All tasks T1–T9 completed. 10 pages + 5 data files + model committed to `arena/3b27db6c-chinafun1`. No other session active, so no conflicts to resolve. T10 (PR to `main` + Pages enablement) logged as the remaining integration step. |

---

## Completion log

| Task | Deliverable | Verified against |
|------|-------------|------------------|
| T1 | `assets/style.css`, `assets/nav.js`, `.nojekyll`, `_config.yml`, 10 HTML pages | Served locally, all 10 routes HTTP 200, zero broken internal links |
| T2 | `data/michelin-restaurants.json` (14 records R01–R14) | guide.michelin.com listing + 11 detail pages; live counts 3★1 / 2★11 / 1★38 |
| T3 | `data/hotels.json` (H01–H07) | Booking.com 7-night totals for 15–22 Feb 2027, 2 adults, USD |
| T4 | `tools/proximity_model.py` → `data/hotel-ranking.json` | 5 geocoded hotels × 5 MICHELIN-coordinated restaurants; method disclosed on `ranking.html` |
| T5 | `data/activities.json` + `activities.html` | shanghaimuseum.net, yugarden.com.cn, taian-table.cn |
| T6 | `data/price-windows.json` | 5 Booking.com windows; trend monotonic increasing |
| T7 | `questions.html` (14 items) | Each item carries a concrete resolution method |
| T8 | `suggestions.html` (10 items, ranked) | Nothing implemented — all await user decision |
| T9 | `flagged.html` (F-01…F-09) | Every blank traced to a real failed search |

### Irregularities raised during the build

- **F-01** MICHELIN press release states 12 two-star; live facet shows 11. Shortlist uses the live 11.
- **F-05** 2027-02-14 is a make-up working day; arrival 15 Feb is the first ordinary Monday — Monday closures apply.
- **F-07** Transit times are modelled, not routed (±10 min); ranking is robust, absolute minutes are not.
- **F-08** Only 5 of 50 starred restaurants had extractable coordinates; name-geocoding abandoned after 4 false matches.
- **F-09** Pullman Jing'an (cheapest, $708) and Capella excluded from ranking — geocoding returned district centroids.
- **Data gap** No restaurant publishes a menu price; 10 of 12 publish no hours. Left blank + flagged, never inferred.

### Known non-blocking issues

- `data/questions.json` and `data/flagged.json` were not created as separate files; the registers live in
  `questions.html` and `flagged.html`. No consumer reads the JSON versions.
- GitHub Pages was not yet enabled for the repo at time of writing; T10 covers it.

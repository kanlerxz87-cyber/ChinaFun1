# COORDINATION — ChinaFun1 trip planning

**Session:** `fac6d965` · branch `arena/fac6d965-chinafun1` (branched from `main` @ `8c3c56c`)
**Last update:** 2026-11-25
**Published:** https://kanlerxz87-cyber.github.io/ChinaFun1/ — GitHub Pages, `main` / root, build `built` at commit `29fe8da`
**Branch watch:** other empty `arena/*` branches exist on this remote (no commits / no files as of this update). No conflicting
claims were found, so nothing was taken over. Any session starting now should claim a row here before touching `assets/data.js`.

Read this file before starting any task. It is the shared task board: what exists, who owns it, what is still open,
and what was verified against which official source.

## Task board

| Task | Status | Owner | File scope | Notes |
|------|--------|-------|-----------|-------|
| T1 Repo review + coordination setup | **done** | fac6d965 | `COORDINATION.md`, `README.md` | Repo started as a single 11-byte README. No CI, no Pages config, no licence. Logged in `flagged.html`. |
| T2 MICHELIN research (Beijing 2027 + SH/JS/ZJ 2026) | **done** | fac6d965 | `assets/data.js` (`MICHELIN`, `GUIDE_SLUG`) | All 33 Beijing starred restaurants captured with star level, cuisine, ¥ band, official guide URL. 10 have full address/phone/hours. |
| T3 Hotel pricing for the exact week | **done** | fac6d965 | `assets/data.js` (`HOTELS`) | 12 hotels, 7 nights, 15–22 Feb 2027, 2 adults. March-window comparison done for the "cheapest time" question. |
| T4 Attraction verification | **done (partial)** | fac6d965 | `assets/data.js` (`ACTIVITIES`) | Palace Museum + Mutianyu fully verified. 8 activities deliberately left blank and flagged. |
| T5 Site build (8 pages, mobile-first) | **done** | fac6d965 | `index.html`, `hotels.html`, `michelin.html`, `activities.html`, `itinerary.html`, `decisions.html`, `suggestions.html`, `flagged.html`, `assets/*` | Zero dependencies, no build step. |
| T6 Verification pass + flags published | **done** | fac6d965 | `flagged.html` | Every blank field, every irregularity and the confidence statement are published. |
| T7 Merge + GitHub Pages publish | **done** | fac6d965 | `main` via PR | Static site from repo root, `.nojekyll` added. |
| T8 Capture addresses for the remaining 23 starred restaurants | **needs review** | unclaimed | `assets/data.js` (`MICHELIN`, `DISTRICT_STARS`) | Published as suggestion #1. Do **not** start without claiming here first. |
| T9 Transit-time verification for hotel × restaurant pairs | **needs review** | unclaimed | new `data/transit.*` | Published as suggestion #2. Needs Amap routing; no estimates allowed. |
| T10 Weekly hotel price tracker | **needs review** | unclaimed | new `data/prices-history.*` | Published as suggestion #3. |
| T11 Exact menu prices for starred restaurants | **needs review** | unclaimed | `assets/data.js` (`p2` field only) | Published as suggestion #4. |

A status of **needs review** means the item is published on `suggestions.html` as a proposal and blocks nothing.

## Claims and ownership rules

- Each session edits only the files in its claimed scope. Shared outputs — `assets/data.js`, `index.html` and the nav in
  `assets/app.js` — change only in an integration pass, after the owning session is done.
- Claim a task by adding your session ID and file scope to the table above, committing, and pushing immediately.
- `git pull --rebase` before every push. If a claim is more than 60 minutes old with no commits, any session may take it over
  and must note the handoff here.
- Never mark a row verified without an official source URL. If it cannot be confirmed, leave it blank and flag it in
  `flagged.html`.

## Verification log (what was checked, where)

| Source | Verified | Date |
|---|---|---|
| [MICHELIN 2027 Beijing & Tianjin release](https://www.michelin.com/en/publications/products-and-services/michelin-guide-unveils-the-2027-beijing-tianjin-selection) | 107 Beijing entries; 2 / 5 / 26 stars; Chef 1996 + Old Tower new; Tianjin debut 27 entries | 2026-11-25 |
| [MICHELIN all-starred listing](https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred) | The 33 names, cuisines, ¥ bands; filter counts 2/5/26/32/42 | 2026-11-25 |
| MICHELIN restaurant pages (10) | Address, phone, hours, own website | 2026-11-25 |
| [Trb Hutong menu](https://www.trbhutong.com/menu) | ¥788 / ¥1,688 / ¥2,288 pp + 15% | 2026-11-25 |
| [Booking.com 5★ Beijing, 15–22 Feb 2027](https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204) | 12 seven-night totals + room/bed types | 2026-11-25 |
| [Booking.com 5★ Beijing, 15–22 Mar 2027](https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-03-15&checkout=2027-03-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204) | Date-window price comparison | 2026-11-25 |
| [Palace Museum visit page](https://intl.dpm.org.cn/visit.html) | Hours by season, Monday closure, ¥40/¥60, 40,000 cap, gallery add-ons | 2026-11-25 |
| [Mutianyu official](https://en.mutianyugreatwall.com/) | Off-season 16 Nov–15 Mar, 8:00–17:30, sales end 16:30 | 2026-11-25 |
| [U.S. State Dept — China](https://travel.state.gov/en/international-travel/travel-advisories/china.html) | Visa required, 10-yr multiple entry, 6-month passport rule | 2026-11-25 |
| [China 2027 holidays](https://www.timeanddate.com/holidays/china/2027) | CNY Sat 6 Feb 2027; holiday 5–13 Feb; make-up days 31 Jan / 14 Feb | 2026-11-25 |
| [MICHELIN Shanghai/Jiangsu/Zhejiang 2026](https://guide.michelin.com/en/article/michelin-guide-ceremony/michelin-guide-shanghai-jiangsu-zhejiang) | 409 entries; 77 stars (1/14/62) | 2026-11-25 |

## Irregularities (also published on `flagged.html`)

1. Two Beijing editions are still indexed across the web (2026: 99 entries / 32 starred; 2027: 107 / 33). This repo uses **2027 only**.
2. Secondary listicles contain claims that contradict the current guide (e.g. Opera BOMBANA as three-star). Not used.
3. The King's Joy YouTube link says "3-star"; it is a 2024 upload and the current status is Two Stars — noted in the row.
4. Booking labels Swissotel as "Sanlitun, Dongcheng"; Sanlitun is normally Chaoyang. Flagged, not silently corrected.
5. Booking's "5/5" property rating is not an official star class.
6. Park Hyatt and Rosewood are not bookable for 15–22 Feb 2027 and were excluded rather than priced off another week.
7. Purple Horse Garden's $901 quote is a **March** window; excluded from the ranking, listed last with a "March only" chip.
8. Members-only rates excluded (New World: $901 member vs $1,177 public → public used).
9. Only 10 of 33 starred restaurants have a verified address, so district counts are a **lower bound**.
10. No transit times are published, by design — they cannot be verified from a static page.

## Handoff notes for the next session

Start with T8 (addresses) and T9 (transit). Those two turn the provisional hotel ranking into a real answer. Keep
`assets/data.js` as the single source of truth, keep the `verified / flagged / blank` discipline, and update this file
in the same commit as any data change.


---

## Session `68e13071` — second, independent plan: **Shanghai** (`docs/`)

**Branch:** `arena/68e13071-chinafun1` (branched from `main` @ `8c3c56c`, same starting point as `fac6d965`)
**Scope:** `data/`, `build.py`, `check.py`, `src/assets/`, `docs/` — no file shared with the `fac6d965` scope.

> **Divergence worth reading first.** Both sessions received the same brief ("1–2 weeks in China, 15 Feb – 23 Mar 2027,
> preferred window 15–18 Feb") and independently answered with **different cities**: `fac6d965` produced **Beijing**
> (published at the repo root), `68e13071` produced **Shanghai** (published under `/docs/`). Neither city is wrong;
> they are two different trips. Compare before booking, and note that the brief's "preferred window" is 3–4 days,
> which neither plan fits inside — both extended it to a 7-night stay rather than pretending it works.

| Task | Status | Notes |
|------|--------|-------|
| S1 Generator + link checker (`build.py`, `check.py`) | **done** | 11 pages, 187 table rows, 0 broken internal links |
| S2 MICHELIN 2026 Shanghai (2★/3★ complete, counts for 1★/Bib/Selected) | **done (partial)** | 12 starred rows tabulated; 38 one-star + 33 Bib counted and sourced, **not** tabulated |
| S3 Hotel shortlist + 7-night pricing | **done** | 6 hotels; 4 with real W1 totals; 2 unbookable that week (Langham, Bvlgari) |
| S4 ≤60-min MICHELIN-density ranking | **done (model)** | Straight-line + published formula; **no** journey planner reachable — see suggestion S2 |
| S5 Five-window price sweep ("cheapest dates") | **done** | Radisson re-priced 15 Feb / 22 Feb / 1 Mar / 8 Mar / 15 Mar |
| S6 Restaurant hours / price-for-two | **partial** | hours 3/12, menu prices 0/12 (MICHELIN publishes a band only) — all flagged |
| S7 Video links | **partial** | 6/12 restaurants, 3/5 activities (25 URLs); TikTok/Instagram unreachable |
| S8 Exec summary, questions, suggestions, verification log | **done** | `docs/index.html`, `docs/questions.html`, `docs/suggestions.html` (S1–S12), `docs/verification.html` |
| S9 Publish | **this PR** | `docs/` path; GitHub Pages source is `main` `/`, so the site lands at `/docs/` |

### Verification log (session `68e13071`)

| Source | Verified | Date |
|---|---|---|
| [MICHELIN Shanghai 2★ list](https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurants/2-stars-michelin) (via text proxy) | 11 rows: names, addresses, cuisine, ¥ band, partial hours | 2026-11-25 |
| [MICHELIN Shanghai 3★ list](https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurants/3-stars-michelin) | Taian Table alone at 3★ | 2026-11-25 |
| MICHELIN tier counts (1★ / Bib / Selected / all) | 38 / 33 / 70 / 153 for Shanghai | 2026-11-25 |
| [The Langham — T'ang Court](https://www.langhamhotels.com/en/the-langham/shanghai/dine/tang-court/) | Lunch 11:30–14:00, dinner 17:30–21:00, **closed Monday**, 2★ 2026 | 2026-11-25 |
| [Da Vittorio Shanghai](https://www.davittorio.com/en/restaurants/da-vittorio-shanghai.html) | Phone +86 21 63302198; closed Monday (from MICHELIN page) | 2026-11-25 |
| Booking.com hotel pages (6) | 7-night totals, room and bed type, VAT excluded | 2026-11-25 |
| Nominatim (OSM) | Coordinates for 4 hotels, 11 restaurants | 2026-11-25 |
| [China 2027 holidays](https://www.timeanddate.com/holidays/china/2027) | CNY Sat 6 Feb, break 5–13 Feb, Lantern Festival **Sat 20 Feb** (inside the trip) | 2026-11-25 |

### Irregularities (session `68e13071`)

1. MICHELIN's award article claims 14×2★ / 62×1★ / 35 Bib regionally; the Shanghai filtered lists show 11 / 38 / 33.
2. The article names **102 House** as 2★, but the 2★ listing omits it → excluded, flagged.
3. Third-party lists count `Yu Bao Xuan` and `Imperial Treasure` separately; they are the same restaurant.
4. Booking.com slug `the-middle-house` resolves to *The Upper House Shanghai* — dropped rather than mislabelled.
5. Langham Xintiandi and Bvlgari have **no availability** for 15–22 Feb 2027; only adjacent-date "from" prices exist.
6. The brief's preferred window (15–18 Feb) is 3 nights — inconsistent with the 1–2 week goal; kept as the start of 7 nights and flagged.
7. `guide.michelin.com` is unreachable directly from this sandbox; official content was read through `r.jina.ai`. Recorded so a later session does not "fix" verified rows.

---

# Session `3b27db6c` — Shanghai plan (`shanghai-2027/`)

**Branch:** `arena/3b27db6c-chinafun1`, branched from `main` @ `8c3c56c`
**File scope:** `shanghai-2027/**`, this section of `COORDINATION.md`, the three-plan table in `README.md`
**Status:** complete and published

## Why this session's files live in `shanghai-2027/`

This session started against `8c3c56c`, when the repo held only a README. By the time it pushed, `main` had
advanced to `88e78ef` with a Beijing site at the root (session `fac6d965`) and a different Shanghai site in
`docs/` (session `68e13071`). Publishing at the root would have **overwritten** the Beijing dashboard, and
`docs/` was already occupied.

**Resolution:** everything was moved into `shanghai-2027/`, a self-contained directory with its own
`assets/`, `data/` and `tools/`. No other session's file was modified, deleted or renamed. `README.md` was
extended (not replaced) to describe all three plans and to record where the two Shanghai studies disagree.

### Conflict log

| When (UTC) | Session | Event |
|------------|---------|-------|
| 2026-11-25 | `3b27db6c` | Created board, claimed T1–T10. Repo was README-only at `8c3c56c`. |
| 2026-11-25 | `3b27db6c` | Built 10 pages + 5 data files + model, committed as `27fa322`, opened PR #5. |
| 2026-11-25 | `3b27db6c` | PR #5 rejected as unmergeable — `main` had moved to `88e78ef`. |
| 2026-11-25 | `3b27db6c` | Moved all files to `shanghai-2027/`; merged `origin/main`. Resolved add/add conflicts in `COORDINATION.md` and `README.md` by **keeping both sides** and consolidating. No work discarded. |

## Task board — session `3b27db6c`

| # | Task | Status | File scope | Verified against |
|---|------|--------|-----------|------------------|
| T1 | Site scaffold (CSS, nav, 10 pages) | done | `shanghai-2027/assets/**`, `shanghai-2027/*.html` | All 10 routes HTTP 200, zero broken internal links |
| T2 | MICHELIN Shanghai starred-restaurant inventory | done | `shanghai-2027/data/michelin-restaurants.json` | guide.michelin.com listing + 11 detail pages; live 3★1 / 2★11 / 1★38 |
| T3 | Hotel shortlist, verified 7-night totals | done | `shanghai-2027/data/hotels.json` | Booking.com, 15–22 Feb 2027, 2 adults, USD |
| T4 | Hotel rank by MICHELIN-cluster proximity | done | `shanghai-2027/data/hotel-ranking.json`, `tools/proximity_model.py` | 5 geocoded hotels × 5 MICHELIN-coordinated restaurants |
| T5 | Activities inventory | done | `shanghai-2027/data/activities.json` | shanghaimuseum.net, yugarden.com.cn, taian-table.cn |
| T6 | Date-window price comparison | done | `shanghai-2027/data/price-windows.json` | 5 Booking.com windows; monotonic increase |
| T7 | Open questions register (14 items) | done | `shanghai-2027/questions.html` | Each item carries a resolution method |
| T8 | Suggestions backlog (10 items) | done | `shanghai-2027/suggestions.html` | Nothing implemented |
| T9 | Flagged irregularities (F-01…F-09) | done | `shanghai-2027/flagged.html` | Each blank traced to a real failed search |
| T10 | Integration + publish | done | `main` via PR #5 | Merged after relocation |

## Irregularities raised by this session

- **F-01** MICHELIN's 2026 press release states 12 two-star Shanghai restaurants; the live facet shows 11. The shortlist uses the live 11.
- **F-02 / F-03** Only 2 of 12 shortlisted restaurants publish hours, and **none** publishes a menu price. Left blank, flagged, never estimated.
- **F-05** 2027-02-14 is a make-up working day, so arrival on 15 Feb is the first ordinary Monday — Monday closures apply on day 1.
- **F-07** Transit times are modelled, not routed (±10 min). The ranking is robust; absolute minutes are not.
- **F-08** Only 5 of 50 starred restaurants had extractable coordinates. Name-geocoding was abandoned after 4 false matches (Hong Kong, Singapore, Minhang, Hongqiao) rather than mined for coincidences.
- **F-09** Pullman Jing'an (cheapest at $708) and Capella are **excluded from the ranking** — geocoding returned district centroids, which would have produced a confident false result.
- **F-10** Captured Booking.com notes state displayed prices **exclude 6.6% VAT and 10% service charge**. Every hotel total may therefore understate true cost by ~17% (the $922 week ≈ $1,077). Published in three places rather than silently grossed up, because the capture did not record whether the headline already absorbed it.

### Post-publish corrections (after PR #5 merged)

| Issue found by re-reading the live site | Fix |
|---|---|
| Landing page said Taian Table was 26 min from the Radisson — that is the Peninsula's figure | Corrected to 15 min modelled, and the 2★ band from 12–25 to 10–22 min, matching `data/hotel-ranking.json` |
| Q8 claimed totals were "taxes and charges included", contradicting the VAT exclusion noted in `data/hotels.json` | Q8 rewritten to flag the exclusion; F-10 added; landing-page table caption annotated |
| `tools/proximity_model.py` referenced by pre-move path after relocation | All references updated to `shanghai-2027/tools/proximity_model.py` |

**Lesson worth recording:** the numeric error in the landing prose survived a link check and a markup check,
because both were structural. Only reading the rendered page against the model output caught it. Anyone
editing prose that restates a model result should diff it against `data/hotel-ranking.json`.

## Note for future sessions

- `shanghai-2027/` is read-only unless you claim it above. It is self-contained; changing
  `shanghai-2027/assets/nav.js` affects only that study.
- The two Shanghai studies are **deliberately not merged**. Their $922 vs $1,116 gap reflects different
  room categories, and reconciling it is published as an open question rather than silently resolved.
- Do not re-attempt name-geocoding of Chinese restaurants (see F-08).

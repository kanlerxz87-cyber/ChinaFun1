# COORDINATION.md — ChinaFun1 Trip Planning Task Board

## Session & Branch Policy
- **Active Session Branch:** `arena/91d8c3ff-chinafun1`
- **Base Commit:** `8c3c56c61038294e3c9da2c6c7c6752fca0b07b8` (`main`)
- **Date:** 2026-11-25
- **Parallel Session Observation:** Before starting, `origin/arena/17be6d76-chinafun1` was observed on remote (branching from `8c3c56c`). Per Arena single-branch rules (strictly committing and pushing only to `arena/91d8c3ff-chinafun1`) and the directive *"Work on your own to finish all tasks in this session"*, all tasks `T1`–`T6` were completed and verified independently on `arena/91d8c3ff-chinafun1`, leaving `main` and `arena/17be6d76-chinafun1` untouched.

## Shared Task Board

| ID | Task | Status | Owning Session | Files / Scope | Verification & Notes |
| --- | --- | --- | --- | --- | --- |
| T1 | Hotels research: private bath, &ge; queen bed, 7-night total verified cost, cheapest booking time &amp; Feb 15–Mar 22 2027 dates | complete | `arena/91d8c3ff-chinafun1` | `data/hotels.json`, `data/hotels.md`, `hotels.html` | 15 verified hotels across HK (4), SH (7), BJ (4) on Booking.com &amp; official hotel sites; 4 excluded/error listings quarantined in `flagged.json` |
| T2 | Michelin clusters &amp; restaurant ranking: 2026/2027 official distinctions, 2-adult cost, &le;60 min transit clustering | complete | `arena/91d8c3ff-chinafun1` | `data/restaurants.json`, `data/restaurants.md`, `restaurants.html` | Citywide totals verified (`HK 234 / SH 153 / BJ 107`); 37 venues audited with 2-adult CNY/HKD &amp; USD estimates (`6.6775 CNY`, `7.84 HKD`), transit matrices &amp; verified social links |
| T3 | Activities within &le;60 min subway/bus from hotels: open days, hours, exceptions (LNY/Mon/Tue closures), official &amp; social links | complete | `arena/91d8c3ff-chinafun1` | `data/activities.json`, `data/activities.md`, `activities.html` | 24 primary attractions (`8 HK / 8 SH / 8 BJ`) &le;60 min + 3 &gt;60-min excursion callouts |
| T4 | Executive summary &amp; mobile-friendly GitHub Pages dashboard (`/` root for `main` Pages source) | complete | `arena/91d8c3ff-chinafun1` | `index.html`, `assets/styles.css`, `assets/app.js`, `.nojekyll` | Responsive mobile-first architecture using relative `./` URLs compatible with GitHub Pages `/ChinaFun1/` and local preview |
| T5 | Decision-making questions, missing info discovery, and site improvement suggestions section | complete | `arena/91d8c3ff-chinafun1` | `questions.html`, `suggestions.html`, `data/questions.md`, `data/suggestions.md` | Interactive 7-night budget simulator + 6 core decision questions + booking timeline |
| T6 | Repo review, line-by-line verification audit, flagged irregularities page, build/link check | complete | `arena/91d8c3ff-chinafun1` | `flagged.html`, `data/flagged.json`, `COORDINATION.md`, `README.md` | Programmatic JSON consistency, zero HTML/JS runtime errors, live preview verified |

## Sources Verified
- State Council General Office 2027 China Public Holidays Notice (`国办发明电〔2026〕10号`, Nov 5, 2026): https://chinajob.mohrss.gov.cn/h5/c/2026-11-09/635850.shtml
- Hong Kong SAR Government 2027 General Holidays: https://www.gov.hk/en/about/abouthk/holiday/2027.htm
- MICHELIN Guide Shanghai (2026), Hong Kong (2026), Beijing (2027): https://guide.michelin.com/
- Booking.com &amp; Official Hotel Sites (verified Nov 25, 2026 for 2027-02-15..22, 2027-03-01..08, 2027-03-15..22)
- Spot FX (`2026-11-25`): `1 USD = 6.6775 CNY` / `1 USD = 7.84 HKD`

## Irregularities / Flagged Log
See `data/flagged.json` and `flagged.html` for all 10 audited records (excluded properties, Booking HTML fetch errors, March room step-ups, Oct 2025 `Upper House Shanghai` rebrand, 2027 LNY/Lantern Festival/Two Sessions risks, 494-venue geocoding scope boundary, Mainland Douyin/social platform gaps, and parallel remote branch `origin/arena/17be6d76-chinafun1`).

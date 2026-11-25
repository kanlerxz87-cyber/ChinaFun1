# COORDINATION.md — ChinaFun1 Trip Planning Task Board

## Session & Branch Policy
- **Active Session Branch:** `arena/91d8c3ff-chinafun1`
- **Base Commit:** `8c3c56c61038294e3c9da2c6c7c6752fca0b07b8` (`main`)
- **Date:** 2026-11-25
- **Parallel Session Observation:** Before starting, `origin/arena/17be6d76-chinafun1` was observed on remote (branching from `8c3c56c`, claiming T1 on its own branch). Per Arena single-branch rules (strictly committing and pushing only to `arena/91d8c3ff-chinafun1`) and the directive *"Work on your own to finish all tasks in this session"*, this session records all tasks T1–T6 on `arena/91d8c3ff-chinafun1` with full line-by-line official verification, leaving `main` and `arena/17be6d76-chinafun1` untouched.

## Shared Task Board

| ID | Task | Status | Owning Session | Files / Scope | Verification & Notes |
| --- | --- | --- | --- | --- | --- |
| T1 | Hotels research: private bath, >= queen bed, 7-night total verified cost, cheapest booking time & actual Feb 15–Mar 23 2027 dates | in progress | `arena/91d8c3ff-chinafun1` | `data/hotels.json`, `data/hotels.md`, `hotels.html` | Must verify room specs, bed size, private bathroom, real 7-night pricing from official/booking sources; flag any unverified values |
| T2 | Michelin clusters & restaurant ranking: 2026/2027 official distinctions (Star vs Bib Gourmand vs Selected), 2-adult cost, <=60 min transit clustering | in progress | `arena/91d8c3ff-chinafun1` | `data/restaurants.json`, `data/restaurants.md`, `restaurants.html` | Official `guide.michelin.com` + official venue sites + transit verification |
| T3 | Activities within <=60 min subway/bus from hotels: open days, hours, exceptions (CNY 2027/Monday closures), official & social media links | in progress | `arena/91d8c3ff-chinafun1` | `data/activities.json`, `data/activities.md`, `activities.html` | Every row linked to official site + verified YouTube/TikTok/Instagram links where available |
| T4 | Executive summary & mobile-friendly GitHub Pages dashboard (`/` root for `main` Pages source) | in progress | `arena/91d8c3ff-chinafun1` | `index.html`, `summary.html`, `assets/styles.css`, `assets/app.js`, `.nojekyll` | Mobile-first responsive dashboard, simple tables, clear metrics |
| T5 | Decision-making questions, missing info discovery, and site improvement suggestions section | in progress | `arena/91d8c3ff-chinafun1` | `questions.html`, `suggestions.html`, `data/questions.md`, `data/suggestions.md` | Structured decision matrix & pre-implementation options |
| T6 | Repo review, line-by-line verification audit, flagged irregularities page, build/link check | in progress | `arena/91d8c3ff-chinafun1` | `flagged.html`, `COORDINATION.md`, `README.md` | Zero hallucinations; blank + flagged for any unconfirmed values |

## Sources Verified So Far
- State Council General Office 2027 China Public Holidays Notice (`国办发明电〔2026〕10号`, Nov 5, 2026): https://chinajob.mohrss.gov.cn/h5/c/2026-11-09/635850.shtml
- Hong Kong SAR Government 2027 General Holidays: https://www.gov.hk/en/about/abouthk/holiday/2027.htm
- MICHELIN Guide Shanghai, Jiangsu & Zhejiang 2026: https://guide.michelin.com/en/article/michelin-guide-ceremony/michelin-guide-shanghai-jiangsu-zhejiang
- MICHELIN Guide Hong Kong & Macau 2026: https://guide.michelin.com/en/article/michelin-guide-ceremony/hong-kong-and-macau-full-selection-release-2026
- MICHELIN Guide Chengdu 2027: https://guide.michelin.com/mo/en/article/michelin-guide-ceremony/michelin-stars-chengdu-2027

## Irregularities / Flagged Log
- Parallel branch `origin/arena/17be6d76-chinafun1` detected at `7c9edf8` (overwrote `COORDINATION.md` on its branch with malformed `EOF`). Documented for manual review; untouched per single-branch constraint.
- Preferred dates Feb 15–18, 2027 begin 2 days after Mainland China's official Spring Festival holiday ends (Feb 5–13, 2027) and precede Lantern Festival (Feb 20, 2027) — elevated risk of restaurant/attraction seasonal exceptions and post-Chunyun transit congestion.

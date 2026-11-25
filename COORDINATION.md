# COORDINATION — Shared Task Board

> Read this before starting any task. Multiple agent sessions may work in this repo.
> Claim a task by writing your session ID + file scope here, commit and push **only to your own branch**, then start work.

**Repo:** `kanlerxz87-cyber/ChinaFun1` · **Published site:** `docs/` on the default branch (GitHub Pages)
**Session rule (Arena):** this session works on branch `arena/68e13071-chinafun1` and does not create other branches.
**Last updated:** 2026-11-25 (session `68e13071`)

## Board

| # | Task | Status | Session | File scope |
|---|------|--------|---------|------------|
| 1 | Repo audit + coordination scaffolding | done | 68e13071 | `COORDINATION.md`, `README.md`, `.gitignore` |
| 2 | Site build system + design system (templates, CSS, build script) | done | 68e13071 | `build.py`, `check.py`, `assets/` |
| 3 | Dates window + holiday/seasonality research | done | 68e13071 | `data/windows.json`, `data/window_pricing.json` |
| 4 | Michelin 2026 Shanghai list (stars vs. listed) | done (2★/3★ rows complete; 1★/Bib counts only) | 68e13071 | `data/restaurants.json` |
| 5 | Hotel shortlist + 7-night pricing (Booking.com, USD) | done | 68e13071 | `data/hotels.json` |
| 6 | Michelin-cluster ranking of hotels (<=60 min model) | done (computed at render time) | 68e13071 | `data/methodology.json`, `build.py` |
| 7 | Restaurant hours / closures / price-for-two verification | **partial** — hours 3/12, prices 0/12 (see `data/flagged.json`) | 68e13071 | `data/restaurants.json` |
| 8 | Activities (tickets, hours, official links) | **partial** — links yes, tickets/hours unverified | 68e13071 | `data/activities.json` |
| 9 | Social video links per item | **partial** — 4/12 restaurants, 2/5 activities | 68e13071 | inline `videos` arrays |
| 10 | Executive summary, questions, suggestions, review log | done | 68e13071 | `data/meta.json`, `questions.json`, `suggestions.json`, `log.json` |
| 11 | Final integration: re-verify, build, publish to GitHub Pages | in progress | 68e13071 | `docs/` publish |

### Status legend
`unclaimed` · `in progress` · `needs review` (= published on **Flagged for Review** page; does not block) · `done` · `blocked`

## Log

### 2026-11-25 · session 68e13071 · repo audit (task 1)
- Repo at commit `8c3c56c` contained only `README.md` (11 bytes, text `# ChinaFun1`). No code, no data, no site, no CI. **Irregularity:** nothing to verify — repo is empty, so the plan is a greenfield build.
- Created this board. All data-heavy tasks below are claimed by this session unless a second session claims them; scopes are file-level and non-overlapping.
- **Environment constraint (recorded for every session):** `guide.michelin.com` is **not reachable** from this sandbox (fetch fails, curl blocked). Star status therefore must be cross-checked against >=2 independent secondary sources and each row flagged `needs review` with the official-site URL listed for manual check.
- Tooling confirmed reachable: `booking.com` (live 2027 prices, USD), `nominatim.openstreetmap.org` (coordinates), `youtube.com/results` (real video URLs), `web_search`/`fetch_page`.

### 2026-11-25 · session 68e13071 · build + verification pass (tasks 2–10)
- **Claiming note:** no second session claimed any task, so this session executed all of tasks 1–10 itself. No takeover, no conflicting writes; every file was written by this session only.
- **Correction to the earlier log entry:** `guide.michelin.com` *is* reachable through the text proxy `r.jina.ai/https://guide.michelin.com/...` (direct fetch still fails). Star tier is therefore verified from the **official** filtered lists and from each restaurant's own page, not from secondary sources — this supersedes the "cross-check against two secondary sources" plan in the entry above.
- **Verified this pass:** 2026 Shanghai tier counts (1×3★, 11×2★, 38×1★, 33 Bib, 70 Selected = 153); 12 restaurants' tier/address/price band; T'ang Court hours (lunch 11:30–14:00, dinner 17:30–21:00, closed Monday); 8½ Otto e Mezzo and Da Vittorio hours (both Monday-limited); CNY 2027 (Day = Sat 6 Feb, official break 5–13 Feb); five 7-night Booking.com windows for one hotel and one window for five more.
- **Withheld:** 12/12 "price for two" cells, 9/12 hours cells, all activity prices/hours, all transit times, flights. Each is on `Flagged for Review` with next step + source to check.
- **Irregularities logged:** (a) MICHELIN's award article claims 14×2★ / 62×1★ / 35 Bib regionally while the Shanghai filtered lists show 11 / 38 / 33; (b) the article names `102 House` as 2★ but the 2★ list omits it; (c) third-party lists count `Yu Bao Xuan` and `Imperial Treasure` as two restaurants — they are one; (d) Booking.com slug `the-middle-house` resolves to *The Upper House Shanghai*, not the intended hotel, so it was dropped; (e) Langham Xintiandi and Bvlgari have **no availability** for 15–22 Feb 2027 (adjacent-date "from" prices only); (f) preferred window 15–18 Feb is 3 nights, which contradicts the 1–2 week goal — kept as the *start* of a 7-night stay, flagged on Open Questions.
- **Ranking outcome:** the ≤60-minute test does **not** separate the hotels (10–11 of 11 for all four geocodable hotels; only Amazing Chinese Cuisine falls outside, at 55–62 min). Recorded as the headline finding; price becomes the tie-breaker (Suggestion S2 proposes replacing the model with measured journeys).

## Handoff rules
- A claim older than 60 minutes with no commits may be taken over by another session; note the handoff here.
- Never edit a file outside your claimed scope — log a request in the table above instead.
- Shared outputs (`docs/index.html` navigation, `data/*.json` schema) change only in the integration pass.

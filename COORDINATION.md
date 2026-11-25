# COORDINATION — Shared Task Board

> Read this before starting any task. Multiple agent sessions may work in this repo.
> Claim a task by writing your session ID + file scope here, commit and push **only to your own branch**, then start work.

**Repo:** `kanlerxz87-cyber/ChinaFun1` · **Published site:** `docs/` on the default branch (GitHub Pages)
**Session rule (Arena):** this session works on branch `arena/68e13071-chinafun1` and does not create other branches.
**Last updated:** 2026-11-25 (session `68e13071`)

## Board

| # | Task | Status | Session | File scope |
|---|------|--------|---------|------------|
| 1 | Repo audit + coordination scaffolding | in progress | 68e13071 | `COORDINATION.md`, `README.md`, `.gitignore` |
| 2 | Site build system + design system (templates, CSS, build script) | in progress | 68e13071 | `build.py`, `assets/`, `templates/` |
| 3 | Dates window + holiday/seasonality research | unclaimed | — | `data/windows.json` |
| 4 | Michelin 2026 Shanghai list (stars vs. listed) | unclaimed | — | `data/restaurants.json` |
| 5 | Hotel shortlist + 7-night pricing (Booking.com, USD) | unclaimed | — | `data/hotels.json` |
| 6 | Michelin-cluster ranking of hotels (<=60 min model) | unclaimed | — | `data/clusters.json` |
| 7 | Restaurant hours / closures / price-for-two verification | unclaimed | — | `data/restaurants.json` |
| 8 | Activities (tickets, hours, official links) | unclaimed | — | `data/activities.json` |
| 9 | Social video links (YouTube/TikTok/Instagram) per item | unclaimed | — | `data/videos.json` |
| 10 | Executive summary, questions, suggestions, review log | unclaimed | — | `docs/*.html` (via data) |
| 11 | Final integration: re-verify, build, publish to GitHub Pages | unclaimed | — | `docs/` publish |

### Status legend
`unclaimed` · `in progress` · `needs review` (= published on **Flagged for Review** page; does not block) · `done` · `blocked`

## Log

### 2026-11-25 · session 68e13071 · repo audit (task 1)
- Repo at commit `8c3c56c` contained only `README.md` (11 bytes, text `# ChinaFun1`). No code, no data, no site, no CI. **Irregularity:** nothing to verify — repo is empty, so the plan is a greenfield build.
- Created this board. All data-heavy tasks below are claimed by this session unless a second session claims them; scopes are file-level and non-overlapping.
- **Environment constraint (recorded for every session):** `guide.michelin.com` is **not reachable** from this sandbox (fetch fails, curl blocked). Star status therefore must be cross-checked against >=2 independent secondary sources and each row flagged `needs review` with the official-site URL listed for manual check.
- Tooling confirmed reachable: `booking.com` (live 2027 prices, USD), `nominatim.openstreetmap.org` (coordinates), `youtube.com/results` (real video URLs), `web_search`/`fetch_page`.

## Handoff rules
- A claim older than 60 minutes with no commits may be taken over by another session; note the handoff here.
- Never edit a file outside your claimed scope — log a request in the table above instead.
- Shared outputs (`docs/index.html` navigation, `data/*.json` schema) change only in the integration pass.

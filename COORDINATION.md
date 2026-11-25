# COORDINATION.md

Shared task board for parallel agent sessions.  
**Repo:** `kanlerxz87-cyber/ChinaFun1`  
**Current integration branch:** `arena/e2445844-chinafun1`  
**Last updated:** 2026-11-25 (UTC)

## Rules
- Claim a task by writing your session ID and file scope, then commit and push the claim immediately. Never start a task another session has claimed.
- Keep scopes non-overlapping. If a task needs a file owned by another session, log the request here instead of editing it.
- `needs review` means published on Flagged for Review page and does not block anything.
- Never mark anything verified without checking it against an official source and linking that source.
- Shared outputs (table data, site index/navigation) changed only by final integration session once all other tasks are done.
- If a claim is >60 minutes old with no commits, another session may take over and note handoff.

## Session
| Session ID | Branch | Status | Started (UTC) | Last update (UTC) |
|---|---|---:|---|---|
| e2445844 | arena/e2445844-chinafun1 | in progress | 2026-11-25 | 2026-11-25 |

## Task Board

| Task ID | Task | Status | Owner | Files/Scope | Notes |
|---|---|---|---|---|---|
| T1 | Create coordination + repo review | done | e2445844 | `COORDINATION.md`, `README.md` | Repo reviewed: only README + initial commit at start. No irregularities. |
| T2 | Research scope, assumptions, open questions | done | e2445844 | `docs/questions.html`, `docs/summary.html` | Questions/missing info documented; assumptions flagged. |
| T3 | Hotel research (verified official sources) | needs review | e2445844 | `docs/hotels.html` | Candidate hotels listed with official domains; **no verified 7-night pricing, no room compliance verification, no transit ranking**. Flagged F1-F3. |
| T4 | Michelin restaurant research & clustering | needs review | e2445844 | `docs/restaurants.html` | Verified subset (3-star/2-star/some 1-star) from official Michelin Guide pages on 2026-11-25. Hours, 2-adult prices, social links, transit unverified. Full 50 starred not completed. |
| T5 | Activities & social links | needs review | e2445844 | `docs/activities.html` | Candidate placeholders only; all fields unverified. |
| T6 | Build GitHub Pages site (static) | done | e2445844 | `docs/**`, `.nojekyll`, `README.md` | Static dashboard created in `docs/` with `.nojekyll`. Mobile-friendly tables/layout. |
| T7 | Executive summary & suggestions | done | e2445844 | `docs/index.html`, `docs/summary.html`, `docs/suggestions.html` | Drafted with evidence-first caveats. |
| T8 | Verification pass, flagged irregularities, final integration | needs review | e2445844 | `docs/verification.html`, `COORDINATION.md` | Verification audit published; 6 open flags. Not fully verified due missing live pricing/room/transit/hours/social data. |

## Verification / Evidence Log

| Timestamp (UTC) | Session | Item | Evidence / Source | Result | Notes |
|---|---|---|---|---|---|
| 2026-11-25 | e2445844 | Repo review | `git log`, file listing | Verified | Initial repo had only `README.md`, commit `8c3c56c`. |
| 2026-11-25 | e2445844 | Michelin 3-star Shanghai | https://guide.michelin.com/en/cn/shanghai-municipality/shanghai/restaurants/3-stars-michelin | Verified | Taian Table shown as only 3-star (1 restaurant). |
| 2026-11-25 | e2445844 | Michelin 2-star Shanghai | https://guide.michelin.com/en/cn/shanghai-municipality/shanghai/restaurants/2-stars-michelin | Verified (subset) | 11 restaurants indicated; subset extracted from fetched chunks. |
| 2026-11-25 | e2445844 | Michelin 1-star Shanghai | https://guide.michelin.com/en/cn/shanghai-municipality/shanghai/restaurants/1-star-michelin | Verified (subset) | 38 restaurants indicated; subset extracted. |
| 2026-11-25 | e2445844 | Michelin all starred | https://guide.michelin.com/en/cn/shanghai-municipality/shanghai/restaurants/all-starred | Verified | 50 starred total indicated. |
| 2026-11-25 | e2445844 | CNY 2027 holiday | https://www.gov.cn/zhengce/content/202611/content_7050000.htm (cited; not directly verified) | Needs review | Secondary sources cite State Council notice (国办发明电〔2026〕10号, 2026-11-05): Feb 5-13 holiday, Jan 31 & Feb 14 makeup workdays. Direct gov.cn verification required. |
| 2026-11-25 | e2445844 | Hotel pricing/room compliance | Official hotel booking engines not captured | Unverified | All hotel prices/totals/booking windows left blank; flagged F1-F2. |
| 2026-11-25 | e2445844 | Transit ranking | No route calculations performed | Unverified | Flagged F3. |

## Flagged for Review (published)

| Flag ID | Severity | Page | Issue | Owner | Status |
|---|---|---|---|---|---|
| F1 | High | hotels/verification | No verified 7-night hotel totals or cheapest booking window from official booking engines. | e2445844 | Open |
| F2 | High | hotels/verification | Private bathroom / queen-equivalent bed not verified on official room pages. | e2445844 | Open |
| F3 | High | restaurants/hotels/verification | Michelin restaurants within 1 hour subway/bus not calculated/verified. | e2445844 | Open |
| F4 | Medium | summary/verification | CNY 2027 State Council notice cited indirectly; direct gov.cn confirmation needed. | e2445844 | Open |
| F5 | Medium | summary/questions | Shanghai destination is an unconfirmed assumption. | e2445844 | Open |
| F6 | Medium | restaurants/activities | YouTube/TikTok/Instagram/social links not verified. | e2445844 | Open |

## Handoffs / Requests

| Timestamp (UTC) | From | To | Request | Status |
|---|---|---|---|---|
| 2026-11-25 | e2445844 | next session | Verify hotel official booking prices for 3 date windows; confirm room bed/bathroom; compute transit times; complete restaurant hours/prices/social links; verify gov.cn CNY notice directly. | Open |

## Log

| Timestamp (UTC) | Session | Action | Details |
|---|---|---|---|
| 2026-11-25 | e2445844 | Claim | Claimed T1-T8 on `arena/e2445844-chinafun1`. Solo session; scopes managed internally. |
| 2026-11-25 | e2445844 | Repo review | Repo contained only `README.md` ("# ChinaFun1") and initial commit `8c3c56c`. No existing site/data. |
| 2026-11-25 | e2445844 | Research | Fetched official Michelin Guide Shanghai pages (3/2/1/all starred). Extracted verified subset. Searched CNY 2027 holiday sources; direct gov.cn verification pending. |
| 2026-11-25 | e2445844 | Site build | Created static GitHub Pages dashboard in `docs/` with index, summary, hotels, restaurants, activities, questions, suggestions, verification pages and shared CSS. |
| 2026-11-25 | e2445844 | Verification | Published verification audit with 6 open flags. No hallucinated pricing/hours/social links; unverified fields left blank. |
# Shared coordination board

Session `b111cd10` · fixed Arena branch `arena/b111cd10-chinafun1` · updated 2026-11-25. Read and claim before work; commit and push claims promptly. A claim older than 60 minutes without commits may be taken over with a handoff note. `needs review` items are published on the review page and do not block others. Keep scopes non-overlapping; request changes to someone else's files here. Rebase before push. Never discard another session's work on conflict; log resolution.

| Task | Status | Owner | File scope | Verification and irregularities |
|---|---|---|---|---|
| T1 Repo review / coordination | done | b111cd10 | COORDINATION.md, README.md | Initially only placeholder README existed. |
| T2 Trip window / executive summary | done | b111cd10 | build.py, index.html, plan.html | [State Council](https://www.gov.cn/zhengce/content/202611/content_7085101.htm); proposed dates and holiday distinguished. |
| T3 Michelin clusters | needs review | b111cd10 | build.py, index.html, restaurants.html | [Shanghai](https://guide.michelin.com/en/cn/shanghai-municipality/restaurants), [Beijing](https://guide.michelin.com/en/cn/beijing-municipality/beijing/restaurants). City counts are not hotel-radius counts; source-snapshot discrepancies flagged. |
| T4 Hotels and ranking | needs review | b111cd10 | build.py, hotels.html | [Hyatt](https://www.hyatt.com/park-hyatt/en-US/shaph-park-hyatt-shanghai/rooms), [Four Seasons](https://www.fourseasons.com/guangzhou/accommodations/rooms/tower_room/). Four rooms checked; dates, totals, transit counts and ranking unverified. |
| T5 Restaurant details | needs review | b111cd10 | build.py, restaurants.html | [Michelin](https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurant/taian-table), [Taian FAQ](https://sh.taian-table.cn/faq/); 2027 costs/hours/official social accounts incomplete. |
| T6 Activities | needs review | b111cd10 | build.py, activities.html | [Shanghai Museum](https://www.shanghaimuseum.net/mu/frontend/pg/m/en/service/visit-west), [Palace Museum](https://intl.dpm.org.cn/visit.html?l=en); transit and date-specific openings unverified. |
| T7 Site build | done | b111cd10 | index.html, *.html, assets/, build.py | Six dependency-free responsive pages; README explains build. |
| T8 Verification | needs review | b111cd10 | data/verification-log.md, tests/ | Checked row sources, local links and date arithmetic; no guarantee external link uptime or mobile browser rendering. Review page records unanswered requirements. |
| T9 Questions / suggestions | done | b111cd10 | build.py, review.html | Proposed ideas separated from implementation; discovery paths and source links supplied. |
| T10 Integration / Pages | needs review | b111cd10 | all integrated files | Automated checks passed. Changing the Pages source via GitHub API returned HTTP 403 (integration lacks permission). An Actions deployment is being attempted; hotel pricing, transit counts and complete inventory remain unresolved. |

## Claim and handoff log

- 2026-11-25: `b111cd10` created board and claimed T1–T10 in commit `a6a7423` before research; no other sessions observed. The task table initially failed to reflect the textual claims; this update corrects that record. All work is on the platform-assigned branch, whose name cannot be changed.
- Single integration session; no conflicts or handoffs reported. Complete source and irregularity notes: [verification log](data/verification-log.md); public status: [Flagged for review](review.html).

## Requests to other sessions

None.

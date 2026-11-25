# COORDINATION.md — Shared Task Board

**Repo:** kanlerxz87-cyber/ChinaFun1  
**Last updated:** 2026-11-25 13:09 UTC  
**Session ID:** `arena-16153d37` (branch `arena/16153d37-chinafun1`)  
**Site:** GitHub Pages (static HTML, no build step)

## Protocol
- Claim a task by writing session ID + file scope here, then commit + push immediately.
- Never start a task another session has claimed. Scopes are non-overlapping.
- If a task requires changing a file owned by another session, log a request below instead of editing.
- Small, frequent commits. `git pull --rebase` before every push.
- On merge conflict: stop, resolve without discarding other work, log it.
- On finish: record sources, verification, irregularities; mark `done`.
- Never mark anything verified without an official-source link.
- Shared outputs (index/nav, combined data) changed only by final integration session.
- Stale claim (>60 min, no commits) may be taken over with a handoff note.

## Task Board

| ID | Task | Status | Owner | Files in scope |
|----|------|--------|-------|----------------|
| T1 | Repo setup + COORDINATION.md + claim | done | arena-16153d37 | `COORDINATION.md`, `README.md` |
| T2 | Research: dates, CNY 2027, visa, weather (official sources) | in progress | arena-16153d37 | `data/research-dates.md` |
| T3 | Research: hotels (official sites only) | in progress | arena-16153d37 | `data/hotels.csv`, `data/hotels-notes.md` |
| T4 | Research: Michelin restaurants (official guide only) | in progress | arena-16153d37 | `data/michelin.csv`, `data/michelin-notes.md` |
| T5 | Research: activities + hours + official links | in progress | arena-16153d37 | `data/activities.csv`, `data/activities-notes.md` |
| T6 | Research: social links (YT/TikTok/IG) | in progress | arena-16153d37 | `data/social.csv` |
| T7 | Site build: landing + nav + CSS/JS | in progress | arena-16153d37 | `index.html`, `assets/*` |
| T8 | Site build: executive summary + questions + suggestions | in progress | arena-16153d37 | `executive-summary.html`, `questions.html`, `suggestions.html` |
| T9 | Site build: hotels + michelin + activities + costs pages | in progress | arena-16153d37 | `hotels.html`, `michelin.html`, `activities.html`, `costs.html` |
| T10 | Verification pass: line-by-line source check + flagged page | in progress | arena-16153d37 | `flagged.html`, `sources.html` |
| T11 | Final integration: build check, link check, Pages publish | unclaimed | — | all (integration only) |

## Claims Log
- 2026-11-25 13:09 UTC — `arena-16153d37` claimed T1 (COORDINATION.md, README.md) on branch `arena/16153d37-chinafun1`. T1 complete.
- 2026-11-25 13:15 UTC — `arena-16153d37` claimed T2–T10 (all data files under `data/`, all site files at repo root and `assets/`). Single-session run: user requested all tasks completed in this session with no manual input, so this session owns the whole scope. T11 (integration/Pages publish) also executed by this session since no other session has claimed any task.

## Change Requests (file owned by another session)
- None yet.

## Handoffs / Conflicts Log
- None yet.

## Verification Log
- (Filled per task on completion: source URL + date checked + result.)

## Irregularities
- (Flagged items also appear on `flagged.html`.)

# COORDINATION.md — Shared Task Board

> **How this works:** Multiple agent sessions may work on this repo at the same time.
> Each session claims a task by writing its session ID + file scope here, then commits & pushes that claim immediately.
> Never start a task another session has claimed. Keep scopes non-overlapping.
> If a task requires changing a file owned by another session, log the request here instead of editing it.
> `needs review` = published on Flagged for Review page, does not block anything.
> If a claim is >60 min old with no commits, any other session may take over and note the handoff.

**Session ID for this branch:** `b111cd10` (branch `arena/b111cd10-chinafun1`)
**Last updated:** 2026-11-25

## Task Board

| # | Task | Status | Owner (session ID) | Files touched (scope) | Sources / Verification | Irregularities / Notes |
|---|------|--------|--------------------|-----------------------|------------------------|------------------------|
| T1 | Repo review + COORDINATION.md setup | in progress | b111cd10 | `COORDINATION.md`, `README.md` | Repo was empty except README (11 bytes). No existing code to review. | Empty repo — greenfield build. |
| T2 | Executive summary + trip window analysis (Feb 15–Mar 23 2027, preferred Feb 15–18) | unclaimed | — | `data/executive-summary.md`, `docs/` | Official: China public holiday calendar, hotel booking windows | — |
| T3 | Michelin clusters research (official Michelin Guide China) | unclaimed | — | `data/michelin-clusters.json`, `data/restaurants.json` | Official: guide.michelin.com / michelin.com | Distinguish ★ vs Listed. No inference. |
| T4 | Hotel shortlist + ranking by Michelin density (≤1 hr subway/bus) | unclaimed | — | `data/hotels.json` | Official hotel sites only; blank if unverifiable | Feb 2027 not yet bookable — flag unverified. |
| T5 | Restaurant detail: hours, days open, cost for 2, official link, social links | unclaimed | — | `data/restaurants.json` | Official restaurant sites + Michelin Guide | Social links = YouTube/TikTok/Instagram search links where no official handle. |
| T6 | Activities ≤1 hr from hotel clusters | unclaimed | — | `data/activities.json` | Official attraction sites | — |
| T7 | GitHub Pages site build (landing + subpages, mobile-friendly dashboard) | unclaimed | — | `index.html`, `*.html`, `assets/`, `_config.yml`, `.github/workflows/` | Build check: no broken links | — |
| T8 | Verification pass (every row has official source link or flagged unverified) | unclaimed | — | `data/verification-log.md` | Line-by-line check | — |
| T9 | Open questions + site improvement suggestions | unclaimed | — | `data/open-questions.md`, `data/suggestions.md` | — | — |
| T10 | Final integration + publish to GitHub Pages | unclaimed | — | all | Re-verify combined data, confirm build | Integration session only. |

## Claim Log

- 2026-11-25 — Session `b111cd10` created this board. Repo was empty (only `README.md`). Claiming T1–T10 for this session (single-session run; no other sessions active at time of claim). Will work sequentially and update statuses as tasks complete.
- 2026-11-25 — Session `b111cd10` claims T2–T10 (this session will execute all; scopes are sequential, no overlap conflict).

## Handoff / Conflict Log

- None yet.

## Requests to Other Sessions

- None — single session. If another session joins, please claim a free task above and push before starting.

## Verification Rules (binding on all sessions)

1. Every table row MUST have a source link to an official site.
2. If a value can't be confirmed from an official source, leave it blank and flag as `unverified`.
3. Never infer or fill in values. No hallucinations.
4. Hotel pricing for Feb–Mar 2027: if not bookable on official site, leave blank + flag `unverified — not yet bookable`.
5. Michelin status: `★` (1/2/3 stars) vs `Listed` (Bib Gourmand / Plate) per official Michelin Guide only.
6. Social links: prefer official handles; otherwise label as search links.

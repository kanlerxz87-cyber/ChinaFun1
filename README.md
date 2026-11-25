# ChinaFun1 — China 2027 trip planning

This repository holds **three independent research studies** for a February–March 2027 trip. They were
produced in separate sessions and are deliberately kept apart, because they disagree with each other and
merging them would hide that.

| Path | Study | Start here |
|------|-------|-----------|
| `/` (root) | **Beijing** — a MICHELIN-led 7-night plan | [`index.html`](index.html) |
| [`docs/`](docs/) | **Shanghai** — dashboard built around a 12-row starred-restaurant shortlist | [`docs/index.html`](docs/index.html) |
| [`shanghai-2027/`](shanghai-2027/) | **Shanghai** — dashboard built around a 14-row shortlist and a published proximity model | [`shanghai-2027/index.html`](shanghai-2027/index.html) |

Live site: **https://kanlerxz87-cyber.github.io/ChinaFun1/**

## Why is there more than one Shanghai plan?

Two sessions independently researched Shanghai and reached **different conclusions from the same
Booking.com data**. The honest thing to do is publish both rather than pick one and present it as
settled.

| | `docs/` | `shanghai-2027/` |
|---|---|---|
| Recommended hotel | Radisson Blu New World, **Junior Suite** | Radisson Blu New World, **queen room** |
| 7-night total | **$1,116** (before 6.6% VAT) | **$922** (Genius member rate; list $1,025) |
| Starred restaurants itemised | 12 | 14 |
| Hotel ranking | Geocoded hotels, one-hour band on 2★+ only | 5 hotels, published transit model with declared constants |
| Restaurant cost column | — | Present, `null` + flagged for all 12 |

**The headline disagreement:** `docs/` concludes that MICHELIN density *does not discriminate* between
central hotels, so price and room quality should decide. `shanghai-2027/` reaches the same practical
conclusion but measures it differently — it ranks all five geocodable hotels and shows the spread is
only 6.6 minutes of modelled time. Both are right that the one-hour rule doesn't bind; they differ on
which room type the $922/$1,116 gap reflects.

Neither document is wrong. They used different room categories, which is exactly the variable the
Beijing study flags as "the real cost driver". Worth reading both price sections side by side before
booking anything.

## Ground rules the studies follow

1. Never infer a value. If an official source doesn't state it, the cell is blank and flagged.
2. Every table row cites a source, or is marked unverified.
3. Distinguish *MICHELIN Guide listed* from *currently holds a star*.
4. Hotel costs are 7-night totals on real dates; restaurant costs are totals for two.
5. Publish what could **not** be found — see each study's flagged / open-questions page.

## Coordination

`COORDINATION.md` is the shared task board. Read it before starting work: claim a task, keep file
scopes non-overlapping, `git pull --rebase` before pushing.

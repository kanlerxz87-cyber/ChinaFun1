# ChinaFun1 — Shanghai, February–March 2027

A source-verified trip plan for **2 adults, 7–14 nights, Shanghai**, inside the window **15 Feb – 23 Mar 2027**
(preferred start 15 Feb 2027).

**Live site:** https://kanlerxz87-cyber.github.io/ChinaFun1/
(GitHub Pages, already enabled on `main` at the root path. Pages publish when this branch is merged.)

Local preview: `python3 -m http.server 8080 --bind 0.0.0.0` then open `/`.

---

## The four answers

| Question | Verified answer |
|---|---|
| Cheapest 7-night stay window | **Mon 8 Mar – Mon 15 Mar 2027** — Waldorf Astoria, Deluxe Queen Room with Two Queen Beds, **$2,374** (vs $2,414 in the preferred week) |
| Cheapest time to *book* | **Now, while the Radisson Collection Hyland 30% promotion is live** — $696 vs a published $994.49. The property states the discount applies to select stays between 19 Nov 2026 and 31 Dec 2027 |
| Best hotel cluster for MICHELIN dining | **Huangpu / the Bund** — T'ang Court (2★), Lu Style (1★), The Yidao, Shanghai and Lao Xing Xian all carry verified Huangpu addresses. Waldorf Astoria ranks first; it is *inside* the cluster |
| Exact MICHELIN dinner for two | **T'ang Court (2★): ¥888** dim sum lunch set for two, or **¥2,288** all-day set for two — both stated inclusive of service charge and taxes |

Cheapest verified compliant stay overall: **Radisson Collection Hyland, $696 for 7 nights** with a selectable king
bed and free cancellation — pending one unverified detail (private bathroom is not stated in the rate text, Q3).

---

## Verification rules this repository follows

1. **Every table row carries an official source link.** 207 external links across 31 hosts.
2. **No value is ever inferred.** Where an official source publishes nothing, the cell is blank and labelled
   `— blank / unverified`. A blank means "not found", never zero and never estimated.
3. **Prices are dated, reproducible quotes.** Each hotel figure links to the exact booking query that produced it,
   with the date parameters in the URL and the fetch timestamp `2026-11-25` recorded.
4. **Source conflicts are shown, not resolved silently.** Eight irregularities (R1–R8) are listed with both
   competing sources linked for manual review.
5. **Secondary sources never set a value.** They are used only as leads and are listed separately on
   [sources.html](sources.html) with that label.

---

## Pages

| Page | Contents |
|---|---|
| [index.html](index.html) | Landing page — verified answers, metric tiles, page index |
| [executive-summary.html](executive-summary.html) | The full decision brief on one page |
| [dates.html](dates.html) | Trip parameters, 2027 weekday map, CNY and Lantern Festival, entry requirements, a 37-row day-by-day closure calendar, Monday-closure collisions, weather conflicts |
| [hotels.html](hotels.html) | Requirement compliance with verbatim room text, master hotel table, 21-row three-window rate comparison, MICHELIN cluster ranking, blank-field register |
| [michelin.html](michelin.html) | All 23 entries — star versus listed, cuisine, price band, official address, cost for two, social links, official booking channels, count-conflict table |
| [activities.html](activities.html) | Five activities with official hours and exceptions, the one-hour travel test, the operator's published journey times, suggested sequencing |
| [costs.html](costs.html) | 7-night hotel totals, the two answers to "when is cheapest", restaurant and activity costs for two, three budget scenarios |
| [questions.html](questions.html) | 17 open questions, each with the verified position, the missing piece and a discovery route |
| [suggestions.html](suggestions.html) | 6 decision paths, 10 site improvements, 8 trip suggestions — **all unimplemented, all awaiting a reviewer decision** |
| [flagged.html](flagged.html) | Repository review, irregularities R1–R8, the 26-row register of deliberately blank values, the provenance policy |
| [sources.html](sources.html) | Complete source register — every URL, its type, its fetch date and what it proves |

---

## Layout

```
COORDINATION.md          shared task board, claims log, verification log, irregularities
README.md                this file
index.html               landing page
*.html                   10 content pages
assets/style.css         mobile-first dashboard stylesheet (no frameworks)
assets/app.js            progressive enhancement: search, filter, sort, nav (all pages readable with JS off)
tools/sitegen.py         page generator — the single source of truth for markup; run it to rebuild pages
data/research-dates.md   trip parameters, weekday map, holidays, entry rules, weather, R1–R5
data/hotels.csv          H1–H5 hotel rows
data/hotels-notes.md     full rate tables, both "cheapest" answers, cluster ranking, blank-field list
data/michelin.csv        M1–M23 restaurant rows
data/michelin-notes.md   guide counts, band legend, clusters C1–C3, booking channels
data/activities.csv      A1–A5 activity rows
data/activities-notes.md official transit times, venue facts, R6, Monday-closure collision matrix
data/social.csv          S1–S21 social links; only the 8 museum accounts are marked verified-official
```

`data/` is the source of truth. Pages are generated from it by `tools/sitegen.py`; the generator emits blank cells
with an explicit `— blank / unverified` marker so an unfilled value can never be mistaken for a zero.

---

## Key findings that change the plan

- **Monday 15 Feb 2027 is a closure day.** Yu Garden (closed Mondays), the Shanghai Museum on People's Square
  (closed Mondays) and T'ang Court (off Monday) are all shut on the preferred start date. Treat that Monday as
  arrival-only — Bund promenade and hotel — or shift the four-day block to **Thu 18 Feb → Sun 21 Feb**, which
  captures the **Lantern Festival on Sat 20 Feb** with every venue open.
- **The People's Square museum hosts only one exhibition during the whole trip.** *On Top of the World Tree:
  Ancient Civilizations of the Americas* runs 9 Jul 2026 – 14 Nov 2027, and the venue hosts no other exhibitions in
  that period. The permanent collections are at **Shanghai Museum East**, 1952 Century Avenue, which is closed
  **Tuesdays** — the opposite day to the People's Square venue.
- **Last entry is 15:00, not 16:00.** An older official museum notice says 16:00; the current official visit page
  says 15:00 and requires advance booking. The current page governs (irregularity R6).
- **Cancellation flexibility costs more than date optimisation.** Free cancellation at the Waldorf adds **$604**;
  moving to the cheapest window saves **$40**.
- **The cheapest room on the page is not a valid option.** Atour Light's Collection Twin Room is $652 for 7 nights
  but has two twin beds, failing the single-bed requirement (irregularity R5).
- **No door-to-door transit minutes are asserted anywhere.** No official journey planner was reachable, so the
  one-hour test is answered from verified shared districts plus the Shanghai Tower operator's own published
  journey times. The gap is Open Question Q7 and Suggestion S1.

---

## What is deliberately not answered

Airfare, visa fee and processing time, metro and bus fares, the Shanghai Tower ticket price and hours, museum
admission prices, the Taian Table degustation price, and the cost for two at the other 22 MICHELIN entries. Each
has an open question with a discovery route on [questions.html](questions.html) and an entry in the blank-value
register on [flagged.html](flagged.html).

---

## Working on this repository

Read [COORDINATION.md](COORDINATION.md) first. It is the shared task board: claim a task with your session ID and
file scope, commit and push the claim immediately, keep scopes non-overlapping, `git pull --rebase` before every
push, and log sources, verification results and irregularities when a task finishes. Nothing may be marked
verified without an official-source link. Suggestions on
[suggestions.html](suggestions.html) are for review and choice before implementation — record decisions in the
blank Decision columns and in COORDINATION.md.

The repository has **no LICENSE**. Choosing one is the owner’s decision, so this session did not infer one; it is
flagged on [flagged.html](flagged.html). A `.gitignore` was added during integration after a Python byte-code cache
was accidentally committed under `tools/`.

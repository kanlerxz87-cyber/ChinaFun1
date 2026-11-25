# COORDINATION — ChinaFun1 trip planning

**Session:** `fac6d965` · branch `arena/fac6d965-chinafun1` (branched from `main` @ `8c3c56c`)
**Last update:** 2026-11-25
**Published:** https://kanlerxz87-cyber.github.io/ChinaFun1/ — GitHub Pages, `main` / root, build `built` at commit `29fe8da`
**Branch watch:** other empty `arena/*` branches exist on this remote (no commits / no files as of this update). No conflicting
claims were found, so nothing was taken over. Any session starting now should claim a row here before touching `assets/data.js`.

Read this file before starting any task. It is the shared task board: what exists, who owns it, what is still open,
and what was verified against which official source.

## Task board

| Task | Status | Owner | File scope | Notes |
|------|--------|-------|-----------|-------|
| T1 Repo review + coordination setup | **done** | fac6d965 | `COORDINATION.md`, `README.md` | Repo started as a single 11-byte README. No CI, no Pages config, no licence. Logged in `flagged.html`. |
| T2 MICHELIN research (Beijing 2027 + SH/JS/ZJ 2026) | **done** | fac6d965 | `assets/data.js` (`MICHELIN`, `GUIDE_SLUG`) | All 33 Beijing starred restaurants captured with star level, cuisine, ¥ band, official guide URL. 10 have full address/phone/hours. |
| T3 Hotel pricing for the exact week | **done** | fac6d965 | `assets/data.js` (`HOTELS`) | 12 hotels, 7 nights, 15–22 Feb 2027, 2 adults. March-window comparison done for the "cheapest time" question. |
| T4 Attraction verification | **done (partial)** | fac6d965 | `assets/data.js` (`ACTIVITIES`) | Palace Museum + Mutianyu fully verified. 8 activities deliberately left blank and flagged. |
| T5 Site build (8 pages, mobile-first) | **done** | fac6d965 | `index.html`, `hotels.html`, `michelin.html`, `activities.html`, `itinerary.html`, `decisions.html`, `suggestions.html`, `flagged.html`, `assets/*` | Zero dependencies, no build step. |
| T6 Verification pass + flags published | **done** | fac6d965 | `flagged.html` | Every blank field, every irregularity and the confidence statement are published. |
| T7 Merge + GitHub Pages publish | **done** | fac6d965 | `main` via PR | Static site from repo root, `.nojekyll` added. |
| T8 Capture addresses for the remaining 23 starred restaurants | **needs review** | unclaimed | `assets/data.js` (`MICHELIN`, `DISTRICT_STARS`) | Published as suggestion #1. Do **not** start without claiming here first. |
| T9 Transit-time verification for hotel × restaurant pairs | **needs review** | unclaimed | new `data/transit.*` | Published as suggestion #2. Needs Amap routing; no estimates allowed. |
| T10 Weekly hotel price tracker | **needs review** | unclaimed | new `data/prices-history.*` | Published as suggestion #3. |
| T11 Exact menu prices for starred restaurants | **needs review** | unclaimed | `assets/data.js` (`p2` field only) | Published as suggestion #4. |

A status of **needs review** means the item is published on `suggestions.html` as a proposal and blocks nothing.

## Claims and ownership rules

- Each session edits only the files in its claimed scope. Shared outputs — `assets/data.js`, `index.html` and the nav in
  `assets/app.js` — change only in an integration pass, after the owning session is done.
- Claim a task by adding your session ID and file scope to the table above, committing, and pushing immediately.
- `git pull --rebase` before every push. If a claim is more than 60 minutes old with no commits, any session may take it over
  and must note the handoff here.
- Never mark a row verified without an official source URL. If it cannot be confirmed, leave it blank and flag it in
  `flagged.html`.

## Verification log (what was checked, where)

| Source | Verified | Date |
|---|---|---|
| [MICHELIN 2027 Beijing & Tianjin release](https://www.michelin.com/en/publications/products-and-services/michelin-guide-unveils-the-2027-beijing-tianjin-selection) | 107 Beijing entries; 2 / 5 / 26 stars; Chef 1996 + Old Tower new; Tianjin debut 27 entries | 2026-11-25 |
| [MICHELIN all-starred listing](https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred) | The 33 names, cuisines, ¥ bands; filter counts 2/5/26/32/42 | 2026-11-25 |
| MICHELIN restaurant pages (10) | Address, phone, hours, own website | 2026-11-25 |
| [Trb Hutong menu](https://www.trbhutong.com/menu) | ¥788 / ¥1,688 / ¥2,288 pp + 15% | 2026-11-25 |
| [Booking.com 5★ Beijing, 15–22 Feb 2027](https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204) | 12 seven-night totals + room/bed types | 2026-11-25 |
| [Booking.com 5★ Beijing, 15–22 Mar 2027](https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-03-15&checkout=2027-03-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204) | Date-window price comparison | 2026-11-25 |
| [Palace Museum visit page](https://intl.dpm.org.cn/visit.html) | Hours by season, Monday closure, ¥40/¥60, 40,000 cap, gallery add-ons | 2026-11-25 |
| [Mutianyu official](https://en.mutianyugreatwall.com/) | Off-season 16 Nov–15 Mar, 8:00–17:30, sales end 16:30 | 2026-11-25 |
| [U.S. State Dept — China](https://travel.state.gov/en/international-travel/travel-advisories/china.html) | Visa required, 10-yr multiple entry, 6-month passport rule | 2026-11-25 |
| [China 2027 holidays](https://www.timeanddate.com/holidays/china/2027) | CNY Sat 6 Feb 2027; holiday 5–13 Feb; make-up days 31 Jan / 14 Feb | 2026-11-25 |
| [MICHELIN Shanghai/Jiangsu/Zhejiang 2026](https://guide.michelin.com/en/article/michelin-guide-ceremony/michelin-guide-shanghai-jiangsu-zhejiang) | 409 entries; 77 stars (1/14/62) | 2026-11-25 |

## Irregularities (also published on `flagged.html`)

1. Two Beijing editions are still indexed across the web (2026: 99 entries / 32 starred; 2027: 107 / 33). This repo uses **2027 only**.
2. Secondary listicles contain claims that contradict the current guide (e.g. Opera BOMBANA as three-star). Not used.
3. The King's Joy YouTube link says "3-star"; it is a 2024 upload and the current status is Two Stars — noted in the row.
4. Booking labels Swissotel as "Sanlitun, Dongcheng"; Sanlitun is normally Chaoyang. Flagged, not silently corrected.
5. Booking's "5/5" property rating is not an official star class.
6. Park Hyatt and Rosewood are not bookable for 15–22 Feb 2027 and were excluded rather than priced off another week.
7. Purple Horse Garden's $901 quote is a **March** window; excluded from the ranking, listed last with a "March only" chip.
8. Members-only rates excluded (New World: $901 member vs $1,177 public → public used).
9. Only 10 of 33 starred restaurants have a verified address, so district counts are a **lower bound**.
10. No transit times are published, by design — they cannot be verified from a static page.

## Handoff notes for the next session

Start with T8 (addresses) and T9 (transit). Those two turn the provisional hotel ranking into a real answer. Keep
`assets/data.js` as the single source of truth, keep the `verified / flagged / blank` discipline, and update this file
in the same commit as any data change.

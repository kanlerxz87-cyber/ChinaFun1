# China 2027 Verified Trip Planner (`china-2027/`)

Self-contained, source-linked dual-city (Beijing & Shanghai) travel dashboard for 2 adults taking a **1–2-week trip** inside **2027-02-15 to 2027-03-23**, built with Python 3 stdlib only and zero external CDN dependencies. If Feb 15 is check-in and Feb 18 checkout, the preferred interval is **3 nights**, below the minimum; whether it describes the whole trip or a start preference remains unresolved. No flexible-start interpretation is inferred.

## Coverage & Verification Dates

Most source and rate captures are dated **2026-11-26**; the two Shanghai luxury hotel quotes are dated **2026-11-25**, and the Beijing holiday notice, Hong Kong Observatory lunar-calendar source, National Immigration Administration policy page, and official Shanghai payment guidance were checked **2026-11-27**. Follow the individual source dates shown in each row.
- **Official 2027 PRC Holiday Calendar**: State Council schedule (Spring Festival Feb 5–13; zero statutory holidays Feb 15–Mar 23; Lantern Festival Sat Feb 20).
- **13 Hotel Quote Snapshots** (8 Beijing, 5 Shanghai): The displayed room rows were captured on Booking.com on 2026-11-25 or 2026-11-26 and list bed/bath requirements, rate terms, and selected stay-date comparisons. The shortlist order is provisional and does not certify the ≤60-minute subway/bus requirement. Snapshots do **not** prove a cheapest purchase date or guarantee availability; they do not price the combined 13-night stay. Prices vary by property and stay date (for example, Grand Millennium Beijing’s Mar 1–8 capture was $783 vs. $838 for Feb 15–22).
- **56 Directly Verified MICHELIN Venues**: 100% of Beijing's 33 starred restaurants (Chaoyang 20, Dongcheng 9, Xicheng 3, Shunyi 1 — 10/33 hours verified, 4 official menu PDFs/totals) + 8 Beijing Bib Gourmand/Selected + 15 Shanghai highlights (live guide totals: 1×3★, 11×2★, 38×1★ = 50 starred, 33 Bib, 70 Selected = 153 total; `Sir Elly's` audit-corrected to MICHELIN Selected).
- **16 Official-Source Verified Activities** (10 Beijing + 6 Shanghai) with exact winter hours, Monday/Tuesday closures, CNY costs for 2 adults, and 91 total verified YouTube, TikTok & Instagram review links.
- **2 In-Scope Itineraries**: 7-night Beijing and 14-day / 13-night Beijing + HSR + Shanghai (7 Beijing nights + 6 Shanghai nights). No quote was captured for the six-night Shanghai stay (check-in Feb 22, checkout Feb 28), so its hotel total remains unpriced. Hotel-to-venue ≤60-minute transit is not certified; district counts are not journey times.
- **Line-by-Line Repo Audit**: Full read-only QA log of sibling repository discrepancies published on `flagged.html`.

## Rebuild & Validate
```bash
python3 china-2027/tools/build.py
python3 china-2027/tools/check.py
```

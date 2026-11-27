# China 2027 Travel Planner (`china-2027/`)

Self-contained dual-city (Beijing & Shanghai) travel dashboard for 2 adults considering travel inside **2027-02-15 to 2027-03-23**, built with Python 3 stdlib only and zero external CDN dependencies. Calendar, MICHELIN, attraction, and transit claims cite official/operator sources; hotel pricing uses separate third-party Booking.com snapshots.

## Research dates
- Core planner research checked **2026-11-26**; hotel rate pages refreshed **2026-11-27**.
- **Official 2027 PRC Holiday Calendar**: State Council schedule (Spring Festival Feb 5–13; zero statutory holidays Feb 15–Mar 23; Lantern Festival Sat Feb 20). Feb 5 is Friday per the Hong Kong Observatory calendar; one Gazette copy conflicts on the weekday, and the discrepancy is flagged.
- **13 Selected Hotels** (8 Beijing, 5 Shanghai): all selected room descriptions meet the private-bathroom + queen/king criteria. Booking.com totals are 7-night USD snapshots for 2 adults/1 room and show taxes/fees included; cancellation, prepayment, breakfast, and Genius/member eligibility are offer-specific. All 13 were captured for Feb 15–22; seven core properties were queried again for Feb 18–25, Mar 1–8, and Mar 16–23. Pullman's Mar 1–8 visible rate was twin-only and is excluded. Its Feb 18–25 $805.25 free-cancellation offer is a twin, not a King; no flexible King offer/terms were verified for Feb 18–25 or Mar 16–23. These partial, dynamic captures do **not** establish a universal cheapest stay date.
- **56 MICHELIN Venues**: 100% of Beijing's 33 starred restaurants (Chaoyang 20, Dongcheng 9, Xicheng 3, Shunyi 1 — 10/33 hours verified, 4 official menu PDFs/totals) + 8 Beijing Bib Gourmand/Selected + 15 Shanghai highlights (live guide totals: 1×3★, 11×2★, 38×1★ = 50 starred, 33 Bib, 70 Selected = 153 total; `Sir Elly's` audit-corrected to MICHELIN Selected).
- **16 Official-Source Verified Activities** (10 Beijing + 6 Shanghai) with exact winter hours, Monday/Tuesday closures, CNY costs for 2 adults, and 91 total verified YouTube, TikTok & Instagram review links.
- **3 Date-Anchored Itineraries**: 7-night Beijing, 14-calendar-day Flagship Beijing + HSR + Shanghai (13 nights; optional 14-night variant), and 21-night / 22-calendar-day Unhurried Deep Dive. Hotel subtotals are not presented as confirmed quotes for dates that were not queried.
- **Line-by-Line Repo Audit**: Read-only QA log of sibling repository discrepancies published on `flagged.html`.

## Rebuild & Validate
```bash
python3 china-2027/tools/build.py
python3 china-2027/tools/check.py
```

# Missing Information Discovery & Site Improvement Suggestions (`T5`)

## Missing Data & Verification Gaps Discovered
1. **Sold-Out & Contradictory Hotel Listings Excluded:** `Atour Bund East Nanjing Rd` (unavailable Feb 15–22 + conflicting "Shared toilet / Private bathroom" tag), `Atour S Beijing Sanlitun` (sold out Feb 15–22), `ibis HK Central & Sheung Wan` (sold out Feb 15–22), and `Radisson Blu New World` / `The Murray HK` (Booking HTML fetch failures) were cleanly quarantined to `flagged.html` rather than padded.
2. **March Room Category Inflation:** `Upper House Shanghai`, `Waldorf Astoria Beijing`, and `Atour Nanluoguxiang` quote larger/pricier room tiers in March because base rooms were depleted — making raw Feb-vs-Mar percentage comparisons partially inventory-driven.
3. **Full 494-Venue Geocoding Boundary:** While citywide MICHELIN totals (**HK 234 / SH 153 / BJ 107**) are verified live on `guide.michelin.com`, exact <=15/30/60-minute hotel matrices cover the **37 individually audited MICHELIN venues + 24 attractions** (full 494-venue coordinate batching remains a worthwhile v2 upgrade via Amap/Apple Maps APIs).
4. **Mainland & New-2026 Social Platform Coverage:** Domestic Mainland restaurants (`Ji Pin Court`, `Bao Du Jin Sheng Long`, `Mingyuan`, `Chao Shang Chao`, `Xin Rong Ji`) primarily publish on **Douyin & Xiaohongshu** rather than YouTube/Instagram/TikTok; new 2026 HK venues (`Terrace Boulud`, `Pedder Chinese`) have official IG + website links but no public TikTok yet.
5. **Post-LNY Restaurant Holiday Schedules (Feb 15–16, 2027):** Individual family-run spots (`Qiao Ai Lai Lai`, `Yat Lok`, `Kau Kee`, `Taian Table`) announce exact Lunar New Year break dates ~2–4 weeks prior; confirm reservations directly in late Jan 2027.

## Suggested Dashboard & Itinerary UX Improvements
1. **Interactive Hotel-to-Venue Transit Explorer (Implemented in `restaurants.html` & `activities.html`):** Selecting any hotel in a city dynamically displays the exact door-to-door transit minutes to every audited restaurant and activity, highlighting `<=15 min` walkable gems vs `<=30 min` subway rides.
2. **Budget Split & Trip Cost Calculator (Implemented in `questions.html`):** Combines 7-night Feb vs Mar hotel costs with a configurable dining mix (e.g., 1× 3-Star + 2× 1/2-Star + 6× Bib Gourmand + activities) in both local currency and USD.
3. **Day-by-Day Conflict & Closure Calendar (Implemented in `activities.html`):** Flags Monday closures, Tuesday closures, Sunday closures (`Kau Kee`), `Lantern Festival Sat Feb 20, 2027`, and `Two Sessions Mar 4–14` right beside venue opening hours.
4. **Future Phase 2 Enhancements (Post-Confirmation):**
   - Generate live **Apple Maps / Google Maps / Amap coordinate deep links** for one-tap mobile navigation while walking between Central / Jing'an / Wangfujing stops.
   - Add **WeChat / SevenRooms / OpenRice reservation countdown reminders** (e.g., Forbidden City T-7d 20:00 CST, Taian Table 1st-of-month release, Amber 60 days out).
   - Export custom selected itinerary as an `.ics` calendar file for both travelers' phones.

# E2 spot re-verification — 2026-11-26 (session 8f562229)

All sources below were fetched and read this session (not pattern-matched, not recalled). Each entry: what was checked → what the official page said → what was done to the data.

| # | Official source (URL) | Claim checked | Result |
|---|---|---|---|
| 1 | https://www.michelin.com/en/publications/products-and-services/michelin-guide-unveils-the-2027-beijing-tianjin-selection | 2027 Beijing & Tianjin guide: 135 establishments combined; Beijing 107 listed; 33 starred (2×3★ / 5×2★ / 26×1★); Chef 1996 promoted Selected→1★; Old Tower debut 1★; 48 Bib Gourmand incl. 7 debuts; 52 Selected; released 28 Oct 2026 | **Match** to data.js (33 rows, 2/5/26). Also independently re-checked by session `24fa9b09` (same date) and by session `f6189cca`'s audit (PR #24). |
| 2 | https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred | Names, tiers, cuisines, ¥ bands of the 33; filter counts (3★=2, 2★=5, 1★=26, Bib=32, Selected=42; "1-33 of 33 restaurants") | **Match.** Used as the cross-check for DISTRICT_STARS (Chaoyang 20 / Dongcheng 9 / Xicheng 3 / Shunyi 1 — all 33 addresses now assigned). |
| 3 | https://guide.michelin.com/us/en/beijing/restaurants/<each of 33 slugs> | Full address + phone for every starred row | **23 previously blank rows filled 2026-11-26** (see missing-fields-audit.md). 10 earlier rows unchanged. No field was inferred. |
| 4 | https://guide.michelin.com/us/en/beijing/restaurants/fu-chun-ju | Hours | **Published: Mon–Sun 11:30–14:30 & 17:30–21:30** — recorded. |
| 5 | https://guide.michelin.com/us/en/beijing/restaurants/il-ristorante-niko-romito-1186723 | Hours | **Published: Mon–Sat 12:00–14:30 & 18:00–22:00; Sun lunch to 15:00** — recorded as one string; phone confirmation still advised before booking. |
| 6 | https://guide.michelin.com/us/en/beijing/restaurants/zhiguan-courtyard | Official website | **None published** (Facilities & Services = phone +86 10 6559 9899 only). `w` left blank, flagged. |
| 7 | https://www.trbhutong.com/menu | TRB Hutong menu prices | **¥788 weekday business lunch pp / ¥1,688 seasonal pp / ¥2,288 signature pp; +15% service**; wine pairings extra. Matches flagged.html; Trb Hutong hours previously verified (daily 11:30–14:30 & 17:30–22:00) — unchanged. |
| 8 | https://intl.dpm.org.cn/visit.html | Palace Museum low-season (Feb 2027) opening | **Tue–Sun 8:30–16:30** (1 Nov–31 Mar; last entry 15:30); closed Mon (except national holidays); CNY 40 adult low-season; Treasure & Clock galleries ¥10; 40,000/day cap; advance booking + passport. Matches data.js verbatim — no edit. |
| 9 | https://en.mutianyugreatwall.com/ | Mutianyu hours / prices | 8:00–17:30; ticket sales end 16:30; check-in 8:00–17:00; off-season 16 Nov–15 Mar. **Ticket prices still not published on the English landing page** — flag stays open; price deliberately not filled. |
| 10 | https://www.youtube.com/oembed?url=... (58 URLs, session 773e75a3, recorded in COORDINATION.md) | The 58 direct video links injected into data.js rows | **All previously oEmbed-verified** by the owning session; this session injected them verbatim (prepend, before the labeled search links) and did not assert any new URL. King's Joy videos are 2024-era uploads describing 3★ status — current status is Two Stars; row notes retained. |
| 11 | https://travel.state.gov/en/international-travel/travel-advisories/china.html | China advisory (US citizens) | Level 2 "Exercise increased caution", issued 2026-10-19 (re-verified this date by session `24fa9b09`; consistent with the plan's visa/passport notes). Not re-fetched this session — recorded as inherited from the same-day independent check rather than re-asserted. |
| 12 | https://www.timeanddate.com/holidays/china/2027 | 2027 Spring Festival dates | Feb 5–13 holiday; make-up workday Sun 14 Feb; Lantern Festival 20 Feb (re-verified this date by session `24fa9b09`; Third-party calendar — already labelled as such). Not re-asserted here. |

## Known discrepancies found (not silently fixed)

- **Poetry·Wine** and **The Beijing Kitchen**: live MICHELIN guide pages show **¥¥**; `assets/data.js` carries **¥¥¥** (earlier read). See `missing-fields-audit.md`. Left unchanged pending an explicit decision; flagged on `flagged.html`.
- **Gastro Esthetics DaDong**: phone printed on guide page in 8-digit local format (+86 51690328) — recorded as printed, noted in the row.
- **King's Joy videos** describe a pre-2026 three-star claim — flagged on `flagged.html`.
- ~~Booking prices~~ are snapshots (25 Nov 2026), not locked quotes — unchanged, still flagged.

## Cross-plan note

Sessions `cac5675c`, `24fa9b09` and `f6189cca` completed the integration + publish passes and PR #24 merged to `main` at `aa02a10` before this session's changes landed. This session rebased onto that commit; the independent 2026-11-26 checks by those sessions (rows 1, 2, 8, 11, 12 above) and this session's reads are mutually consistent.

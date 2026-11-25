# T5 — Activities: verified hours, prices, and the ≤1-hour travel test

Session `arena-16153d37` · Official sources fetched 2026-11-25 UTC.

## A. The ≤1-hour requirement — what can and cannot be verified

The brief asks that activities sit within **1 hour of travel by subway or bus** from the hotel. No commercial routing API and no official Shanghai Metro journey planner were reachable in this session, so **no hotel→venue minute figure is invented**. Instead, the only official published journey times found are reproduced verbatim below, from the Shanghai Tower operator's own transport page:

Source: https://en.shanghaitower.com/Publictransit.html (fetched 2026-11-25)

| Origin (official) | Official published route | Official published time |
|---|---|---|
| Shanghai Railway Station, South Square | Metro Line 1 to **People's Square Station**, transfer to Line 2, alight **Dongchang Road** | **40 minutes** |
| Shanghai Railway Station, North Square | Metro Line 4 to Century Avenue, transfer Line 2, alight Dongchang Road | **50 minutes** |
| Shanghai South Railway Station | Metro Line 1 to People's Square, transfer Line 2, alight Dongchang Road | **50 minutes** |
| Shanghai South Railway Station | Metro Line 3 to Zhongshan Park, transfer Line 2, alight Dongchang Road | **60 minutes** |
| Hongqiao Airport | Metro Line 2 from Songhong Road to Dongchang Road | **about 50 minutes** |
| Pudong Airport | Maglev → transfer Metro Line 2 at Longyang Road → Dongchang Road | **50 minutes** |
| Pudong Airport | Airport Bus Line 5 → Shanghai East Hospital | **70 minutes** |
| Shanghai Port International Cruise Terminal | — | **about 5 km, 20 minutes** |

Official access point for the tower itself: *"Walk from Metro Line 2 Lujiazui Station Exit 6, passing LG2 of Shanghai IFC Mall"* or *"Walk from Metro Line 14 Lujiazui Station Exit 9A"*.

### What this officially supports
- **People's Square is on Metro Line 1 and connects to Line 2** (stated in the operator's own routing text). Both Radisson Collection Hyland Shanghai and Atour Light (People's Square / West Nanjing Road) sit in that node.
- The operator's own published envelope for a **Line 1 → Line 2 → Dongchang Road** journey, measured from Shanghai Railway Station, is **40–50 minutes** — i.e. inside the 1-hour limit. The Lujiazui tower access station is on the same Line 2.
- The Bund and Lujiazui are officially linked by **The Bund Sightseeing Tunnel** ("Walk from Pudong exit"), relevant to the two Bund hotels (Peninsula, Waldorf Astoria).

### What remains UNVERIFIED (flagged, not estimated)
- Door-to-door minutes from any specific hotel to any specific venue.
- Whether a given bus line runs at the hour planned.
- Fare amounts (no official fare page located).
→ Recorded as open item **Q7** in `questions.html` and as suggestion **S4** in `suggestions.html`.

## B. Venue-by-venue verified facts

### A1 · Shanghai Museum on People's Square — **the single most important scheduling fact in this plan**
Official page: https://www.shanghaimuseum.net/mu/frontend/pg/m/en/service/visit-west (fetched 2026-11-25)

| Field | Verified value |
|---|---|
| Address | 201 Ren Min Da Dao (South Entrance Gate on Wusheng Road) |
| Days | Tuesday to Sunday; **closed Mondays** (except national holidays) |
| Hours | **09:00–17:00, last entry 15:00**; a Day & Evening Session option runs **09:00–21:00, last entry 19:00** |
| Exhibition lock | *"During the exhibition **On Top of the World Tree: Ancient Civilizations of the Americas (9 July 2026 – 14 November 2027)**, the Shanghai Museum on People's Square will host **no other exhibitions**. Visitors wishing to view permanent displays and other special exhibitions may go to the Shanghai Museum East (Address: 1952 Century Avenue, Pudong New Area)."* |
| Booking | Individual visitors book via the official WeChat Mini Program; **official page states "Overseas visitors can book through trip.com"**; present original valid ID; enter via South Gate individual passage |
| Groups ≥20 | telephone reservation 7 days in advance (excluding visit day), 021-63724550 |
| Green Channel | 65+, active/retired military, martyrs' families, fire & rescue, public security police — venue access only, excludes galleries |
| Disability | free admission with valid ID |
| Enquiries | 021-60226699 |
| Photography | no flash, no selfie sticks, no tripods; no personal live broadcasts or recordings without permission |
| Admission price | **not stated on the fetched page → blank / flagged** |

**Consequence for the requested dates:** the entire trip window (2027-02-15 → 2027-03-23) sits **inside** the Americas exhibition run. Therefore:
1. People's Square = **only** *On Top of the World Tree* during this trip.
2. The classic permanent collections (bronzes, ceramics, jade, calligraphy, painting) are at **Shanghai Museum East** (1952 Century Avenue, Pudong) for the whole trip.
3. **2027-02-15 is a Monday → People's Square is closed.** The preferred start date cannot include it.

**R6 (irregularity):** an official news notice dated 2025-08-25 (https://www.shanghaimuseum.net/mu/frontend/pg/m/article/id/I00004797) states 9:00–17:00 with **last entry 16:00** and **walk-in entry with ID, no reservation required** from 1 September. The current Visit page (guidelines "take effect on 30 June") states **last entry 15:00** and requires **advance booking** via WeChat Mini Program / trip.com for overseas visitors. The two official pages conflict. The Visit page is treated as current; **both are linked** so the conflict can be reviewed manually. Plan for last entry 15:00 and pre-booking.

### A2 · Shanghai Museum East
Official notice used: https://www.shanghaimuseum.net/mu/frontend/pg/m/article/id/I00004684 (dated 2024-09-10) · current visit page https://www.shanghaimuseum.net/mu/frontend/pg/m/en/service/visit-east (**not fetched — flagged**)

- Hours per that notice: **10:00–18:00, last entry 17:00**; **closed every Tuesday** (except public holidays).
- Address verified from the People's Square page: **1952 Century Avenue, Pudong New Area**.
- Walk-in with valid ID through the **B1 East Gate**; The Curio-City and Digital Gallery still require WeChat reservation.
- Groups ≥20: 021-20729999 ext. 134, 7–14 days ahead.
- **Flagged:** hours come from a 2024 notice, not the current page → re-verify before travel (open item Q5).

### A3 · Shanghai Tower — Top of Shanghai Observatory
Official page: https://en.shanghaitower.com/shagnhai.html

- Route published officially: B1 *Top of Shanghai Exhibition Hall* → **118F Observatory at 546 m, 360° view** → *SKY632 Art Space* on 125F/126F.
- Inquiry hotline **(8621)80370150**, inquiry time Monday–Sunday 9:00–18:00.
- **Ticket price: NOT published on the official page → blank / flagged (R3).** Widely quoted third-party figures (¥180 adult / 08:30–22:00) are **not** used anywhere on this site as verified values.
- Official instruction: carry ID cards or passports.
- Official online ticket channels named by the operator: **Ctrip.com, LY.com, Lvmama.com, Meituan.com, Dianping.com**.

### A4 · Yu Garden — fully verified including price
Official page: https://www.yugarden.com.cn/page/articleview/message.html

| Field | Verified value |
|---|---|
| Hours | **9:00–16:30**; entry stops **16:00**; closes 16:30 |
| Closed | every **Monday**, except national statutory holidays; Spring Festival times per announcement |
| Off-season ticket | **¥30 per adult** — applies 1 Dec – 31 Mar, so **every date in the trip window** |
| Peak-season ticket | ¥40 per adult (1 Apr – 30 Jun; 1 Sep – 30 Nov) |
| **Total for 2 adults** | **¥60** (2 × ¥30) |
| Half price | minors over 6 to 18 inclusive; full-time undergraduates and below (ID + student card); seniors 60+ with valid ID |
| Free | children ≤1.3 m or ≤6 years (accompanied, max 3 per adult); disability and military/martyr-family/fire-rescue/police categories with valid documents |
| Gates | **North Gate, 168 Fuyou Road** (groups + individuals) · **South Gate, 279 Yuyuan Old Street** (individuals only, at the Nine-Turn Bridge exit) |
| Address | 218 Anren Street, Huangpu District, 200010 |
| Phone | 021-63260830 |
| Tickets | official **上海豫园 WeChat mini program** online; ticket windows at both gates offline |
| Discount cap | one discount ticket per person per day |

**Monday clash:** Yu Garden is closed on the preferred start date 2027-02-15 (Monday).

### A5 · The Bund riverside promenade
No official hours/admission page was located → both fields **blank and flagged**. Its relevance is verified instead through official hotel addresses (Peninsula = No. 32 The Bund; Waldorf Astoria = No.2 Zhong Shan Dong Yi Rd) and the Shanghai Tower operator's official mention of **The Bund Sightseeing Tunnel** and of the cruise terminal being ~5 km / 20 minutes away.

## C. Monday-closure collision matrix (verified closures vs requested dates)

| Venue | Mon 2027-02-15 | Tue 2027-02-16 | Wed 2027-02-17 | Thu 2027-02-18 | Fri 2027-02-19 | Sat 2027-02-20 (Lantern Festival) | Sun 2027-02-21 |
|---|---|---|---|---|---|---|---|
| Shanghai Museum People's Square | **CLOSED** | open | open | open | open | open | open |
| Yu Garden | **CLOSED** | open | open | open | open | open | open |
| T'ang Court (2★) | **OFF** | open | open | open | open | open | open |
| Shanghai Museum East | open | **CLOSED** | open | open | open | open | open |
| Shanghai Tower Observatory | **hours not published — flagged** | flagged | flagged | flagged | flagged | flagged | flagged |

**Recommended fix (no manual input needed to apply):** treat Mon 2027-02-15 as arrival/settling day (Bund promenade + hotel), and schedule Yu Garden, People's Square museum and T'ang Court on Tue–Sun. Alternatively shift the 4-day preferred block to **Thu 2027-02-18 → Sun 2027-02-21**, which also captures the Lantern Festival on Sat 2027-02-20.

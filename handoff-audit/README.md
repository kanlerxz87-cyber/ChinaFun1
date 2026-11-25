# China trip — release handoff audit

**Recommendation:** Carry February 15–22, 2027 as the first seven-night quote window for two adults; it includes all preferred dates. Compare February 18–25 and March 16–23 using identical rate conditions before selecting a stay. These are planning windows, not verified offers. Do not publish a winning hotel or a cheapest booking date yet.

## Findings for Flagged for Review

| Evidence reviewed | Issue | Release action / official verification source |
|---|---|---|
| `17be6d76:data/hotels.md`, five hotel rows | Aggregator and destination-wide nightly rates multiplied by seven are not date-specific official checkout totals. The 10-count hotel also ranks ahead of the 11-count hotel. | Blank all unsupported prices and rankings. Check the exact property and room at [Marriott](https://www.marriott.com/) or [The Peninsula](https://www.peninsula.com/) for their respective properties. |
| `3cb26b2c:data/hotels.md`, Langham | The URL is for three nights, not seven, and 7 × $219 is $1,533, not $1,527. Neither is an official rate. | Blank total; use [The Langham Shanghai](https://www.langhamhotels.com/en/the-langham/shanghai/). |
| `17be6d76:data/hotels.md`, Monday recommendation | A citywide weekday average does not tell you when to buy a particular seven-night stay; Monday Feb 15 would be same-day for the preferred arrival. | Blank best booking date; track repeat quotes for the *same* dates and cancellation terms on the hotel’s official booking engine. Future minimum cannot be guaranteed. |
| Both restaurant datasets | Michelin price symbols do not substantiate dollar ranges; city/category pages do not substantiate individual hours, transit, or holiday closures. A Hong Kong social profile does not establish relevance to a Shanghai venue. | Check branch-specific awards in the [Michelin Guide](https://guide.michelin.com/), then verify the two-person all-in amount from a named menu and confirm date-specific hours directly. Blank unsupported social links and closure claims. |
| Both hotel/restaurant datasets | Neighborhood membership does not prove door-to-door travel under 60 minutes; ranking also requires a consistent universe of starred, Bib Gourmand and selected restaurants. | Use the [Beijing transport authority](https://jtw.beijing.gov.cn/) and [Shanghai Metro](https://www.shmetro.com/) as starting points. Record entrances, walking segments, waits, transfers and timestamp; do not treat unknown routes as zero or as passing. |
| `3cb26b2c:data/activities.md`, Palace Museum | Tour reseller links are not operator evidence. The official English visit page verifies Tue–Sun, Nov–Mar 08:30–16:30 (last entry 15:30), national-holiday Monday exception except Lunar New Year’s Eve, and possible irregular closures. It says no same-day ticket sales. | Cite the [Palace Museum](https://intl.dpm.org.cn/visit.html). Leave dated exceptions and social coverage blank until independently verified. Base admission CNY 80 for two adults (2 × CNY 40, excludes special galleries). Feb 15 is a Monday; use Feb 16 as a candidate only, subject to the [museum notices](https://intl.dpm.org.cn/notice.html). |

## Decisions and discovery plan

1. **Which hotel meets the hard requirements?** Capture official room name, bed dimensions/type, exclusive bathroom, two-adult occupancy and availability. Do not treat a property amenity as confirmation for the quoted room.
2. **What is the cheapest verified stay?** Record all mandatory taxes and fees, currency, quote timestamp, payment and cancellation terms per seven-night window. Show best observed price separately from a prediction about when to book.
3. **Which base makes the most outings reachable?** Compare routes at opening and dinner times. Require matching venue identities, then count confirmed distinct restaurants per hotel by Michelin award class. Track untested pairs separately.
4. **What can actually go on the itinerary?** Check official operator notices and reservations. Keep dated availability separate from normal published hours. Check each social video or post for the actual venue and distinguish official from editorial material.
5. **What entry rules apply?** Check rules for each traveler’s passport and entry itinerary with the [Chinese Embassy](https://us.china-embassy.gov.cn/eng/). Departure city is not evidence of nationality.

## Suggested site improvements (not implemented)

- **First:** Add field-level source, checked-at date, and missing-value reason. Avoid marking an entire row verified based on one field.
- **Second:** Show side-by-side seven-night quote snapshots with room, fees and refundability; keep dinner totals in the comparison view without implying every candidate restaurant will be visited.
- **Third:** Add a route evidence drawer and filters for star class, verified price and same-day availability. Show the denominator and unresolved pairs next to each count.

## Integration status

Main at `8c3c56c` contains only `README.md`. The task board is fragmented across five branch-local copies, with overlapping claims on research, dashboard and publication. The GitHub Pages API reported an existing build sourced from `main:/`; that is not evidence the trip dashboard is live. Keep its source unchanged until one integrator reconciles the claims and release candidates. The source links above are operator/authority links for manual checking, not proof of the unverified values. This is a targeted audit, not approval of either dataset or a complete external link check.

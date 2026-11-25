# ChinaFun1 — Shanghai Trip Planning Dashboard

Evidence-first trip planning workspace for a 1–2 week China trip (couple, 2 adults), with a focus on Shanghai Michelin clusters, hotel verification, and decision support.

## Live site (GitHub Pages)

The static site is in [`docs/`](./docs/). To publish with GitHub Pages:
1. In GitHub repo settings, set **Pages** source to **Deploy from a branch**.
2. Select branch `arena/e2445844-chinafun1` (or merged target branch) and folder `/docs`.
3. Save. The dashboard will be served from GitHub Pages.

## What’s included

- `docs/index.html` — Landing dashboard
- `docs/summary.html` — Executive summary
- `docs/hotels.html` — Hotel candidates, criteria, and verification gaps
- `docs/restaurants.html` — Michelin-starred restaurant subset (verified from official Michelin Guide pages)
- `docs/activities.html` — Candidate activities (verification pending)
- `docs/questions.html` — Blocking questions and missing information
- `docs/suggestions.html` — Improvement suggestions and decision paths
- `docs/verification.html` — Verification audit and flagged irregularities
- `COORDINATION.md` — Shared task board/log for parallel sessions

## Verification policy

- Every table row should carry an official/source link.
- Values not confirmed from an official/authoritative primary source are left blank and flagged as unverified.
- No prices, hours, availability, or social links are inferred.
- Time-sensitive data (hotel pricing, hours, Michelin status) must be re-verified before booking.

## Key assumptions (unconfirmed)

- Destination assumed **Shanghai, China** because user requested "Trip Planning China" without a city.
- Preferred dates: 2027-02-15 to 2027-02-18; 7-night pricing benchmark window still needs selection.
- Transit criterion interpreted as subway/bus within ~1 hour.

See [`docs/questions.html`](./docs/questions.html) for full decision-blocking questions.
# China 2027 decision layer (original site: session `815c7943`; inventory update: `a94e6d8b`)

A static, dependency-free comparison site at `integration-2027/`. It preserves four single-city, seven-night hotel snapshots captured on 25 Nov 2026 and links separately to the Beijing + Shanghai planner. The dual-city study is not folded into the one-city price table because it has no single combined seven-night hotel total. Rates on every plan are dated snapshots, not live quotes.

- `index.html` — executive summary, four single-city rows and a separate dual-city option
- `plans.html` — 25 Nov seven-night price snapshots, source dates, tax/room caveats and the separate multi-city path
- `social.html` — original cross-plan video index with official venue links; blank hours/costs remain flagged
- `questions.html`, `suggestions.html`, `flagged.html`, `sources.html` — open decisions, proposals, irregularities and source audit
- `data/*.json` — single source for each generated page, including the dual-city study and official-source links
- `tools/build.py` — regenerates the pages; `tools/check.py` — checks local links, source fields and dual-city references

The 2026-11-27 integration pass re-read the State Council holiday notice and the live MICHELIN lists; source dates are recorded per row. It did not re-price hotels. The official State Council Chinese notice confirms the Spring Festival break (Feb 5–13, 2027) and workdays Jan 31 / Feb 14; the English schedule omits the workday detail. The Shanghai 2026 regional release's count of 156 Shanghai restaurants remains distinct from the live MICHELIN filter's 153 category sum, and is flagged rather than reconciled by inference.

```bash
python3 integration-2027/tools/build.py && python3 integration-2027/tools/check.py
```

Verification rule: a video enters the social index only after its watch page was read; restaurant/activity hours and menu values remain blank unless the linked official source establishes them. Inherited hotel quotes retain the owning session's dated Booking.com source and caveats.

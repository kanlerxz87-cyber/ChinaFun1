# China 2027 decision layer (original research session `815c7943`; final integration update `e411628d`)

A static, dependency-free comparison site at `integration-2027/`. It does **not** replace any source trip plan. The current hub links five research dashboards: four single-city studies (one Beijing, three Shanghai) and one later dual-city Beijing + Shanghai study.

- `index.html` — executive summary and inventory of all five dashboards
- `plans.html` — dated seven-night hotel snapshots with source links and room/tax/cancellation caveats; values are not live quotes or directly comparable
- `social.html` — cross-plan social register with official venue sources and blank hours/costs flagged
- `questions.html`, `suggestions.html`, `flagged.html`, `sources.html` — decision register, proposals, irregularities and audit trail
- `data/*.json` — page data
- `tools/build.py` — regenerates all pages; `tools/check.py` — local-link and source-field checks

```bash
python3 integration-2027/tools/build.py && python3 integration-2027/tools/check.py
```

The final integration update added the later dual-city planner (`china-2027/`) and corrected stale inventory and holiday-source statements. The dual-city page's $425 Beijing and $621 Shanghai examples are **separate 7-night city alternatives**, not a combined multi-city trip price; each is a dated Booking.com snapshot, excludes VAT, and has different cancellation terms. The State Council holiday notice is linked directly on the questions/flagged pages. This update did not re-quote prices, edit source-plan datasets, or certify that inherited external pages remain unchanged.

Verification rule: videos enter the cross-plan index only after the linked watch page was read; venue hours, meal costs and other values are blank unless an official source is provided. Inherited source-plan data stays attributed to its original page and date.

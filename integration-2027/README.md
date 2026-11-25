# China 2027 decision layer (session `815c7943`)

A static, dependency-free integration site at `integration-2027/`. It does **not** replace any of the four plans.

- `index.html` — executive summary and the four plans side by side
- `plans.html` — dated seven-night price snapshots with each owning session's source
- `social.html` — 19 social pages fetched and read this session, with official venue links, blank hours/costs flagged
- `questions.html`, `suggestions.html`, `flagged.html`, `sources.html` — decision register, unimplemented proposals, full blank register and audit trail
- `data/*.json` — single source for each page
- `tools/build.py` — regenerates all pages; `tools/check.py` — local-link and source-field checks

```bash
python3 integration-2027/tools/build.py && python3 integration-2027/tools/check.py
```

Verification rule: a video enters the index only after its watch page was read; a venue cell is blank unless an
official source was read by this session or an earlier session's dated source link is explicitly marked inherited.

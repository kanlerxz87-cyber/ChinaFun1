# China, considered

Static, evidence-first China trip planner for two adults, 15 February–23 March 2027. The website consists of `index.html`, category pages and `assets/style.css`; it works without JavaScript. Research is a limited shortlist, not a complete hotel ranking. Unverified rates, routes and other missing information are flagged on the site instead of being invented.

## Rebuild and check

Requires Python 3; no external dependencies or build service.

```sh
python3 build.py
python3 tests/check_site.py
python3 -m http.server 8000
```

Visit `http://localhost:8000/`. Commit regenerated HTML alongside changes to `build.py`. Official source and checking notes appear on the Flagged for Review page and in `data/verification-log.md`. GitHub Pages serves the repository root. External links can change or require authentication or regional access; a successful local link check is not a promise about external availability.

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

## Publication status

The repository's existing Pages site uses `main`; this project is on `arena/b111cd10-chinafun1`. Publication has **not** succeeded. Changing the Pages source and adding this branch to the `github-pages` environment policy both returned HTTP 403 from the GitHub integration. [Deployment attempt](https://github.com/kanlerxz87-cyber/ChinaFun1/actions/runs/45621706155) was rejected by the environment's main-only branch policy. A repository administrator needs to allow this branch for that environment and configure Pages to use GitHub Actions, then run the `Deploy trip planner` workflow.

# Lesson pages

Each lesson is one self-contained HTML page (no build step needed to open it).

- `src/template.html` — shared layout, styles and the small lesson engine (SVG charts from embedded data, quiz, practice checklist).
- `src/<id>.html` — the body of each lesson (`1-01.html` … `1-10.html`).
- `src/lessons.json` — lesson ids and titles. `src/urls.json` — each lesson's published artifact URL (used for prev/next links).
- `src/data/*.json` — real NSE/BSE series, made by `tools/prep_data.py` from the free daily dataset at github.com/aswinv90/indian-market-historical-data.

Build (from this folder): `python3 tools/build.py`. It writes `dist/<id>.html` (the file published as a private claude.ai artifact) and `../site/lessons/<id>.html` (the same page in a doctype skeleton, for this repo).

`tools/shot.js` and `tools/el.js` take Playwright screenshots for layout checks.

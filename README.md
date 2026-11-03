# Learn stock market

A private, self-paced course that takes a complete beginner to expert level in the Indian stock market (NSE/BSE), with short-term swing trading as the main focus. Futures and options are covered to understand them, never to trade them.

The course outline lives in the [curriculum doc](https://claude.ai/artifact/56icvrSfDii52S12ZcVftY): 6 levels, 63 lessons, about 9 to 12 months at an hour a day.

## What's here

| Path | What it is |
| --- | --- |
| `docs/curriculum.md` | The approved curriculum, exported from the curriculum doc. |
| `site/index.html` | The course hub: level map, lesson navigation, progress tracker and glossary. One self-contained file, no build step. |

## Run it locally

Open `site/index.html` in a browser, or serve the folder:

```bash
cd site && python3 -m http.server 8000
# then open http://localhost:8000
```

Progress is saved in your browser's local storage when run locally. When the same page runs as a claude.ai artifact, it also saves to the artifact's database so progress follows you across devices.

## Adding a lesson

Lessons are written level by level as separate pages. When one is ready, add its link to `LESSON_URLS` near the top of the script in `site/index.html`, keyed by lesson id (for example `"1.01"`).

## Privacy

This repo is private. Don't enable GitHub Pages: Pages sites on most plans are public even when the repo is private, and the live broker data used from Level 4 is licensed for personal use only.

# content-creation-playbook

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tips](https://img.shields.io/badge/tips-110%20total-0F766E)](#whats-inside)
[![Master list](https://img.shields.io/badge/master%20list-50%20ways-B45309)](pdf/00-master-50-ways.pdf)
![Format](https://img.shields.io/badge/format-LaTeX%20PDF-informational)
![Scope](https://img.shields.io/badge/sources-2026%20web%20research-blueviolet)

A concise, research-backed playbook for improving content creation, delivered as six
typeset LaTeX PDFs: one master list of **50 cross-cutting ways** to improve, plus a
**12-tip guide for each major content type**. Every tip is a single actionable sentence;
every PDF ends with its source list (4–6 current 2026 creator guides, platform-data
studies, and craft manuals each).

## What's inside

| PDF | Focus | Tips |
|---|---|---|
| [00 — Master list](pdf/00-master-50-ways.pdf) | Cross-cutting playbook, 8 categories | 50 |
| [01 — Video & YouTube](pdf/01-video-youtube.pdf) | Long-form video: hooks, retention loops, chapters | 12 |
| [02 — Writing, blogging & newsletters](pdf/02-writing-blogging-newsletters.pdf) | Articles & email: scannability, CTAs, cadence | 12 |
| [03 — Podcasting & audio](pdf/03-podcasting-audio.pdf) | Recording, structure, editing workflow | 12 |
| [04 — Social & short-form](pdf/04-social-short-form.pdf) | TikTok / Reels / Shorts: the 3-second hook economy | 12 |
| [05 — Visual design & thumbnails](pdf/05-visual-design-thumbnails.pdf) | Thumbnails & covers: composition, light, contrast | 12 |

## The master list, category by category

The 50 cross-cutting tips are grouped into 8 categories that map to a content piece's
life cycle:

- **Strategy & positioning (7)** — niche down to one sentence, pick 3–5 content pillars,
  hyper-specify your audience, write the title before the content, keep a running idea backlog.
- **Craft & storytelling (8)** — hook first/context second, front-load the payoff
  (25–40% rule), open a loop every 60–90 seconds, the so-what test, micro-payoffs.
- **Production quality (7)** — fix audio before video, light simply, rule of thirds,
  test clips before full takes, batch production, cut every dead pause.
- **Packaging (6)** — one dominant subject, 3–4 word text limit, preview at thumbnail size,
  lock a two-color visual brand.
- **Distribution & repurposing (7)** — fixed cadence, repurpose long → short, optimize per
  platform, build the email list, SEO/AEO basics.
- **Engagement & community (5)** — one CTA per piece, mine comments, feature your audience.
- **Analytics & iteration (5)** — weekly reviews, track saves/shares over likes,
  A/B test one variable, read retention curves by timestamp, kill your bottom third.
- **Systems & sustainability (5)** — calendar slack, AI for structure/humans for facts,
  media kit, protect the creator, ship before it's perfect.

## Highlights from each type guide

**Video & YouTube** — the retention architecture:
- Hook in the first 5–10 seconds that delivers the title's exact promise
- Visual proof anchor within 10 seconds (show the result, then explain)
- Pattern interrupts every 30–60 seconds; re-hooks every 60–90 seconds
- Front-load value by the 25–40% mark; timestamped chapters; film two hooks and
  compare retention at 48 hours (aim 70%+ at the 30-second mark)

**Writing, blogging & newsletters** — the skim-proof draft:
- Headline/subject line first: specific and curiosity-honest, never clickbait
- Paragraphs of 2–3 sentences; newsletters under 300–500 words with one primary CTA
- Bold every unclear term and hyperlink the explanation; curate ruthlessly —
  depth on two topics beats surface coverage of ten
- Segment the list by interest and engagement; A/B test subject lines one variable at a time

**Podcasting & audio** — fix the room, then the structure:
- Record in a soft room (the closet trick), mic 4–6 inches off-axis, pop filter, headphones always
- Cold-open with the episode's best 15–30 seconds; intro under 60 seconds
- Re-order for narrative, not chronology; content edit *before* EQ/compression;
  target −16 LUFS for stereo delivery

**Social & short-form** — a hook economy:
- The first 3 seconds drive most completion variance — write 20 hooks before filming one video
- Script three beats: hook (0–3 s) → proof (3–30 s) → payoff/CTA (last 5 s)
- Completion beats duration: a 45-second video at 70% completion beats 15 seconds at 40%
- Saves are 2–3× more valuable than likes; post 3–7×/week; strip watermarks when repurposing

**Visual design & thumbnails** — design for the 120-pixel preview:
- One dominant subject filling 30–60% of the frame, high-contrast background separation
- Flat, even light on faces — add drama in post, fix underexposure never
- The 3-element rule (face + object + short text), 2–3 colors max, ≤4 words of bold outlined text
- Preview at thumbnail size before publishing; change one design variable per test

## Why these tips

Each document was compiled from targeted web research in October 2026 across the
respective domain — creator-economy guides, platform-data analyses (completion-rate and
cadence studies for TikTok/Reels/Shorts, retention-curve research for YouTube), and
craft manuals. Sources are printed at the end of every PDF. No tip made the list
without a source behind it.

## Rebuilding

```bash
python3 build_pdfs.py     # regenerates tex/ and compiles all 6 PDFs (pdflatex ×2 passes each)
```

- Requires TeX Live with `tcolorbox`, `titlesec`, `enumitem`, `booktabs`, `amssymb`, `hyperref`
- `build_pdfs.py` is the single source of truth — all tips live in its Python data
  structures; `tex/` and `pdf/` are generated artifacts
- Verified: master list numbers 1–50 across 4 pages; each type guide numbers 1–12 across 2 pages

## License

MIT — see [LICENSE](LICENSE).

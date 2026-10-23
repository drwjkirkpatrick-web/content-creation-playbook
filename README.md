# content-creation-playbook

A concise, research-backed playbook for improving content creation — as a set of
typeset LaTeX PDFs, one per major content type.

![Type](https://img.shields.io/badge/type-web--research%20playbook-blue)
![Format](https://img.shields.io/badge/format-LaTeX%20PDF-orange)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## What's inside

| PDF | Content | Tips |
|---|---|---|
| [`pdf/00-master-50-ways.pdf`](pdf/00-master-50-ways.pdf) | Cross-cutting playbook (8 categories: strategy, storytelling, production, packaging, distribution, community, analytics, sustainability) | 50 |
| [`pdf/01-video-youtube.pdf`](pdf/01-video-youtube.pdf) | Long-form video / YouTube — hooks, retention loops, chaptering | 12 |
| [`pdf/02-writing-blogging-newsletters.pdf`](pdf/02-writing-blogging-newsletters.pdf) | Blogs, articles, email newsletters — scannability, CTAs, cadence | 12 |
| [`pdf/03-podcasting-audio.pdf`](pdf/03-podcasting-audio.pdf) | Podcasts — recording, structure, editing workflow | 12 |
| [`pdf/04-social-short-form.pdf`](pdf/04-social-short-form.pdf) | TikTok / Reels / Shorts — the 3-second hook economy | 12 |
| [`pdf/05-visual-design-thumbnails.pdf`](pdf/05-visual-design-thumbnails.pdf) | Thumbnails, covers, social imagery — composition and light | 12 |

Every tip is one actionable sentence. Every PDF ends with its source list —
each document is compiled from 4–6 current (2026) creator guides, platform-data
studies, and craft manuals.

## Rebuilding

```bash
python3 build_pdfs.py     # regenerates tex/ and compiles all 6 PDFs (pdflatex ×2 passes each)
```

Requires TeX Live with `tcolorbox`, `titlesec`, `enumitem`, `booktabs`, `amssymb`.

## Structure

- `build_pdfs.py` — content corpus + LaTeX generator (single source of truth; edit tips here)
- `tex/` — generated `.tex` sources
- `pdf/` — compiled PDFs

## License

MIT — see [LICENSE](LICENSE).

# Project State: content-creation-playbook

> **Last updated:** 2026-10-23
> **Current phase:** done (v1.0)
> **Overall health:** green

---

## 1. Goal (1–2 sentences)
A research-backed, typeset playbook for improving content creation: one master list of
50 cross-cutting tips plus per-type guides (video, writing, podcasting, short-form social,
visual design), delivered as LaTeX-compiled PDFs.

## 2. Current Status
### Done
- [x] Web research across 6 domains (general creation, video/YouTube, writing/newsletters,
      podcasting, short-form social, visual design/thumbnails)
- [x] Content corpus: 50 master tips (8 categories) + 12 tips × 5 type-specific docs
- [x] LaTeX generator `build_pdfs.py` (tcolorbox/titlesec styling, per-doc source lists)
- [x] All 6 PDFs compiled and verified (master numbered 1–50; type docs 12 each)
- [x] GitHub repo created and pushed

### Not Started
- (none — possible future: per-type expansion to 20 tips each, EPUB/HTML versions)

## 3. Architecture & Key Decisions
| Decision | Rationale | Date |
|---|---|---|
| Single `build_pdfs.py` as source of truth | Tips live in Python data structures; tex/ and pdf/ are generated artifacts | 2026-10-23 |
| pdflatex + tcolorbox/titlesec styling | Available in system TeX Live 2022; no font/diacritic needs → no xelatex required | 2026-10-23 |
| Sources embedded per PDF | Every doc traceable to its research; no floating claims | 2026-10-23 |

## 4. Blockers & Risks
- None open. (Note: `amssymb` needed for ▶ labels; tcolorbox + hyperref need two pdflatex passes.)

## 5. Next Step (only ONE)
> **Next:** None — v1.0 shipped. Revisit if tips need updating against newer platform data.

## 6. Environment & Tooling Notes
- pdflatex (TeX Live 2022/dev/Debian), pdfTeX 3.141592653-2.6
- Python 3 stdlib only for the generator
- Repo: https://github.com/drwjkirkpatrick-web/content-creation-playbook (public, main)

## 7. Recent Session Log
- 2026-10-23: Researched 6 content domains, built generator, compiled 6 PDFs (110 tips total), published to GitHub.

## 8. References
- Generator: `build_pdfs.py`
- Sources: embedded per-PDF in the `Sources` section

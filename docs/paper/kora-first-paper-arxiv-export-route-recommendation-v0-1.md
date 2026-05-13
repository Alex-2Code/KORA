# KORA First Paper arXiv Export Route Recommendation v0.1

Status date: 2026-05-13

## Purpose

This recommendation summarizes the safest export route after the v0.5 dry run. It does not select a final arXiv category, does not submit to arXiv, does not create a final source package, and does not mark the paper as submission-ready.

## Recommended Route

Recommended route: Pandoc-to-LaTeX starting export with manual source-package cleanup.

Rationale:

- `pandoc` is available locally and successfully converts manuscript v0.5 from Markdown to LaTeX in `/tmp`.
- Direct PDF generation is blocked locally because no LaTeX engine is installed.
- Mermaid diagrams need explicit conversion or replacement before an arXiv-compatible package.
- Wide Markdown tables need final layout review before PDF generation.
- A manual LaTeX cleanup pass keeps figure, table, citation, and artifact-package decisions visible before submission.

## Fallback Route

Fallback route: HTML or GitHub-rendered Markdown review only.

This route can support human review of content and structure, but it should not be treated as the arXiv source-package route.

## Required Next Steps

1. Confirm final arXiv category and category compatibility.
2. Confirm arXiv license.
3. Choose Mermaid handling:
   - render Figure 1 and Figure 2 to approved figure assets,
   - convert diagrams to LaTeX/TikZ manually, or
   - replace diagrams with ASCII/text diagrams if source simplicity is preferred.
4. Convert wide tables to layout-safe LaTeX tables or simplified text tables.
5. Convert the preliminary BibTeX subset into the final package bibliography format.
6. Generate a clean PDF/source package in a temporary or package-specific area.
7. Run final human review before any upload.

## BibTeX Handling

The export route should use the conservative bibliography subset already aligned with manuscript v0.5. Full BibTeX remains incomplete, and deferred or still-not-eligible records should not be introduced during export cleanup.

## Source Package Contents

Expected source package inputs, pending final approval:

- Manuscript source derived from `docs/paper/kora-first-paper-manuscript-v0-5.md`.
- Finalized bibliography subset derived from `docs/paper/kora-first-paper-preliminary-bibtex-v0-1.md`.
- Approved figure sources or rendered figure files for Figure 1 and Figure 2.
- Layout-safe versions of Table 1, Table 2, and Appendix Table A1.
- Artifact/reproducibility appendix content.
- No raw benchmark artifacts.
- No provider responses, API keys, private user data, production traffic, release assets, or generated temporary evidence packets.

## No-Submit Status

No arXiv submission was made. No final source package was created. No PDF or binary figure output was committed.

## Submission Status

The recommended export route is identified, but final category, license, figure conversion, table layout, bibliography formatting, source-package generation, and human review remain pending. The paper remains not submission-ready.

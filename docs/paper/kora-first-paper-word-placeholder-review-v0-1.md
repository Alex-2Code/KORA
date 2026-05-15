# KORA First Paper Word Placeholder Review v0.1

Status date: 2026-05-15

## Purpose

This report records the cleanup of the Word review draft after human review found that the inserted figure images did not render correctly. The Word-first review route continues with text placeholders for Figure 1 and Figure 2. PDF and arXiv source-package work remain paused. The paper remains not submission-ready.

## Source Manuscript

- `docs/paper/kora-first-paper-manuscript-v0-5.md`

The repository manuscript was preserved. A local-only working Markdown copy was created for Word review.

## Local Output Root

Generated outputs were written under the local-only generated paper output root:

```text
generated_paper_outputs/word_draft_v0_5_placeholders/
```

This directory is outside the public KORA repository and is not tracked.

## Placeholder Word Output

| Output | Status | Approximate size | Committed |
|---|---|---:|---:|
| `kora-first-paper-manuscript-v0-5-word-review-placeholders.docx` | generated | 21,877 bytes | no |
| `kora-first-paper-manuscript-v0-5-word-review-placeholders.md` | generated local working copy | 28,466 bytes | no |

The placeholder Word draft contains no embedded media files.

## Placeholder Text

Figure 1 placeholder:

```text
[Figure 1 placeholder: KORA execution-control architecture. Final publication-quality figure to be inserted after manuscript body review.]
```

Figure 2 placeholder:

```text
[Figure 2 placeholder: Direct baseline vs KORA-controlled deterministic-heavy benchmark flow. Final publication-quality figure to be inserted after manuscript body review.]
```

## Reason for Switching to Placeholders

Human review found that arrows in the inserted figure images were broken. The current figure images are not being forced into the Word draft. The goal is to keep manuscript-body review moving while deferring final figure creation.

## Figure Status

| Figure | Current status | Next action |
|---|---|---|
| Figure 1: KORA execution-control architecture | deferred | Recreate publication-quality figure after manuscript body finalization |
| Figure 2: direct baseline vs KORA-controlled deterministic-heavy benchmark flow | deferred | Recreate publication-quality figure after manuscript body finalization |

Previous redesigned figures are not accepted for publication use. They are superseded by placeholders for Word review.

## Verification

- Word generation passed.
- Placeholder DOCX contains both Figure 1 and Figure 2 placeholder text.
- Placeholder DOCX contains no embedded media.
- No PDF was generated.
- No generated DOCX, local Markdown working copy, PDF, image, source package, or binary output was committed.

## Remaining Review Items

- Review manuscript body using the placeholder Word draft.
- Review Table 1, Table 2, Algorithm 1, and Appendix Table A1 in Word.
- Finalize publication-quality figures only after manuscript-body review.
- Resume PDF/arXiv source-package work only after Word review and figure decisions are complete.

## Status

Word-first review continues with placeholders. Figure insertion is not complete. Final figure creation is deferred. The paper remains not submission-ready.

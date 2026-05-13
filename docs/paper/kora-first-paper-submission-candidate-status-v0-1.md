# KORA First Paper Submission-Candidate Status v0.1

Status date: 2026-05-13

## Purpose

This status note records the bundled manuscript synchronization and claim-to-evidence pass that produced manuscript v0.4 as a submission-candidate draft. It does not mark the paper as submission-ready.

## Manuscript v0.4

Manuscript v0.4 was created:

- `docs/paper/kora-first-paper-manuscript-v0-4.md`

v0.4 is a submission-candidate draft, not a final submission package.

## Manuscript v0.5

Manuscript v0.5 was created:

- `docs/paper/kora-first-paper-manuscript-v0-5.md`

v0.5 is a submission-candidate draft that mechanically inserts the prior figure, table, algorithm, and appendix artifact materials into the manuscript. It is not a final submission package.

## What Was Synchronized

- Manuscript citations were compared against preliminary BibTeX v0.1.
- Manuscript v0.3 cited `[R02]`, which remains still-not-eligible and absent from preliminary BibTeX.
- Manuscript v0.4 removes `[R02]` from background-only text and the preliminary references section.
- Manuscript v0.4 now cites only records currently present in preliminary BibTeX.
- Preliminary BibTeX still has 16 entries.
- Unused preliminary BibTeX entries remain `[R14]`, `[R16]`, `[R21]`, and `[R24]`.

## Claim Wording

The bounded claim is preserved:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

No production, API-cost, energy, broad superiority, formal approval, or submission-readiness claim was added.

## Remaining Required Blockers

- Full BibTeX remains incomplete.
- `[R02]`, `[R15]`, `[R19]`, `[R20]`, `[R22]`, and `[R23]` remain still-not-eligible.
- `[R17]` and `[R18]` remain deferred.
- Final citation style conversion and final bibliography formatting remain pending.
- Final manuscript-to-final-BibTeX synchronization remains pending.
- Final claim-to-evidence audit must be repeated after any future manuscript or bibliography changes.
- Final figures and tables are not locked.
- Final export package is not prepared.
- Clean reproduction transcript and artifact package review remain pending.
- Final human review remains pending.

## User Approval Still Needed

- Target venue or target package format.
- Whether `[R17]` and `[R18]` should be included or excluded once venue direction is known.
- Whether benchmark-methodology records `[R19]` through `[R24]` should be integrated into the manuscript methodology section.
- Whether optional workload, latency, API-cost, production-traffic, or energy work stays out of the first submission scope.

## Target Venue, Export, and Package Decisions

The first target package direction is arXiv-style technical report / preprint. Endorsement has been obtained and is not a current blocker. arXiv category compatibility, license, export format, and final human approval remain pending. No conference, workshop, or journal target has been selected.

## arXiv-Style Package Draft

The arXiv-style package draft docs now exist:

- `docs/paper/kora-first-paper-arxiv-metadata-checklist-v0-1.md`
- `docs/paper/kora-first-paper-arxiv-bibliography-scope-v0-1.md`
- `docs/paper/kora-first-paper-arxiv-style-package-readiness-v0-1.md`
- `docs/paper/kora-first-paper-future-venue-scan-v0-1.md`

These files record the supplied author metadata, endorsement status, conservative bibliography scope, original systems/evaluation framing, and future venue-scan placeholder. They do not submit to arXiv, select an arXiv category, select a conference/workshop/journal, or mark the paper as submission-ready.

## Figure, Table, and Algorithm Asset Pass

The figure/table/algorithm asset pass now exists:

- `docs/paper/kora-first-paper-figure-table-algorithm-plan-v0-1.md`
- `docs/paper/kora-first-paper-figure-table-algorithm-drafts-v0-1.md`

These files inventory existing visual assets, draft paper-ready text diagrams, benchmark tables, an evidence-boundary table, deterministic-first routing pseudocode, and an appendix artifact inventory table. Manuscript v0.4 was not edited in this pass; final insertion, numbering, layout, and export treatment require human review.

## Manuscript Asset Insertion Pass

Manuscript v0.5 now inserts:

- Figure 1: KORA execution-control architecture.
- Figure 2: direct baseline vs KORA-controlled benchmark flow.
- Table 1: deterministic-heavy benchmark result summary.
- Table 2: evidence boundary and non-claim table.
- Algorithm 1: deterministic-first routing pseudocode.
- Appendix Table A1: artifact and reproducibility inventory.

The inserted assets remain draft Markdown/Mermaid/text assets. Final rendering, numbering, layout, and export treatment remain pending.

## Submission Package Packet

The venue-neutral submission package readiness packet now exists:

- `docs/paper/kora-first-paper-submission-package-readiness-v0-1.md`
- `docs/paper/kora-first-paper-final-human-review-packet-v0-1.md`
- `docs/paper/kora-first-paper-reproduction-transcript-checklist-v0-1.md`
- `docs/paper/kora-first-paper-artifact-package-inventory-v0-1.md`

These files organize package blockers, human review decisions, reproduction transcript expectations, and artifact inventory. They do not select a venue, finalize an export package, or mark the paper as submission-ready.

## Status

The manuscript has advanced to v0.5 submission-candidate draft status. Full BibTeX remains incomplete, final asset rendering/export review remains pending, and the paper remains not submission-ready.

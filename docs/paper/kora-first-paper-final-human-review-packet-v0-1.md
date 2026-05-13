# KORA First Paper Final Human Review Packet v0.1

Status date: 2026-05-13

## Purpose

This packet lists the human decisions still required before any submission-ready decision. It does not answer those decisions and does not mark the paper as submission-ready.

## Source Files Reviewed

- `docs/paper/kora-first-paper-manuscript-v0-4.md`
- `docs/paper/kora-first-paper-submission-package-readiness-v0-1.md`
- `docs/paper/kora-first-paper-submission-candidate-status-v0-1.md`
- `docs/paper/kora-first-paper-final-bibliography-claim-audit-v0-1.md`
- `docs/paper/kora-first-paper-submission-readiness-gate-v0-1.md`
- `docs/paper/kora-first-paper-manuscript-claim-to-evidence-audit-v0-1.md`
- `docs/paper/kora-first-paper-manuscript-bibliography-sync-v0-1.md`
- `docs/paper/kora-first-paper-preliminary-bibtex-v0-1.md`

## Review Checklist

| Review item | Human decision needed | Current status |
|---|---|---|
| Title and abstract | Approve final wording or request edits | Pending |
| Claim boundary | Approve the bounded deterministic-heavy benchmark claim | Pending |
| Bibliography scope | Confirm the conservative first arXiv-style package scope | Draft scope supplied; final approval pending |
| Limitations | Approve limitations and non-claim language | Pending |
| Artifact and reproducibility | Approve artifact package scope and reproduction transcript expectations | Pending |
| Figures, tables, and algorithm | Approve final diagrams, tables, pseudocode, captions, numbering, and placement | Draft assets exist; final approval pending |
| Author and affiliation metadata | Approve final author block, affiliation, and email display | Draft metadata supplied; final approval pending |
| Acknowledgement, funding, conflict, and ethics metadata | Approve minimal required disclosure text if any | Pending |
| Target venue and export format | Confirm arXiv category, license, and export route | arXiv-style direction supplied; details pending |
| Final submission-ready decision | Decide whether the exact final package is ready to submit | Pending |

## Bibliography Scope Decisions

- Current arXiv-style draft decision: `[R17]` and `[R18]` remain excluded from the first arXiv-style package.
- Current arXiv-style draft decision: `[R19]` through `[R24]` remain tracker/audit-only for now.
- Current arXiv-style draft decision: optional workload, latency, API-cost, production, energy, KORA Studio, and real customer-data evidence stay outside first package scope.
- Deferred and still-not-eligible records should remain excluded from manuscript body citations unless later resolved.
- Confirm that no missing metadata should be filled without source-backed verification.

## Evidence Scope Decisions

- Decide whether optional expanded workload evidence stays outside the first submission scope.
- Decide whether latency p50/p95 evidence stays outside the first submission scope.
- Decide whether API-cost, production-traffic, energy, and real customer-data studies stay outside the first submission scope.
- Decide whether KORA Studio discussion remains outside the first submission scope.

## Figure, Table, and Algorithm Decisions

- Decide whether Figure 1 and Figure 2 should use Mermaid-rendered diagrams, exported graphics, or text/ASCII form.
- Decide whether Table 1 replaces or augments the existing deterministic-heavy benchmark table in manuscript v0.4.
- Decide whether Table 2 belongs in the main text, limitations, or appendix.
- Decide whether Algorithm 1 belongs in Section 3 or an appendix.
- Decide whether the appendix artifact inventory table should be included in the arXiv-style package or kept as reviewer-support material.
- Confirm final numbering and captions after export format is selected.

## Venue and Export Decisions

- Current direction: arXiv-style technical report / preprint first.
- Endorsement status: already obtained / not blocking.
- arXiv category compatibility remains pending because the endorsed category is not recorded here.
- Later conference, workshop, or journal scanning is deferred and should not select a target in the current package draft.
- Approve whether export preparation should proceed after category, license, bibliography formatting, and figures/tables are stable.

## Claim Boundary Reminder

The current safe claim is:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

This packet does not approve stronger claims about production cost reduction, real API-cost reduction, production benchmark proof, broad workload superiority, energy reduction evidence, formal government validation, signed partner validation, guaranteed adoption or funding, or formal artifact approval.

## Signoff Status

No final human signoff is recorded in this document. The paper remains not submission-ready until the pending decisions above are explicitly resolved and the exact final package is reviewed.

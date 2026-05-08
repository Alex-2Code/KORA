# KORA OSS Operating System v0.1

Date: `2026-05-06`

## Purpose

KORA's goal is to grow into a category-building OSS infrastructure project.

GitHub is the operating HQ, not just code storage.

KORA should support development, community, paper, EIC, investor, partner, and grant readiness from one evidence base.

## OSS Ambition

KORA aims to define the AI Execution Control Layer category.

KORA uses the vision phrase "Inference OS for AI systems."

vLLM may be used as an analogy for category ambition, but KORA must not claim it has achieved vLLM-level adoption.

## GitHub Feature Map

| Feature | KORA use |
|---|---|
| README | Public front door, quickstart, category framing, and current official repo note. |
| Issues | Concrete tasks, bug reports, docs work, benchmark feedback, community follow-up, and claim-sensitive review requests. |
| Labels | Routing layer for area, role, difficulty, review status, claim sensitivity, and evidence type. |
| Projects | Shared operating boards for core development and community/evidence operations. |
| Discussions | Community Q&A, announcements, ideas, use cases, contributor onboarding, and benchmark result discussion. |
| Wiki | Beginner-friendly onboarding and handbook material. |
| Pull Requests | Reviewable implementation and documentation changes. |
| Releases | Versioned public release notes and bounded evidence summaries. |
| Milestones | Release and evidence-cycle grouping. |
| Actions | Automated tests, checks, and future benchmark validation workflows. |
| Security | Responsible handling of security reports and sensitive areas. |
| CODEOWNERS | Future ownership routing for review responsibility. |
| Issue templates | Structured intake for community tasks, content review, partner leads, bugs, and docs. |
| PR templates | Future standard checklist for validation, claim safety, and review ownership. |

## Operating Tracks

| Track | Owner type | Primary artifacts | GitHub tools used | Review requirements |
|---|---|---|---|---|
| CORE | Technical owner | Code, tests, examples, architecture docs | Issues, PRs, Actions, Projects, Milestones | Technical review; claim-sensitive docs require Albert review |
| PAPER | Research owner | Technical reports, benchmark reports, authorship policy | Issues, Discussions, PRs, docs/paper | Albert review for claims, authorship, and evidence wording |
| EIC | Narrative owner | Grant-ready summaries, evidence packets, roadmap docs | Issues, Projects, docs/claims | Review required |
| INVESTOR | Narrative owner | Intro language, evidence summaries, category thesis | docs/claims, Issues | Review required |
| PARTNER | Ecosystem owner | Lead notes, use cases, pilot candidates, LOI candidates | Issues, Discussions, Projects | Albert review for external wording |
| COMMUNITY | Community owner | Discussions, open roles, weekly sync issues, feedback summaries | Issues, Discussions, Projects, docs/community | Claim-sensitive content requires Albert review |
| OPS | Operations owner | Weekly reports and board hygiene | Projects, Issues, docs/ops | Keep internal/private boundaries clear |

## GitHub Projects Model

Recommended project board: `KORA Core Development`

Recommended columns:

- Backlog
- Ready
- In Progress
- Needs Review
- Blocked
- Done

Recommended project board: `KORA Community & Evidence Ops`

Recommended columns:

- Backlog
- Ready
- In Progress
- Needs Albert Review
- Approved
- Published / Done
- Blocked

## Labels Model

Area:

- `area:core`
- `area:docs`
- `area:benchmark`
- `area:examples`
- `area:community`
- `area:paper`
- `area:ops`

Role:

- `role:early-builder`
- `role:benchmark-runner`
- `role:docs-contributor`
- `role:example-builder`
- `role:ai-assisted`
- `role:moderator`
- `role:research`

Difficulty:

- `good first issue`
- `difficulty:easy`
- `difficulty:medium`
- `difficulty:advanced`

Review:

- `needs-review`
- `needs-albert-review`
- `approved`

Status:

- `blocked`
- `ready`
- `in-progress`
- `done`

Claim sensitivity:

- `claim-sensitive`
- `claim-safe`

Evidence type:

- `evidence:benchmark`
- `evidence:runtime`
- `evidence:feedback`
- `evidence:case-study`
- `evidence:partner-interest`

## Issue Triage Workflow

1. Intake the issue or external signal.
2. Apply area, role, difficulty, status, and claim-sensitivity labels.
3. Assign an owner or mark owner needed.
4. Clarify done criteria.
5. Link to `docs/claims/` if claim-sensitive.
6. Move through the relevant project board.
7. Close with evidence, merged PR, linked discussion, or follow-up issue.

## PR Workflow

- Use branch names like `task###_short_scope`.
- Keep PRs small and reviewable.
- Run validation commands appropriate to scope.
- Name the review owner.
- Do not push directly to `main`.
- Claim-sensitive docs require Albert review.
- PRs should explain files changed, validation run, and claim-safety status.

## Discussions Workflow

Recommended categories:

- Announcements
- Q&A
- Benchmark Results
- Use Cases
- Ideas
- Contributors
- Research & Paper

Discussions are for open-ended conversation. Issues are for owned work with done criteria.

## Wiki Workflow

The Wiki is for beginner-friendly onboarding and handbook material.

Official claim, evidence, release, and operating docs live in the repository under `docs/` so they can be reviewed through PRs.

## Evidence Intake Workflow

Benchmark results, user feedback, use cases, and partner interest should not remain only in Telegram, social media, email, or direct conversations.

Route evidence into GitHub:

- Benchmark result -> Discussion or Issue, then reviewed docs if useful.
- User feedback -> Discussion or Issue.
- Use case -> Discussion, Issue, or docs/community summary.
- Partner interest -> partner-lead issue template or private tracker if sensitive.
- Claim-sensitive evidence -> link to `docs/claims/` and request Albert review.

## Weekly Cadence

- Weekly community sync issue.
- Weekly metrics snapshot.
- Weekly Albert review queue.
- Monthly OSS report.
- EOD/SOD internal context flow.

## Public / Private Boundary

- Public repo docs are public-facing unless clearly marked internal.
- Personal data and resumes should not be posted in public issues.
- Partner or government interest should not be overstated.
- Internal EOD/SOD prompts are internal operating artifacts.

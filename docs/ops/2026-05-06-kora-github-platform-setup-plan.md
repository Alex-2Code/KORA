# KORA GitHub Full-Platform Setup Plan

Date: `2026-05-06`

## Purpose

GitHub is KORA's OSS operating HQ.

This plan defines what should be configured manually on GitHub versus what should live in the repository.

The plan supports development, community, research, EIC/grant readiness, investor readiness, and partner readiness from one shared evidence base.

## Setup Phases

Phase 1: Essential OSS operating foundation.

- Issues, labels, basic project boards, PR workflow, and core docs links.

Phase 2: Community and research activation.

- Discussions, Wiki onboarding, community roles, benchmark feedback intake, and paper/research contribution routing.

Phase 3: Automation and quality gates.

- GitHub Actions for smoke checks, docs checks, claim scanning, and benchmark command checks.

Phase 4: Governance and scale.

- CODEOWNERS, branch protections, maintainer roles, security process, release governance, and contributor programs.

## GitHub Feature Map

| Feature | Purpose | Owner | Public/private boundary | Setup method |
|---|---|---|---|---|
| README | Public front door and quickstart. | Albert / maintainers | Public | Repo file |
| Issues | Track actionable work and feedback. | Track owners | Public unless sensitive | GitHub UI + templates |
| Labels | Route issues and PRs. | Ops coordinator / maintainers | Public | GitHub UI; documented in repo |
| Projects | Coordinate work status. | Track owners | Public or private by board | GitHub UI |
| Discussions | Community Q&A, ideas, and feedback. | Community lead | Public | GitHub UI |
| Wiki | Beginner handbook and onboarding. | Community/ops | Public if enabled | GitHub UI |
| Pull Requests | Review code and docs before merge. | Maintainers | Public | GitHub native |
| PR template | Standardize validation and review. | Maintainers | Public | Repo file |
| CODEOWNERS | Route required reviews later. | Maintainers | Public | Repo file |
| Milestones | Group release and evidence cycles. | Maintainers | Public | GitHub UI |
| Releases | Publish versioned release notes. | Albert / release owner | Public | GitHub UI / gh |
| Actions | Automate quality checks. | Technical owner | Public check results | Repo files |
| Security | Receive and track sensitive reports. | Security owner | Private where needed | GitHub UI |
| Insights | Observe project activity. | Maintainers | Repo-visible metrics | GitHub native |

## Recommended Project Boards

### KORA Core Development

Purpose:

- Track core code, tests, examples, benchmarks, releases, and technical docs.

Columns:

- Backlog
- Ready
- In Progress
- Needs Review
- Blocked
- Done

Issue types:

- bugs
- features
- tests
- examples
- benchmark work
- release docs

Owners:

- Albert and future technical maintainers.

Review cadence:

- weekly technical review
- release-cycle review before tags or releases

### KORA Community & Evidence Ops

Purpose:

- Track community, content, outreach, evidence intake, partner-interest routing, and claim-sensitive review.

Columns:

- Backlog
- Ready
- In Progress
- Needs Albert Review
- Approved
- Published / Done
- Blocked

Issue types:

- community tasks
- content review
- benchmark feedback
- partner leads
- discussion summaries
- weekly sync issues

Owners:

- Sumanta, ops coordinator, Albert for review-sensitive items.

Review cadence:

- weekly community sync
- weekly Albert review queue

## Manual Versus Repo-Managed Setup

| Setup type | Items |
|---|---|
| Manually configured in GitHub UI | enable Issues, enable Discussions, decide Wiki, create labels, create Projects, create milestones, review branch protection, review collaborator permissions |
| Tracked as repo files | README, issue templates, future PR template, future CODEOWNERS, Actions workflows |
| Tracked as docs only | label taxonomy, Discussions/Wiki plan, project board model, manual setup checklist |
| Future automation candidate | label sync, milestone creation, issue forms, project automation, claim-scan checks |

## Recommended Setup Order

1. Confirm Issues enabled.
2. Confirm Discussions enabled.
3. Confirm Wiki enabled if desired.
4. Create labels.
5. Create Project board.
6. Configure Discussions categories.
7. Add PR template.
8. Add CODEOWNERS later.
9. Add basic GitHub Actions later.
10. Create milestones.
11. Publish open roles / contributor docs links.

## Governance Notes

- Direct pushes to `main` should be avoided.
- Claim-sensitive files require Albert review.
- Partner/government/investor language requires Albert review.
- Releases and tags should be Albert-controlled until maintainers are added.
- Manual setup changes should be logged in a future GitHub setup log.

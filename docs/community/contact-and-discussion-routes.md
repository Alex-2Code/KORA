# Contact and Discussion Routes

## Purpose

This document defines where to ask questions, propose workloads, report bugs, raise security issues, and open pull requests for KORA.

## Current Status

- GitHub Issues are available for bugs and scoped work items.
- GitHub Discussions are the recommended future route for questions and workload proposals once enabled/configured.
- Until Discussions are enabled, contributors should use the documented issue templates or small scoped PRs.
- Security issues must follow [SECURITY.md](../../SECURITY.md).

## Recommended Routes

| Need | Recommended route | Current status |
|---|---|---|
| General question | GitHub Discussions Q&A | recommended once enabled |
| Workload proposal | GitHub Discussions Workload Proposals or workload proposal issue template | issue template available now; Discussions route pending |
| Bug report | GitHub Issues | available |
| Security issue | [SECURITY.md](../../SECURITY.md) | available |
| Small contribution | Pull Request | available |
| Good first issue candidate | [Good-first-issue candidate list](good-first-issue-candidates.md) | available as candidate list; issues not yet created |
| KORA Studio idea | Future discussion or issue after maintainer approval | planning only |

## Workload Proposals

Use the [workload proposal template](workload-proposal-template.md) for proposal structure.

The public issue template is available at [`.github/ISSUE_TEMPLATE/workload_proposal.md`](../../.github/ISSUE_TEMPLATE/workload_proposal.md).

Workload proposals must use synthetic or sanitized data only.

Do not include:

- secrets
- API keys
- private user/customer data
- proprietary datasets
- raw provider responses

Accepted proposals do not imply production validation, production cost reduction, real API-cost reduction, broad workload superiority, or energy reduction.

## Questions

Once GitHub Discussions are enabled, questions should go to Q&A.

Until then, use a small issue only if the question is tied to a bug, documentation problem, or concrete workload proposal.

## Bugs

Use GitHub Issues for bugs.

Include:

- reproduction steps
- expected behavior
- actual behavior
- command output where safe
- relevant environment details that do not expose secrets or private data

Do not include secrets, private data, raw provider responses, private machine details, or proprietary datasets.

## Security Issues

Security-sensitive reports must follow [SECURITY.md](../../SECURITY.md).

Do not open public issues for security-sensitive reports.

Do not post secrets or vulnerability details in public Discussions/issues.

## Pull Requests

Keep PRs small.

Use one concern per PR. Include tests or docs when relevant.

Avoid claim wording changes unless specifically requested. Do not add private internals content.

## Maintainer Review

Maintainers may redirect issues into discussions or PRs once Discussions are enabled.

Maintainers may close broad or unsafe proposals and ask for a smaller scoped contribution.

Benchmark and claim changes require maintainer review.

## Pending Setup

- Enable/configure GitHub Discussions.
- Decide initial Discussion categories.
- Convert selected good-first-issue candidates into real GitHub Issues.
- Confirm canonical public contact route in README.

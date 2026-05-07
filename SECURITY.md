# Security Policy

KORA is alpha / prerelease software. Security reports are welcome, but the project does not yet have a formal security response SLA.

For general, non-sensitive contribution flow, use [CONTRIBUTING.md](CONTRIBUTING.md).

## Reporting a security concern

Please do not open a public issue for sensitive security reports.

Private reporting route:

- Use GitHub private vulnerability reporting for this repository if it is enabled.
- If it is not enabled, contact the repository owner or maintainer directly.
- Maintainers should replace this placeholder with a project-specific private security contact before broad contributor outreach: `SECURITY_CONTACT_TO_BE_REPLACED_BY_MAINTAINERS`.

Include enough detail for maintainers to understand and reproduce the concern when possible:

- affected version or commit
- affected command, API, or file
- steps to reproduce
- expected security impact
- any suggested mitigation

## What to report privately

Security concerns may include:

- credential exposure
- unsafe command execution paths
- dependency vulnerabilities with exploitability
- release, tag, or signing concerns
- data leakage or artifact exposure
- unexpected model invocation or hidden external calls
- bypass of validation, budgets, or retry limits

## What can remain public

Use public GitHub issues for non-sensitive project work, such as:

- documentation typos
- non-sensitive bugs
- benchmark wording issues
- onboarding friction

Do not paste secrets, tokens, local absolute paths, private machine details, or sensitive reproduction material into public issues.

## Public disclosure

Please give maintainers time to review a sensitive report before publishing details publicly.

During alpha, maintainers will review reports as project capacity allows. Fixes may be handled as regular commits unless a coordinated disclosure process is needed.

## Artifact and release hygiene

Raw benchmark JSON artifacts should not be uploaded in security reports unless maintainers request them privately.

Do not upload release assets, create tags, or change release metadata as part of a security report or fix unless maintainers explicitly direct that work.

Benchmark evidence and claim boundaries are documented in [docs/README.md](docs/README.md) and [experiments/README.md](experiments/README.md). Security reports should not add production cost, real API-cost, production benchmark, full runtime-integrated benchmark, broad workload superiority, or energy reduction claims.

## Scope

This policy applies to the public KORA repository and the current alpha CLI, example, telemetry, and packaging surface.

# KORA AI-Assisted Contribution Guide

Date: 2026-05-08

## Purpose

AI-assisted contributions are welcome when they are small, reviewable, and accountable.

The contributor remains responsible for correctness, maintainability, security, and claim safety.

## Rules

- Start from an open GitHub Issue or a clearly described docs task.
- Keep PRs small and focused.
- Explain the scope of the change.
- Run the relevant validation commands.
- Do not modify benchmark claims, release claims, partner claims, or claim registry wording unless the task explicitly asks for that.
- Do not submit large generated code or documentation dumps.
- Do not include secrets, API keys, private user data, credentials, or proprietary datasets.

## Recommended Workflow

1. Pick an issue or propose a small docs/code change.
2. Comment with intent if the issue is already open.
3. Create a branch or fork.
4. Implement the smallest useful change.
5. Run tests or docs checks.
6. Open a PR with changed files and validation commands.
7. Respond to review.

## Good First AI-Assisted Work

- documentation fixes
- example walkthroughs
- tests for existing behavior
- CLI help text improvements
- benchmark reproduction notes that preserve claim boundaries

## Work Requiring Maintainer Review

- core execution behavior
- benchmark methodology
- claim wording
- release documentation
- security-sensitive files
- public language that mentions results, validation, adoption, funding, partners, or government use

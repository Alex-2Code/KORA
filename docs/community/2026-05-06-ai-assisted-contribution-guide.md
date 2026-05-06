# KORA AI-Assisted Contribution Guide

Date: `2026-05-06`

## Purpose

AI-assisted and vibe-coding contributions are welcome, but they must remain accountable.

The contributor is responsible for the quality, correctness, safety, and maintainability of the submitted work.

## Rules

- Start from an open GitHub issue.
- Keep PRs small.
- Explain whether AI tools were used.
- Run validation commands.
- Do not modify benchmark claims, release claims, partner claims, or the claim registry unless explicitly assigned.
- Do not submit large generated code dumps.
- The contributor is responsible for output quality.

## Recommended Workflow

1. Pick an issue.
2. Comment with intent.
3. Fork or create a branch.
4. Implement a small change.
5. Run tests/checks.
6. Open a PR.
7. Disclose AI assistance.
8. Respond to review.

## Good First AI-Assisted Work

- docs fixes
- examples
- benchmark result templates
- FAQ
- small CLI usability improvements
- tests
- tutorials

## Work Requiring Special Approval

- core architecture
- benchmark methodology
- claim wording
- release docs
- investor/EIC/partner language
- security-sensitive areas

## Reusable AI Prompt

```text
You are helping me contribute to KORA, an open-source AI Execution Control Layer project.

Work only on the issue scope I provide.
Keep the change small.
Do not change benchmark claims, release claims, partner claims, or claim registry wording unless the issue explicitly asks for that.
Do not invent evidence, partners, grants, investors, publications, or benchmark results.
Prefer existing repo style.
After drafting, list files changed and validation commands I should run.
Mark anything claim-sensitive for Albert review.
```

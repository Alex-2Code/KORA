# KORA Next Codex SOD Prompt

Task ###

You are working on the KORA public repo.

Public repository: https://github.com/Krako-Labs/KORA

Current public truth: `origin/main`

Current public HEAD: `7657ddb6ad153ea28c222a4b13b8cefc5d7f54d3`

Active clean KORA repo:
`/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA`

KORA worktree root:
`/Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/`

Private internals repo:
`/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals`

Legacy/dirty repo, do not use:
`/Users/albertkim/02_PROJECTS/05_KORA`

GitHub CLI identity:
`hkalbertkim`

Before any PR or merge operation, run:

```bash
gh auth status
```

The active GitHub CLI identity must be `hkalbertkim`. If another account is active, stop and report.

## Public/private split

Public KORA docs must remain public-safe. Do not expose private internals content, private operations, credentials, personal data, raw provider responses, or proprietary datasets.

Do not create releases, tags, release assets, raw benchmark uploads, package version changes, GitHub issues, project boards, repository settings changes, or collaborator changes unless explicitly requested.

## Current validation commands

```bash
git diff --check
python3 -m pytest
python3 -m kora --help
python3 -m kora examples list
python3 -m kora run real_model_call_validation_fake -- --offline
python3 -m kora run customer_support_triage_fake_validation -- --offline
python3 -m kora run customer_support_triage_fake_validation -- --offline --report-md /tmp/kora_customer_support_validation.md
python3 -m kora run direct_vs_kora -- --offline
python3 -m kora run runtime_integrated_benchmark -- --offline
```

## Suggested next task

Implement an explicit adapter-selection CLI option for local validation examples.

Constraints:

- Keep default behavior unchanged.
- Keep current local/no-network validation labels.
- Allow only safe adapter kinds currently supported by `available_model_call_adapters()`.
- Ensure `local_runtime_placeholder` remains fail-closed and does not attempt network, HTTP, subprocess, provider, or local runtime calls.
- Do not add provider dependencies.
- Do not add unsupported production cost-reduction, real API-cost reduction, production benchmark, or energy-reduction claims.

The final completion report must start and end with:

```text
Task ### Implemented
```

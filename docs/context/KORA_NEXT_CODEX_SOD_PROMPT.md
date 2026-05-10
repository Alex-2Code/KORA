# KORA Next Codex SOD Prompt

## Current Public State

- Public repository: https://github.com/Krako-Labs/KORA
- Current public truth: `origin/main`
- Current public HEAD: `42cfd64207705d2251d031fa74054416c36b8fae`
- Active clean repo: `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA`
- Worktree root: `/Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/`
- Legacy/dirty repo, do not use: `/Users/albertkim/02_PROJECTS/05_KORA`

## GitHub CLI Identity Requirement

Before any GitHub PR operation, run:

```bash
export GH_CONFIG_DIR="$HOME/.config/gh-hkalbertkim"
gh auth status
```

The active GitHub CLI identity must be `hkalbertkim`.

## Public / Private Split

- Public KORA repo contains technical docs, examples, tests, validation paths, paper track docs, and Studio planning/runtime skeletons.
- Private internals repo contains internal operations and contributor coordination materials.
- Do not commit local private context files to public KORA.
- Do not expose private internals/campaign content in public KORA docs.

## Current Validation Commands

```bash
git diff --check
python3 -m pytest
python3 -m kora --help
python3 -m kora examples list
python3 -m kora studio --help
python3 -m kora studio
python3 -m kora run real_model_call_validation_fake -- --offline
python3 -m kora run customer_support_triage_fake_validation -- --offline
python3 -m kora run customer_support_triage_fake_validation -- --offline --report-md /tmp/kora_customer_support_validation.md
python3 -m kora run direct_vs_kora -- --offline
python3 -m kora run runtime_integrated_benchmark -- --offline
```

If touching Studio server behavior, also run a bounded local server health/status check and ensure no server process remains.

## Next Paper Task Candidate

Task 313A - collect verified references plan / initial verified reference scaffold.

Rules:

- Do not add fake citations.
- Use verified references only.
- If web access is unavailable, create a reference collection TODO/scaffold only.
- Do not add production cost, real API-cost, energy, production validation, real provider validation, or broad workload superiority claims.

## Next Studio Task Candidate

Task 313B - add KORA Studio static placeholder page served from `/`.

Rules:

- No React/Vite yet.
- Standard library only.
- Static HTML placeholder.
- Local-only.
- No browser launch.
- No Ollama/provider calls.
- Add tests for HTML content.

## Completion Report

The final completion report for each task must start and end with:

```text
Task ### Implemented
```

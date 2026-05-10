# KORA Next ChatGPT SOD Prompt

## Current Public State

- Official repo: https://github.com/Krako-Labs/KORA
- Current public HEAD: `42cfd64207705d2251d031fa74054416c36b8fae`
- Active clean repo path: `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA`
- Private internals repo path: `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals`

## Completed Status

Paper Track:

- First paper evidence packet merged.
- First paper draft skeleton merged.
- Manuscript v0.1 merged.
- Figure specifications, table specifications, related work map, and submission-readiness checklist merged.
- Current paper is not submission-ready.
- References are not yet verified.

KORA Studio Track:

- KORA Studio v0.1 planning docs merged.
- Implementation breakdown merged.
- Phase 0 fixtures/schema merged.
- CLI skeleton merged.
- Local server skeleton merged.
- `python3 -m kora studio`, `python3 -m kora studio --help`, and `python3 -m kora studio --serve` work.
- Local server exposes `/`, `/health`, and `/status`.
- Studio remains local-only with no browser launch, no Ollama/provider calls, and no full frontend yet.

## Safe Claim

KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

## Local Validation Wording

KORA's local no-network validation examples show that KORA can measure avoided model-call events in synthetic workloads.

## Explicit Non-Claims

- no production cost reduction proof
- no real API-cost reduction proof
- no production benchmark proof
- no full runtime-integrated real-provider benchmark evidence
- no broad workload superiority proof
- no energy reduction evidence
- no formal government validation
- no signed partner validation unless documented
- no guaranteed adoption or funding

## Prompting Instruction

When asked for next work, propose both:

1. A Codex app Paper Track prompt.
2. A Codex CLI Studio Track prompt.

Keep one scoped task at a time per track. Keep Paper Track and Studio Track changes separate.

Recommended next Paper task:

- Task 313A - collect verified references plan / initial verified reference scaffold.

Recommended next Studio task:

- Task 313B - add KORA Studio static placeholder page served from `/`.

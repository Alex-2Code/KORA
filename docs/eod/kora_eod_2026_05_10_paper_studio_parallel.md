# KORA EOD Report - Paper and Studio Parallel Workstreams

## Date

2026-05-10

## Public repo

https://github.com/Krako-Labs/KORA

## Public HEAD

`42cfd64207705d2251d031fa74054416c36b8fae`

## Internals repo

https://github.com/Krako-Labs/internals

## Internals HEAD

`641f7a68ba98e06f55472a0dff9959d896e90ece`

## GitHub CLI identity

`hkalbertkim`

## Summary

Today advanced KORA along two parallel tracks:

- Paper Track: first paper evidence, draft, manuscript, figure/table planning, and submission-readiness planning.
- Studio Track: KORA Studio planning, fixtures/schema, CLI skeleton, and local server skeleton.

Community onboarding also advanced through contributor pathway docs, public route guidance, a good-first issue pool, the first external contributor PR, and a private India contributor onboarding packet.

## Completed Work - Paper Track

- First paper evidence packet merged.
- First paper draft skeleton merged.
- Manuscript v0.1 merged.
- Figure specifications merged.
- Table specifications merged.
- Related work map merged.
- Submission-readiness checklist merged.
- Current limitations remain explicit: synthetic workloads, no production traffic, no real provider validation, no real API-cost proof, no energy measurement, no broad workload superiority claim, and no verified references yet.

## Completed Work - KORA Studio Track

- KORA Studio v0.1 product/spec docs merged.
- Paper/Studio docs integration cleanup merged.
- KORA Studio implementation breakdown docs merged.
- Phase 0 fixtures/schema merged.
- CLI skeleton merged.
- Local server skeleton merged.

Current commands:

```bash
python3 -m kora studio --help
python3 -m kora studio
python3 -m kora studio --serve
```

Current local server skeleton exposes:

- `/`
- `/health`
- `/status`

Current Studio boundaries:

- local-only, `127.0.0.1` by default
- no browser launch yet
- no Ollama/provider calls
- no dependencies added
- no full frontend yet

## Completed Work - Contributor / Community

- Public contributor pathway docs merged in PR #78.
- Contact/discussion route docs merged in PR #79.
- Good-first issue pool expanded.
- Labels for validation, claim-safe, workload, examples, community, tests, kora-studio, and help wanted confirmed or created as needed.
- First external contributor PR #91 from `aqilaziz` merged, closing issue #90.
- Private internals India contributor onboarding batch created and pushed.

## Current Validation Commands

```bash
python3 -m pytest
python3 -m kora --help
python3 -m kora examples list
python3 -m kora studio --help
python3 -m kora studio
python3 -m kora studio --serve
python3 -m kora run real_model_call_validation_fake -- --offline
python3 -m kora run customer_support_triage_fake_validation -- --offline
python3 -m kora run customer_support_triage_fake_validation -- --offline --report-md /tmp/kora_customer_support_validation.md
python3 -m kora run direct_vs_kora -- --offline
python3 -m kora run runtime_integrated_benchmark -- --offline
```

## Current Safe Public Claim

KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

## Current Local Validation Wording

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

## Current Paper Next Steps

1. Collect verified references.
2. Add references/BibTeX only after verification.
3. Generate figure drafts.
4. Capture clean command transcript.
5. Add p50/p95 latency if measured.
6. Expand customer-support workload to 100 requests.
7. Add local model runtime validation, for example Ollama.

## Current Studio Next Steps

1. Add static placeholder page.
2. Add report viewer static page.
3. Add counter dashboard static page.
4. Add model/runtime detection design or implementation.
5. Add browser launch only after local server/UI stabilizes.
6. Add Ollama detection before Ollama calls.
7. Do not add provider/API integration yet.

## Open PR / Issue Status

Open PRs:

- PR #110: `docs: add workload safety note to README` by `enoshdev`.

Key open good-first issues:

- #83 Add an example output block for customer-support triage validation.
- #84 Add validation counter glossary.
- #85 Improve Help Test KORA contributor wording.
- #86 Clarify adapter selection kinds.
- #88 Add a troubleshooting note for report output paths.
- #89 Add business and community contribution guidance.
- #92 Add a README note for workload proposal safety.
- #93 Add example JSON snippet for workload proposal template.
- #94 Add troubleshooting note for "example not listed".
- #95 Add a small FAQ about deterministic routes.
- #96 Add a small note explaining generated report artifacts.
- #98 Add KORA Studio MVP screen list draft.
- #99 Add counter-card ideas for future KORA Studio dashboard.
- #101 Add a short FAQ about generated Markdown reports.
- #102 Add a small note about compatibility command names.
- #103 Add a lightweight contributor checklist for documentation PRs.
- #104 Add workload proposal examples for RAG routing.
- #105 Add a short note about KORA Studio planning scope.

External contributor PRs needing review:

- PR #110 remains open and should be reviewed for duplicate scope and claim safety.

## Remaining TODOs

- Krako 2.0: TBD.
- Continue external contributor review as PRs arrive.
- Keep local context refreshed after major merges.
- Decide whether to enable more Discussions workflows if needed.
- Cleanup old worktrees only after explicit approval.

## Next ChatGPT SOD Prompt

```text
You are helping plan the next KORA session.

Public repo: https://github.com/Krako-Labs/KORA
Current public HEAD: 42cfd64207705d2251d031fa74054416c36b8fae
Active clean repo: /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA
Worktree root: /Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/
Private internals repo: /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals

Latest completed status:
- Paper Track: evidence packet, draft skeleton, manuscript v0.1, figure/table specs, related work map, and submission-readiness checklist are merged.
- KORA Studio Track: v0.1 planning docs, implementation breakdown, Phase 0 fixtures/schema, CLI skeleton, and local server skeleton are merged.
- Current public HEAD includes PR #116 local server skeleton.

Safe claim:
KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Local validation wording:
KORA's local no-network validation examples show that KORA can measure avoided model-call events in synthetic workloads.

Non-claims:
No production cost reduction proof, no real API-cost reduction proof, no production benchmark proof, no full runtime-integrated real-provider benchmark evidence, no broad workload superiority proof, no energy reduction evidence, no formal government validation, no guaranteed adoption or funding.

Please provide both:
1. A Codex app Paper Track prompt.
2. A Codex CLI Studio Track prompt.

Recommended next Paper task:
Task 313A - collect verified references plan / initial verified reference scaffold.

Recommended next Studio task:
Task 313B - add KORA Studio static placeholder page served from `/`.

Keep one scoped task at a time per track.
```

## Next Codex Paper Track SOD Prompt

```text
Task 313A

You are working on the KORA Paper Track only.

Public repository: https://github.com/Krako-Labs/KORA
Current public truth: origin/main
Current KORA public HEAD: 42cfd64207705d2251d031fa74054416c36b8fae
Active clean KORA repo: /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA
Worktree root: /Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/
Legacy/dirty repo, do not use: /Users/albertkim/02_PROJECTS/05_KORA

Goal:
Collect verified references plan / initial verified reference scaffold for the KORA first paper.

Rules:
- Paper Track only.
- Do not modify docs/kora-studio/.
- Do not add fake citations.
- Use verified references only.
- If web access is unavailable, create a reference collection TODO/scaffold only.
- Do not add new benchmark claims.
- Do not claim production cost reduction, real API-cost reduction, energy reduction, production validation, real provider validation, or broad workload superiority.

Validation:
- git diff --check
- python3 -m pytest
- python3 -m kora --help
- python3 -m kora examples list
- python3 -m kora run runtime_integrated_benchmark -- --offline
- changed-file public/private and secret scan

Completion report must start and end with:
Task 313A Implemented
```

## Next Codex Studio Track SOD Prompt

```text
Task 313B

You are working on the KORA Studio Track only.

Public repository: https://github.com/Krako-Labs/KORA
Current public truth: origin/main
Current KORA public HEAD: 42cfd64207705d2251d031fa74054416c36b8fae
Active clean KORA repo: /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA
Worktree root: /Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/
Legacy/dirty repo, do not use: /Users/albertkim/02_PROJECTS/05_KORA

Goal:
Add a KORA Studio static placeholder page served from `/`.

Scope:
- No React/Vite yet.
- Standard library only.
- Static HTML placeholder.
- Local-only.
- No browser launch.
- No Ollama/provider calls.
- Add tests for HTML content.
- Preserve current `/health` and `/status` behavior.

Validation:
- git diff --check
- python3 -m pytest
- python3 -m kora studio --help
- python3 -m kora studio
- local server health/status check with no lingering process
- changed-file public/private and secret scan

Completion report must start and end with:
Task 313B Implemented
```

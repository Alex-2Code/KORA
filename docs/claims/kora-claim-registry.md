# KORA Claim Registry

## Purpose

This document is the source of truth for what KORA can and cannot claim publicly.

It applies to README content, releases, documentation, GitHub Discussions, X/Twitter, LinkedIn, Telegram, investor materials, EIC/grant materials, partner outreach, paper drafts, and LLM-assisted writing.

All public or externally reusable KORA language should be checked against this registry before publication.

## Official Category Language

Category:

- AI Execution Control Layer

Vision phrase:

- Inference OS for AI systems

Approved category one-liner:

> KORA is an AI Execution Control Layer that structures AI requests into verifiable task graphs before escalating to expensive model inference.

Approved technical one-liner:

> KORA routes deterministic work away from unnecessary model invocation through task graphs, validation, fallback, and telemetry.

Approved OSS one-liner:

> KORA is an open-source infrastructure project for building inference-first AI systems.

## Current Approved Benchmark Claim

Use exactly:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

Supporting detail:

- Workload: `experiments/workloads/deterministic_heavy_v1_100.json`
- Generator: `experiments/generate_workload.py`
- Seed: `42`
- Total tasks: `100`
- Deterministic/no-model tasks: `80`
- Fallback/model-candidate tasks: `20`
- Direct-baseline simulated model invocations: `100`
- KORA-controlled simulated model invocations: `20`
- Avoided simulated model invocations: `80`
- Avoided invocation rate: `80%`
- Deterministic outputs checked: `80`
- Mismatches: `0`
- Fallback/model-candidate skipped: `20`

## Claim Status Table

| Claim | Status | Allowed wording | Forbidden wording | Required evidence before escalation | Approved channels |
|---|---|---|---|---|---|
| Category claim: KORA as AI Execution Control Layer | Approved | KORA is an AI Execution Control Layer. | KORA has already become the dominant execution-control standard. | Broader adoption evidence before dominance language. | README, docs, discussions, social, investor/EIC intro, partner intro |
| vLLM analogy claim | Review required | KORA aims to become category-defining for execution control before unnecessary inference is invoked, similar to how vLLM became category-defining for LLM serving. | KORA is already the vLLM of execution control. | Adoption, deployment, and ecosystem evidence before stronger analogy. | Docs, investor/EIC drafts, partner drafts with Albert review |
| v0.2.0-alpha release claim | Approved | KORA v0.2.0-alpha is a prerelease with bounded deterministic-heavy benchmark evidence. | v0.2.0-alpha proves broad operational impact. | Additional release evidence before expanded impact wording. | Releases, changelog, README, docs |
| deterministic-heavy benchmark claim | Approved with exact wording | In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline. | KORA reduced real costs by 80%. | Runtime-integrated and real billing evidence before cost language. | README, docs, release notes, social with exact wording |
| runtime-integrated benchmark claim | Not approved yet | Runtime-integrated benchmark evidence is planned. | KORA has full runtime-integrated benchmark proof. | Merged runtime-integrated benchmark, result artifacts, validation commands, reviewed report. | Internal roadmap until evidence exists |
| real application workload replay claim | Not approved yet | Real application workload replay is a future evidence track. | KORA has proven results on real application workloads. | Reproducible real workload replay, source path, validation, report. | Internal roadmap until evidence exists |
| production cost reduction claim | Prohibited | Not currently supported. | KORA proves production cost reduction. | Production deployment evidence, baseline, billing data, methodology, review. | None until evidence exists |
| real API cost reduction claim | Prohibited | Not currently supported. | KORA proves real API-cost reduction. | Real API usage data, billing methodology, baseline, review. | None until evidence exists |
| cloud/data center validation claim | Prohibited unless documented | Exploratory infrastructure conversations may be tracked internally. | KORA is validated by cloud/data center partners. | Signed or documented validation, approved wording, source record. | Partner docs only after approval |
| energy efficiency claim | Prohibited | Not currently supported. | KORA proves energy reduction. | Energy methodology, measurement, baseline, third-party review if needed. | None until evidence exists |
| government/institution interest claim | Review required | Exploratory discussion or early interest, if true. | Government validation or government-approved KORA. | Written documentation and Albert approval. | Internal tracking or approved partner/EIC material |
| partner/LOI claim | Review required | LOI candidate or partner discussion, if true. | Signed partnership unless actually signed. | Signed document or written record, approved wording. | Partner tracker, approved outreach |
| community adoption claim | Review required | Early community feedback or initial contributors, if documented. | KORA has guaranteed adoption. | Public metrics, issue/discussion activity, contributor evidence. | Community updates with review if numeric |
| paper/publication claim | Review required | Technical report in preparation. | Peer-reviewed proof or accepted paper unless accepted/published. | Accepted publication, DOI/proceedings link, paper artifact. | Paper roadmap, docs, investor/EIC drafts with review |

## vLLM Analogy Boundaries

Allowed:

> KORA aims to become category-defining for execution control before unnecessary inference is invoked, similar to how vLLM became category-defining for LLM serving.

Forbidden:

- KORA is already the vLLM of execution control.
- KORA has achieved vLLM-level adoption.
- KORA is proven at vLLM scale.

## Do-Not-Claim List

Do not claim:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority proof
- energy reduction evidence
- formal government validation
- signed cloud/data center/telco partnership unless actually signed
- guaranteed adoption
- guaranteed future funding
- EIC approval or grant success
- investor commitment unless documented

## Channel Review Levels

Level A: Safe to publish without Albert review.

Examples:

- General KORA category one-liner.
- GitHub quickstart invitation.
- Benchmark run invitation.
- Open-source contribution invitation.
- "unpaid early contributor role" language.

Level B: Requires Albert review.

Examples:

- Benchmark numeric claim.
- vLLM analogy.
- EIC/grant wording.
- investor-facing wording.
- partner/cloud/data center/telco wording.
- government/institution interest wording.
- paper authorship/contribution wording.

Level C: Prohibited or special approval required.

Examples:

- cost reduction percentage.
- production proof.
- energy savings proof.
- signed partnership claim.
- formal government validation.
- "guaranteed" language.
- unapproved fundraising/investor commitment language.

## LLM-Assisted Writing Rules

- Any LLM-generated KORA content must be checked against this registry.
- LLMs must not invent evidence, partners, grants, investors, publications, or benchmark results.
- LLM-generated content mentioning numbers, partners, grants, or papers requires Albert review.
- If an LLM is uncertain whether a phrase is allowed, it should mark the phrase for Albert review instead of publishing it.

## Update Policy

This registry must be updated when new evidence is merged into `origin/main`.

Claim escalation requires:

- evidence
- source path
- validation command
- review

No claim should be escalated based on aspiration, roadmap, informal interest, or private conversation alone.

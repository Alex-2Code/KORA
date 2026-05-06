# KORA Public Language Guide

## Purpose

This is a practical copywriting guide for public KORA communication.

Use it with `docs/claims/kora-claim-registry.md` when drafting README copy, GitHub Discussions, social posts, Telegram updates, investor/EIC language, partner outreach, and paper-related text.

## Approved Short Descriptions

README:

> KORA is an open-source AI Execution Control Layer that structures AI requests into verifiable task graphs before escalating to expensive model inference.

GitHub Discussions:

> KORA helps developers explore deterministic-first execution, validation, fallback, and telemetry before model calls become the default path.

X/Twitter:

> KORA is building an AI Execution Control Layer: task graphs, deterministic routing, validation, fallback, and telemetry before unnecessary inference.

LinkedIn:

> KORA is an open-source infrastructure project for AI execution control. It structures requests into verifiable task graphs and escalates to model inference only when needed.

Telegram:

> KORA is the open-source AI Execution Control Layer project. Use this repo for issues, discussions, PRs, benchmark feedback, and community coordination: https://github.com/Krako-Labs/KORA

Investor intro:

> KORA is building the AI Execution Control Layer: infrastructure that structures AI requests into task graphs, routes deterministic work away from unnecessary model invocation, and preserves validation and telemetry before inference escalation.

EIC/grant intro:

> KORA is an open-source AI infrastructure project focused on execution control before inference escalation, with a bounded public benchmark evidence path and a roadmap toward runtime-integrated evaluation.

Partner intro:

> KORA explores how AI systems can control execution before inference escalation through task graphs, deterministic routing, validation, fallback, and telemetry.

Paper intro:

> KORA studies execution control for AI systems by converting requests into task graphs, routing deterministic work before model invocation, and preserving validation and telemetry for reproducible evaluation.

## Approved Migration Note

> KORA has moved into its official Krako Labs home at https://github.com/Krako-Labs/KORA.

> Same code, same history, bigger mission.

## Approved Benchmark Wording

Short version:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

Technical version:

> On `experiments/workloads/deterministic_heavy_v1_100.json`, generated from seed `42`, the direct-baseline mode counted 100 simulated model invocations while KORA-controlled mode counted 20. Deterministic outputs checked: 80. Mismatches: 0. Fallback/model-candidate skipped: 20.

Social media version:

> In KORA's reproducible 100-task deterministic-heavy benchmark, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline. This is simulated benchmark evidence, not a production claim.

Paper-safe version:

> In the current deterministic-heavy benchmark workload, KORA-controlled execution avoids 80 of 100 simulated model invocations relative to a naive direct baseline, with 80 deterministic outputs checked and 0 mismatches.

Investor/EIC-safe version:

> KORA's current public evidence is a reproducible simulated benchmark: in a 100-task deterministic-heavy workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline. The next evidence track is runtime-integrated evaluation.

## Prohibited Rewrites

Do not rewrite:

- "80 of 100 simulated model invocations avoided" as "80% cost reduction."
- "simulated model invocation" as "real API call."
- "benchmark workload" as "production workload."
- "interest" as "partnership."
- "planned validation" as "validated."

## Public Contributor Role Boundary Language

Approved language:

> These are unpaid early open-source contributor roles, not employment positions.

> Future paid roles, grants, internships, or contributor programs may be considered if funding becomes available, but they are not guaranteed.

## Partner / Government / Institution Language

Allowed:

- early interest
- exploratory discussion
- potential pilot candidate
- LOI candidate

Forbidden unless documented and approved:

- validated by
- partnered with
- officially backed by
- government-approved

## Paper / Publication Language

Allowed:

- technical report in preparation
- paper roadmap
- community benchmark contribution program planned

Forbidden unless actually accepted or published:

- published paper
- accepted conference paper
- peer-reviewed proof

## Example LLM Prompt For Safe KORA Writing

```text
You are writing public KORA content.

Use these approved one-liners:
- KORA is an AI Execution Control Layer that structures AI requests into verifiable task graphs before escalating to expensive model inference.
- KORA routes deterministic work away from unnecessary model invocation through task graphs, validation, fallback, and telemetry.

Preserve this benchmark wording exactly unless asked to omit the benchmark:
"In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline."

Do not rewrite simulated benchmark evidence as production evidence, cost reduction, real API-cost reduction, energy reduction, partner validation, government validation, investor commitment, or publication proof.

If a draft mentions numbers, partners, grants, investors, institutions, papers, or adoption, mark it for Albert review.

If evidence is missing, write "needs review" instead of inventing support.
```

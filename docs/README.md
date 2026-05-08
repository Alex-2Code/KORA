# KORA Documentation Index

## Purpose

This is the starting point for navigating KORA documentation.

KORA is an open-source execution-control layer that turns AI requests into structured execution paths before inference.

Most AI apps call the model too soon. KORA changes the default. Structure first. Inference second.

## Start

- [Main README](../README.md)
- [Current v0.3.0-alpha prerelease](https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha)
- [KORA Category Thesis](vision/2026-05-06-kora-category-thesis.md)

## Understand

![KORA control layer architecture](assets/kora-control-layer-architecture.svg)

KORA control layer architecture.

- [KORA Claim Registry](claims/kora-claim-registry.md)
- [KORA Public Language Guide](claims/kora-public-language-guide.md)
- [Telemetry and observability counters](telemetry-and-observability.md#current-public-counters)
- [Testing and validation strategy](testing-and-validation-strategy.md)
- [Research agenda](research-agenda.md)
- [Whitepaper](whitepaper.md)

## Run

- [Examples directory](../examples/)
- [Experiments regeneration guide](../experiments/README.md)
- [Benchmark real app guide](benchmark-real-app.md)
- [Benchmark overview](benchmark.md)
- [Customer-support triage workload spec](workloads/customer-support-triage.md)
- [Good first issue candidates](good_first_issues.md)

Core local commands:

```bash
python3 -m kora --help
python3 -m kora examples list
python3 -m kora run real_model_call_validation_fake -- --offline
python3 -m kora run direct_vs_kora -- --offline
python3 -m kora run runtime_integrated_benchmark -- --offline
```

## Inspect Evidence

Use this path for the current `v0.3.0-alpha` prerelease runtime evidence and regeneration flow:

1. Current workload: [`experiments/workloads/deterministic_heavy_v1_100.json`](../experiments/workloads/deterministic_heavy_v1_100.json)
2. Workload generator: [`experiments/generate_workload.py`](../experiments/generate_workload.py)
3. Benchmark runner: [`experiments/run_benchmark.py`](../experiments/run_benchmark.py)
4. Summary generator: [`experiments/summarize_benchmark_results.py`](../experiments/summarize_benchmark_results.py)
5. Runtime benchmark example: [`examples/runtime_integrated_benchmark`](../examples/runtime_integrated_benchmark)
6. Runtime evidence reviewer guide: [`docs/reports/v0.3.0-alpha-runtime-evidence-reviewer-guide.md`](reports/v0.3.0-alpha-runtime-evidence-reviewer-guide.md)
7. Artifact policy and regeneration commands: [`docs/reports/benchmark_artifact_policy.md`](reports/benchmark_artifact_policy.md)
8. Current benchmark summary: [`docs/benchmarks/kora_benchmark_result_v1_100.md`](benchmarks/kora_benchmark_result_v1_100.md)
9. Validation roadmap: [`docs/benchmarks/validation-roadmap.md`](benchmarks/validation-roadmap.md)
10. Real model-call validation design: [`docs/benchmarks/real-model-call-validation-design.md`](benchmarks/real-model-call-validation-design.md)
11. Real model-call validation report template: [`docs/benchmarks/real-model-call-validation-report-template.md`](benchmarks/real-model-call-validation-report-template.md)
12. Fake model-call validation example: [`examples/real_model_call_validation_fake`](../examples/real_model_call_validation_fake)
13. Customer-support triage workload spec: [`docs/workloads/customer-support-triage.md`](workloads/customer-support-triage.md)
14. Claim boundary source: [`docs/claims/kora-claim-registry.md`](claims/kora-claim-registry.md)

Current approved public claim:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

This evidence does not claim production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, or energy reduction evidence.

Raw benchmark JSON artifacts are reproducible outputs and are not frozen or committed for this alpha release.

Additional evidence and release docs:

- [v0.3.0 runtime-integrated benchmark architecture](design/v0.3.0-runtime-integrated-benchmark-evidence-architecture.md)
- [v0.3.0-alpha release-readiness checklist](reports/v0.3.0-alpha-release-readiness-checklist.md)
- [v0.3.0-alpha docs and claim audit](reports/v0.3.0-alpha-docs-claim-audit.md)
- [v0.3.0-alpha release validation packet](reports/v0.3.0-alpha-release-validation-packet.md)
- [v0.3.0-alpha release approval checkpoint](reports/v0.3.0-alpha-release-approval-checkpoint.md)
- [v0.3.0-alpha post-release EOD report](eod/kora_eod_2026_05_07_v0.3.0-alpha_release.md)
- [v0.3.0-alpha post-release cleanup plan](reports/v0.3.0-alpha-post-release-cleanup-plan.md)
- [v0.3.1-alpha roadmap](planning/v0.3.1-alpha-roadmap.md)

## Help Test

- [Help Test KORA](community/help-test-kora.md)
- [KORA validation roadmap](benchmarks/validation-roadmap.md)
- [KORA social media announcement guide](community/KORA_SOCIAL_MEDIA_ANNOUNCEMENT_GUIDE.md)
- [KORA community manager guide](community/KORA_COMMUNITY_MANAGER_GUIDE.md)

Good candidate workloads:

- customer-support triage
- repetitive RAG workflows
- agent workflows with budget or escalation rules
- deterministic-heavy backend workflows
- LLM apps with high repeated request patterns

## Contribute

- [Canonical governance document](../GOVERNANCE.md)
- [Contributing guide](../CONTRIBUTING.md)
- [Security policy](../SECURITY.md)
- [Code of conduct](../CODE_OF_CONDUCT.md)
- [KORA open roles](community/2026-05-06-kora-open-roles.md)
- [AI-assisted contribution guide](community/2026-05-06-ai-assisted-contribution-guide.md)
- [Community sync issue template](community/2026-05-06-community-sync-issue-template.md)
- [KORA OSS Operating System](ops/2026-05-06-kora-oss-operating-system.md)
- [KORA GitHub Platform Setup Plan](ops/2026-05-06-kora-github-platform-setup-plan.md)
- [Discussions and Wiki plan](ops/2026-05-06-kora-discussions-and-wiki-plan.md)
- [Label taxonomy](ops/2026-05-06-kora-label-taxonomy.md)

## Maintainers And Operators

- [KORA OSS Operating System](ops/2026-05-06-kora-oss-operating-system.md)
- [Manual GitHub setup checklist](ops/2026-05-06-kora-manual-github-setup-checklist.md)
- [Repository hygiene audit](ops/2026-05-06-kora-repository-hygiene-audit.md)

## Public Documentation Boundary Note

Public KORA documentation should read as normal open-source project documentation.

Do not place private credentials, personal data, unpublished partner notes, or internal operating material in public docs.

## Evidence Preservation Note

Older reports, EOD documents, benchmark summaries, and migration docs may look historical, but they should not be deleted casually. They preserve release, benchmark, paper, EIC/grant, investor, and operating evidence.

Use the [repository hygiene audit](ops/2026-05-06-kora-repository-hygiene-audit.md) before any cleanup.

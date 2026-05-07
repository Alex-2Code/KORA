# KORA Documentation Index

## Purpose

This is the starting point for navigating KORA documentation.

KORA is an AI Execution Control Layer / Inference OS for AI systems. It structures requests into task graphs, runs deterministic work first, validates outputs, and escalates to model inference only when needed.

The documentation is organized by audience and use case so developers, contributors, operators, paper readers, EIC/grant reviewers, investors, and partners can find the right files without relying on repository history.

## Start Here

- [Main README](../README.md)
- [Current v0.2.0-alpha release](https://github.com/Krako-Labs/KORA/releases/tag/v0.2.0-alpha)
- [KORA Category Thesis](vision/2026-05-06-kora-category-thesis.md)
- [KORA Project Source](context/KORA_PROJECT_SOURCE.md)
- [KORA Claim Registry](claims/kora-claim-registry.md)
- [KORA Public Language Guide](claims/kora-public-language-guide.md)
- [KORA Current State](context/KORA_CURRENT_STATE.md)
- [KORA OSS Operating System](ops/2026-05-06-kora-oss-operating-system.md)
- [KORA GitHub Platform Setup Plan](ops/2026-05-06-kora-github-platform-setup-plan.md)

## Current Benchmark Evidence Path

Use this path for the current `v0.2.0-alpha` benchmark evidence and regeneration flow:

1. Current workload: [`experiments/workloads/deterministic_heavy_v1_100.json`](../experiments/workloads/deterministic_heavy_v1_100.json)
2. Workload generator: [`experiments/generate_workload.py`](../experiments/generate_workload.py)
3. Benchmark runner: [`experiments/run_benchmark.py`](../experiments/run_benchmark.py)
4. Summary generator: [`experiments/summarize_benchmark_results.py`](../experiments/summarize_benchmark_results.py)
5. Experiments regeneration guide: [`experiments/README.md`](../experiments/README.md)
6. Artifact policy and regeneration commands: [`docs/reports/benchmark_artifact_policy.md`](reports/benchmark_artifact_policy.md)
7. Raw artifact freeze decision: [`docs/reports/v0.2.0-alpha-raw-artifact-freeze-decision.md`](reports/v0.2.0-alpha-raw-artifact-freeze-decision.md)
8. Current benchmark summary: [`docs/benchmarks/kora_benchmark_result_v1_100.md`](benchmarks/kora_benchmark_result_v1_100.md)
9. Release/changelog context: [`CHANGELOG.md`](../CHANGELOG.md)
10. Claim boundary source: [`docs/claims/kora-claim-registry.md`](claims/kora-claim-registry.md)

Next evidence architecture: [`docs/design/v0.3.0-runtime-integrated-benchmark-evidence-architecture.md`](design/v0.3.0-runtime-integrated-benchmark-evidence-architecture.md)

Reviewer-facing runtime evidence flow: [`docs/reports/v0.3.0-alpha-runtime-evidence-reviewer-guide.md`](reports/v0.3.0-alpha-runtime-evidence-reviewer-guide.md)

Future `v0.3.0-alpha` release-readiness checklist: [`docs/reports/v0.3.0-alpha-release-readiness-checklist.md`](reports/v0.3.0-alpha-release-readiness-checklist.md)

Final `v0.3.0-alpha` docs and claim audit: [`docs/reports/v0.3.0-alpha-docs-claim-audit.md`](reports/v0.3.0-alpha-docs-claim-audit.md)

Initial runtime-path harness command:

```bash
python3 -m kora run runtime_integrated_benchmark -- --offline
```

Safe claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

This evidence does not claim production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, or energy reduction evidence.

Raw benchmark JSON artifacts are reproducible outputs and are not frozen or committed for this alpha release.

## Document Status Labels

- **Current release evidence**: current release, benchmark, artifact, and claim-boundary docs for `v0.2.0-alpha`.
- **Benchmark/artifact policy**: rules and commands for regenerating benchmark workloads, raw outputs, and generated summaries.
- **Release preparation history**: readiness, merge, review, and release-prep reports preserved for auditability.
- **EOD/SOD reports**: operating handoff records and dated continuity reports.
- **Historical/background docs**: older benchmark notes, strategy, architecture, and context docs that may still be useful but are not the current evidence entry point.

## Documentation By Audience

### A. New Users And Developers

- [Main README](../README.md)
- [Examples directory](../examples/)
- [Telemetry and observability counters](telemetry-and-observability.md#current-public-counters)
- [Good first issue candidates](good_first_issues.md)
- [Current benchmark evidence path](#current-benchmark-evidence-path)
- [v0.3.0-alpha runtime evidence reviewer guide](reports/v0.3.0-alpha-runtime-evidence-reviewer-guide.md)
- [Technical preview results](technical_preview_results.md) - historical/background benchmark context
- [Benchmark real app guide](benchmark-real-app.md)
- [Benchmark overview](benchmark.md) - historical/background benchmark note
- [Benchmark summaries](benchmarks/) - current and historical benchmark summaries
- [Experiments directory](../experiments/)

### B. Contributors And Community

- [Canonical governance document](../GOVERNANCE.md)
- [Contributing guide](../CONTRIBUTING.md)
- [Security policy](../SECURITY.md)
- [Code of conduct](../CODE_OF_CONDUCT.md)
- [KORA open roles](community/2026-05-06-kora-open-roles.md)
- [AI-assisted contribution guide](community/2026-05-06-ai-assisted-contribution-guide.md)
- [Albert-Sumanta GitHub sync](community/2026-05-06-albert-sumanta-github-sync.md)
- [Community sync issue template](community/2026-05-06-community-sync-issue-template.md)
- [KORA OSS Operating System](ops/2026-05-06-kora-oss-operating-system.md)
- [KORA GitHub Platform Setup Plan](ops/2026-05-06-kora-github-platform-setup-plan.md)
- [Discussions and Wiki plan](ops/2026-05-06-kora-discussions-and-wiki-plan.md)
- [Label taxonomy](ops/2026-05-06-kora-label-taxonomy.md)

### C. Operators And Maintainers

- [KORA OSS Operating System](ops/2026-05-06-kora-oss-operating-system.md)
- [Korean ops coordinator handbook](ops/2026-05-06-kora-ops-coordinator-handbook-ko.md)
- [GitHub platform setup plan](ops/2026-05-06-kora-github-platform-setup-plan.md)
- [Manual GitHub setup checklist](ops/2026-05-06-kora-manual-github-setup-checklist.md)
- [Repository hygiene audit](ops/2026-05-06-kora-repository-hygiene-audit.md)
- [KORA Project Source](context/KORA_PROJECT_SOURCE.md)
- [KORA ChatGPT Operating Context](context/KORA_CHATGPT_OPERATING_CONTEXT.md)
- [KORA Codex Operating Context](context/KORA_CODEX_OPERATING_CONTEXT.md)
- [KORA Current State](context/KORA_CURRENT_STATE.md)

### D. Claims, Public Language, And Communications

- [KORA Claim Registry](claims/kora-claim-registry.md)
- [KORA Public Language Guide](claims/kora-public-language-guide.md)
- [KORA Category Thesis](vision/2026-05-06-kora-category-thesis.md)
- [Repository migration checklist](ops/2026-05-06-kora-repo-migration-checklist.md)

### E. Paper And Research

- [Authorship and contribution policy](paper/2026-05-06-kora-authorship-and-contribution-policy.md)
- [KORA Category Thesis](vision/2026-05-06-kora-category-thesis.md)
- [Technical preview results](technical_preview_results.md) - historical/background benchmark context
- [Benchmark summaries](benchmarks/) - current and historical benchmark summaries
- [Benchmark artifact policy](reports/benchmark_artifact_policy.md) - benchmark/artifact policy
- [Research agenda](research-agenda.md)
- [Whitepaper](whitepaper.md)

### F. EIC, Investor, Partner, And Grant Readiness

- [KORA Category Thesis](vision/2026-05-06-kora-category-thesis.md)
- [KORA Project Source](context/KORA_PROJECT_SOURCE.md)
- [KORA Claim Registry](claims/kora-claim-registry.md)
- [Repository migration checklist](ops/2026-05-06-kora-repo-migration-checklist.md)
- [KORA OSS Operating System](ops/2026-05-06-kora-oss-operating-system.md)
- [KORA GitHub Platform Setup Plan](ops/2026-05-06-kora-github-platform-setup-plan.md)
- [v0.2.0-alpha EOD report](reports/kora_eod_2026-05-05_v0.2.0-alpha.md)
- [Current benchmark evidence path](#current-benchmark-evidence-path)
- [v0.3.0-alpha release-readiness checklist](reports/v0.3.0-alpha-release-readiness-checklist.md)
- [Benchmark evidence summaries](benchmarks/) - current and historical benchmark summaries

### G. Internal Continuity And Handoff

- [KORA_PROJECT_SOURCE.md](context/KORA_PROJECT_SOURCE.md)
- [KORA_CHATGPT_OPERATING_CONTEXT.md](context/KORA_CHATGPT_OPERATING_CONTEXT.md)
- [KORA_CODEX_OPERATING_CONTEXT.md](context/KORA_CODEX_OPERATING_CONTEXT.md)
- [KORA_CURRENT_STATE.md](context/KORA_CURRENT_STATE.md)
- [EOD reports](eod/)
- [Release and readiness reports](reports/)

## Evidence Preservation Note

Older reports, EOD documents, benchmark summaries, and migration docs may look historical, but they should not be deleted casually. They preserve release, benchmark, paper, EIC/grant, investor, and operating evidence.

Use the [repository hygiene audit](ops/2026-05-06-kora-repository-hygiene-audit.md) before any cleanup.

## Public / Private Boundary Note

Most docs in this repository are public-facing unless marked internal.

Internal EOD/SOD prompts are operating artifacts. They should not contain private credentials, personal data, private partner notes, unpublished investor conversations, or other sensitive information.

## Next Cleanup Steps

Start with the [repository hygiene audit](ops/2026-05-06-kora-repository-hygiene-audit.md).

Future cleanup should proceed in this order:

1. Audit first.
2. Add safe links and indexes.
3. Request explicit approval before moving, renaming, or removing files.
4. Preserve release and benchmark evidence throughout cleanup.

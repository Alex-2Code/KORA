# Changelog

## v0.3.0-alpha runtime evidence release-preparation draft

Status: draft/pre-release preparation. No `v0.3.0-alpha` tag has been created, no GitHub Release has been created, no release assets have been uploaded, and no package version change is included in this draft.

Related docs:

- [Runtime-integrated benchmark evidence architecture](docs/design/v0.3.0-runtime-integrated-benchmark-evidence-architecture.md)
- [Runtime evidence reviewer guide](docs/reports/v0.3.0-alpha-runtime-evidence-reviewer-guide.md)
- [v0.3.0-alpha release-readiness checklist](docs/reports/v0.3.0-alpha-release-readiness-checklist.md)
- [v0.3.0-alpha docs claim audit](docs/reports/v0.3.0-alpha-docs-claim-audit.md)
- [v0.3.0-alpha release validation packet](docs/reports/v0.3.0-alpha-release-validation-packet.md)

### Runtime evidence path

- Added the runtime-integrated benchmark evidence architecture design for the bounded `v0.3.0-alpha` evidence path.
- Added the initial runtime-path benchmark harness through `python3 -m kora run runtime_integrated_benchmark -- --offline`.
- Added runtime benchmark JSON output through `--json-out /tmp/kora_runtime_integrated_benchmark.json`.
- Added a Markdown evidence packet/report generator through `python3 examples/runtime_integrated_benchmark/report.py --input /tmp/kora_runtime_integrated_benchmark.json --md-out /tmp/kora_runtime_integrated_benchmark.md`.
- Added telemetry-connected runtime benchmark summaries through `python3 -m kora telemetry --input /tmp/kora_runtime_integrated_benchmark.json --json-out /tmp/kora_runtime_integrated_benchmark.telemetry.json --md-out /tmp/kora_runtime_integrated_benchmark.telemetry.md`.
- Added a reviewer-facing reproduction guide, a `v0.3.0-alpha` release-readiness checklist, and a docs cross-link and public claim-boundary audit.

### Current runtime benchmark counters

- Workload: `experiments/workloads/deterministic_heavy_v1_100.json`
- Total tasks: `100`
- Deterministic route count: `80`
- Fallback/model-candidate route count: `20`
- Simulated baseline model invocations: `100`
- KORA-controlled model invocations: `20`
- Avoided simulated model invocations: `80`
- Avoided simulated model invocation rate: `0.8`
- Deterministic outputs checked: `80`
- Mismatches: `0`
- Runtime path execution status: `ok`
- Telemetry event count: `100`

### Artifact policy

- Generated benchmark JSON, Markdown evidence packets, and telemetry summaries remain in `/tmp` or user-provided ignored output paths unless a future release task explicitly selects and reviews a frozen artifact.
- Raw generated benchmark artifacts are not committed by this draft.
- No release assets or raw benchmark artifacts should be uploaded without explicit approval.

### Claim boundary

- Safe claim: In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.
- This draft does not claim production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, energy reduction evidence, formal government validation, signed partner validation, guaranteed adoption, or guaranteed funding.

## v0.2.0-alpha benchmark evidence expansion

Status: published prerelease.

GitHub Release: https://github.com/Krako-Labs/KORA/releases/tag/v0.2.0-alpha

Related docs:

- [KORA Documentation Index](docs/README.md)
- [Experiments regeneration guide](experiments/README.md)
- [Benchmark artifact policy](docs/reports/benchmark_artifact_policy.md)
- [Raw artifact freeze decision](docs/reports/v0.2.0-alpha-raw-artifact-freeze-decision.md)

### Benchmark evidence path

- Added deterministic expected-output correctness checks to the benchmark runner.
- Added automated Markdown summary generation from benchmark result JSON artifacts.
- Added a raw benchmark artifact policy for ephemeral `/tmp` outputs, Markdown summaries, and future frozen evidence decisions.
- Expanded correctness/error/fallback benchmark coverage for deterministic success, deterministic mismatch, fallback/model-candidate skip behavior, unsupported categories, malformed deterministic input, and stable `v1_100` counters.
- Added release notes draft, readiness, merge-readiness, pre-merge review, merge-candidate validation, and raw artifact freeze decision docs for `v0.2.0-alpha`.

### Current reproducible benchmark counters

- Workload: `experiments/workloads/deterministic_heavy_v1_100.json`
- Total tasks: `100`
- Direct-baseline simulated model invocations: `100`
- KORA-controlled simulated model invocations: `20`
- Avoided simulated model invocations: `80`
- Avoided invocation rate: `80%`
- Deterministic outputs checked: `80`
- Mismatches: `0`
- Fallback/model-candidate skipped: `20`

### Claim boundary

- This is reproducible deterministic-heavy benchmark evidence.
- Safe claim: In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.
- This does not claim production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, or energy reduction evidence.

## v0.1 alpha public surface

Current public alpha snapshot for KORA.

### Public CLI surface

- `python3 -m kora examples list`
- `python3 -m kora run <example>`
- `python3 -m kora telemetry`

### Runnable examples

- `hello_kora`
- `retry_demo`
- `direct_vs_kora`
- `real_workload_harness`
- `stress_test`

### Reproducible first-run path

```bash
python3 -m kora examples list
python3 -m kora run hello_kora
python3 -m kora run retry_demo
python3 -m kora run direct_vs_kora -- --offline
python3 -m kora telemetry --input docs/reports/sample_telemetry_input.json
```

### Documentation

- The first run -> telemetry -> benchmark progression is now explicit.

### Limitations

- This is an alpha surface.
- This is not a production release.

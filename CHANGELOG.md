# Changelog

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

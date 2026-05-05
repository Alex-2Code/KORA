# Benchmark Artifact Policy

This policy covers raw benchmark result artifacts and generated Markdown summaries for the deterministic-heavy benchmark evidence path.

## Current Policy

Raw benchmark JSON artifacts are reproducible execution outputs. They should generally not be committed to the repository.

Raw JSON artifacts should remain ephemeral unless they are explicitly selected as frozen release evidence. Use `/tmp` or another ignored path for routine benchmark runs.

Markdown summaries generated from raw artifacts may be committed when they support release notes, public evidence, or reviewed technical reports. Summaries should be generated from result JSON artifacts rather than manually assembled.

Tracked workload definitions, benchmark scripts, summary scripts, tests, and documentation remain source artifacts and should stay trackable. For example, `experiments/workloads/deterministic_heavy_v1_100.json` is a tracked workload definition, not a raw benchmark result output.

## Frozen Raw Artifact Requirements

If raw benchmark JSON artifacts are ever committed as frozen release evidence, the accompanying documentation must include:

- workload id or workload path
- generator seed and generation command
- benchmark command used for each raw artifact
- date generated
- code commit used to generate the artifact
- claim boundary and non-claims

Frozen raw artifacts should be intentionally named and reviewed. They should not be added as incidental outputs from local runs.

## Claim Boundary

Current safe claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

Forbidden claims:

- production cost reduction
- real API-cost reduction
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority
- energy reduction evidence

Benchmark summaries must state that the current evidence is reproducible benchmark evidence from simulated benchmark artifacts, not production cost/API/energy proof.

## Regeneration Guide

Use `/tmp` paths for raw generated outputs unless a release process explicitly selects frozen artifacts.

Regenerate the workload from seed `42`:

```bash
python3 experiments/generate_workload.py \
  --count 100 \
  --seed 42 \
  --benchmark-name deterministic_heavy_v1 \
  --output /tmp/kora_deterministic_heavy_v1_100.regenerated.json

cmp experiments/workloads/deterministic_heavy_v1_100.json \
  /tmp/kora_deterministic_heavy_v1_100.regenerated.json
```

Run the dry-run benchmark:

```bash
python3 experiments/run_benchmark.py \
  --mode dry-run \
  --workload experiments/workloads/deterministic_heavy_v1_100.json \
  --output /tmp/kora_deterministic_heavy_v1_100.dry_run.json
```

Run the direct-baseline benchmark:

```bash
python3 experiments/run_benchmark.py \
  --mode direct-baseline \
  --workload experiments/workloads/deterministic_heavy_v1_100.json \
  --output /tmp/kora_deterministic_heavy_v1_100.direct_baseline.json
```

Run the KORA-controlled benchmark:

```bash
python3 experiments/run_benchmark.py \
  --mode kora-controlled \
  --workload experiments/workloads/deterministic_heavy_v1_100.json \
  --output /tmp/kora_deterministic_heavy_v1_100.kora_controlled.json
```

Generate a Markdown summary from raw result artifacts:

```bash
python3 experiments/summarize_benchmark_results.py \
  --direct-baseline /tmp/kora_deterministic_heavy_v1_100.direct_baseline.json \
  --kora-controlled /tmp/kora_deterministic_heavy_v1_100.kora_controlled.json \
  --output /tmp/kora_deterministic_heavy_v1_100.summary.md
```

If a generated Markdown summary is selected for public evidence, review it for the claim boundary before committing it under `docs/reports/` or another reviewed documentation location.

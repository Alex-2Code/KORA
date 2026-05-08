# KORA Social Media Announcement Guide

Date: 2026-05-08

Audience: KORA community managers, contributors, and maintainers

Current release: `v0.3.0-alpha`

Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

## Purpose

This guide keeps public KORA messaging sharp, reproducible, and claim-safe.

Use it for GitHub Discussions, LinkedIn, X/Twitter, Discord, Telegram, README-adjacent copy, and public community updates.

## Public-Safe Message Spine

Hook:

> Most AI apps call the model too soon.

Shift:

> KORA puts execution control before inference.

Mechanism:

- Task graphs.
- Deterministic-first execution.
- Validation before escalation.
- Telemetry around every path.
- Model calls only when needed.

Evidence:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Next validation:

> Now we are expanding validation across real model-call paths, support triage, RAG routing, and agent budget-guard workloads.

CTA:

> Clone the repo. Run the alpha. Inspect the path. Bring a workload.

Tagline:

> Structure first. Inference second.

## Launch Objective

The launch message should make developers and AI infrastructure builders understand one thing quickly:

KORA changes the default from model-first execution to structured execution before inference.

The release link should be paired with local reproduction and workload-testing invitations, not broad production claims.

## Strong Short Hooks

- Most AI apps call the model too soon.
- KORA changes the default.
- Structure first. Inference second.
- The model call should be a decision, not the default.
- Every request should not become a prompt by default.
- KORA puts execution control before inference.
- Clone the repo. Run the alpha. Inspect the path. Bring a workload.
- KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

## Core Message Pillars

- **Pain**: Every request becomes a prompt. Every prompt becomes tokens. Every token becomes latency, cost, and infrastructure pressure.
- **Mechanism**: KORA turns a request into a task graph, runs deterministic work first, validates the path, records telemetry, and escalates to a model only when needed.
- **Evidence**: KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.
- **Boundary**: This is alpha benchmark evidence, not a universal production cost-reduction claim.
- **Next step**: KORA needs real workload validation across runtime-integrated model-call paths, support triage, RAG answer routing, and agent budget guards.

## Channel Guidance

### LinkedIn

- Lead with the developer pain and strategic execution-control narrative.
- Include the release URL.
- Include the approved evidence claim.
- Invite real workload testing.

### X/Twitter

- Lead with the shortest hook.
- Keep the benchmark claim bounded.
- Link to the release or repo.
- Ask for workload examples, not hype.

### Discord And Telegram

- Lead with the release and one command to try.
- Ask people to bring sanitized workloads.
- Route reproduction questions to GitHub Discussions.

### GitHub Discussions

- Lead with commands, expected counters, and reproducibility.
- Ask for environment details if counters differ.
- Make the artifact policy clear.

## Post Templates

### Short Post

Most AI apps call the model too soon.

KORA changes the default: structure first, inference second.

KORA `v0.3.0-alpha` is live:

https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Clone the repo. Run the alpha. Inspect the path. Bring a workload.

### Longer Post

Most AI apps call the model too soon.

Every request becomes a prompt.
Every prompt becomes tokens.
Every token becomes latency, cost, and infrastructure pressure.

KORA is an open-source execution-control layer for AI workloads.

It turns a request into a task graph, runs deterministic work first, validates the path, records telemetry, and escalates to a model only when needed.

KORA `v0.3.0-alpha` is live:

https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

Current alpha evidence:

KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

This is alpha benchmark evidence, not a universal production cost-reduction claim.

Now we are expanding validation across real model-call paths, support triage, RAG routing, and agent budget-guard workloads.

Clone the repo. Run the alpha. Inspect the path. Bring a workload.

### GitHub Discussions Announcement

KORA `v0.3.0-alpha` is available as a GitHub prerelease:

https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

Most AI apps call the model too soon. KORA changes the default by putting execution control before inference.

Run the runtime benchmark locally:

```bash
python3 -m kora run runtime_integrated_benchmark -- --offline
```

Generate temporary JSON output:

```bash
python3 -m kora run runtime_integrated_benchmark -- --offline --json-out /tmp/kora_runtime_integrated_benchmark.json
```

Generate the Markdown evidence packet:

```bash
python3 examples/runtime_integrated_benchmark/report.py --input /tmp/kora_runtime_integrated_benchmark.json --md-out /tmp/kora_runtime_integrated_benchmark.md
```

Generate the telemetry summary:

```bash
python3 -m kora telemetry --input /tmp/kora_runtime_integrated_benchmark.json --json-out /tmp/kora_runtime_integrated_benchmark.telemetry.json --md-out /tmp/kora_runtime_integrated_benchmark.telemetry.md
```

Expected runtime counters:

- `total_tasks`: 100
- `deterministic_route_count`: 80
- `fallback_or_model_candidate_route_count`: 20
- `simulated_baseline_model_invocations`: 100
- `kora_controlled_model_invocations`: 20
- `avoided_simulated_model_invocations`: 80
- `avoided_simulated_model_invocation_rate`: 0.8
- `deterministic_outputs_checked`: 80
- `mismatch_count`: 0
- `runtime_path_execution_status`: ok
- `telemetry_event_count`: 100

If your counters differ, please open a Benchmark Reproduction discussion with your command, environment, and expected vs actual output.

## Technical Visual Placeholders

Do not generate final marketing images as part of this guide. Use technical diagrams and placeholders that can be reviewed in the repo.

Preferred asset paths:

- `docs/assets/kora-execution-control-overview.svg`
- `docs/assets/kora-validation-roadmap.svg`
- `docs/assets/kora-benchmark-evidence-card.svg`
- `docs/assets/kora-help-test-flow.svg`

Image guidance:

- README image: model-first vs KORA-controlled path
- validation roadmap image: current alpha -> real model-call runtime -> support triage -> RAG routing -> agent budget guard
- benchmark evidence image: 100 tasks / 80 avoided / 20 model-candidate or escalation path / 0 deterministic mismatches
- help-test image: bring workload -> map deterministic paths -> define escalation rules -> run KORA -> inspect telemetry -> share results

Avoid:

- generic AI brain
- fantasy AI art
- crypto/NFT style
- gold 3D text
- people/robot mascot
- exaggerated cost/energy saving imagery
- money icons
- GPU savings icons
- energy-saving icons
- unreadable tiny labels

## Reply Templates

### Does this reduce real API cost?

Not yet. The current milestone is alpha benchmark evidence, not real API-cost proof. The best way to evaluate this release is to run the local command and inspect the generated evidence packet.

### Is this production benchmark evidence?

No. The current claim is bounded to a reproducible deterministic-heavy benchmark workload. It is not production benchmark proof.

### Does this prove energy savings?

No. KORA is not making energy-reduction claims from this milestone.

### Can I upload my benchmark JSON?

Please keep generated JSON/Markdown outputs local unless a maintainer asks for a specific artifact. The release does not upload raw benchmark artifacts as assets.

### Can I compare my own workload?

Yes. Sanitized own-workload experiments are welcome, but label them as your own experiment unless they are reviewed and documented as official KORA evidence.

### My counters are different.

Open a Benchmark Reproduction discussion with your command, environment, and expected vs actual counters. Maintainers should review mismatch reports.

## Boundary Reminder

Approved public benchmark claim:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Do not claim:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority proof
- energy reduction evidence
- formal government validation
- signed partner validation unless actually signed and documented
- guaranteed adoption or funding

Keep launch posts focused on reproducible benchmark evidence, validation next steps, and workload invitations.

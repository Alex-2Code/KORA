# KORA Social Media Announcement Guide

Date: 2026-05-07

Audience: Sumanta and KORA community managers

Current release: `v0.3.0-alpha`

Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

## Purpose

This guide helps the KORA community manager announce `v0.3.0-alpha` safely on social and community channels such as LinkedIn, X/Twitter, Discord, Telegram, GitHub Discussions, and similar public forums.

It is a public messaging and claim-control guide. Use it to share the release clearly while keeping benchmark, artifact, and release boundaries intact.

## Current Release Facts

- Release: `v0.3.0-alpha`
- Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha
- GitHub prerelease: `true`
- Release assets: none
- Raw benchmark artifacts uploaded: none
- Package version unchanged: `0.1.0a0`

## Core Message Pillars

- KORA is an open-source execution-control layer.
- `v0.3.0-alpha` adds an initial runtime-path benchmark evidence flow.
- The release includes a runtime benchmark command, JSON output path, Markdown evidence packet/report generation, and telemetry-connected summary.
- The evidence is reproducible locally.
- Claims are intentionally bounded and transparent.
- Generated benchmark outputs should stay in `/tmp` or user-provided paths unless explicitly approved otherwise.

## Safe Benchmark Claim

Use this exact benchmark claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

Do not remove the workload boundary or present this as production evidence.

## Must-Not-Say List

Do not state or imply:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority proof
- energy reduction evidence
- formal government validation
- signed partner validation
- guaranteed adoption or funding

## Approved Short Social Post

KORA `v0.3.0-alpha` is out as a GitHub prerelease:

https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

This release adds an initial runtime-path benchmark evidence flow with a reproducible local path for JSON output, Markdown evidence packet generation, and telemetry summary.

Current bounded claim: In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

This is non-production benchmark evidence and does not claim production cost reduction or real API-cost reduction proof.

## Approved Longer LinkedIn-Style Post

Many LLM-first systems send work to a model even when part of the request could be handled deterministically first.

KORA takes a different direction: it is an open-source execution-control layer that structures work into task graphs, runs deterministic steps first, validates outputs, and escalates to model inference only when needed.

`v0.3.0-alpha` is now available as a GitHub prerelease:

https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

This prerelease adds an initial runtime-path benchmark evidence flow:

- runtime benchmark command
- JSON output path
- Markdown evidence packet/report generation
- telemetry-connected summary
- reviewer-facing local reproduction path

Current bounded benchmark claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

The evidence is intentionally bounded. It is not production benchmark evidence, does not prove real API-cost reduction, does not prove production cost reduction, and does not prove energy reduction.

If you want to review the evidence path, reproduce it locally from the release and keep generated JSON/Markdown outputs in `/tmp` or another local output path.

## GitHub Discussions Announcement Draft

KORA `v0.3.0-alpha` is available as a GitHub prerelease:

https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

This prerelease adds the initial runtime-path benchmark evidence flow. It includes a reproducible local path for generating runtime benchmark JSON, a Markdown evidence packet, and telemetry summary output.

Run the benchmark locally:

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

Current bounded benchmark claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

This is bounded, non-production benchmark evidence. It does not claim production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, or energy reduction evidence.

Please post reproduction questions in Discussions and include the command run, environment notes, and expected vs actual counters.

## X/Twitter Thread Draft

1. KORA `v0.3.0-alpha` is available as a GitHub prerelease: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

2. KORA is an open-source execution-control layer. The direction is structure first, inference second.

3. This prerelease adds an initial runtime-path benchmark evidence flow: offline runtime command, JSON output path, Markdown evidence packet generation, and telemetry summary.

4. Current bounded claim: in a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

5. Boundary: this is non-production benchmark evidence. It does not prove production cost reduction, real API-cost reduction, broad workload superiority, or energy reduction.

6. Reproduce locally from the release and share questions in GitHub Discussions.

## Discord/Telegram Announcement Draft

KORA `v0.3.0-alpha` is now available as a GitHub prerelease:

https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

This release adds an initial runtime-path benchmark evidence flow with local JSON output, Markdown evidence packet generation, and telemetry summary commands.

Current bounded claim: In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

This is bounded, non-production evidence. It does not claim production cost reduction, real API-cost reduction, or energy reduction proof.

Please reproduce locally and share questions in GitHub Discussions.

## Comment Reply Templates

### Does this reduce real API cost?

The current evidence does not prove real API-cost reduction. The public claim is limited to a reproducible 100-task deterministic-heavy benchmark workload with simulated model invocation counters. Real API-cost evaluation would require a separate approved evidence path.

### Is this production benchmark evidence?

No. The current release provides bounded, non-production benchmark evidence and a reproducible local evidence-generation path. It should not be described as production benchmark proof.

### Does this prove energy savings?

No. KORA does not currently claim energy reduction evidence. Please keep discussion limited to the documented benchmark and telemetry counters.

### Can I upload my benchmark JSON?

Please do not upload raw benchmark artifacts as release assets or treat them as official release artifacts. Keep generated JSON/Markdown outputs local unless a maintainer explicitly asks for a specific artifact for review.

### How do I reproduce this locally?

Use the offline runtime benchmark command:

```bash
python3 -m kora run runtime_integrated_benchmark -- --offline
```

For the full local evidence path, generate JSON, then the Markdown report, then telemetry summary using the commands in the GitHub Discussions announcement draft above.

### Can I compare my own workload?

Yes, but describe it as your own experiment unless it has been reviewed and documented as part of KORA's official evidence path. Do not present external workload results as official KORA release evidence without maintainer review.

### Where should I ask questions?

Use GitHub Discussions for reproduction questions, ideas, and community support. Open an Issue only when you have an actionable bug report, documentation fix, benchmark mismatch, or scoped feature proposal.

## Hashtag Suggestions

Conservative hashtags:

- `#OpenSource`
- `#AIInfrastructure`
- `#LLMOps`
- `#DeveloperTools`
- `#Benchmarking`
- `#Reproducibility`

Avoid hype hashtags that imply guaranteed cost reduction, energy reduction, production validation, or broad workload superiority.

## Visual/Post Asset Guidance

- Use the release URL and GitHub repo screenshots if helpful.
- Do not create graphs implying production cost or energy savings.
- Do not show raw benchmark artifacts as official release assets.
- If showing counters, label them as reproducible non-production benchmark counters.
- Do not imply that generated local artifacts were uploaded as release assets.

## Escalation Rule

Escalate to maintainers if:

- someone makes production, API-cost, or energy claims
- someone reports mismatched counters
- someone wants to upload raw benchmark artifacts
- a journalist or investor asks for production numbers
- someone asks for partner or government validation
- someone asks whether KORA is proven in production
- someone proposes changing release assets, package version, tag state, or claim wording

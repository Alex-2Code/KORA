# KORA Community Manager Guide

Date: 2026-05-08

Current release: `v0.3.0-alpha`

Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

## Purpose

This public guide helps contributors and maintainers keep KORA community responses accurate, useful, and claim-safe.

KORA is an open-source execution-control layer for AI workloads. Public community guidance should point people toward the repo, the quickstart, the validation roadmap, and the bounded benchmark evidence.

## Public Message

Use this message spine:

- Most AI apps call the model too soon.
- KORA changes the default.
- Structure first. Inference second.

KORA turns AI requests into structured execution paths before inference: task graphs, deterministic-first execution, validation, telemetry, and model escalation only when needed.

## Current Alpha Evidence

Approved public claim:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Keep the workload boundary attached to the claim. Do not restate it as a production result, a real API-cost result, or a universal workload result.

## What To Say

Public KORA responses may say:

- KORA `v0.3.0-alpha` is available as a GitHub prerelease.
- KORA is designed around execution control before inference.
- The current evidence is bounded to a reproducible deterministic-heavy alpha benchmark workload.
- KORA is expanding validation across real model-call runtime paths, support triage, RAG routing, and agent budget-guard workloads.
- Developers can clone the repo, run the alpha, inspect the execution path, and bring a sanitized workload for discussion.

## What Not To Say

Do not state or imply:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority proof
- energy reduction evidence
- formal government validation
- signed partner validation unless actually signed and documented
- guaranteed adoption, funding, or support commitments

## Routing Community Questions

Use GitHub Discussions for:

- setup questions
- benchmark reproduction questions
- workload ideas
- contributor questions
- public clarification around KORA's roadmap

Use GitHub Issues for:

- reproducible bugs
- focused documentation fixes
- scoped feature proposals
- benchmark reproduction mismatches with exact commands and outputs

For security issues, use the process in `SECURITY.md`.

## Public Reply Examples

### What Is KORA?

KORA is an open-source execution-control layer for AI workloads. It turns requests into structured execution paths before inference, so deterministic work, validation, telemetry, and escalation rules happen before a model call becomes necessary.

### What Does The 80% Result Mean?

The current approved public claim is: KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload. That is alpha benchmark evidence, not a universal production cost-reduction claim.

### How Can I Test My Workload?

Start with the README quickstart, run the offline examples, and review `docs/community/help-test-kora.md`. Please use sanitized examples and do not share secrets, API keys, private user data, or proprietary datasets in public channels.

### Is KORA Production-Proven?

No. KORA is alpha software. The current evidence is bounded to the documented deterministic-heavy benchmark workload, and the next validation work is focused on runtime-integrated model-call paths and real workload testing.

### Is KORA An Agent Framework?

KORA is not primarily an agent framework. It is an execution-control layer that helps decide when deterministic work, validation, telemetry, and model escalation should happen in an AI workload.

## Major Reply Checklist

Before posting a substantial public reply, check:

- Is the approved benchmark claim worded with its workload boundary?
- Does the reply avoid production cost, real API-cost, energy, and broad superiority claims?
- Does it avoid asking for secrets, private user data, or proprietary datasets?
- Does it route concrete bugs to Issues and exploratory discussion to Discussions?
- Does it link to public docs rather than private operating material?

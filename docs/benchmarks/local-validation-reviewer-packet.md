# Local No-Network Validation Reviewer Packet

## Purpose

This packet helps reviewers reproduce KORA's local/no-network validation path without API keys, external providers, private data, or network calls.

It is intended for technical review of the current validation plumbing: routing decisions, aggregate model-call counters, and Markdown report generation from synthetic workloads.

## What This Packet Shows

- A direct baseline records deterministic local validation adapter events for every request.
- A KORA-controlled path avoids model-call events for deterministic routes.
- The customer-support triage workload demonstrates an application-shaped synthetic workload.
- Markdown reports are generated from aggregate counters.

## What This Packet Does Not Show

This packet is not real provider validation, not real API-cost reduction evidence, not production validation, not production cost-reduction proof, not energy-reduction evidence, and not broad workload superiority proof.

This packet is not:

- real provider validation
- real API-cost reduction evidence
- production validation
- production cost-reduction proof
- energy-reduction evidence
- broad workload superiority proof

## Prerequisites

- A Python environment that can run the KORA test suite and CLI.
- An editable install or local package setup if your environment does not already resolve `python3 -m kora`.
- No API keys required.
- No provider credentials required.
- No network access required for these validation examples.

## Quick Start Commands

```bash
python3 -m kora --help
python3 -m kora examples list

python3 -m kora run real_model_call_validation_fake -- --offline
python3 -m kora run customer_support_triage_fake_validation -- --offline
```

## Generate Reviewer Reports

```bash
python3 -m kora run real_model_call_validation_fake -- --offline --report-md /tmp/kora_local_validation.md

python3 -m kora run customer_support_triage_fake_validation -- --offline --report-md /tmp/kora_customer_support_validation.md
```

Reports are written only when `--report-md` is provided. Use `/tmp` or another local output path for generated artifacts unless a report is intentionally selected for review.

Generated reports are not committed by default. They contain aggregate counters and boundary language. They do not contain raw prompts, raw provider responses, secrets, or private data.

## Adapter Selection

The local validation examples default to the `local_validation` adapter.

```bash
python3 -m kora run real_model_call_validation_fake -- --offline --adapter local_validation
python3 -m kora run customer_support_triage_fake_validation -- --offline --adapter local_validation
```

The `blocked` and `local_runtime_placeholder` adapter kinds are fail-closed safety paths. `blocked` represents an unconfigured model-call path. `local_runtime_placeholder` is design-only, makes no runtime calls, and does not contact local HTTP endpoints, subprocess runtimes, remote providers, or provider APIs.

## Expected Generic Local Validation Counters

For `real_model_call_validation_fake`, expected counters are:

| Counter | Expected value |
|---|---:|
| `total_requests` | 10 |
| `baseline_model_calls` | 10 |
| `kora_model_calls` | 4 |
| `avoided_model_calls` | 6 |
| `avoided_model_call_rate` | 0.6 |
| `deterministic_routes` | 6 |
| `model_escalations` | 4 |

Expected labels:

- `provider`: `local_validation`
- `model`: `deterministic-local`

## Expected Customer-Support Triage Counters

For `customer_support_triage_fake_validation`, expected counters are:

| Counter | Expected value |
|---|---:|
| `total_requests` | 12 |
| `baseline_model_calls` | 12 |
| `kora_model_calls` | 4 |
| `avoided_model_calls` | 8 |
| `avoided_model_call_rate` | 0.6667 |
| `deterministic_routes` | 8 |
| `model_escalations` | 4 |

Expected labels:

- `provider`: `local_validation`
- `model`: `deterministic-local`

## How To Read The Counters

- `baseline_model_calls`: model-call events recorded by the direct baseline path.
- `kora_model_calls`: model-call events recorded by the KORA-controlled path.
- `avoided_model_calls`: `baseline_model_calls - kora_model_calls`.
- `avoided_model_call_rate`: `avoided_model_calls / baseline_model_calls`.
- `deterministic_routes`: requests handled through deterministic routing.
- `model_escalations`: requests routed to the deterministic local validation adapter.
- `validation_pass_count`: route or response checks that passed.
- `validation_fail_count`: route or response checks that failed.
- `error_count`: runtime errors counted during the example.
- `fallback_count`: requests that fell back because the route was unsupported or unresolved.

## Privacy And Artifact Handling

- Do not include secrets.
- Do not include API keys.
- Do not include private data.
- Do not include raw provider responses.
- Do not use real customer data.
- Do not use proprietary datasets.
- Review generated local reports before sharing them.

## Claim-Safe Language

Allowed:

> KORA's local no-network validation examples show that KORA can measure avoided model-call events in synthetic workloads.

Allowed:

> In the customer-support triage synthetic workload, the local validation path records 8 avoided model-call events out of 12 requests.

Not allowed:

- KORA reduces production AI costs by 66.7%.
- KORA reduces real API costs by 66.7%.
- KORA is production-proven for customer support.
- KORA reduces energy consumption.
- KORA has real provider validation from this packet.

## Troubleshooting

- Command not found: confirm you are in the KORA repository and the package is importable with `python3 -m kora --help`.
- Editable install missing: install the project in editable mode if your environment does not resolve local modules.
- Example not listed: run `python3 -m kora examples list` from a fresh checkout of `origin/main`.
- Report path not writable: use `/tmp` or another writable local directory.
- Stale checkout: run `git fetch origin` and confirm your local branch is current.
- Expected counters differ: confirm you are running with `--offline` and have not modified the synthetic workload files.

## Next Validation Step

The next step after this packet is a local model adapter or remote provider adapter using the same reporting structure, while preserving privacy and claim boundaries.

The reviewer packet commands still use local/no-network validation. Local runtime adapters remain design-only and fail-closed until a concrete adapter is implemented and validated.

See the [local model adapter design](local-model-adapter-design.md) for the next local runtime pathway after local/no-network validation.

# Real Model-Call Runtime Validation Report

## Date

`YYYY-MM-DD`

## Workload

- Workload name:
- Workload path:
- Workload type:
- Workload privacy class: `synthetic | sanitized | private_do_not_commit`

Do not paste raw API keys, raw private prompts, raw private responses, or proprietary datasets into this report.

## Mode

Select one:

- `offline`
- `local_model`
- `remote_provider`

## Provider/runtime

Optional:

- Provider/runtime:

## Model

Optional:

- Model:

## Environment

Sanitized environment details:

- KORA commit:
- Python version:
- Operating system:
- Adapter mode:
- Adapter:
- Model-call counter source:
- Token counter source:
- Provider configuration source: environment variables only, if remote provider mode is used

For the local no-network validation example, use:

- Mode: `local_no_network_model_call_validation`
- Provider/runtime: `local_validation`
- Model: `deterministic-local`
- Cost summary: `N/A` unless a real provider with explicit pricing is configured later

For the customer-support triage local validation example, use:

- Mode: `customer_support_triage_local_validation`
- Workload: `customer_support_triage_synthetic_v1`
- Provider/runtime: `local_validation`
- Model: `deterministic-local`
- Cost summary: `N/A` unless a real provider with explicit pricing is configured later

Do not include API keys, tokens, credentials, private hostnames, private dataset names, or raw provider response IDs unless explicitly approved.

## Generated Local Validation Reports

Local no-network validation examples can generate reviewer-facing Markdown reports from aggregate counters:

```bash
python3 -m kora run customer_support_triage_fake_validation -- --offline --report-md /tmp/kora_customer_support_validation.md
python3 -m kora run real_model_call_validation_fake -- --offline --report-md /tmp/kora_local_validation.md
```

Write generated reports to `/tmp` or another local output path unless the report is intentionally selected for review. Generated reports should not include secrets, raw provider responses, private data, production data, or raw prompts.

## Commands

```bash
# Direct baseline command

# KORA-controlled command

# Report generation command
```

## Summary Counters

| Counter | Value | Notes |
|---|---:|---|
| `total_requests` |  |  |
| `baseline_model_calls` |  |  |
| `kora_model_calls` |  |  |
| `avoided_model_calls` |  |  |
| `avoided_model_call_rate` |  |  |
| `validation_pass_count` |  |  |
| `validation_fail_count` |  |  |
| `error_count` |  |  |
| `fallback_count` |  |  |
| `latency_p50_ms` |  |  |
| `latency_p95_ms` |  |  |

## Baseline Result

Describe the direct baseline result.

Expected baseline:

```text
request -> model -> output -> validation -> telemetry
```

Include:

- total requests
- model calls
- validation result
- errors
- latency summary
- token summary, if available

## KORA-Controlled Result

Describe the KORA-controlled result.

Expected KORA-controlled path:

```text
request -> task graph -> deterministic path or model escalation -> validation -> telemetry
```

Include:

- deterministic routes
- model escalations
- KORA model calls
- validation result
- errors
- fallbacks
- latency summary
- token summary, if available

## Avoided Model Calls

Formula:

```text
avoided_model_calls = baseline_model_calls - kora_model_calls
avoided_model_call_rate = avoided_model_calls / baseline_model_calls
```

Result:

- Avoided model calls:
- Avoided model-call rate:

## Validation Result

Summarize:

- validation pass count
- validation fail count
- expected-output checks
- expected-property checks
- semantic validation method, if used

Do not include raw private prompts or raw private responses.

## Errors And Fallbacks

Summarize:

- error count
- fallback count
- timeout count, if available
- provider error count, if available
- validation failure examples using sanitized summaries only

## Latency Summary

| Metric | Baseline | KORA-controlled |
|---|---:|---:|
| total latency ms |  |  |
| p50 latency ms |  |  |
| p95 latency ms |  |  |

## Token Summary If Available

| Metric | Baseline | KORA-controlled |
|---|---:|---:|
| input tokens |  |  |
| output tokens |  |  |
| total tokens |  |  |

If token counters are unavailable for the selected adapter, state that clearly.

## Cost Summary If Explicitly Configured

Estimated cost may be included only if provider pricing is explicitly configured.

Measured cost may be included only if provider billing data is explicitly supplied later and approved for reporting.

| Metric | Baseline | KORA-controlled |
|---|---:|---:|
| estimated cost |  |  |
| measured cost |  |  |

Do not infer real API-cost reduction from token estimates alone.

## Privacy And Artifact Handling

Confirm:

- [ ] No API keys are included.
- [ ] No credentials are included.
- [ ] No raw private prompts are included.
- [ ] No raw private responses are included.
- [ ] No proprietary datasets are included.
- [ ] Workload is synthetic or sanitized if committed.
- [ ] Generated raw JSON remains in `/tmp` or another ignored path unless explicitly approved.
- [ ] Report includes claim boundary.

## Claim-Safe Language

Allowed after successful reviewed validation:

> KORA reduced measured model invocations by X% in a runtime-integrated validation workload using real model calls.

Use only after the actual value, workload, commands, counters, and report have been reviewed.

## Non-Claims

This report does not claim:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence unless separately reviewed and approved
- broad workload superiority proof
- energy reduction evidence
- provider-specific performance endorsement
- production validation

Do not write:

- KORA reduces production AI costs by X%.
- KORA reduces real API costs by X%.
- KORA reduces energy consumption by X%.
- KORA is production-proven.

## Reproduction Notes

Include:

- exact commit
- commands
- workload path
- adapter mode
- sanitized environment details
- known limitations
- whether the run used offline, local model, or remote provider mode

## Reviewer Notes

Reviewer:

Review date:

Checklist:

- [ ] Commands reproduce.
- [ ] Counters are internally consistent.
- [ ] Direct baseline and KORA-controlled path are both included.
- [ ] Claim boundary is included.
- [ ] No secrets or private data are included.
- [ ] Claim language is checked against `docs/claims/kora-claim-registry.md`.

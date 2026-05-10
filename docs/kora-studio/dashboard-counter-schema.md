# KORA Studio Dashboard Counter Schema

## Purpose

This document defines the initial counter fields that a future KORA Studio dashboard can display from local validation summaries and report artifacts.

## Counter Fields

| Field | Display label | Definition |
|---|---|---|
| `total_requests` | Total requests | Number of requests or tasks in the local validation run. |
| `baseline_model_calls` | Baseline model calls | Model-call events recorded by the direct baseline path. |
| `kora_model_calls` | KORA model calls | Model-call events recorded by the KORA-controlled path. |
| `avoided_model_calls` | Avoided model calls | Difference between baseline model calls and KORA model calls. |
| `avoided_model_call_rate` | Avoided model-call rate | Avoided model calls divided by baseline model calls when available. |
| `deterministic_routes` | Deterministic routes | Requests handled by deterministic or fast local paths. |
| `model_escalations` | Model escalations | Requests escalated to the selected model-call path. |
| `validation_pass_count` | Validation passes | Validation checks that passed. |
| `validation_fail_count` | Validation failures | Validation checks that failed. |
| `error_count` | Errors | Runtime or validation errors counted by the example. |
| `fallback_count` | Fallbacks | Requests that fell back because the route was unsupported or unresolved. |

## Example JSON Object

```json
{
  "total_requests": 12,
  "baseline_model_calls": 12,
  "kora_model_calls": 4,
  "avoided_model_calls": 8,
  "avoided_model_call_rate": 0.6667,
  "deterministic_routes": 8,
  "model_escalations": 4,
  "validation_pass_count": 12,
  "validation_fail_count": 0,
  "error_count": 0,
  "fallback_count": 0,
  "mode": "customer_support_triage_local_validation",
  "provider": "local_validation",
  "model": "deterministic-local",
  "no_network": true
}
```

## Claim-Safe Display Rules

- label local/no-network counters clearly
- describe counters as model-call events unless a later adapter provides validated measured local model calls
- do not convert counters into production cost claims
- do not convert counters into real API-cost claims
- do not convert counters into energy claims
- do not show billing fields in v0.1
- keep report boundary language visible near summary cards

## Cost and Energy Boundary

No cost or energy conversion should be displayed without separately validated evidence, reviewed methodology, and approved claim language.

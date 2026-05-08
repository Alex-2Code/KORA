# Customer-Support Triage Workload

## Purpose

This is the first application-oriented validation workload spec for KORA. It uses synthetic customer-support requests to test deterministic-first routing and conditional model escalation.

The goal is to define how KORA can route repetitive support requests through structured execution paths before inference.

## Why Customer Support

Customer-support queues often contain repeated requests that follow known policies, structured flows, or lookup patterns.

Many requests can be handled by deterministic routing, policy checks, templates, or validated lookup placeholders. Ambiguous, novel, multi-intent, or policy-sensitive requests should escalate to a model only when needed.

That makes customer-support triage a practical first workload for KORA execution-control validation.

## Workload Status

This document defines a synthetic workload spec.

It is:

- synthetic workload design
- not production traffic
- not based on private customer data
- not a production-cost claim
- not a real API-cost claim
- intended for future fake, local, or real model-call validation

## Routing Classes

### 1. `deterministic_faq`

Examples:

- password reset
- refund policy link
- shipping status instructions
- account email change instructions

Expected route: `deterministic`

Model call should be avoided when the request matches a known FAQ intent.

Validation rule concept: confirm the response type and required help-center link or instruction key.

Escalation rule concept: escalate if intent confidence is low, the request includes multiple intents, or the user asks for a policy exception.

### 2. `deterministic_policy`

Examples:

- standard return window
- warranty eligibility rule
- cancellation deadline rule

Expected route: `deterministic`

Model call should be avoided when the request maps to an explicit policy table or rule.

Validation rule concept: confirm the returned policy value matches the documented policy key.

Escalation rule concept: escalate if the request asks for an exception, includes missing facts, or conflicts with a policy boundary.

### 3. `structured_lookup`

Examples:

- order status lookup placeholder
- invoice lookup placeholder
- subscription plan lookup placeholder

Expected route: `deterministic`

Model call should be avoided when the request can be routed to a structured lookup placeholder or known backend path.

Validation rule concept: confirm the lookup placeholder or route key is present.

Escalation rule concept: escalate if the lookup fails, the account context is missing, or the request contains policy-sensitive follow-up content.

### 4. `model_required`

Examples:

- ambiguous complaint
- unusual edge case
- sensitive escalation
- missing information
- multi-intent request

Expected route: `model_required`

Model call should not be avoided when deterministic rules cannot safely resolve the request.

Validation rule concept: confirm an escalation reason is present and the response is marked for review or model handling.

Escalation rule concept: escalate when the request is ambiguous, policy-sensitive, missing required information, or asks for a nuanced response.

## Synthetic Request Schema

Each synthetic request should use this conceptual schema:

- `request_id`
- `input`
- `route_class`
- `expected_route`: `deterministic` or `model_required`
- `deterministic_handler`
- `validation_rule`
- `expected_response_type`
- `privacy_class`: `synthetic`
- `notes`

Example:

```json
[
  {
    "request_id": "cst-001",
    "input": "I need help resetting my password.",
    "route_class": "deterministic_faq",
    "expected_route": "deterministic",
    "deterministic_handler": "faq.password_reset",
    "validation_rule": "required_link_present",
    "expected_response_type": "faq_instruction",
    "privacy_class": "synthetic",
    "notes": "Known FAQ intent."
  },
  {
    "request_id": "cst-002",
    "input": "Can I return an unopened item after 20 days?",
    "route_class": "deterministic_policy",
    "expected_route": "deterministic",
    "deterministic_handler": "policy.standard_return_window",
    "validation_rule": "policy_value_matches",
    "expected_response_type": "policy_answer",
    "privacy_class": "synthetic",
    "notes": "Explicit policy table route."
  },
  {
    "request_id": "cst-003",
    "input": "Please check order ORDER-EXAMPLE-001.",
    "route_class": "structured_lookup",
    "expected_route": "deterministic",
    "deterministic_handler": "lookup.order_status_placeholder",
    "validation_rule": "lookup_placeholder_present",
    "expected_response_type": "lookup_placeholder",
    "privacy_class": "synthetic",
    "notes": "Synthetic lookup placeholder only."
  },
  {
    "request_id": "cst-004",
    "input": "I was charged twice and I am upset. I also need to change my plan.",
    "route_class": "model_required",
    "expected_route": "model_required",
    "deterministic_handler": null,
    "validation_rule": "escalation_reason_present",
    "expected_response_type": "model_escalation",
    "privacy_class": "synthetic",
    "notes": "Multi-intent complaint requiring model escalation."
  }
]
```

## Example Synthetic Workload

| request_id | input summary | route_class | expected_route | deterministic_handler or escalation reason | validation_rule |
|---|---|---|---|---|---|
| `cst-001` | Password reset instructions | `deterministic_faq` | `deterministic` | `faq.password_reset` | `required_link_present` |
| `cst-002` | Refund policy link request | `deterministic_faq` | `deterministic` | `faq.refund_policy_link` | `required_link_present` |
| `cst-003` | Shipping status instructions | `deterministic_faq` | `deterministic` | `faq.shipping_status_instructions` | `response_type_matches` |
| `cst-004` | Account email change instructions | `deterministic_faq` | `deterministic` | `faq.account_email_change` | `response_type_matches` |
| `cst-005` | Standard return window | `deterministic_policy` | `deterministic` | `policy.standard_return_window` | `policy_value_matches` |
| `cst-006` | Warranty eligibility rule | `deterministic_policy` | `deterministic` | `policy.warranty_eligibility` | `policy_value_matches` |
| `cst-007` | Order status placeholder | `structured_lookup` | `deterministic` | `lookup.order_status_placeholder` | `lookup_placeholder_present` |
| `cst-008` | Invoice lookup placeholder | `structured_lookup` | `deterministic` | `lookup.invoice_placeholder` | `lookup_placeholder_present` |
| `cst-009` | Ambiguous complaint | `model_required` | `model_required` | ambiguous complaint needs nuanced response | `escalation_reason_present` |
| `cst-010` | Unusual policy edge case | `model_required` | `model_required` | policy exception request | `escalation_reason_present` |
| `cst-011` | Sensitive escalation | `model_required` | `model_required` | sensitive customer escalation | `escalation_reason_present` |
| `cst-012` | Missing information and multi-intent request | `model_required` | `model_required` | missing facts and multi-intent routing | `escalation_reason_present` |

## Direct Baseline

A naive direct baseline sends every support request to the model.

For this 12-request synthetic workload, the direct baseline would use 12 model calls.

## KORA-Controlled Path

KORA routes:

```text
request -> task graph -> deterministic handler or model escalation -> validation -> telemetry
```

For this workload design, deterministic FAQ, policy, and structured lookup requests should use deterministic handlers. Ambiguous, unusual, sensitive, or incomplete requests should use model escalation.

## Expected Counters

For the 12-request synthetic workload, expected ideal routing is:

- `total_requests`: 12
- `baseline_model_calls`: 12
- `kora_model_calls`: 4
- `avoided_model_calls`: 8
- `avoided_model_call_rate`: 0.6667
- `deterministic_routes`: 8
- `model_escalations`: 4
- `validation_pass_count`: TBD until implemented
- `validation_fail_count`: TBD until implemented
- `error_count`: TBD until implemented

These are workload-design expectations, not measured production results.

## Fake Runtime Validation Example

Run the no-network customer-support triage fake validation example:

```bash
python3 -m kora run customer_support_triage_fake_validation -- --offline
```

Expected counters for the current synthetic workload:

- `total_requests`: 12
- `baseline_model_calls`: 12
- `kora_model_calls`: 4
- `avoided_model_calls`: 8
- `avoided_model_call_rate`: 0.6667

This example uses `DeterministicFakeModelCallAdapter` with synthetic data only. It is fake, local, and no-network validation for the routing and model-call counter path.

It does not prove real provider validation, real API-cost reduction, production validation, production cost reduction, broad workload superiority, or energy reduction.

## Validation Rules

Example validation rules:

- `response_type_matches`
- `required_link_present`
- `policy_value_matches`
- `lookup_placeholder_present`
- `escalation_reason_present`
- `no_private_data_emitted`

## Telemetry Fields

Expected telemetry fields:

- `route_class`
- `selected_route`
- `model_call_used`
- `validation_result`
- `escalation_reason`
- `deterministic_handler`
- `latency_ms`
- `error`
- `fallback_used`

## Privacy and Safety

This workload must use:

- no private customer data
- no real tickets
- no credentials
- no raw production logs
- no proprietary datasets
- sanitized or synthetic data only

## Claim Boundaries

This workload can support future measured model-invocation reduction claims only after implementation and validation.

Allowed future language after validation:

> KORA reduced measured model invocations by X% in a synthetic customer-support triage validation workload.

Not allowed:

- KORA reduces customer-support costs by X%.
- KORA reduces production support API costs by X%.
- KORA is production-proven for customer support.
- KORA replaces human support agents.

## Next Implementation Step

Next implementation work should:

1. Implement the synthetic workload file as a runnable validation path.
2. Wire the workload into `DeterministicFakeModelCallAdapter`.
3. Compare direct baseline and KORA-controlled routing.
4. Emit a JSON summary and Markdown report.

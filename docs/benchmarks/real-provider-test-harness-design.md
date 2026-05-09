# Real Provider Test Harness Design

## Purpose

This packet defines a design-only dry-run test harness for future real provider adapter validation.

The harness exists to test provider adapter boundaries, fixture rules, reporting shape, fail-closed behavior, and approval gates before any real provider implementation is added.

This document does not implement provider calls, network calls, HTTP clients, subprocess runtimes, provider credential handling, external model downloads, provider dependencies, or raw benchmark artifacts.

KORA includes a small schema validator for dry-run fixture metadata in `kora/provider_fixture.py`. The validator is local and non-executing: it checks fixture shape, counters, and safety flags, but it does not construct provider requests, load credentials, call providers, call network endpoints, invoke subprocess runtimes, or download models.

## Non-Goals

This packet does not provide:

- real provider validation
- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated real-provider benchmark evidence
- broad workload superiority proof
- energy reduction evidence
- provider-specific performance endorsement

It also does not add runnable provider adapters, credential loading, provider SDKs, local model runtimes, remote endpoints, subprocess execution, or model downloads.

## Dry-Run-First Harness Lifecycle

The future harness should move through these phases in order:

1. Load a synthetic workload.
2. Load documentation-only provider fixtures.
3. Validate fixture schema and safety rules.
4. Route requests through direct-baseline and KORA-controlled plans.
5. Count baseline candidate events.
6. Count KORA routed events.
7. Count provider-attempted events as zero in dry-run mode.
8. Count provider-blocked events for every provider path that would require real execution.
9. Emit aggregate dry-run counters and claim-boundary language.
10. Fail closed if any fixture contains prohibited content.

Dry-run mode should never construct, send, replay, or simulate a raw provider request. It should only exercise the control-plane contract that decides what would be eligible for provider execution after a later, separately approved implementation.

## Fixture Schema

Dry-run fixtures should describe metadata and expected counter behavior, not provider payloads.

Supported dry-run contract fields:

- `fixture_version`
- `provider_label`: fake provider name only
- `model_label`: fake model name only
- `mode`: `dry_run` or `fixture`
- `request_id`
- `baseline_candidate_events`
- `kora_routed_events`
- `avoided_model_call_events`
- `provider_attempted_events`
- `provider_blocked_events`
- `no_network`: must be `true`
- `no_provider_call`: must be `true`
- `contains_real_provider_response`: must be `false`
- `contains_customer_data`: must be `false`
- `contains_secret_material`: must be `false`
- `notes`: safe explanatory strings only

Design-only harnesses may wrap this per-request contract in a larger fixture envelope with fields such as:

- `fixture_id`
- `workload_id`
- `privacy_class`: `synthetic` or `sanitized`
- `requests`
- `expected_counters`
- `claim_boundary`
- `artifact_policy`

Minimal validator input example:

```json
{
  "fixture_version": "0.1",
  "provider_label": "example-provider",
  "model_label": "example-model",
  "mode": "dry_run",
  "request_id": "dry_run_request_001",
  "baseline_candidate_events": 2,
  "kora_routed_events": 1,
  "avoided_model_call_events": 1,
  "provider_attempted_events": 0,
  "provider_blocked_events": 2,
  "no_network": true,
  "no_provider_call": true,
  "contains_real_provider_response": false,
  "contains_customer_data": false,
  "contains_secret_material": false,
  "notes": ["Synthetic metadata only."]
}
```

Recommended request fields:

- `request_id`
- `expected_route`: `deterministic`, `model_required`, or `ambiguous`
- `baseline_candidate_event`: boolean
- `kora_routed_event`: boolean
- `provider_attempt_allowed`: always false in dry-run fixtures
- `provider_block_expected`: boolean
- `validation_rule`
- `notes`

Recommended counter fields:

- `total_requests`
- `baseline_candidate_events`
- `kora_routed_events`
- `avoided_model_call_events`
- `provider_attempted_events`
- `provider_blocked_events`
- `validation_pass_count`
- `validation_fail_count`
- `error_count`
- `fallback_count`

## Documentation-Only Fixture Example

This example is illustrative only. It is not a runnable fixture and it contains no provider request or provider response.

```json
{
  "fixture_id": "provider_dry_run_synthetic_example_v1",
  "fixture_version": "0.1",
  "mode": "dry_run",
  "provider_label": "example-provider",
  "model_label": "example-model",
  "workload_id": "synthetic_provider_dry_run_v1",
  "privacy_class": "synthetic",
  "requests": [
    {
      "request_id": "dry_run_shipping_001",
      "expected_route": "deterministic",
      "baseline_candidate_event": true,
      "kora_routed_event": false,
      "provider_attempt_allowed": false,
      "provider_block_expected": true,
      "validation_rule": "synthetic_route_check",
      "notes": "Synthetic metadata only; no prompt or provider response."
    },
    {
      "request_id": "dry_run_account_001",
      "expected_route": "model_required",
      "baseline_candidate_event": true,
      "kora_routed_event": true,
      "provider_attempt_allowed": false,
      "provider_block_expected": true,
      "validation_rule": "synthetic_escalation_check",
      "notes": "Synthetic metadata only; dry-run blocks provider execution."
    }
  ],
  "expected_counters": {
    "total_requests": 2,
    "baseline_candidate_events": 2,
    "kora_routed_events": 1,
    "avoided_model_call_events": 1,
    "provider_attempted_events": 0,
    "provider_blocked_events": 2,
    "validation_pass_count": 2,
    "validation_fail_count": 0,
    "error_count": 0,
    "fallback_count": 0
  },
  "artifact_policy": {
    "raw_prompts_emitted": false,
    "raw_provider_responses_emitted": false,
    "secrets_allowed": false,
    "private_data_allowed": false
  }
}
```

## Fixture Safety Rules

Fixtures must be safe for public review by default.

The current schema validator enforces these fail-closed rules:

- `mode` must be `dry_run` or `fixture`
- `no_network` must be `true`
- `no_provider_call` must be `true`
- `contains_real_provider_response` must be `false`
- `contains_customer_data` must be `false`
- `contains_secret_material` must be `false`
- `provider_attempted_events` must be `0`
- `provider_blocked_events` must be zero or greater
- `avoided_model_call_events` must be zero or greater
- all counter fields must be integers and non-negative

Invalid fixtures raise a clear validation error before any report generation or future provider boundary is reached.

Required rules:

- use synthetic or sanitized metadata only
- use fake provider names only
- use fake model names only
- include no secrets
- include no API keys
- include no access tokens
- include no private customer data
- include no proprietary datasets
- include no raw prompts unless separately approved in a future task
- include no raw provider responses unless separately approved in a future task
- include no provider request identifiers unless reviewed and redacted
- include no private hostnames, account identifiers, billing details, or user identifiers

Any fixture that violates these rules should fail validation before report generation.

## Adapter Invocation Boundary

The dry-run harness should stop before provider execution.

Allowed boundary:

```text
workload -> routing plan -> dry-run provider eligibility check -> aggregate counters
```

Forbidden boundary in this design:

```text
workload -> provider request construction -> provider execution -> provider response parsing
```

Dry-run checks may verify that a request would require a provider adapter after explicit opt-in, but they must not call a provider adapter, local runtime, HTTP endpoint, subprocess runtime, or model SDK.

## Fail-Closed Behavior Before Provider Enablement

Before any real provider implementation is approved, provider paths should fail closed.

Expected behavior:

- provider adapter selected without implementation -> non-zero exit or blocked dry-run status
- missing future provider configuration -> blocked before provider request construction
- prohibited fixture field -> blocked before report generation
- unsupported privacy class -> blocked before report generation
- raw provider response present -> blocked before report generation
- secret-like value present -> blocked before report generation

Dry-run reports must make blocked provider paths visible through `provider_blocked_events` and reviewer notes.

## Required Counters

The dry-run harness should use counters that distinguish candidate routing from actual provider execution.

Required counters:

- `total_requests`
- `baseline_candidate_events`
- `kora_routed_events`
- `avoided_model_call_events`
- `avoided_model_call_event_rate`
- `provider_attempted_events`
- `provider_blocked_events`
- `deterministic_routes`
- `model_escalations`
- `validation_pass_count`
- `validation_fail_count`
- `error_count`
- `fallback_count`

In dry-run mode, `provider_attempted_events` must remain `0`.

## Required Report Fields

Before any future real-provider validation, reports should include:

- harness mode
- workload identifier
- fixture identifier
- adapter kind
- provider label
- model label
- total requests
- baseline candidate events
- KORA routed events
- avoided model-call events
- provider-attempted events
- provider-blocked events
- validation pass/fail counts
- error and fallback counts
- fixture safety status
- artifact policy status
- raw prompt emission flag
- raw provider response emission flag
- claim boundary text
- non-claim list

Reports should not include cost fields in dry-run mode. If cost fields are added in a later real-provider task, estimated and measured values must be separated and claim-reviewed.

Current local/no-network validation reports include a provider fixture dry-run contract status section for reviewer visibility. That section is aggregate metadata only. It records values such as `mode=dry_run`, `no_network=true`, `no_provider_call=true`, `provider_attempted_events=0`, and prohibited-content flags set to false. It does not include provider requests, provider responses, credentials, customer data, raw prompts, network calls, or provider execution.

## Future CI Test Plan

Future CI tests can validate the dry-run contract without provider access:

- fixture schema accepts safe synthetic metadata
- fixture schema rejects `no_network=false`
- fixture schema rejects `no_provider_call=false`
- fixture schema rejects secret-like values
- fixture schema rejects raw provider responses
- fixture schema rejects customer data flags
- fixture schema rejects negative counters
- fixture schema rejects unknown modes
- dry-run mode keeps `provider_attempted_events` at `0`
- provider-required routes increment `provider_blocked_events`
- deterministic routes reduce `kora_routed_events`
- reports include aggregate counters and boundary language
- help, import, example listing, and report rendering make no provider calls
- fail-closed paths do not write misleading success reports
- safety scans detect accidental provider dependencies or executable network paths

These tests must not require provider credentials, network access, local model runtimes, or external downloads.

## Human Approval Gates

Before any future real provider implementation, require explicit review of:

- adapter name and selection mechanism
- provider configuration boundary
- credential handling design
- privacy and artifact policy
- fixture and workload safety
- report schema and redaction rules
- failure behavior
- CI skip/enable rules
- claim language
- release and artifact handling plan

Approval for a design packet is not approval to implement provider calls.

## Evidence Boundaries

### Synthetic / No-Network Evidence

Current local/no-network examples show that KORA can measure avoided model-call events in synthetic workloads. They do not validate real provider behavior.

### Dry-Run Fixture Evidence

Dry-run fixture evidence would show that KORA can validate provider adapter control-plane boundaries, fixture safety, blocked provider paths, and report shape without making provider calls. It would not be real provider validation.

### Future Real-Provider Evidence

Future real-provider evidence would require an explicitly implemented provider adapter, explicit opt-in, reviewed provider configuration, reviewed workload, sanitized artifacts, and separate claim review.

Even future real-provider evidence would not automatically prove production cost reduction, real API-cost reduction, production benchmark performance, broad workload superiority, or energy reduction.

## Claim Boundary

The current safe public claim remains:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Allowed local/no-network wording remains:

> KORA's local no-network validation examples show that KORA can measure avoided model-call events in synthetic workloads.

This design packet creates no new provider, production, cost, adoption, funding, or energy claim.

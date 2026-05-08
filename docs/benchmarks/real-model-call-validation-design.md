# Real Model-Call Runtime Validation Design

## Purpose

This document defines a claim-safe design for validating KORA with runtime-integrated workloads that include real model calls or local model calls.

The goal is to move from the current deterministic-heavy alpha benchmark toward measured model invocation reduction in workloads where some requests can be handled deterministically and other requests require model escalation.

This is a design document. It does not implement new provider calls, does not require secrets, and does not create benchmark artifacts.

## Current Baseline

Current approved public claim:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

This is alpha benchmark evidence. It is not production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, or energy reduction evidence.

Current relevant public surfaces:

- `examples/runtime_integrated_benchmark/`
- `experiments/workloads/deterministic_heavy_v1_100.json`
- `experiments/run_benchmark.py`
- `kora/model_call.py`
- `kora/adapters/base.py`
- `kora/adapters/mock.py`
- `kora/adapters/openai_adapter.py`
- `kora/executor.py`
- `kora/telemetry.py`
- `tests/test_runtime_integrated_benchmark.py`

The existing runtime-integrated benchmark path currently supports offline/mock execution for reproducibility. Real model-call validation should extend this path without weakening artifact, privacy, or claim boundaries.

## Validation Question

When a workload contains requests that can be handled deterministically and requests that require model escalation, can KORA reduce measured model invocations versus a naive direct baseline while preserving expected outputs and validation results?

## Scope

This validation design includes:

- runtime-integrated validation
- real model-call or local model-call adapters
- provider-neutral measurement design
- environment-variable based provider configuration
- aggregate counters and sanitized summaries
- synthetic or sanitized workloads
- no secrets committed
- no raw provider responses committed
- no private user data
- no production traffic required for initial validation

## Non-Scope

This validation design does not include:

- production cost-reduction claims
- universal 80% claims
- energy-reduction claims
- provider-specific performance endorsements
- raw billing proof unless explicitly added later
- production traffic
- release assets
- raw benchmark artifact uploads
- package version changes

## Test Modes

### 1. Offline Deterministic Simulation Mode

Offline deterministic simulation mode is the current reproducible path.

Properties:

- requires no provider credentials
- uses deterministic handlers and mock adapter behavior
- can run in CI and local development
- is useful for regression testing and public reproduction
- records simulated baseline counts and KORA-controlled adapter counts

This mode preserves the current alpha claim boundary. It should not be described as real API-cost evidence or production evidence.

### 2. Local Model-Call Mode

Local model-call mode should run through a local runtime or local provider abstraction, such as Ollama, llama.cpp, vLLM, or a repo-supported local adapter if one is added later.

See the [local model adapter design](local-model-adapter-design.md) for the provider-neutral local runtime pathway and configuration principles.

Properties:

- records measured local model invocation count
- records latency when available
- may estimate token usage or leave token usage unavailable depending on adapter support
- does not require remote provider credentials
- should use synthetic or sanitized workloads
- should not commit raw model prompts or responses by default

Local model-call mode can support claims about measured model invocations in a documented local validation workload. It should not be described as production evidence.

### 3. Remote Provider Mode

Remote provider mode should run through provider adapters configured only through environment variables.

Examples:

- OpenAI via `OPENAI_API_KEY`
- Anthropic or other providers if provider-neutral adapters are added later

Properties:

- provider keys must come from environment variables only
- no keys, tokens, or credentials are committed
- raw prompts and raw responses are not committed
- output artifacts store only aggregate counters and sanitized summaries by default
- provider name and model name are optional report fields
- estimated cost is recorded only when pricing is explicitly configured
- measured cost is recorded only if billing data is explicitly supplied later

Remote provider mode can support a future measured model-call reduction claim only after commands, counters, workload, and claim language are reviewed.

## Workload Structure

Real model-call validation should use a workload structure that supports both direct baseline execution and KORA-controlled execution.

Each request should include:

- `request_id`
- `input`
- `expected_route`: `deterministic`, `model_required`, or `ambiguous`
- `deterministic_handler`, if applicable
- `validation_rule`, if applicable
- `expected_output` or `expected_properties`, if applicable
- `privacy_class`: `synthetic`, `sanitized`, or `private_do_not_commit`
- `notes`

Example synthetic workload snippet:

```json
{
  "name": "real_model_call_validation_synthetic_v1",
  "version": "0.1",
  "requests": [
    {
      "request_id": "support_shipping_001",
      "input": {
        "text": "Where can I find the shipping status for my order?"
      },
      "expected_route": "deterministic",
      "deterministic_handler": "support.shipping_status_policy",
      "validation_rule": "contains_shipping_status_steps",
      "expected_properties": {
        "category": "shipping_status",
        "requires_model": false
      },
      "privacy_class": "synthetic",
      "notes": "Synthetic repetitive support request."
    },
    {
      "request_id": "support_ambiguous_001",
      "input": {
        "text": "My account was locked after several failed logins and I need help."
      },
      "expected_route": "ambiguous",
      "deterministic_handler": null,
      "validation_rule": "routes_to_escalation_or_safe_policy",
      "expected_properties": {
        "category": "account_risk",
        "requires_model": true
      },
      "privacy_class": "synthetic",
      "notes": "Synthetic ambiguous request that may require model escalation."
    }
  ]
}
```

Workloads marked `private_do_not_commit` must not be committed to the repository. Sanitized or synthetic workloads are preferred for public validation.

## Baselines

### Direct Baseline

The direct baseline calls the model for every request.

Expected direct-baseline flow:

```text
request -> model -> output -> validation -> telemetry
```

Direct baseline counters should include:

- total requests
- baseline model calls
- validation pass/fail
- errors
- latency
- token usage where available

### KORA-Controlled Path

The KORA-controlled path routes each request through execution control before model escalation.

Expected KORA-controlled flow:

```text
request -> task graph -> deterministic path or model escalation -> validation -> telemetry
```

KORA-controlled counters should include:

- deterministic routes
- model escalations
- KORA model calls
- validation pass/fail
- fallback count
- errors
- latency
- token usage where available

## Counters To Measure

Every validation run should report:

- `total_requests`
- `baseline_model_calls`
- `kora_model_calls`
- `avoided_model_calls`
- `avoided_model_call_rate`
- `deterministic_routes`
- `model_escalations`
- `fallback_count`
- `validation_pass_count`
- `validation_fail_count`
- `error_count`
- `latency_total_ms`
- `latency_p50_ms`
- `latency_p95_ms`
- `token_input_total`, if available
- `token_output_total`, if available
- `estimated_cost`, if provider pricing is explicitly configured
- `measured_cost`, only if provider billing data is explicitly supplied later

Cost counters must not be used to claim real API-cost reduction unless billing data, methodology, baseline, and claim language are separately reviewed.

## Provider-Neutral Adapter Interface

KORA uses a provider-neutral adapter boundary for model-call measurement in future validation harnesses.

Current implementation:

- `ModelCallRequest`: normalized request with `request_id`, `prompt`, metadata, and privacy class.
- `ModelCallResponse`: normalized response with measured model-call count, latency, token counters where available, provider/model labels, and metadata.
- `ModelCallAdapter`: protocol for adapters that return measured model-call counters.
- `DeterministicFakeModelCallAdapter`: deterministic local validation adapter for tests and harness development.
- `BlockedModelCallAdapter`: fail-closed adapter for cases where real provider use has not been explicitly configured.

The adapter selection skeleton currently supports `local_validation`, `blocked`, and `local_runtime_placeholder` kinds so future local model-call validation can add runtime adapters behind explicit opt-in.
- `ModelCallSummary`: aggregate counter helper for validation reports.

The deterministic local validation adapter is the only local implementation added at this stage. It requires no credentials, performs no external calls, and records provider/model as `local_validation` / `deterministic-local`.

Future local or remote provider adapters can plug into the same interface. Remote provider calls must use environment variables for configuration and must not commit secrets, raw prompts, raw responses, private user data, or proprietary datasets.

## Local No-Network Model-Call Runtime Example

The first runtime validation example is a local no-network model-call path:

```bash
python3 -m kora run real_model_call_validation_fake -- --offline
```

The command name is preserved for compatibility. The emitted mode/provider/model labels use local no-network validation terminology.

This example uses the deterministic local validation adapter with a synthetic 10-request workload. The direct baseline records local validation model-call events for every request. The KORA-controlled path handles deterministic routes without local validation model-call events and escalates only model-required routes through the provider-neutral adapter boundary.

The example validates model-call counter plumbing before real local or remote provider adapters are added. It requires no secrets, uses no network, emits aggregate counters only, and does not commit raw prompts or raw provider responses.

The example can generate a reviewer-facing Markdown report from aggregate counters with `--report-md`. Generated reports are evidence packets for local/no-network review before real provider or production validation.

For a reviewer-facing walkthrough, see the [local no-network validation reviewer packet](local-validation-reviewer-packet.md).

Claim boundary: this is not real provider validation, real API-cost validation, production validation, production cost reduction proof, broad workload superiority proof, or energy reduction evidence.

## Customer-Support Triage Local Validation Example

The first application-oriented local validation example uses the synthetic customer-support triage workload:

```bash
python3 -m kora run customer_support_triage_fake_validation -- --offline
```

The command name is preserved for compatibility. The emitted mode/provider/model labels use customer-support local validation terminology.

This extends local/no-network validation from generic counter plumbing to a realistic support triage workload shape. It still uses the deterministic local validation adapter, requires no secrets, makes no network calls, and emits aggregate counters only.

The example can generate a reviewer-facing Markdown report from aggregate counters with `--report-md`.

This is a step before local model or remote provider validation. It is not real provider validation, real API-cost validation, or production validation.

## Telemetry Output

Real model-call validation should emit sanitized artifacts only.

Recommended artifact shape:

- JSON summary
- Markdown report
- aggregate counters
- sanitized environment details
- optional provider name
- optional model name
- validation result summary
- error and fallback counts
- no raw prompts by default
- no raw provider responses by default
- no secrets
- no private user data

Example summary shape:

```json
{
  "validation_name": "real_model_call_validation_synthetic_v1",
  "mode": "local_model",
  "provider": "local",
  "model": "example-local-model",
  "total_requests": 20,
  "baseline_model_calls": 20,
  "kora_model_calls": 8,
  "avoided_model_calls": 12,
  "avoided_model_call_rate": 0.6,
  "deterministic_routes": 12,
  "model_escalations": 8,
  "fallback_count": 0,
  "validation_pass_count": 20,
  "validation_fail_count": 0,
  "error_count": 0,
  "latency_total_ms": 12345,
  "latency_p50_ms": 410,
  "latency_p95_ms": 1200,
  "token_input_total": null,
  "token_output_total": null,
  "estimated_cost": null,
  "measured_cost": null,
  "claim_boundary": "This is validation evidence for a documented workload. It is not production cost reduction proof, real API-cost reduction proof, production benchmark proof, broad workload superiority proof, or energy reduction evidence."
}
```

Do not commit raw provider responses or private prompts as evidence artifacts.

## Claim Upgrade Path

Current approved public claim:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Future conditional language after successful real model-call runtime validation:

> KORA reduced measured model invocations by X% in a runtime-integrated validation workload using real model calls.

Future conditional language after tested app workload validation:

> KORA reduced measured model invocations by X% in tested application workloads.

Still not allowed unless proven separately:

- KORA reduces production AI costs by X%.
- KORA reduces real API costs by X%.
- KORA reduces energy consumption by X%.
- KORA is production-proven.

Claim escalation requires merged evidence, documented methodology, validation commands, reviewed results, and claim-registry approval.

## Validation Acceptance Criteria

Minimum acceptance criteria:

- workload is synthetic or sanitized
- commands are reproducible
- counters are emitted
- direct baseline and KORA-controlled path are both run
- model-call counts are measured
- validation pass/fail is reported
- errors are counted
- fallbacks are counted
- no secrets are committed
- no raw provider responses are committed
- no raw private prompts are committed
- report includes claim boundary

Recommended public review criteria:

- workload schema is documented
- adapter mode is documented
- model/provider details are either sanitized or explicitly approved for publication
- generated JSON and Markdown artifacts remain in `/tmp` or ignored paths unless explicitly selected for review
- claim language is checked against `docs/claims/kora-claim-registry.md`

## Recommended Implementation Phases

### Phase 1: Design Doc And Report Template

Add this design document and a report template without adding provider calls or requiring secrets.

### Phase 2: Provider-Neutral Model-Call Adapter Interface

Define a small adapter interface for counted model calls that can support mock, local, and remote providers.

The interface should report:

- invocation count
- latency
- token usage where available
- sanitized model/provider metadata
- error state

### Phase 3: Local Model-Call Mode

Add local model-call execution with a local runtime or local adapter abstraction.

Use the [local model adapter design](local-model-adapter-design.md) as the configuration and adapter-boundary contract for this phase.

This phase should not require remote provider credentials and should not commit raw model responses.

### Phase 4: Remote Provider Mode Via Environment Variables

Add remote provider execution through environment variables only.

This phase should include strict artifact handling:

- no keys committed
- no raw prompts committed by default
- no raw responses committed by default
- aggregate summaries only

### Phase 5: Customer-Support Triage Workload

Add a synthetic or sanitized customer-support triage workload with deterministic categories, ambiguous cases, and model-required cases.

### Phase 6: Public Claim Review And Docs Update

Review evidence and claim language before updating README, claim registry, or public announcement materials.

## Open Questions

- Which provider or local runtime should be validated first?
- How should token and cost counters be normalized across providers?
- How should semantic validation be handled without storing raw private responses?
- How can artifact generation avoid raw prompt and response leakage by default?
- What workload should become the first public validation workload?
- Should local model-call validation and remote provider validation have separate report templates?
- What minimum sample size is sufficient for the first real model-call validation report?

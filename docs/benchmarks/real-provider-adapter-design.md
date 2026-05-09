# Real Provider Adapter Design

## Purpose

This packet defines how future real provider adapters may integrate with KORA's provider-neutral model-call measurement boundary.

This is a design-only document. It does not implement real provider calls, network calls, HTTP clients, provider credential handling, subprocess runtimes, external model downloads, provider dependencies, or benchmark artifacts.

For the dry-run-first validation contract that should precede any future real provider implementation, see the [real provider test harness design](real-provider-test-harness-design.md).

## Current Default

KORA's current validation paths remain local/no-network by default.

Current safe adapter kinds:

- `local_validation`: default deterministic local validation adapter.
- `local_runtime`: explicit opt-in deterministic in-process local runtime stub.
- `blocked`: fail-closed adapter for unconfigured model-call paths.
- `local_runtime_placeholder`: fail-closed design-only placeholder for unsupported runtime paths.

Future real provider adapters must not become the default path. They must require explicit selection and configuration.

## Non-Goals

This design does not provide:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated real-provider benchmark evidence
- broad workload superiority proof
- energy reduction evidence
- formal government validation
- signed partner validation
- guaranteed adoption or funding

This design also does not add provider SDKs, provider-specific runtime clients, provider credentials, HTTP calls, subprocess calls, or external model downloads.

## Provider Adapter Lifecycle

A future real provider adapter should follow a fail-closed lifecycle:

1. Adapter unavailable by default.
2. User explicitly selects a provider adapter.
3. Adapter performs local preflight validation of required configuration.
4. Missing or invalid configuration fails before any provider request is constructed.
5. Request envelope is normalized through `ModelCallRequest`.
6. Provider execution occurs only in a future implementation after explicit opt-in and preflight success.
7. Provider response is normalized through `ModelCallResponse`.
8. Aggregate counters are recorded through `ModelCallSummary` or an equivalent reporting boundary.
9. Reports include only aggregate counters and sanitized summaries by default.

Every failure before explicit provider execution should produce a clear error and should not silently fall back to another provider or local runtime.

## Explicit Opt-In Requirement

Future real provider adapters must require explicit user action. A provider adapter should not run because a credential happens to exist in the environment, a default model name is available, or a workload includes a prompt-like field.

Required opt-in properties:

- explicit adapter selection
- explicit provider configuration
- clear provider and model labels in output
- no default remote provider fallback
- no implicit network call during help, example listing, import, test discovery, or report rendering

The local/no-network validation examples should continue to work without provider configuration.

## Fail-Closed Behavior

Future provider adapters should fail closed for:

- missing provider configuration
- missing provider credential
- invalid provider model selection
- unsupported adapter kind
- unsupported workload privacy class
- disabled artifact policy
- attempted raw prompt or raw response persistence
- provider timeout or malformed response

Failures should be visible through the command exit status, reviewer-facing error text, and aggregate error counters where a report is intentionally produced.

## Provider Credential Boundary

Provider credentials are future runtime configuration, not repository content.

Future implementations must preserve these boundaries:

- no provider credentials committed to the repository
- no provider credentials in examples, docs, reports, tests, or fixtures
- no provider credential values in logs, errors, telemetry, Markdown reports, or JSON summaries
- missing credentials fail closed before provider execution
- provider credential source may be described generically, but secret values must never be emitted

This packet does not implement credential loading, validation, storage, or redaction logic.

## Telemetry And Counter Requirements

Future real provider adapters should preserve the existing measurement shape while adding provider-specific fields only when they are safe and available.

Required aggregate fields:

- total requests
- baseline model calls
- KORA model calls
- avoided model calls
- avoided model-call rate
- deterministic routes
- model escalations
- validation pass count
- validation fail count
- error count
- fallback count
- adapter kind
- provider label
- model label

Optional fields, when safely available:

- latency totals and percentiles
- input token counts
- output token counts
- provider request identifiers after review and redaction
- provider error classes without raw provider payloads

Cost fields must remain absent unless pricing, billing data, workload, baseline, and claim language are separately reviewed. Estimated cost and measured cost should be clearly distinguished if they are ever added later.

## Report Artifact Requirements

Future provider reports should be conservative by default:

- aggregate counters only
- sanitized summaries only
- no raw prompts
- no raw provider responses
- no provider credentials
- no private user data
- no proprietary datasets
- no raw benchmark artifacts committed by default

Generated reports should use local output paths, such as `/tmp`, unless a report is intentionally reviewed and selected for publication.

## Security And Privacy Boundaries

Future provider validation should use synthetic or sanitized workloads first. Workloads containing private data must not be committed and must not be used for public evidence without a separate privacy review.

Provider adapters should treat request text, provider responses, request identifiers, and error payloads as potentially sensitive. Public documentation and reports should describe methodology, counters, and sanitized results rather than raw provider exchanges.

## Future Test Plan

Before any real provider implementation is added, the test plan should cover:

- default behavior remains local/no-network
- provider adapter is unavailable unless explicitly selected
- missing provider configuration fails closed before provider execution
- unsupported provider configuration fails clearly
- help and example listing make no provider calls
- tests do not require provider credentials
- report generation excludes secrets, raw prompts, and raw provider responses
- fail-closed paths do not write misleading success reports
- provider-specific tests are skipped unless explicitly enabled in a controlled environment
- safety scans detect newly introduced network, subprocess, provider SDK, or credential-handling code

The [real provider test harness design](real-provider-test-harness-design.md) defines a dry-run fixture and reporting contract for this pre-implementation stage.

## Evidence Boundary

Current public evidence remains local/no-network or deterministic-heavy:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

KORA's local no-network validation examples show that KORA can measure avoided model-call events in synthetic workloads.

Future provider evidence would differ from the current synthetic/no-network evidence because it would include explicitly configured provider execution, provider/model labels, measured provider invocation counters, and a reviewed workload methodology. That future evidence would still not imply production cost reduction, real API-cost reduction, production benchmark proof, broad workload superiority, or energy reduction unless those claims are separately supported and reviewed.

This design packet alone creates no new performance, cost, production, or energy claim.

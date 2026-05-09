# Local Model Adapter Design

## Purpose

This design defines how KORA can later connect to local model runtimes through the provider-neutral `ModelCallAdapter` interface.

The goal is to preserve the same measurement shape used by current local/no-network validation examples while allowing future adapters for local model runtimes. This document is a design contract only. It does not implement Ollama, llama.cpp, vLLM, remote provider calls, or new dependencies.

## Current State

KORA currently supports local/no-network validation with deterministic local validation adapters.

Current properties:

- no external provider calls are required
- no local model runtime is required
- no API keys or provider credentials are required
- examples emit aggregate model-call counters
- Markdown reports are generated from aggregate counters
- reviewer-facing guidance is documented in the local validation reviewer packet

This design is the next step toward local model validation. It defines how future local runtime adapters should plug in without changing the public claim boundary.

## Target Local Runtimes

Future adapters may support local runtimes such as:

- Ollama
- llama.cpp
- vLLM
- other local HTTP runtimes
- subprocess-based local runtimes

KORA should remain provider-neutral. Supporting one local runtime first should not make that runtime the default public measurement standard.

## Adapter Boundary

Future local adapters should implement the same boundary already used by validation harnesses:

- `ModelCallRequest`
- `ModelCallResponse`
- `ModelCallAdapter.call(request)`

The adapter input is a prompt/request envelope. The adapter output must include:

- output text
- measured model-call count
- latency when available
- input token count when available
- output token count when available
- provider/runtime label
- model label
- sanitized metadata

Adapters must not leak raw private prompts or raw model responses into committed artifacts. Runtime outputs should be kept local by default, and public reports should use aggregate counters and sanitized summaries.

## Local Runtime Modes

### 1. Disabled / Blocked Mode

Disabled or blocked mode is the default safe behavior for unconfigured runtime paths.

Properties:

- no runtime required
- no network required
- fails closed with a clear error
- does not silently fall back to a remote provider

### 2. Deterministic Local Validation Mode

Deterministic local validation mode is the current no-network validation path.

Properties:

- uses the deterministic local validation adapter
- requires no local model runtime
- is deterministic and suitable for tests and CI
- measures the model-call counter path before real local adapters are introduced

### 3. Local Runtime Mode

Local runtime mode is a future opt-in mode for adapters such as Ollama, llama.cpp, vLLM, or another local runtime.

Properties:

- requires explicit user opt-in
- uses a local runtime endpoint or command configured by environment variable or CLI flag
- normally requires no secrets
- records measured local model-call counters
- keeps raw outputs local by default
- does not commit raw prompts or raw responses by default

## Configuration Principles

Future local adapter configuration should follow these principles:

- no hard-coded endpoints that imply external calls
- no committed credentials
- no default remote provider fallback
- environment variables may be used later for local endpoint selection
- CLI flags may be used later for explicit adapter selection
- default behavior remains local/no-network validation or blocked mode unless the user opts in

Potential future environment variable names:

- `KORA_LOCAL_MODEL_RUNTIME`
- `KORA_LOCAL_MODEL_ENDPOINT`
- `KORA_LOCAL_MODEL_NAME`

These names are design placeholders only. They are not active requirements unless implemented in a later task.

## Adapter Selection Skeleton

KORA now includes a small adapter selection skeleton for local validation and future local runtime work.

Current supported adapter kinds:

- `local_validation`: returns the deterministic local validation adapter used by local/no-network examples.
- `local_runtime`: returns an explicit opt-in deterministic in-process local runtime stub for local/no-network validation.
- `blocked`: returns a fail-closed adapter for unconfigured model-call paths.
- `local_runtime_placeholder`: returns fail-closed behavior and documents that local runtime adapters are design-only for now.

The local validation examples expose an explicit `--adapter` option for the current safe adapter kinds. The `local_runtime` adapter is a concrete local/no-network runtime stub: it runs in process, uses deterministic output, records aggregate counters, and does not call local HTTP endpoints, subprocess runtimes, remote providers, provider APIs, or external model downloads. The default remains `local_validation`.

`local_runtime_placeholder` remains design-only and fail-closed for unsupported runtime paths.

Reviewer-facing reproduction commands, no-network baseline counters, and fail-closed adapter checks are listed in the [local no-network validation reviewer packet](local-validation-reviewer-packet.md).

The `local_runtime_placeholder` adapter kind does not call Ollama, llama.cpp, vLLM, remote providers, local HTTP endpoints, or subprocess runtimes. It exists so future adapters can plug into the same selection path without changing the validation examples or claim boundaries.

## Blocked Local Runtime Adapter Skeleton

KORA includes an explicit blocked local runtime adapter skeleton for the `local_runtime_placeholder` kind.

The skeleton reserves the future local runtime adapter boundary while failing closed by design. It:

- accepts an inert local runtime configuration object for future runtime, model, endpoint, command, timeout, and metadata fields
- does not read environment variables automatically
- does not validate configuration by contacting a runtime
- does not call Ollama, llama.cpp, vLLM, local HTTP endpoints, subprocess runtimes, or remote providers
- does not require any local runtime installation for tests or examples
- raises a clear error stating that local runtime adapters are not implemented yet and that no provider call was attempted

Current runnable validation remains local/no-network validation through the deterministic local validation adapter by default. The `local_runtime` adapter provides an explicit opt-in local runtime stub for exercising the same boundary without external runtime calls. Future runtime-specific adapters can extend the same selection path without replacing the fail-closed placeholder.

Future adapter kinds should keep the same behavior shape:

- explicit adapter selection
- clear provider/runtime label
- clear model label
- measured counters where available
- fail-closed behavior when unconfigured
- no silent fallback to remote providers

## Counters To Measure

Future local model adapters should record:

- `model_calls`
- `latency_ms`
- `input_tokens` if available
- `output_tokens` if available
- provider/runtime label
- model label
- `error_count`
- `fallback_count`
- `validation_result` where applicable

Token counters may be unavailable or adapter-specific. Reports should distinguish measured token counts from estimates.

## Privacy And Artifacts

Local model validation must preserve the current artifact policy:

- no raw private prompts committed
- no raw model outputs committed by default
- no private customer data
- no proprietary datasets
- reports contain aggregate counters and sanitized summaries only
- local generated reports are reviewed before sharing

If a future reviewer needs example outputs, they should use synthetic or sanitized prompts and explicitly reviewed artifacts.

## Failure Handling

Future local adapters should fail clearly and measurably:

- local runtime unavailable -> clear error
- timeout -> error counter
- malformed response -> error counter
- unsupported runtime -> clear error
- invalid endpoint or command -> clear error
- no silent fallback to a remote provider

Validation summaries should make failures visible through `error_count`, `fallback_count`, and reviewer-facing notes.

## Claim Boundaries

Local model adapter validation, once implemented, may support measured local model-call validation language.

Allowed future language after implementation and validation:

> KORA reduced measured local model invocations by X% in a runtime-integrated local model validation workload.

Not allowed from this design alone:

- KORA reduces production AI costs
- KORA reduces real API costs
- KORA is production-proven
- KORA reduces energy consumption
- KORA is validated across broad workloads

This design does not create production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, or energy reduction evidence.

## Implementation Phases

### Phase 1: Design Doc And Configuration Contract

Define the adapter pathway, configuration principles, privacy policy, failure handling, and claim boundary.

### Phase 2: Adapter Selection Interface

Add a small adapter selection boundary that can choose blocked mode, deterministic local validation mode, or a future local runtime adapter.

### Phase 3: Local Runtime Adapter Skeleton With Blocked Behavior

Add a local runtime adapter skeleton that fails closed unless explicitly configured. This phase should still require no local runtime for tests.

### Phase 4: Ollama Or llama.cpp Adapter Behind Explicit Opt-In

Implement one local runtime adapter behind explicit opt-in. The adapter should be skipped or blocked by default in CI unless the runtime is configured.

### Phase 5: Customer-Support Triage Local Model Validation

Run the existing synthetic customer-support triage workload through the local runtime adapter and emit the same aggregate counters and Markdown report structure.

### Phase 6: Claim Review And Docs Update

Review measured counters, privacy handling, reproducibility, and claim language before updating public docs.

## Open Questions

- Which local runtime should be supported first?
- Should the first adapter use HTTP, subprocess execution, or both?
- How should token counts be normalized across local runtimes?
- What timeout defaults are appropriate for reviewer runs and CI?
- What semantic validation strategy should be used for local model outputs?
- Where should optional reviewed artifacts live, and what should stay local only?

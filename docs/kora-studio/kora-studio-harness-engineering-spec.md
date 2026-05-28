# KORA Studio Harness Engineering Specification

## Status and Claim Boundary

KORA Studio is not a fully shipped product yet. This specification defines harness requirements before broader product expansion, especially before Studio UI surfaces make stronger claims about execution routing, model capability, or workflow efficiency.

The harness does not prove production cost reduction. It does not prove real API-cost reduction unless an approved real-provider workload is later added and documented. It does not prove energy reduction, broad workload superiority, or that unsupported larger models can run on hardware that cannot load them.

KORA Studio should make execution paths measurable before making broader product claims.

## Why Harness Engineering Comes First

KORA Studio's UI must not simply show attractive demo animations. The Execution Viewer, Model Capability UI, and Standard Mode vs KORA Boost comparison need reproducible harness outputs behind them.

Required harness outputs include:

- request classification
- selected route
- deterministic route use
- model escalation
- validation result
- counters
- latency where measured
- adapter state
- local-only/provider-disabled status

The harness is required so Studio can show what happened in a run without implying production observability, provider validation, cost reduction, energy reduction, or unsupported model capability.

## Harness Layers

### 1. Fixture workload layer

The fixture workload layer supplies local sample requests and repeatable task sets for development and validation.

Requirements:

- local sample requests
- deterministic-heavy task sets
- customer-support-like synthetic tasks
- future local workflow tasks
- no private data by default

### 2. System profile layer

The system profile layer reports what the local machine appears able to support, while failing closed when a value cannot be safely detected.

Requirements:

- OS
- CPU/GPU architecture
- RAM/VRAM/unified memory where safely detectable
- runtime availability
- installed local models where safely detectable
- local storage writability
- port availability
- unknown/fail-closed behavior

Initial implementation status: the preview server exposes a standard-library-only system profile scaffold through `/status`. It reports OS, machine, Python version, safely detectable total memory, local executable presence for runtime candidates, local storage writability, localhost defaults, provider-disabled state, and cloud-sync-disabled state. It does not call runtime APIs, provider APIs, model APIs, or external network services.

### 3. Model capability estimator layer

The model capability estimator layer separates physical model capability from workflow feasibility.

Requirements:

- physically runnable model tier
- continuous local chat tier
- larger-model workflow feasibility
- memory/runtime/quantization dependency
- recommendations labelled as estimates until validated

Initial implementation status: the preview server exposes a local heuristic model capability estimate through `/status` and the static preview page. Recommendations are estimates until validated on the machine and do not claim unsupported larger-model execution.

Model catalog scaffold status: the preview server exposes a static curated local catalog scaffold through `/status`. It does not fetch remote catalogs, search Hugging Face, call Ollama registries, download models, execute models, or claim all open-source LLM support. Catalog recommendations are estimates until validated and must keep download/execution actions disabled until separate implementation work lands.

Runtime status scaffold status: the preview server exposes local runtime executable status, localhost-only service reachability fields, and an installed-model summary through `/status`. Catalog examples remain distinct from installed models. Service reachability is not model execution readiness and may remain `not_checked`; installed-model detection remains fail-closed. The scaffold does not execute models, list models, download models, call provider APIs, or use cloud sync.

Disabled action scaffold status: catalog recommendations expose planned download/run action metadata with actions disabled by default. The preview page may show disabled labels such as "Download not connected yet" and "Run not connected yet", but no download, execution, registry lookup, provider call, or cloud sync is connected.

### 4. Deterministic route layer

The deterministic route layer captures non-model execution choices and their validation results.

Requirements:

- deterministic code path
- structured lookup path
- policy path
- validation path
- route miss
- validation failure
- model fallback

### 5. Local model route layer

The local model route layer captures model-needed execution without making unsupported capability claims.

Requirements:

- local model execution path
- runtime adapter boundary
- model-called event
- latency/token capture where available
- no unsupported capability claims

### 6. Adapter route layer

The adapter route layer makes execution mode explicit.

Requirements:

- mock adapter
- local runtime adapter
- Ollama adapter as planned/optional if not implemented
- llama.cpp adapter as planned/optional if not implemented
- OpenAI/provider adapter as explicit opt-in only if planned
- external/distributed route disabled by default unless explicitly enabled

### 7. SSE/event capture layer

The SSE/event capture layer provides local event data for the Execution Viewer and replay surfaces.

Requirements:

- event stream for Execution Viewer
- stage replay
- status transitions
- error/fallback events
- no real browser launch in tests

### 8. Metrics aggregation layer

The metrics aggregation layer summarizes counters and measured values without converting them into unsupported claims.

Requirements:

- counters
- latency
- token usage where available
- estimated cost only when source data is explicit and claim-safe
- no energy conversion by default

### 9. Report export layer

The report export layer creates local claim-safe artifacts for inspection and review.

Requirements:

- local report export
- JSON summary
- Markdown summary
- claim boundary block
- adapter state block
- no raw provider responses by default

## Required Event Schema

The harness event schema must support UI replay and local report generation with these fields:

| Field | Purpose |
|---|---|
| `run_id` | Local run identifier. |
| `request_id` | Request identifier within the run. |
| `stage_id` | Stable stage identifier. |
| `stage_name` | Human-readable stage name. |
| `route_class` | Route category such as deterministic, structured lookup, policy, local model, provider, or fallback. |
| `status` | Stage status such as pending, running, passed, failed, skipped, or fallback. |
| `started_at` | Stage start timestamp where available. |
| `completed_at` | Stage completion timestamp where available. |
| `latency_ms` | Stage latency in milliseconds where measured. |
| `model_called` | Whether the stage called a model path. |
| `deterministic_route_used` | Whether the deterministic route was used. |
| `structured_lookup_used` | Whether a structured lookup route was used. |
| `validation_result` | Validation result where available. |
| `adapter_name` | Adapter identifier. |
| `adapter_mode` | Adapter mode such as mock, local-runtime, provider-opt-in, or disabled. |
| `provider_calls_enabled` | Whether provider calls were enabled for this run. |
| `cloud_sync_enabled` | Whether cloud sync was enabled for this run. |
| `counters_snapshot` | Counter values after this event where available. |
| `error_code` | Error code for failed or fallback stages. |
| `error_message` | Claim-safe error message. |

This schema is for UI and local report generation. It does not imply production observability.

## Required Metrics

The harness must define these metrics before the UI relies on them:

- `total_requests`
- `baseline_model_calls`
- `kora_model_calls`
- `avoided_model_calls`
- `avoided_model_call_rate`
- `deterministic_routes`
- `structured_lookup_routes`
- `policy_routes`
- `model_escalations`
- `validation_pass_count`
- `validation_fail_count`
- `error_count`
- `fallback_count`
- `latency_ms`
- `p50_latency_ms` where applicable
- `p95_latency_ms` where applicable
- `p99_latency_ms` where applicable
- `input_tokens` where available
- `output_tokens` where available
- `estimated_cost` only when source data is explicit and claim-safe

No energy metric is enabled by default. The harness must not make a production cost-reduction claim. It must not make a real API-cost reduction claim unless an approved real-provider workload is explicitly added and documented.

## Model Capability and Recommendation Boundary

The harness must distinguish these capability labels:

- Physically runnable local model: a model that the user's machine can actually load and run under the detected runtime, memory, quantization, and validation conditions.
- Recommended continuous local chat tier: the model tier estimated to be comfortable for sustained local interaction on the detected machine.
- Workflow-usable larger model: a larger model path that may be practical for some workflows because KORA routes non-model work away from the model path, while still requiring actual model availability and validation.
- Optional external/provider/distributed route: a route that is disabled by default and requires explicit opt-in.
- Unsupported model: a model that should not be presented as locally runnable or workflow-usable under the current detected conditions.

Safe language:

- KORA does not make large models smaller.
- KORA does not remove RAM/VRAM/unified-memory/model-loading requirements.
- KORA can make larger-model workflows more practical by sending less work to the model.
- Larger-model workflow support remains conditional on memory, runtime, quantization, adapter state, and validation.

Forbidden examples:

- "KORA runs 70B locally on hardware that cannot load 70B."
- "KORA removes VRAM requirements."
- "KORA makes a 7B machine equal to 70B."
- "KORA supports all open-source LLMs."
- "KORA guarantees cost or energy reduction."

## Standard Mode vs KORA Boost Harness

Standard Mode:

- request goes to selected model path by default
- model call counted
- latency/token metrics captured where available

KORA Boost:

- deterministic route first
- structured lookup/policy validation
- model fallback only when needed
- avoided model calls counted only when validation succeeds

Acceptance criteria:

- same fixture input can be run in Standard and KORA Boost
- comparison reports route differences
- comparison does not overclaim production behavior

## Local-Only Default and Provider Boundary

Local-only mode is the default. Provider calls are disabled by default. Cloud sync is disabled by default. No API key is required for default local mode.

External/provider routes require explicit opt-in. Raw provider responses are not stored in public artifacts by default.

## Failure Modes

The harness must represent these failure modes clearly and claim-safely:

- system profile unknown
- runtime not installed
- runtime installed but not running
- model not installed
- model download unavailable
- insufficient memory
- port unavailable
- browser launch failure
- deterministic route miss
- validation failure
- model fallback
- adapter error
- SSE disconnect
- report export failure

## Test Requirements

Future implementation should include tests for:

- system profile mock
- model capability estimator mock
- event schema validation
- metric aggregation
- Standard vs KORA Boost comparison
- provider disabled default
- cloud sync disabled default
- browser launch mocked, not real in CI
- no-network local mode
- report export claim boundary

## Acceptance Criteria for Future Implementation

Future harness implementation is acceptable when:

- harness can run deterministic fixture workload locally
- harness can emit event stream for Execution Viewer
- harness can export claim-safe report
- system profile UI can show unknown fields safely
- model recommendations are clearly labelled estimates until validated
- adapter state is always visible
- no unsupported larger-model claim is shown
- no provider/cloud route is enabled by default

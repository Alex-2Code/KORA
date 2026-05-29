# KORA Studio v0.4 Local Run Trigger Plan

## Status and Goal

KORA Studio v0.3 is complete as a local preview/demo readiness milestone. It exposes local deterministic harness requests, generated event stages, generated counters, local harness comparison output, and report summary metadata without provider calls, cloud sync, model downloads, or real model execution.

KORA Studio v0.4 should add a local run trigger surface for approved deterministic sample requests and may optionally expose event-stream scaffolding for generated harness events.

Task 434 adds the first local run trigger endpoint scaffold. `POST /api/harness/run` accepts approved sample request IDs only and returns generated local deterministic harness events, counters, comparison summary, and report metadata summary. `GET /api/harness/run/{run_id}` retrieves in-memory run records while the local server process is alive.

Task 435 adds non-SSE generated event retrieval through `GET /api/harness/events?run_id=<id>`. The endpoint returns generated harness events for an existing in-memory local run. It is not SSE, not token streaming, and not model output. Arbitrary prompt execution, model execution, provider calls, downloads, runtime model listing, private directory scanning, and persistence remain out of scope.

v0.4 remains a local preview/demo milestone. It is not a production release, hosted service, provider billing dashboard, cost-reduction dashboard, energy dashboard, generic local chatbot, or LM Studio replacement.

## Scope

Allowed:

- approved deterministic sample requests
- local-only run trigger
- generated harness events
- generated counters
- generated Standard Mode vs KORA Boost comparison
- optional SSE/event-stream scaffold
- local report metadata update

Forbidden:

- provider calls
- cloud sync
- model downloads
- real model execution
- private model directory scanning
- runtime model list commands
- real installed model claims
- production cost reduction claim
- energy outcome claim
- unsupported larger-model execution claim

## Proposed API Surface

Planned endpoints:

- `GET /api/harness/requests`
- `POST /api/harness/run`
- `GET /api/harness/run/{run_id}`
- optional `GET /api/harness/events?run_id=<id>`
- optional `GET /api/harness/sse?run_id=<id>`

`POST /api/harness/run` must accept only approved request IDs or approved sample payloads. v0.4 should not introduce arbitrary prompt execution unless the prompt shape is explicitly bounded, validated, synthetic/local-only, and routed through the same claim-safe harness path.

Model-needed routes must return `execution_not_connected`, not model output. A model-needed route may be represented as a boundary event and counted as an escalation boundary, but it must not call a model, provider, runtime adapter, registry, or remote service.

## Proposed UI Surface

The local preview UI should add or refine:

- selectable approved sample request list
- Run Local Harness button
- generated event timeline
- Standard Mode vs KORA Boost comparison panel
- counters panel
- report placeholder update
- visible claim boundary panel

The Run Local Harness button should trigger only approved local harness samples. Any future custom payload input must be explicitly labelled as local deterministic sample input and must reject arbitrary model prompts unless a later task defines a safe bounded path.

## Event-stream Boundary

If SSE is included:

- stream only generated harness events
- stream no real model tokens
- perform no provider streaming
- perform no model execution
- expose reconnect/failure behavior
- mark stream status as local harness event stream only
- tests must not require a browser or network beyond localhost

SSE should be optional in v0.4. A simple non-streaming run endpoint plus generated event retrieval is acceptable if it keeps the milestone smaller and safer.

## Run State Model

Run states:

- `created`
- `running`
- `completed`
- `failed`
- optional `cancelled`
- `execution_not_connected` for model-needed boundaries

Run state must be local process memory only unless a later task explicitly adds a local persistence boundary. No cloud state, provider state, model runtime state, or private model directory state should be inferred.

## Required Metrics

The run output should include:

- `total_requests`
- `baseline_model_calls`
- `kora_model_calls`
- `avoided_model_calls`
- `deterministic_routes`
- `model_escalations`
- `validation_pass_count`
- `validation_fail_count`
- `stage_count`
- `event_count`
- `report_metadata_status`

Metrics remain local deterministic harness counters. They do not prove production behavior, provider billing changes, cost reduction, or energy outcomes.

## Acceptance Criteria

- approved sample request can be triggered locally
- generated events are returned
- counters are updated from generated harness output
- UI makes the run visible
- model-needed boundary does not execute a model
- provider calls remain disabled
- cloud sync remains disabled
- model downloads remain disabled
- run/download model actions remain disabled
- smoke check covers `/health`, `/status`, `/`, and planned harness endpoints if implemented in later tasks

## Test Plan

Required tests:

- approved request trigger
- invalid request rejected
- generated event shape
- generated counter shape
- model-needed boundary returns `execution_not_connected`
- no provider behavior
- no model behavior
- no download behavior
- optional SSE smoke test if SSE is added
- preview smoke check update

Tests must not:

- open a real browser
- call providers
- call external model APIs
- download models
- execute models
- scan private model directories
- run runtime model list commands
- require a runtime such as Ollama to be installed

## v0.4 Task Breakdown

### Task 434 - Local Run Trigger Endpoint Scaffold

Add local-only endpoint scaffolding for approved harness request IDs. Keep arbitrary prompt execution out of scope.

### Task 435 - Generated Run State and In-Memory Store

Add an in-memory run store for generated harness runs. Store only synthetic/local harness metadata and generated events.

### Task 436 - Optional Event Stream Endpoint

Add optional SSE/event-stream scaffolding for generated harness events if the non-streaming endpoint is not enough for the UI. Stream no model tokens.

### Task 437 - UI Trigger Panel

Add a preview UI panel for selecting an approved sample request and triggering a local harness run. Keep model download/run actions disabled.

### Task 438 - Comparison and Counter Update from Selected Run

Update the comparison and counter panels from the selected generated run.

### Task 439 - Report Metadata from Selected Run

Update report placeholder metadata from the selected generated run. Do not scan arbitrary local files or write report exports.

### Task 440 - v0.4 Smoke Check and Readiness Report

Extend smoke checks for v0.4 endpoints and surfaces, then add a v0.4 readiness report after validation.

## Claim Boundary

KORA Studio v0.4 planning does not add runtime behavior by itself. The plan defines a future local-only run trigger milestone for deterministic harness data. Provider calls, cloud sync, model downloads, model execution, private directory scans, runtime model list commands, production cost claims, energy outcome claims, unsupported larger-model execution claims, and LM Studio replacement claims remain out of scope.

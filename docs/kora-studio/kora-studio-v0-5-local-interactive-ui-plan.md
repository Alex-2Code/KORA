# KORA Studio v0.5 Local Interactive UI Plan

## Status and Goal

KORA Studio v0.4 is complete as a local deterministic harness preview/demo milestone. It exposes approved local harness requests, local run trigger endpoints, generated run records, generated events, generated SSE events, local harness comparison data, and report metadata preview without model execution, provider calls, downloads, cloud sync, private directory scanning, runtime model listing, or file export.

KORA Studio v0.5 should add a local interactive UI for approved deterministic sample requests and selected-run state, while keeping all model/provider/download boundaries disabled.

v0.5 remains a local preview/demo milestone. It is not a production release, hosted service, provider billing dashboard, cost-reduction dashboard, energy dashboard, generic local chatbot, or LM Studio replacement.

## Scope

Allowed:

- approved deterministic sample request selector
- Run Local Harness button
- selected-run state
- `fetch` `POST /api/harness/run`
- `fetch` `GET /api/harness/run/{run_id}`
- `fetch` `GET /api/harness/events?run_id=<id>`
- optional connection to `GET /api/harness/sse?run_id=<id>` only if scoped later
- render generated event timeline for selected run
- render Standard Mode vs KORA Boost comparison for selected run
- render generated counters for selected run
- render report metadata preview for selected run
- local-only browser UI
- dependency-free implementation or minimal use of an existing frontend stack only

Forbidden:

- arbitrary prompt input
- model execution
- provider calls
- model downloads
- cloud sync
- private model directory scanning
- runtime model list commands
- external network behavior
- production cost reduction claim
- energy outcome claim
- unsupported larger-model execution claim
- LM Studio replacement claim

## UI Behavior

The local preview UI should behave as follows:

1. Request list loads from existing local harness data or `/status`.
2. User selects one approved sample request.
3. User clicks Run Local Harness.
4. UI shows a loading state.
5. UI receives the generated local harness run response.
6. UI stores the selected `run_id` in browser state only.
7. UI renders the selected run status, event timeline, counters, comparison, report metadata, and claim boundary.
8. Refresh behavior may reset selected state unless persistence is explicitly added in a later task.

The UI must not include arbitrary prompt input. It must not add a model run form, model download action, provider action, cloud action, private directory picker, or runtime model list action.

## Selected-run State Model

The local browser state should include:

- `selected_request_id`
- `selected_run_id`
- `run_status`
- `run_error`
- `run_response`
- `events`
- `counters`
- `comparison_summary`
- `report_metadata_summary`
- `claim_boundary`

State is browser-local only for this milestone. It should not be persisted to disk, synced to cloud, or treated as production telemetry.

## API Usage Boundary

The interactive UI may use only existing local endpoints:

- `POST /api/harness/run` for approved request IDs only.
- `GET /api/harness/run/{run_id}` for local in-memory run retrieval.
- `GET /api/harness/events?run_id=<id>` for generated event retrieval.

Optional later scope:

- `GET /api/harness/sse?run_id=<id>` for generated harness event SSE display only.

Out of scope:

- arbitrary prompt endpoint
- model execution endpoint
- provider endpoint
- download endpoint
- file export endpoint
- cloud sync endpoint
- runtime model list endpoint

## Claim Boundary UI

Every interactive run result must visibly show:

- local deterministic harness output only
- no model execution
- no provider calls
- no downloads
- no cloud sync
- model-needed boundary returns `execution_not_connected`
- not production evidence

The selected-run UI should display claim boundaries near the run result, not only in separate documentation.

## Error Handling

The UI should handle:

- invalid request rejected
- run endpoint unavailable
- unknown `run_id`
- events unavailable
- network-to-localhost failure
- UI timeout
- malformed local response
- selected state reset

Error messages must be claim-safe. They should not suggest model execution, provider fallback, download fallback, or cloud recovery.

## Test Plan

Required tests:

- UI renders approved request selector.
- Run Local Harness calls only `POST /api/harness/run`.
- Arbitrary prompt input is absent.
- Selected-run state updates from local run response.
- Event timeline renders generated events.
- Counters render generated counters.
- Comparison renders local harness comparison.
- Report metadata renders metadata preview.
- Errors display claim-safe messages.
- No model behavior is introduced.
- No provider behavior is introduced.
- No download behavior is introduced.
- No cloud behavior is introduced.
- Smoke check is updated if feasible.

Tests must not:

- open a real browser unless explicitly scoped to a local preview smoke check
- call external network
- call providers
- call external model APIs
- download models
- execute models
- scan private model directories
- run runtime model list commands

## v0.5 Task Breakdown

### Task 442 - Interactive Request Selector Scaffold

Add a dependency-free or existing-stack UI scaffold that renders approved deterministic sample requests as selectable local items. Do not add arbitrary prompt input.

Status: Initial selector scaffold exists and Task 443 connects the Run Local Harness button to `POST /api/harness/run` for approved selected request IDs only. Selected-run state remains browser-local and in-memory.

### Task 443 - Run Local Harness Button and Selected-run State

Connect the selected approved request to `POST /api/harness/run` and store the selected run response in browser state only.

Status: Connected in the local preview with minimal vanilla JavaScript. It sends only the approved `request_id`, does not add arbitrary prompt input, and does not call model, provider, download, cloud, events, or SSE endpoints from the selector task.

### Task 444 - Selected-run Event Timeline Rendering

Render generated event stages for the selected run from the local run response or `GET /api/harness/events?run_id=<id>`.

Status: Connected in the local preview after a successful approved local harness run. The UI fetches `GET /api/harness/events?run_id=<id>` and renders generated local harness events only. The selected-run timeline is not SSE, not model token streaming, not provider output, and does not execute a model.

### Task 445 - Selected-run Comparison and Counters Rendering

Render selected-run counters and Standard Mode vs KORA Boost comparison from local harness output only.

Status: Connected in the local preview from the selected local harness run response. The counters are generated local harness output only, not production telemetry, and the comparison is generated from approved local harness output only, not production cost evidence.

### Task 446 - Selected-run Report Metadata Rendering

Render selected-run report metadata preview and disabled file export boundary from local harness output only.

Status: Connected in the local preview from the selected local harness run response. The report metadata is preview-only, renders from `report_metadata_summary`, and does not export files, write files, download reports, execute models, call providers, or enable cloud sync.

### Task 447 - Interactive UI Smoke Check and Readiness Report

Update local preview smoke checks for the interactive UI markers and add a v0.5 readiness report after validation.

### Task 448 - Consolidated v0.5 Goal Report

Add a consolidated public-safe v0.5 goal report with implemented surfaces, validation results, claim boundaries, known limitations, and next recommended milestone.

## Acceptance Criteria

- The UI lists approved deterministic sample requests.
- The UI can trigger a local harness run for an approved request.
- The UI stores selected run state in browser memory only.
- The UI renders generated timeline, counters, comparison, and report metadata for the selected run.
- The UI shows local-only/no-model/no-provider/no-download/no-cloud boundaries.
- The UI does not expose arbitrary prompt input.
- Model-needed examples remain `execution_not_connected`.
- Existing `/health`, `/status`, `/`, `/api/harness/run`, `/api/harness/run/{run_id}`, `/api/harness/events`, and `/api/harness/sse` behavior remains intact.

## Claim Boundary

KORA Studio v0.5 planning does not add runtime behavior by itself. The plan defines a future local interactive UI milestone for approved deterministic harness data. Provider calls, cloud sync, model downloads, model execution, private directory scans, runtime model list commands, external network behavior, production cost claims, energy outcome claims, unsupported larger-model execution claims, and LM Studio replacement claims remain out of scope.

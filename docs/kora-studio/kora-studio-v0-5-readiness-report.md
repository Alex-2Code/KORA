# KORA Studio v0.5 Readiness Report

## Status

KORA Studio v0.5 is ready as a local preview/demo milestone for interactive approved-request harness runs.

v0.5 remains a local deterministic harness preview. It is not a production release, hosted service, LM Studio replacement, generic local chatbot, provider billing dashboard, cost-reduction dashboard, or energy dashboard.

## Current HEAD

Validation baseline HEAD:

```text
525bc543b0406cb6b7b1779c89016263239da57e
```

Branch and public truth:

- branch: `main`
- remote: `origin`
- public truth: `origin/main`

## Validation Commands and Results

Validated on 2026-05-30:

```bash
git diff --check
```

Result: passed.

```bash
python3 -m pytest
```

Result: 231 passed.

```bash
python3 -m pytest tests -k "studio or sse or execution or harness"
```

Result: 93 passed, 138 deselected.

## Live Smoke Check Results

Validated against a live local preview started with:

```bash
python3 -m kora studio --no-browser
```

Then checked with:

```bash
python3 scripts/check_kora_studio_preview.py
```

Result: passed.

Covered surfaces:

- `/health`
- `/status`
- `/api/harness/run`
- `/api/harness/run/<run_id>`
- `/api/harness/events?run_id=<id>`
- `/api/harness/sse?run_id=<id>`
- `/`

The smoke check verifies local-only status, provider/cloud disabled state, approved request trigger behavior, generated event retrieval, generated SSE output, and v0.5 preview UI markers for selector, selected-run summary, selected-run event timeline, selected-run counters/comparison, and selected-run report metadata.

## Endpoints Covered

- `GET /health`
- `GET /status`
- `GET /`
- `POST /api/harness/run`
- `GET /api/harness/run/{run_id}`
- `GET /api/harness/events?run_id=<id>`
- `GET /api/harness/sse?run_id=<id>`

## v0.5 Implemented Surface

KORA Studio v0.5 adds an interactive local preview surface on top of the v0.4 deterministic harness endpoints:

- approved request selector
- Run Local Harness button
- selected-run browser state
- selected-run summary
- selected-run generated event timeline
- selected-run counters
- selected-run Standard Mode vs KORA Boost comparison
- selected-run report metadata preview
- existing generated harness run endpoint
- existing in-memory run retrieval endpoint
- existing generated events endpoint
- existing SSE endpoint for generated harness events only

The UI sends only approved local harness request IDs to the local harness run endpoint. It does not expose arbitrary prompt input.

## Claim Boundaries

- KORA Studio v0.5 is local deterministic harness only.
- Event data is generated harness data only.
- Selected-run state is browser-local only.
- Approved deterministic sample requests are the only interactive run source.
- No arbitrary prompt execution is connected.
- No model execution is connected.
- No provider calls are connected.
- No model downloads are connected.
- No cloud sync is connected.
- No private model directory scanning is connected.
- No runtime model list commands are connected.
- No report file export is connected.
- No report file writing is connected.
- No external network behavior is connected.
- No production cost reduction claim is made.
- No energy outcome claim is made.
- No unsupported larger-model execution claim is made.
- KORA Studio is not an LM Studio replacement.

## Known Limitations

- v0.5 is still a local preview/demo milestone, not a production product.
- Run records are in-memory only and disappear when the server process stops.
- Selected-run state is browser memory only and resets on refresh.
- The UI uses minimal embedded vanilla JavaScript rather than a full frontend application shell.
- The SSE endpoint exists, but the selected-run UI uses the non-SSE generated events endpoint.
- Model-needed boundaries return `execution_not_connected`; no model output is produced.
- Report metadata is preview-only; there is no report export, file write, or report download.
- Catalog entries remain examples, not installed-model claims.
- Installed model detection remains scaffolded unless a future task connects a safe local method.

## Next Recommended v0.6 Direction

Recommended next goal:

KORA Studio v0.6 local frontend interaction hardening.

Suggested focus:

- clearer local interactive state transitions
- selected-run error and retry UX
- optional SSE UI for generated harness events only
- multi-run local preview state
- stronger manual visual QA checklist for the interactive flow
- continued local-only/no-model/no-provider/no-download boundaries


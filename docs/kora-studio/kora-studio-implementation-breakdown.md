# KORA Studio Implementation Breakdown

## Status

This document breaks KORA Studio v0.1 planning into implementation phases. KORA Studio is not implemented yet.

## Implementation Principle

KORA Studio should start as a local-first, single-user, no-cloud viewer/workspace for KORA validation artifacts and local model workflows.

- Mac/Linux first
- CLI launch first
- browser UI first
- local-only storage first
- Ollama-first runtime direction
- no provider billing dashboard in v0.1
- no API-cost or energy claims

## Phase 0 — Planning and Fixtures

Goal: Prepare static fixtures and UI requirements before runtime code.

Tasks:

- define sample local validation JSON summary fixture
- define sample Markdown report fixture
- define dashboard counter schema
- define project/chat mock data
- define KORA Boost copy placement
- define no-cloud/no-API-key onboarding copy

Deliverables:

- `docs/kora-studio/fixtures-plan.md`
- `docs/kora-studio/report-viewer-requirements.md`
- `docs/kora-studio/dashboard-counter-schema.md`
- `docs/kora-studio/fixture-schema-reference.md`
- `docs/kora-studio/fixtures/`

No code required.

## Phase 1 — CLI Launch Skeleton

Status: Initial CLI skeleton is available through `python3 -m kora studio`. It prints planning/preview status only; it does not start a server, open a browser, call a model runtime, or call a provider.

Goal: Add a `kora studio` command that starts a placeholder local server or prints clear next-step status.

Scope:

- command registration
- local-only status output
- no browser launch required initially if too early
- no real model runtime calls
- no provider calls

Acceptance criteria:

- `python3 -m kora studio --help` or equivalent works
- command clearly says Studio is experimental/planning if not fully implemented
- tests cover command availability

## Phase 2 — Local Studio Server Skeleton

Status: Initial local server skeleton is available through `python3 -m kora studio --serve`. It exposes preview `/health`, `/status`, and `/` endpoints on localhost only. It does not include the full frontend, runtime integration, model calls, browser launch, Ollama calls, or provider calls.

Goal: Create a local-only server boundary.

Scope:

- minimal local HTTP server or FastAPI-style skeleton if dependency already exists
- health endpoint
- static placeholder page endpoint
- no cloud upload
- no model calls
- no external network dependency

Acceptance criteria:

- local server starts and stops cleanly
- health endpoint returns local status
- tests do not require network beyond localhost

## Phase 3 — Static Web UI Prototype

Goal: Create a static UI prototype for KORA Studio.

Screens:

- Welcome / Setup
- Model Selection
- Project Chat Workspace
- Execution Trace Panel
- Report Viewer

Scope:

- static assets or minimal frontend structure
- no runtime calls
- no model downloads
- no account system

Acceptance criteria:

- UI can be served locally
- KORA Boost copy appears correctly
- planning-only status is clear

## Phase 4 — Report Viewer

Goal: Render existing local Markdown validation reports.

Scope:

- select local report path
- render Markdown
- show counter summary if structured data is available
- warn not to commit generated reports by default

Acceptance criteria:

- can load `/tmp/kora_customer_support_validation.md`
- displays boundary language
- does not upload report

## Phase 5 — Counter Dashboard

Goal: Show KORA validation counters as cards.

Counters:

- `total_requests`
- `baseline_model_calls`
- `kora_model_calls`
- `avoided_model_calls`
- `avoided_model_call_rate`
- `deterministic_routes`
- `model_escalations`
- `validation_pass_count`
- `validation_fail_count`
- `error_count`
- `fallback_count`

Acceptance criteria:

- cards render from fixture or summary JSON
- no cost or energy conversion
- local/no-network mode clearly labeled

## Phase 6 — Project Chat Mock

Goal: Create a project-based chat shell with mock/local placeholder messages.

Scope:

- project list
- conversation panel
- message list
- Standard Mode / KORA Boost toggle
- execution trace placeholder

Non-scope:

- no real model chat yet
- no provider calls
- no cloud sync

## Phase 7 — Ollama Runtime Detection

Goal: Detect whether Ollama is installed/available.

Scope:

- local detection only
- fail closed if unavailable
- no model pull yet
- no remote provider fallback

Acceptance criteria:

- detected / not detected state
- clear install/help copy
- tests can mock detection

## Phase 8 — Model List and Recommendation

Goal: Show supported local model options and recommended model/workflow.

Scope:

- static supported model list first
- system capability heuristic later
- Standard Mode recommendation
- KORA Boost workflow recommendation

Acceptance criteria:

- does not claim impossible model support
- no bigger-model physical execution claim
- uses benefit copy safely

## Phase 9 — Local Chat Integration

Goal: Integrate selected local runtime after explicit opt-in.

Scope:

- future task only
- likely Ollama first
- no provider API keys
- no cloud upload
- local runtime only

Acceptance criteria:

- model calls are measured
- execution path is visible
- local/no-network and local-runtime modes remain distinct

## Phase 10 — KORA Boost Execution Trace

Goal: Show route-level trace for each chat interaction.

Trace fields:

- `selected_route`
- `model_called`
- `deterministic_route_used`
- `model_escalation_used`
- `validation_result`
- `latency_ms`
- `counters`

Acceptance criteria:

- user can see what took the fast path
- user can see when model was used
- no unsupported cost/energy conversion

## Recommended First 10 Implementation Issues

These are future issue candidates. Do not create the issues from this document without maintainer approval.

| Title | Phase | Target files | Difficulty | Contributor suitability | Claim risk |
|---|---:|---|---|---|---|
| Add KORA Studio fixture plan | 0 | `docs/kora-studio/fixtures-plan.md` | small | good first docs issue | low |
| Add report viewer requirements | 0 | `docs/kora-studio/report-viewer-requirements.md` | small | good first docs issue | low |
| Add dashboard counter schema | 0 | `docs/kora-studio/dashboard-counter-schema.md` | small | good first docs issue | medium if counters are overinterpreted |
| Add `kora studio` CLI help stub | 1 | `kora/cli.py`, CLI tests | small | Python contributor | medium if wording implies shipped Studio |
| Add local Studio server design skeleton | 2 | future server module, tests | medium | Python contributor | low if no external calls |
| Add static welcome/setup page mock | 3 | future static UI files or docs mock | small | frontend/docs contributor | low |
| Add KORA Boost mode card mock | 3 | future static UI files or docs mock | small | frontend/docs contributor | medium if copy overclaims |
| Add report viewer static mock | 4 | future static UI files or docs mock | medium | frontend contributor | medium if reports expose raw data |
| Add counter dashboard fixture | 5 | future fixture path, tests | small | good first data/docs issue | medium if cost/energy fields are added |
| Add Ollama detection design note | 7 | future runtime design doc | small | local-runtime contributor | medium if support is implied before code |

## Claim-Safety Rules

- do not claim KORA Studio exists until code exists
- do not claim production cost reduction
- do not claim real API-cost reduction
- do not claim energy reduction
- do not claim larger models physically run unless validated
- use "Less waiting. Better answers. No hardware upgrade." as product benefit copy
- use technical explanation after benefit copy

## Implementation Order Recommendation

1. fixtures and schemas
2. CLI stub
3. local server skeleton
4. static UI
5. report viewer
6. counter dashboard
7. runtime detection
8. local chat

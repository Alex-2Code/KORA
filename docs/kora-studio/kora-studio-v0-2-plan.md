# KORA Studio v0.2 Plan

## Status

KORA Studio v0.1 is complete as a local fixture-backed AI Task Execution Router demo scaffold.

Current planning baseline:

- branch: `main`
- baseline HEAD: `3988677c1ab966225a60ccb8e4df16132f43fbb3`
- public truth: `origin/main`
- v0.1 readiness report: `docs/kora-studio/kora-studio-v0-1-readiness-report.md`

KORA Studio v0.2 should make the v0.1 demo feel like a coherent first-run local setup experience. It remains a local preview/demo readiness milestone, not a production release.

## Positioning

KORA Studio is a local-first AI Task Execution Router workspace.

LM Studio runs local models. KORA Studio routes local AI workflows. The model is one execution path, not the default path.

KORA Studio should help users understand:

- what their machine can physically run
- what model tiers are estimated to fit
- what runtime is detected
- what catalog examples are only candidates
- what is actually installed locally
- what actions are disabled or planned
- how KORA Boost routes deterministic, structured, lookup, and validation work away from the model path first

## v0.1 Complete State

The v0.1 local preview already provides:

- `kora studio` localhost launch
- browser auto-open by default
- `--no-browser`
- `/health`
- `/status`
- `/`
- Launch/local-only status
- Your Computer
- Model Capability Estimate
- Runtime Status
- Catalog vs Installed
- Setup Guidance
- disabled download/run action metadata
- KORA Boost Boundary
- Execution Viewer fixture/mock events
- Standard Mode vs KORA Boost fixture/mock comparison
- Report Viewer placeholder
- provider-disabled and cloud-disabled defaults
- no API key requirement for default local mode

## v0.2 Objective

KORA Studio v0.2 should polish the first-run experience so a user can move through the local setup story in a clear order:

1. Launch/local-only status
2. Your Computer
3. Model Capability Estimate
4. Runtime Status
5. Catalog vs Installed
6. Setup Guidance
7. Disabled Download/Run Actions
8. KORA Boost Boundary
9. Execution Viewer fixture
10. Standard Mode vs KORA Boost comparison fixture
11. Report Viewer placeholder
12. v0.2 readiness state

## v0.2 Milestone Plan

### Task 417 — v0.2 Planning

Add this v0.2 plan and link it from the Studio docs index.

### Task 418 — First-Run UI Copy and Hierarchy Polish

Polish the static preview UI and related copy so the first-run experience reads as one coherent onboarding flow. Keep all actions disabled/planned unless already safe.

### Task 419 — Visual QA Checklist

Add a public-safe manual QA checklist for launch, endpoints, section order, disabled actions, forbidden claims, fixture labels, report boundaries, and responsive layout sanity.

### Task 420 — Status Endpoint Coherence

Review `/status` response shape and add tests for required v0.2 contract fields while preserving backward compatibility where possible.

### Task 421 — Local Server Smoke Check

Add a non-mutating smoke-test helper or documented procedure for checking `/health`, `/status`, and `/` on localhost without providers, downloads, or model execution. Initial helper target: `scripts/check_kora_studio_preview.py`.

### Task 422 — v0.2 Readiness Report

Create the v0.2 readiness report after validation. It should include current HEAD, validated commands, implemented surfaces, non-scope, claim boundaries, known limitations, and the next recommended milestone.

## Claim Boundaries

KORA Studio v0.2 must not claim:

- production readiness
- real provider validation
- real cost reduction
- energy reduction
- all open-source LLM support
- unsupported larger-model execution
- provider/cloud/distributed routes enabled by default

Safe wording:

- KORA Studio is a local-first AI Task Execution Router workspace.
- Catalog examples are not installed models.
- Model recommendations are estimates until validated.
- KORA does not remove model memory requirements.
- Larger-model workflows may become more practical when deterministic work avoids the model path.
- Download and run actions remain disabled until explicitly connected.
- Provider calls and cloud sync are disabled by default.
- Execution data is fixture/mock only until live harness wiring is implemented.
- v0.2 is a local preview/demo readiness milestone, not a production release.

## Non-Scope

v0.2 does not add:

- real model download
- real model execution
- provider calls
- cloud sync
- remote catalog fetching
- Hugging Face or Ollama registry calls
- private model directory scans
- runtime model list commands
- active report file picker/export
- production monitoring
- billing, cost, or energy dashboards

## Validation Expectations

Each milestone should run:

- `git diff --check`
- `python3 -m pytest tests/test_kora_studio_cli.py`
- `python3 -m pytest tests/test_kora_studio_server.py`
- `python3 -m pytest tests/test_kora_studio_system_profile.py`
- `python3 -m pytest tests/test_kora_studio_model_catalog.py`
- `python3 -m pytest tests/test_kora_studio_runtime_status.py`
- `python3 -m pytest tests/test_kora_studio_execution_fixture.py`
- `python3 -m pytest tests -k "studio or sse or execution or harness"`

Final v0.2 readiness should also run:

- `python3 -m pytest`

Forbidden wording scans should be reviewed after each milestone. Matches in explicit forbidden-wording sections are acceptable; product claims are not.

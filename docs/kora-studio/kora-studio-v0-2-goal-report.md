# KORA Studio v0.2 Goal Report

## Status

KORA Studio v0.2 is complete as a local preview/demo readiness milestone for the first-run local setup experience.

This report consolidates the v0.2 work from Task 417 through Task 422. KORA Studio v0.2 remains a local-first AI Task Execution Router workspace preview, not a production product.

## Repository State

- branch: `main`
- public truth: `origin/main`
- completed v0.2 HEAD: `6c700af0916d9e9ee5824d6f3f6fd8bfda45bd5c`
- readiness status exposed by `/status`: `local_preview_demo_ready`
- v0.2 readiness report: `docs/kora-studio/kora-studio-v0-2-readiness-report.md`

## Goal Objective

KORA Studio v0.2 focused on turning the v0.1 local preview into a coherent first-run local setup experience. The goal was to make the preview explain what the local machine can run, what model recommendations mean, what runtime and catalog states are known, what actions are disabled, and how KORA Boost routes deterministic and structured work away from the model path first.

## Completed Milestones

- Task 417: added the v0.2 plan and linked it from the Studio docs index.
- Task 418: polished the first-run preview flow around the v0.2 section hierarchy.
- Task 419: added the v0.2 visual QA checklist.
- Task 420: added grouped v0.2 `/status` contract fields and tests.
- Task 421: added the local preview smoke-check helper.
- Task 422: added the v0.2 readiness report and marked `/status` readiness as `local_preview_demo_ready`.

## Files and Artifacts Added

- `docs/kora-studio/kora-studio-v0-2-plan.md`
- `docs/kora-studio/kora-studio-v0-2-visual-qa-checklist.md`
- `docs/kora-studio/kora-studio-v0-2-readiness-report.md`
- `scripts/check_kora_studio_preview.py`
- `tests/test_kora_studio_preview_smoke.py`

Existing public docs and tests were also updated to link the new reports, verify the status contract, and keep the preview claim-safe.

## Product Surfaces Now Covered

The local preview covers:

- `python3 -m kora studio` localhost launch
- browser auto-open by default
- `python3 -m kora studio --no-browser`
- `python3 -m kora studio --status`
- `/health`
- `/status`
- `/`
- first-run UI section order
- system profile scaffold
- model capability estimate scaffold
- static curated model catalog scaffold
- runtime status scaffold
- installed model detection scaffold, disabled by default
- setup guidance scaffold
- disabled download/run action metadata
- fixture/mock Execution Viewer events
- fixture/mock Standard Mode vs KORA Boost comparison
- report viewer/export placeholder
- local smoke-check helper
- visual QA checklist
- readiness report

## Status Endpoint Coverage

`/status` now exposes grouped v0.2 fields for:

- `studio_status`
- `launch_boundary`
- `v0_2_status`
- `system_profile`
- `model_capability_estimate`
- `runtime_status`
- `installed_models_summary`
- `model_catalog_status`
- `recommended_models`
- `setup_guidance_status`
- `disabled_action_state`
- `execution_viewer_status`
- `standard_vs_kora_comparison_status`
- `report_viewer_status`
- `claim_boundaries`

The status response keeps provider calls disabled, cloud sync disabled, download actions disconnected, run actions disconnected, and model execution disconnected.

## Preview UI Coverage

The root preview page presents the first-run story in this order:

1. Launch / Local-only Status
2. Your Computer
3. Model Capability Estimate
4. Runtime Status
5. Catalog vs Installed
6. Setup Guidance
7. Disabled Download/Run Actions
8. KORA Boost Boundary
9. Execution Viewer
10. Standard Mode vs KORA Boost
11. Report Viewer Placeholder

The preview shows provider calls disabled, cloud sync disabled, no model download, no model execution, fixture-only execution data, fixture-only comparison data, and report placeholder boundaries.

## Smoke Check Coverage

`scripts/check_kora_studio_preview.py` checks an already-running local preview at `http://127.0.0.1:8765`.

It verifies:

- `/health`
- `/status`
- `/`
- local-only server state
- provider-disabled state
- cloud-disabled state
- disabled download/run/model-execution state
- fixture-only execution and comparison state
- report placeholder state
- first-run UI markers

The helper rejects non-local URLs and does not start services, call providers, download models, execute models, scan private model directories, or run runtime model list commands.

## Validation Summary

Task 422 reported:

- `git diff --check`: passed
- `python3 -m pytest`: 204 passed
- `python3 -m pytest tests -k "studio or sse or execution or harness"`: 66 passed, 138 deselected
- live local smoke check with `python3 scripts/check_kora_studio_preview.py`: passed for `/health`, `/status`, and `/`

## Claim Boundaries

KORA Studio v0.2 remains claim-safe:

- KORA Studio v0.2 is local preview/demo readiness, not a production product.
- Execution Viewer data remains fixture/mock unless otherwise validated.
- Standard Mode vs KORA Boost comparison remains fixture/mock unless otherwise validated.
- Report viewer/export remains placeholder/fixture metadata unless otherwise validated.
- Provider calls are disabled by default.
- Cloud sync is disabled by default.
- Download/run actions are disabled.
- No model execution is connected.
- No model downloads are connected.
- No private model directory scanning is connected.
- No runtime model list commands are connected.

## Explicit Non-Claims

KORA Studio v0.2 does not claim:

- production readiness
- real provider validation
- real cost reduction
- energy reduction
- all open-source LLM support
- unsupported larger-model execution
- LM Studio replacement behavior
- provider/cloud/distributed routes enabled by default

## Known Limitations

- The root page is still a static preview surface.
- The separate React demo remains a scaffold.
- Runtime service reachability is a scaffold and does not prove model execution readiness.
- Installed model detection is scaffold-only and disabled by default.
- Catalog entries are curated examples only.
- Download and run actions are disabled.
- Execution Viewer data is fixture/mock only.
- Standard Mode vs KORA Boost comparison data is fixture/mock only.
- Report Viewer data is fixture metadata only.
- Visual QA checklist is manual; screenshots are not committed.

## Recommended Next Milestone

The next milestone should start a new v0.x planning slice. A conservative next step is a UI/data contract cleanup pass that keeps the preview local-only while deciding whether the next implementation should focus on a more product-like static frontend layout, safer runtime readiness UX, local installed-model detection design, or fixture-backed interaction polish.

Any future work that adds provider calls, model download, model execution, runtime model list commands, private directory scanning, or remote catalog fetching should require explicit approval and a separate claim-boundary review.

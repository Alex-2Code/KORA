# KORA Studio v0.1 Local Demo Spec

## Product Definition

KORA Studio v0.1 is a local-first AI Task Execution Router demo scaffold for Mac and Linux. It launches from the KORA CLI, opens a localhost browser UI, and demonstrates claim-safe local workflow-routing surfaces with fixture/mock data.

KORA Studio v0.1 is not a fully shipped product and is not production-ready. It does not execute models, download models, call providers, enable cloud sync, or claim unsupported larger-model execution.

## Target Users

- local AI users
- developers testing local LLM workflows
- AI app builders
- technical reviewers
- contributors exploring KORA validation

## User Problem

Local model users often do not know which model their machine can run, how to compare direct model usage with KORA-controlled execution, or how much model work is being avoided.

## Core Promise

Less waiting. Better answers. No hardware upgrade.

## KORA Boost Explanation

KORA Boost handles simple work through fast paths and saves model power for the tasks that need it.

## Standard Mode

Standard Mode runs the selected local model directly.

## KORA Boost

KORA Boost routes simple or structured work through fast local paths first, then uses the model when deeper reasoning is needed.

## v0.1 Demo Surfaces

- CLI launch: `kora studio`
- localhost-only web UI
- browser auto-open by default
- local-only launch/status panel
- Your Computer panel
- Model Capability Estimate panel
- Runtime Status panel
- Catalog vs Installed panel
- disabled download/run action labels
- Setup Guidance panel
- KORA Boost Boundary panel
- Standard Mode vs KORA Boost fixture comparison
- Execution Viewer placeholder using fixture/mock events
- Report Viewer placeholder using fixture metadata

## v0.1 Non-Features

- no cloud sync
- no team accounts
- no billing
- no hosted SaaS
- no provider billing dashboard
- no energy dashboard
- no real provider adapter by default
- no production monitoring
- no real model download
- no real model execution
- no real runtime model listing
- no arbitrary private model directory scan
- no arbitrary report file scan
- no active report export

## Success Criteria

- user can launch Studio locally with `kora studio`
- user can open the localhost-only browser UI
- user can see local-only, provider-disabled, and cloud-disabled status
- user can see system profile and model capability estimate scaffolds
- user can see runtime status and catalog-vs-installed boundaries
- user can see disabled download/run action boundaries
- user can see Standard Mode vs KORA Boost fixture comparison counters
- user can inspect fixture/mock execution path events
- user can see report viewer/export placeholder boundaries

## Claim Safety

Do not describe KORA Studio v0.1 as proving production cost reduction, real API-cost reduction, energy reduction, production validation, or broad workload superiority.

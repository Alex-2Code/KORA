# KORA Studio

## Status

KORA Studio is a future planning area. It is not implemented yet.

## Purpose

KORA Studio is intended to become a local-first AI workspace for Mac and Linux that helps users run local LLM workflows, compare Standard Mode and KORA Boost, and inspect KORA execution paths, model-call counters, and validation reports.

## Core User Benefit

KORA Boost

Less waiting. Better answers. No hardware upgrade.

KORA Boost handles simple work through fast paths and saves model power for the tasks that need it.

## Initial Scope

The first MVP should focus on:

- Mac and Linux first
- CLI launch
- local browser UI
- local runtime detection
- Ollama-first model selection
- Standard Mode vs KORA Boost
- project-based chat
- execution path visibility
- model-call counters
- local validation report viewer
- local-only storage

## Non-Scope

KORA Studio v0.1 planning is:

- not a hosted SaaS product yet
- not a production monitoring platform yet
- not an API-cost dashboard yet
- not an energy dashboard yet
- not a real provider billing dashboard yet
- not a claim that KORA Studio is implemented today

## Source Artifacts

Likely source artifacts include:

- local validation Markdown reports
- JSON summaries from local validation examples
- synthetic workload files
- reviewer packet outputs
- future local model validation reports

## Public/Private Boundary

KORA Studio docs in public KORA should describe technical design, local validation artifacts, and contributor-friendly planning only. Internal product strategy, launch planning, campaign materials, and private operating notes belong in the private internals repo.

## Claim Boundary

KORA Studio planning does not create new benchmark claims. It should only visualize already generated validation counters and claim-safe reports.

## CLI Skeleton

A minimal planning/preview CLI skeleton is available:

```bash
python3 -m kora studio
```

The command prints the current KORA Studio status and links to the Studio docs and fixtures. It does not start a server, open a browser, call a model runtime, call a provider, or require API keys. The next implementation phases are tracked in the [KORA Studio implementation breakdown](kora-studio-implementation-breakdown.md).

## Local Server Skeleton

A preview local-only server skeleton is available behind an explicit flag:

```bash
python3 -m kora studio --serve
```

Status:

- preview/local-only skeleton
- default host: `127.0.0.1`
- default port: `8765`
- endpoints: `/health`, `/status`, `/`
- no browser launch yet
- no Ollama calls
- no provider calls
- no API keys required

The server skeleton is not the full KORA Studio runtime or frontend. It exists to define the local server boundary for future Studio implementation work.

## Static Preview Page

The local server root serves a static UI prototype v0.1:

```bash
python3 -m kora studio --serve
```

Open locally:

```text
http://127.0.0.1:8765/
```

The page shows local status cards, endpoint references, a static workflow preview, and explicit limitations. It uses embedded HTML/CSS, does not auto-launch a browser, does not call Ollama or providers, does not connect a model/runtime, does not require API keys, and does not use a frontend framework yet.

## Implementation Planning

- [KORA Studio implementation breakdown](kora-studio-implementation-breakdown.md)
- [Report viewer requirements](report-viewer-requirements.md)
- [Dashboard counter schema](dashboard-counter-schema.md)
- [Fixtures plan](fixtures-plan.md)
- [Fixture schema reference](fixture-schema-reference.md)
- [Phase 0 sample fixtures](fixtures/README.md)
- [Local server placeholder page](kora-studio-local-server-placeholder-page.md)

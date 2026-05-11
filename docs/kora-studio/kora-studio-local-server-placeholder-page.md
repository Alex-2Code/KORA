# KORA Studio Local Server Placeholder Page

## Status

The KORA Studio local server root now renders a static UI prototype v0.1 for the server skeleton. It is still not a full frontend and does not make KORA Studio production-ready.

## Static UI Prototype v0.1

The page is a self-contained HTML preview served from `/`. It uses embedded CSS only and does not load external scripts, external stylesheets, CDNs, generated assets, frontend build tools, or runtime integrations.

Page sections:

- Header with `KORA Studio`, `Local v0.1 Skeleton`, and deterministic-first local workflow exploration copy
- Status cards for local server state, disabled provider calls, disconnected model/runtime integration, disabled browser launch, and disconnected Ollama integration
- Endpoint panel for `/health` and `/status`
- Workflow preview for request handling, deterministic checks, local status, and a future runtime placeholder
- Limitations panel with explicit no-provider, no-model/runtime, no-Ollama, no-browser-launch, and no unsupported-claims boundaries
- Footer with local-only and claim-safe wording

## How to Run

```bash
python3 -m kora studio --serve
```

Open the local page at:

```text
http://127.0.0.1:8765/
```

The server remains localhost-only by default. Browser auto-launch is not implemented.

## Endpoints

- `/` serves the static UI prototype v0.1
- `/health` returns local health status JSON
- `/status` returns local preview status, KORA Boost copy, docs paths, and fixture paths

## Current Limitations

- no full frontend yet
- no browser launch
- no Ollama integration
- no provider calls
- no model/runtime integration yet
- no project UI yet
- no API keys required
- no client-side calls, telemetry, local storage, or session storage

## Claim Boundary

The page is for deterministic-first local workflow exploration. It does not create production claims, API-cost claims, energy claims, benchmark claims, provider-validation claims, or deployment-readiness claims.

## Privacy Boundary

The placeholder page is static and self-contained. It does not expose environment variables, provider responses, private data, private internals, campaign material, or proprietary datasets.

# KORA Studio Local Server Placeholder Page

## Status

The KORA Studio local server placeholder page is a static preview page for the v0.1 server skeleton. It is not a full frontend and does not make KORA Studio production-ready.

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

- `/` serves the static placeholder page
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

## Claim Boundary

The page is for deterministic-first local workflow exploration. It does not create production claims, API-cost claims, energy claims, benchmark claims, provider-validation claims, or deployment-readiness claims.

## Privacy Boundary

The placeholder page is static and self-contained. It does not expose environment variables, provider responses, private data, private internals, campaign material, or proprietary datasets.

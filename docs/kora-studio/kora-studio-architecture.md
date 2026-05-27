# KORA Studio Architecture

## Architecture Status

This is a planning architecture. The full KORA Studio runtime is not implemented yet. An initial local server skeleton exists for preview/status endpoints only.

## Core Positioning

KORA Studio turns a local machine into an AI Task Execution Router workspace. It routes each task to the right path: CPU deterministic fast path, structured lookup, local model, or larger execution path only when needed.

KORA Studio should not be framed as merely a local LLM chatbot or an LM Studio clone. LM Studio helps users run local models. KORA Studio should help users run local AI workflows by making the model one execution path, not the default path.

Safe product wording:

- KORA Studio turns your local machine into an AI Task Execution Router.
- Run local AI workflows, not just local models.
- KORA routes deterministic work away from the model so larger-model workflows become more practical.
- The model becomes one execution path, not the default path.

Model capability boundary:

- KORA Studio must distinguish physically runnable local models from workflow-usable models.
- Larger-model workflow support depends on actual memory, runtime support, quantization, and validation on the user's machine.
- KORA can route work so larger-model workflows are used more selectively, but it does not remove RAM, VRAM, unified-memory, or model-loading requirements.
- External, provider, or distributed execution routes must stay disabled by default unless the user explicitly enables them.

Forbidden wording:

- KORA is an LM Studio replacement.
- KORA physically removes RAM, VRAM, unified-memory, or model memory requirements.
- KORA runs 70B locally on hardware that cannot load 70B.
- KORA proves GPT-4-level local performance.
- KORA guarantees cost reduction.
- KORA guarantees energy reduction.
- KORA supports all open-source LLMs.
- KORA runs larger models than the user's hardware can physically support.

## Components

### CLI Launcher

Responsibilities:

- `kora studio`
- start local Studio server
- open browser
- pass local configuration

### Local Studio Server

Skeleton status: a preview localhost-only server skeleton exposes `/health`, `/status`, and `/` endpoints. It does not implement the full Studio runtime, browser launch, model runtime integration, Ollama calls, or provider calls.

Responsibilities:

- serve web UI
- detect system/runtime status
- expose local APIs
- manage project/session state
- invoke KORA execution paths
- read local validation reports
- never upload data by default

### Web UI

Responsibilities:

- welcome/setup screen
- system profile
- model capability panel
- model selection
- project chat
- execution trace panel
- counter dashboard
- report viewer

Required UI narrative:

1. System Profile
   - show what the computer can physically run
   - detect OS, CPU/GPU, RAM/VRAM/unified memory, runtime, and installed models
2. Model Capability
   - recommend a continuous local chat tier
   - show larger model workflow options
   - clearly distinguish physically runnable local models, workflow-usable models, and optional external/distributed/provider routes
   - explain that larger-model workflows depend on memory, runtime support, quantization, and validation
3. KORA Boost Explanation
   - Standard Mode sends every step to the model.
   - KORA Boost routes deterministic and structured tasks to CPU/local fast paths first.
   - Larger models become more practical because they are reserved for model-needed tasks.
4. Execution Path UI
   - deterministic code
   - structured lookup
   - local model
   - larger model
   - external/provider/distributed route disabled by default
   - model escalation only when needed

### KORA Runtime Layer

Responsibilities:

- Standard Mode direct local model path
- KORA Boost execution-control path
- deterministic/fast path routing
- model escalation
- validation result
- telemetry counters

### Local Model Runtime

Initial runtime:

- Ollama first

Future runtimes:

- llama.cpp
- MLX
- vLLM
- other local runtimes

Future runtime support must be explicit opt-in and fail-closed until implemented.

### Local Storage

Options:

- SQLite or local JSON first
- project metadata
- conversation history
- execution traces
- report references

## Data Flow

```text
CLI -> Local Studio Server -> Browser UI
Browser UI -> KORA Runtime Layer -> Local Runtime
KORA Runtime Layer -> Execution Trace -> Counter Dashboard
Validation Reports -> Report Viewer
```

## Security and Privacy

- local-first
- no API keys required for v0.1 local flow
- no cloud upload by default
- no raw provider responses committed
- no private data in public artifacts

## Non-Goals

- no hosted cloud dashboard
- no user accounts
- no billing
- no production monitoring
- no provider cost dashboard in v0.1

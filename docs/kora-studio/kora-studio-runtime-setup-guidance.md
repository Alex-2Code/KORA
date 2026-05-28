# KORA Studio Runtime Setup Guidance

## Status and Boundary

This document is an informational setup guidance scaffold for KORA Studio. It is not an installer, model downloader, runtime adapter, registry client, or model execution path.

No install command is executed by KORA Studio in this scaffold. No model is downloaded. No model is executed. No private model directories are scanned. No runtime model list command is called. No provider call is made. Provider and cloud routes are disabled by default.

Setup guidance is informational in this scaffold. Disabled actions point to guidance, not to an active installer.

## Purpose

KORA Studio needs a public-safe place to explain runtime and model setup boundaries before any active install, download, or run behavior is connected. This keeps the local AI Task Execution Router experience explicit about what is detected, estimated, installed, downloadable, and executable.

## What This Guidance Does

- Defines setup concepts for local runtime readiness.
- Explains catalog examples, installed models, downloadable models, and runnable models as separate states.
- Gives disabled action UI a guidance target without connecting an installer.
- Preserves local-only, provider-disabled, cloud-disabled defaults.
- Keeps KORA Boost language tied to routing less work to the model, not to changing hardware requirements.

## What This Guidance Does Not Do

- It does not install runtimes.
- It does not download models.
- It does not execute models.
- It does not scan private model directories.
- It does not call runtime model list commands.
- It does not call provider APIs.
- It does not fetch Hugging Face, Ollama registry, or remote catalog data.
- It does not prove model execution readiness.

## Runtime Setup Concepts

Runtime setup should be represented as distinct local states:

- Runtime executable detected: a local executable path was detected safely.
- Service reachable: a localhost-only service endpoint may be reachable.
- Installed models detected: a future safe local method may confirm installed models.
- Model execution connected: a future explicit execution adapter may run a selected model.

These states must not be collapsed into a single "ready" label until future validation supports it.

## Catalog vs Installed vs Downloadable

Catalog examples are curated examples. They are not installed models.

Installed models are models detected locally by an approved local-only method. That method is not connected by default in this scaffold.

Downloadable models are future action candidates only. Download actions remain disabled and do not imply that a model is available, supported, installed, or runnable.

## Runtime Readiness Distinction

KORA Studio should distinguish:

- executable detected
- service reachable
- installed models detected
- model execution connected

Runtime executable detection is not model execution readiness. Service reachability is not model execution readiness. Installed model detection is not connected by default.

## Planned Runtime Guidance

Mock runtime: used for deterministic local UI and test scaffolding only.

Ollama planned guidance: future guidance may explain how an explicitly user-managed local Ollama runtime relates to KORA Studio state. This scaffold does not call Ollama APIs, list Ollama models, pull models, or run models.

llama.cpp planned guidance: future guidance may explain how an explicitly user-managed local llama.cpp runtime relates to KORA Studio state. This scaffold does not execute binaries, scan model folders, list models, or run models.

Provider/external route: disabled by default. Any provider, external, or distributed route must require explicit opt-in in future work.

## Disabled Action UI Behavior

Disabled download and run actions may point to this guidance. They must not look like active installers or active run controls.

Acceptable labels include:

- Download not connected yet
- Run not connected yet
- Setup guidance is informational
- Validate model fit before use

## Failure Modes

- Runtime executable not detected.
- Runtime service not reachable.
- Installed model detection not connected.
- Model not installed.
- Model download unavailable.
- Model execution not connected.
- Insufficient memory for a selected model.
- Provider route disabled.

## Claim-Safe Wording

- Setup guidance is informational in this scaffold.
- Disabled actions point to guidance, not to an active installer.
- Catalog examples are not installed models.
- Runtime executable detection is not model execution readiness.
- KORA does not remove model memory requirements.

## Forbidden Wording

- Download now
- Run now
- Install now
- All open-source LLMs supported
- KORA runs 70B locally on unsupported hardware
- KORA removes VRAM/RAM requirements
- Cost or energy reduction proven

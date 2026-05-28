"""Static claim-safe KORA Studio model catalog scaffold."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from kora.studio_system_profile import StudioSystemProfile

MODEL_CATALOG_CLAIM_BOUNDARY = (
    "Model recommendations are estimates until validated on this machine. "
    "KORA does not remove model memory requirements. "
    "Download and execution are not connected yet."
)
MODEL_ACTION_CLAIM_BOUNDARY = (
    "Model actions are disabled planning scaffolds. Catalog examples are not installed models. "
    "KORA does not remove model memory requirements."
)
SETUP_GUIDANCE_PATH = "docs/kora-studio/kora-studio-runtime-setup-guidance.md"

REQUIRED_MODEL_CATALOG_FIELDS = {
    "model_id",
    "display_name",
    "family",
    "parameter_tier",
    "quantization",
    "runtime_compatibility",
    "estimated_memory_gb",
    "local_chat_tier",
    "workflow_role",
    "recommendation_tags",
    "license_note",
    "source_note",
    "validation_status",
    "claim_boundary",
}

STATIC_MODEL_CATALOG: list[dict[str, Any]] = [
    {
        "model_id": "example-mini-local",
        "display_name": "Example mini local model",
        "family": "generic local model family",
        "parameter_tier": "small/mini",
        "quantization": "quantized",
        "runtime_compatibility": ["ollama", "llama.cpp"],
        "estimated_memory_gb": 4,
        "local_chat_tier": "small/mini local models only",
        "workflow_role": "physically_runnable_local_candidate",
        "recommendation_tags": ["conservative", "local-chat", "low-memory"],
        "license_note": "Check the selected model license before use.",
        "source_note": "Static local catalog example; no remote catalog lookup performed.",
        "validation_status": "estimate_until_validated",
        "claim_boundary": MODEL_CATALOG_CLAIM_BOUNDARY,
    },
    {
        "model_id": "example-3b-quantized",
        "display_name": "Example 3B quantized model",
        "family": "generic local model family",
        "parameter_tier": "3B",
        "quantization": "quantized",
        "runtime_compatibility": ["ollama", "llama.cpp"],
        "estimated_memory_gb": 6,
        "local_chat_tier": "3B-7B quantized tier",
        "workflow_role": "physically_runnable_local_candidate",
        "recommendation_tags": ["local-chat", "quantized", "starter"],
        "license_note": "Check the selected model license before use.",
        "source_note": "Static local catalog example; no remote catalog lookup performed.",
        "validation_status": "estimate_until_validated",
        "claim_boundary": MODEL_CATALOG_CLAIM_BOUNDARY,
    },
    {
        "model_id": "example-7b-8b-quantized",
        "display_name": "Example 7B-8B quantized model",
        "family": "generic local model family",
        "parameter_tier": "7B-8B",
        "quantization": "quantized",
        "runtime_compatibility": ["ollama", "llama.cpp"],
        "estimated_memory_gb": 10,
        "local_chat_tier": "7B-8B quantized tier",
        "workflow_role": "physically_runnable_local_candidate",
        "recommendation_tags": ["local-chat", "balanced", "quantized"],
        "license_note": "Check the selected model license before use.",
        "source_note": "Static local catalog example; no remote catalog lookup performed.",
        "validation_status": "estimate_until_validated",
        "claim_boundary": MODEL_CATALOG_CLAIM_BOUNDARY,
    },
    {
        "model_id": "example-13b-quantized",
        "display_name": "Example 13B quantized model",
        "family": "generic local model family",
        "parameter_tier": "13B",
        "quantization": "quantized",
        "runtime_compatibility": ["ollama", "llama.cpp"],
        "estimated_memory_gb": 24,
        "local_chat_tier": "7B-13B quantized tier",
        "workflow_role": "larger_model_workflow_candidate",
        "recommendation_tags": ["workflow", "larger-model", "quantized"],
        "license_note": "Check the selected model license before use.",
        "source_note": "Static local catalog example; no remote catalog lookup performed.",
        "validation_status": "estimate_until_validated",
        "claim_boundary": MODEL_CATALOG_CLAIM_BOUNDARY,
    },
    {
        "model_id": "example-larger-workflow",
        "display_name": "Example larger workflow model",
        "family": "generic local or external-capable model family",
        "parameter_tier": "larger workflow tier",
        "quantization": "runtime-dependent",
        "runtime_compatibility": ["local runtime if validated", "external/provider route disabled by default"],
        "estimated_memory_gb": 48,
        "local_chat_tier": "larger workflow tier",
        "workflow_role": "larger_model_workflow_candidate",
        "recommendation_tags": ["workflow", "model-needed-tasks", "requires-validation"],
        "license_note": "Check the selected model license and route policy before use.",
        "source_note": "Static local catalog example; no remote catalog lookup performed.",
        "validation_status": "estimate_until_validated",
        "claim_boundary": MODEL_CATALOG_CLAIM_BOUNDARY,
    },
]


def get_static_model_catalog() -> list[dict[str, Any]]:
    """Return static catalog entries without remote calls."""

    return deepcopy(STATIC_MODEL_CATALOG)


def _memory_gb_from_profile(profile: StudioSystemProfile | dict[str, Any]) -> float | None:
    profile_dict = profile.to_dict() if isinstance(profile, StudioSystemProfile) else profile
    memory_gb = profile_dict.get("total_memory_gb")
    return float(memory_gb) if isinstance(memory_gb, (int, float)) else None


def _is_candidate_allowed(entry: dict[str, Any], memory_gb: float | None) -> bool:
    estimated_memory = entry.get("estimated_memory_gb")
    if not isinstance(estimated_memory, (int, float)):
        return False
    if memory_gb is None:
        return entry["model_id"] in {"example-mini-local", "example-3b-quantized", "example-13b-quantized"}
    if entry["workflow_role"] == "physically_runnable_local_candidate":
        return estimated_memory <= memory_gb
    return estimated_memory <= max(memory_gb, 16)


def _attach_disabled_action_state(item: dict[str, Any], *, runtime_detected: bool, runtime_service_reachable: bool) -> None:
    item["download_action_status"] = "not_connected"
    item["download_action_enabled"] = False
    item["download_action_label"] = "Download not connected yet"
    item["download_action_reason"] = (
        "Setup guidance is informational in this scaffold; download is not connected."
        if not runtime_detected
        else "Download is planned but not connected; see setup guidance for boundaries."
    )
    item["run_action_status"] = "not_connected"
    item["run_action_enabled"] = False
    item["run_action_label"] = "Run not connected yet"
    item["run_action_reason"] = (
        "Validate model fit before use; runtime service and execution are not connected yet."
        if runtime_service_reachable
        else "Runtime service and model execution are not connected yet."
    )
    item["install_guidance"] = (
        "Setup guidance is informational only and does not install or download models."
        if not runtime_detected
        else "Catalog examples are not installed models; setup guidance does not install or download models."
    )
    item["runtime_guidance"] = (
        "Runtime service reachability is not model execution readiness. Download and execution are not connected yet."
    )
    item["setup_guidance_path"] = SETUP_GUIDANCE_PATH
    item["disabled_actions_route_to_guidance"] = True
    item["action_claim_boundary"] = MODEL_ACTION_CLAIM_BOUNDARY


def recommend_catalog_models(
    profile: StudioSystemProfile | dict[str, Any],
    capability_estimate: dict[str, Any],
    runtime_status: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Return claim-safe catalog recommendations from the static local catalog."""

    memory_gb = _memory_gb_from_profile(profile)
    recommendation_status = str(capability_estimate.get("recommendation_status", "unknown"))
    runtimes = runtime_status or []
    runtime_detected = any(item.get("executable_detected") is True for item in runtimes if isinstance(item, dict))
    runtime_service_reachable = any(item.get("service_reachable") is True for item in runtimes if isinstance(item, dict))
    installed_model_ids = {
        str(model.get("model_id"))
        for runtime in runtimes
        if isinstance(runtime, dict)
        for model in runtime.get("installed_models", [])
        if isinstance(model, dict) and model.get("model_id")
    }
    recommended: list[dict[str, Any]] = []

    for entry in get_static_model_catalog():
        if not _is_candidate_allowed(entry, memory_gb):
            continue

        item = deepcopy(entry)
        estimated_memory = item["estimated_memory_gb"]
        if memory_gb is None:
            item["candidate_type"] = "unknown_needs_validation"
            item["recommendation_status"] = "unknown_needs_validation"
            item["recommendation_note"] = (
                "Memory is unknown, so this example is not claimed as physically runnable until validated."
            )
        elif item["workflow_role"] == "physically_runnable_local_candidate" and estimated_memory <= memory_gb:
            item["candidate_type"] = "physically_runnable_local_candidate"
            item["recommendation_status"] = recommendation_status
            item["recommendation_note"] = (
                "This is a local candidate estimate based on memory tier and still requires runtime validation."
            )
        else:
            item["candidate_type"] = "larger_model_workflow_candidate"
            item["recommendation_status"] = "needs_validation"
            item["recommendation_note"] = (
                "This is a workflow candidate only; KORA Boost may reduce model-needed work, but memory and runtime "
                "requirements still apply."
            )
        item["download_available"] = False
        item["execution_available"] = False
        item["catalog_candidate"] = True
        item["estimated_runnable"] = item["candidate_type"] == "physically_runnable_local_candidate"
        item["runtime_detected"] = runtime_detected
        item["runtime_service_reachable"] = runtime_service_reachable
        item["installed_locally"] = item["model_id"] in installed_model_ids
        item["installed_model_detection_status"] = "detected" if item["installed_locally"] else "not_connected"
        item["catalog_vs_installed_boundary"] = "Catalog examples are not installed models unless explicitly detected."
        item["download_available"] = False
        item["execution_connected"] = False
        _attach_disabled_action_state(
            item,
            runtime_detected=runtime_detected,
            runtime_service_reachable=runtime_service_reachable,
        )
        item["claim_boundary"] = MODEL_CATALOG_CLAIM_BOUNDARY
        recommended.append(item)

    if not any(item["candidate_type"] == "larger_model_workflow_candidate" for item in recommended):
        larger = deepcopy(STATIC_MODEL_CATALOG[-1])
        larger["candidate_type"] = "larger_model_workflow_candidate"
        larger["recommendation_status"] = "needs_validation"
        larger["recommendation_note"] = (
            "Shown as a larger-model workflow example only. It is not claimed as physically runnable here."
        )
        larger["download_available"] = False
        larger["execution_available"] = False
        larger["catalog_candidate"] = True
        larger["estimated_runnable"] = False
        larger["runtime_detected"] = runtime_detected
        larger["runtime_service_reachable"] = runtime_service_reachable
        larger["installed_locally"] = larger["model_id"] in installed_model_ids
        larger["installed_model_detection_status"] = "detected" if larger["installed_locally"] else "not_connected"
        larger["catalog_vs_installed_boundary"] = "Catalog examples are not installed models unless explicitly detected."
        larger["download_available"] = False
        larger["execution_connected"] = False
        _attach_disabled_action_state(
            larger,
            runtime_detected=runtime_detected,
            runtime_service_reachable=runtime_service_reachable,
        )
        larger["claim_boundary"] = MODEL_CATALOG_CLAIM_BOUNDARY
        recommended.append(larger)

    return recommended

from __future__ import annotations

from kora.studio_model_catalog import (
    MODEL_CATALOG_CLAIM_BOUNDARY,
    REQUIRED_MODEL_CATALOG_FIELDS,
    get_static_model_catalog,
    recommend_catalog_models,
)
from kora.studio_runtime_status import get_runtime_status
from kora.studio_system_profile import estimate_model_capability, get_system_profile


def _recommend_for_memory(memory_gb: float | None) -> list[dict]:
    profile = get_system_profile(which=lambda command: None, total_memory_gb=memory_gb)
    runtime_status = get_runtime_status(which=lambda command: None)
    return recommend_catalog_models(profile, estimate_model_capability(profile), runtime_status)


def test_catalog_entries_include_required_fields() -> None:
    catalog = get_static_model_catalog()

    assert catalog
    for entry in catalog:
        assert REQUIRED_MODEL_CATALOG_FIELDS.issubset(entry)
        assert entry["validation_status"] == "estimate_until_validated"
        assert entry["claim_boundary"] == MODEL_CATALOG_CLAIM_BOUNDARY
        assert isinstance(entry["runtime_compatibility"], list)
        assert "remote catalog lookup performed" in entry["source_note"].lower()
        assert "download now" not in str(entry).lower()


def test_recommendations_for_unknown_memory_are_conservative() -> None:
    recommendations = _recommend_for_memory(None)

    assert recommendations
    assert any(item["candidate_type"] == "unknown_needs_validation" for item in recommendations)
    assert any(item["candidate_type"] == "larger_model_workflow_candidate" for item in recommendations)
    for item in recommendations:
        assert item["download_available"] is False
        assert item["execution_available"] is False
        assert item["download_action_enabled"] is False
        assert item["run_action_enabled"] is False
        assert item["download_action_label"] == "Download not connected yet"
        assert item["run_action_label"] == "Run not connected yet"
        assert item["disabled_actions_route_to_guidance"] is True
        assert item["setup_guidance_path"] == "docs/kora-studio/kora-studio-runtime-setup-guidance.md"
        assert "guidance" in item["download_action_reason"].lower()
        assert "not install or download" in item["install_guidance"].lower()
        assert item["download_action_status"] == "not_connected"
        assert item["run_action_status"] == "not_connected"
        assert "not connected" in item["runtime_guidance"].lower()
        assert item["catalog_candidate"] is True
        assert item["installed_locally"] is False
        assert item["execution_connected"] is False
        assert "not claimed as physically runnable" in item["recommendation_note"].lower() or "requires" in item[
            "recommendation_note"
        ].lower()


def test_recommendations_for_small_memory_tier() -> None:
    recommendations = _recommend_for_memory(4)

    runnable_ids = {
        item["model_id"]
        for item in recommendations
        if item["candidate_type"] == "physically_runnable_local_candidate"
    }
    assert "example-mini-local" in runnable_ids
    assert "example-3b-quantized" not in runnable_ids
    assert any(item["candidate_type"] == "larger_model_workflow_candidate" for item in recommendations)


def test_recommendations_distinguish_catalog_runtime_and_installed_status() -> None:
    runtime_status = get_runtime_status(which=lambda command: "/mock/bin/ollama" if command == "ollama" else None)
    profile = get_system_profile(which=lambda command: None, total_memory_gb=16)
    recommendations = recommend_catalog_models(profile, estimate_model_capability(profile), runtime_status)

    assert recommendations
    for item in recommendations:
        assert item["catalog_candidate"] is True
        assert item["runtime_detected"] is True
        assert item["runtime_service_reachable"] is False
        assert item["installed_locally"] is False
        assert item["installed_model_detection_status"] == "not_connected"
        assert "Catalog examples are not installed models" in item["catalog_vs_installed_boundary"]
        assert item["download_available"] is False
        assert item["download_action_enabled"] is False
        assert item["download_action_label"] == "Download not connected yet"
        assert item["execution_connected"] is False
        assert item["run_action_enabled"] is False
        assert item["run_action_label"] == "Run not connected yet"


def test_recommendations_can_reflect_explicit_mock_installed_models() -> None:
    runtime_status = get_runtime_status(
        which=lambda command: None,
        detect_installed_models=True,
        installed_model_detector=lambda runtime_id: [
            {
                "model_id": "example-mini-local",
                "display_name": "Example mini local model",
                "runtime_id": runtime_id,
                "source": "mock_test_data",
                "detection_method": "mock_detector",
                "validation_status": "mocked_not_validated",
            }
        ]
        if runtime_id == "ollama"
        else [],
    )
    profile = get_system_profile(which=lambda command: None, total_memory_gb=16)
    recommendations = recommend_catalog_models(profile, estimate_model_capability(profile), runtime_status)
    by_id = {item["model_id"]: item for item in recommendations}

    assert by_id["example-mini-local"]["installed_locally"] is True
    assert by_id["example-mini-local"]["installed_model_detection_status"] == "detected"
    assert by_id["example-3b-quantized"]["installed_locally"] is False
    assert by_id["example-3b-quantized"]["installed_model_detection_status"] == "not_connected"


def test_recommendations_include_disabled_action_guidance() -> None:
    recommendations = _recommend_for_memory(16)

    assert recommendations
    for item in recommendations:
        assert item["download_action_status"] == "not_connected"
        assert item["download_action_enabled"] is False
        assert item["run_action_status"] == "not_connected"
        assert item["run_action_enabled"] is False
        assert "KORA does not remove model memory requirements" in item["action_claim_boundary"]
        assert item["disabled_actions_route_to_guidance"] is True
        assert "guidance" in item["download_action_reason"].lower()
        assert "readiness" in item["run_action_reason"].lower() or "not connected" in item["run_action_reason"].lower()
        assert "Download now" not in str(item)
        assert "Run now" not in str(item)
        assert "Install now" not in str(item)


def test_recommendations_for_mid_memory_tiers() -> None:
    sixteen_gb_ids = {
        item["model_id"]
        for item in _recommend_for_memory(16)
        if item["candidate_type"] == "physically_runnable_local_candidate"
    }
    thirty_two_gb_ids = {
        item["model_id"]
        for item in _recommend_for_memory(32)
        if item["candidate_type"] == "physically_runnable_local_candidate"
    }

    assert "example-7b-8b-quantized" in sixteen_gb_ids
    assert "example-13b-quantized" not in sixteen_gb_ids
    assert "example-7b-8b-quantized" in thirty_two_gb_ids


def test_recommendations_for_64gb_tier_include_larger_workflow_candidate() -> None:
    recommendations = _recommend_for_memory(64)

    assert any(item["model_id"] == "example-13b-quantized" for item in recommendations)
    assert any(item["candidate_type"] == "larger_model_workflow_candidate" for item in recommendations)
    text = " ".join(str(value) for item in recommendations for value in item.values()).lower()
    assert "all open-source llms supported" not in text
    assert "runs 70b locally" not in text
    assert "removes vram requirements" not in text
    assert "guarantees cost" not in text
    assert "guarantees energy" not in text

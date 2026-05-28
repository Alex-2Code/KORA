from __future__ import annotations

from kora.studio_model_catalog import (
    MODEL_CATALOG_CLAIM_BOUNDARY,
    REQUIRED_MODEL_CATALOG_FIELDS,
    get_static_model_catalog,
    recommend_catalog_models,
)
from kora.studio_system_profile import estimate_model_capability, get_system_profile


def _recommend_for_memory(memory_gb: float | None) -> list[dict]:
    profile = get_system_profile(which=lambda command: None, total_memory_gb=memory_gb)
    return recommend_catalog_models(profile, estimate_model_capability(profile))


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

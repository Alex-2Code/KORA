from __future__ import annotations

import json
from pathlib import Path

from kora.studio_harness_requests import (
    LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
    LOCAL_HARNESS_REQUEST_SCHEMA_FIELDS,
    LOCAL_HARNESS_REQUESTS_FIXTURE_PATH,
    get_local_harness_request_by_id,
    get_local_harness_request_summary,
    get_local_harness_requests,
    validate_local_harness_request,
)


def test_local_harness_requests_cover_required_task_families() -> None:
    requests = get_local_harness_requests()
    task_families = {request["task_family"] for request in requests}

    assert len(requests) == 5
    assert {
        "json_required_fields",
        "policy_rule_classification",
        "known_faq_lookup",
        "structured_record_normalization",
        "ambiguous_generation_boundary",
    } == task_families


def test_local_harness_requests_include_required_fields_and_boundaries() -> None:
    requests = get_local_harness_requests()

    assert all(validate_local_harness_request(request) for request in requests)
    for request in requests:
        assert set(LOCAL_HARNESS_REQUEST_SCHEMA_FIELDS) <= set(request)
        assert request["claim_boundary"] == LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY
        assert request["provider_calls_enabled"] is False
        assert request["cloud_sync_enabled"] is False
        assert request["model_execution_connected"] is False
        assert "private" not in request["input_text"].lower()


def test_local_harness_requests_distinguish_model_needed_boundary() -> None:
    requests = get_local_harness_requests()
    model_needed = [request for request in requests if request["expected_model_needed"]]
    deterministic = [request for request in requests if not request["expected_model_needed"]]

    assert len(model_needed) == 1
    assert model_needed[0]["expected_route_class"] == "model_needed_boundary"
    assert model_needed[0]["expected_validation_result"] == "not_applicable"
    assert len(deterministic) == 4
    assert all(request["expected_validation_result"] == "pass" for request in deterministic)


def test_get_local_harness_request_by_id_returns_copy() -> None:
    request = get_local_harness_request_by_id("local-harness-known-faq-001")
    assert request is not None
    request["task_family"] = "mutated"

    fresh_request = get_local_harness_request_by_id("local-harness-known-faq-001")
    assert fresh_request is not None
    assert fresh_request["task_family"] == "known_faq_lookup"
    assert get_local_harness_request_by_id("missing") is None


def test_local_harness_request_summary_is_claim_safe() -> None:
    summary = get_local_harness_request_summary()

    assert summary["local_harness_request_status"] == "static_local_deterministic_request_set"
    assert summary["local_harness_request_count"] == 5
    assert summary["local_harness_request_schema_fields"] == LOCAL_HARNESS_REQUEST_SCHEMA_FIELDS
    assert summary["local_harness_model_needed_request_count"] == 1
    assert summary["local_harness_requests_fixture_path"] == LOCAL_HARNESS_REQUESTS_FIXTURE_PATH
    assert summary["local_harness_request_claim_boundary"] == LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY
    assert summary["provider_calls_enabled"] is False
    assert summary["cloud_sync_enabled"] is False
    assert summary["model_execution_connected"] is False
    assert summary["download_connected"] is False


def test_local_harness_requests_fixture_matches_module() -> None:
    fixture_path = Path(LOCAL_HARNESS_REQUESTS_FIXTURE_PATH)
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    module_requests = get_local_harness_requests()

    assert fixture["fixture_type"] == "local_harness_requests"
    assert fixture["privacy_class"] == "synthetic"
    assert fixture["claim_boundary"] == LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY
    assert fixture["provider_calls_enabled"] is False
    assert fixture["cloud_sync_enabled"] is False
    assert fixture["model_execution_connected"] is False
    assert fixture["download_connected"] is False
    assert fixture["schema_fields"] == LOCAL_HARNESS_REQUEST_SCHEMA_FIELDS
    assert fixture["requests"] == module_requests

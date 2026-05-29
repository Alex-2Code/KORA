from __future__ import annotations

import pytest

from kora.studio_execution_fixture import EXECUTION_EVENT_SCHEMA_FIELDS
from kora.studio_harness_events import (
    LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY,
    build_local_harness_counters,
    build_local_harness_events,
    validate_local_harness_event,
)
from kora.studio_harness_requests import get_local_harness_request_by_id


def test_local_harness_events_cover_deterministic_route_stages() -> None:
    run = build_local_harness_events("local-harness-json-required-fields-001")
    stage_ids = [event["stage_id"] for event in run["events"]]

    assert stage_ids == [
        "request_received",
        "route_selected",
        "deterministic_check",
        "validation",
        "model_fallback_skipped",
        "final_counters",
    ]
    assert all(validate_local_harness_event(event) for event in run["events"])
    assert run["local_harness_event_schema_fields"] == EXECUTION_EVENT_SCHEMA_FIELDS


def test_local_harness_structured_lookup_adds_lookup_stage() -> None:
    run = build_local_harness_events("local-harness-known-faq-001")
    stage_ids = [event["stage_id"] for event in run["events"]]

    assert "structured_lookup" in stage_ids
    assert run["counters_snapshot"]["structured_lookup_routes"] == 1
    assert run["counters_snapshot"]["avoided_model_calls"] == 1
    assert run["counters_snapshot"]["kora_model_calls"] == 0
    assert run["events"][-1]["counters_snapshot"] == run["counters_snapshot"]


def test_local_harness_model_needed_boundary_does_not_execute_model() -> None:
    run = build_local_harness_events("local-harness-ambiguous-model-needed-001")
    stage_by_id = {event["stage_id"]: event for event in run["events"]}

    assert "model_needed_boundary" in stage_by_id
    assert "model_fallback_skipped" not in stage_by_id
    assert stage_by_id["model_needed_boundary"]["status"] == "execution_not_connected"
    assert run["counters_snapshot"]["model_escalations"] == 1
    assert run["counters_snapshot"]["fallback_count"] == 1
    assert run["counters_snapshot"]["avoided_model_calls"] == 0
    assert all(event["model_called"] is False for event in run["events"])


def test_local_harness_events_are_local_only_and_claim_safe() -> None:
    run = build_local_harness_events("local-harness-policy-rule-001")

    assert "synthetic deterministic requests" in LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY
    assert "do not execute models" in LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY
    assert "call providers" in LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY
    assert run["claim_boundary"] == LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY
    assert run["provider_calls_enabled"] is False
    assert run["cloud_sync_enabled"] is False
    assert run["model_execution_connected"] is False
    assert run["download_connected"] is False
    for event in run["events"]:
        assert event["adapter_name"] == "local_deterministic_harness"
        assert event["adapter_mode"] == "local_fixture"
        assert event["provider_calls_enabled"] is False
        assert event["cloud_sync_enabled"] is False
        assert event["error_code"] is None
        assert event["error_message"] is None


def test_local_harness_counters_match_request_route_expectations() -> None:
    policy_request = get_local_harness_request_by_id("local-harness-policy-rule-001")
    assert policy_request is not None
    policy_counters = build_local_harness_counters(policy_request)

    assert policy_counters["policy_routes"] == 1
    assert policy_counters["deterministic_routes"] == 0
    assert policy_counters["structured_lookup_routes"] == 0
    assert policy_counters["validation_pass_count"] == 1
    assert policy_counters["avoided_model_calls"] == 1
    assert policy_counters["avoided_model_call_rate"] == 1.0


def test_local_harness_event_builder_rejects_unknown_request_id() -> None:
    with pytest.raises(ValueError, match="Unknown local harness request id"):
        build_local_harness_events("missing-request")


def test_local_harness_event_builder_rejects_invalid_request() -> None:
    with pytest.raises(ValueError, match="missing required claim-safe fields"):
        build_local_harness_events(
            {
                "request_id": "bad",
                "input_text": "bad",
                "task_family": "bad",
            }
        )

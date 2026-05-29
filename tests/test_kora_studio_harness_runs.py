from __future__ import annotations

import pytest

from kora.studio_harness_runs import (
    LOCAL_HARNESS_RUN_CLAIM_BOUNDARY,
    clear_local_harness_run_records,
    get_local_harness_run_record,
    get_local_harness_run_store_status,
    trigger_local_harness_run,
)


def test_trigger_local_harness_run_accepts_approved_request_id() -> None:
    clear_local_harness_run_records()

    run = trigger_local_harness_run("local-harness-json-required-fields-001")

    assert run["ok"] is True
    assert run["request_id"] == "local-harness-json-required-fields-001"
    assert run["run_id"].startswith("local-harness-trigger-")
    assert run["run_status"] == "completed"
    assert run["selected_request"]["expected_route_class"] == "deterministic_code"
    assert run["generated_events"][0]["stage_id"] == "request_received"
    assert run["generated_events"][-1]["stage_id"] == "final_counters"
    assert run["generated_events"][0]["run_id"] == run["run_id"]
    assert run["generated_counters"]["baseline_model_calls"] == 1
    assert run["generated_counters"]["kora_model_calls"] == 0
    assert run["generated_counters"]["avoided_model_calls"] == 1
    assert run["comparison_summary"]["metrics"]["avoided_model_calls"] == 1
    assert run["report_metadata_summary"]["report_source"] == "local_harness_summary"
    assert run["model_needed_boundary_status"] == "not_needed"
    assert run["provider_calls_enabled"] is False
    assert run["cloud_sync_enabled"] is False
    assert run["model_execution_connected"] is False
    assert run["download_connected"] is False
    assert run["runtime_model_list_connected"] is False
    assert run["private_directory_scan_enabled"] is False
    assert run["claim_boundary"] == LOCAL_HARNESS_RUN_CLAIM_BOUNDARY


def test_trigger_local_harness_run_preserves_model_needed_boundary_without_execution() -> None:
    clear_local_harness_run_records()

    run = trigger_local_harness_run("local-harness-ambiguous-model-needed-001")

    assert run["run_status"] == "completed"
    assert run["selected_request"]["expected_model_needed"] is True
    assert run["model_needed_boundary_status"] == "execution_not_connected"
    assert run["generated_counters"]["model_escalations"] == 1
    assert run["generated_counters"]["kora_model_calls"] == 0
    assert run["generated_counters"]["avoided_model_calls"] == 0
    assert any(event["status"] == "execution_not_connected" for event in run["generated_events"])
    assert all(event["model_called"] is False for event in run["generated_events"])
    assert run["model_execution_connected"] is False


def test_trigger_local_harness_run_rejects_unknown_request_id() -> None:
    clear_local_harness_run_records()

    with pytest.raises(ValueError, match="Unknown approved local harness request id"):
        trigger_local_harness_run("missing-request")


def test_local_harness_run_store_is_in_memory_only() -> None:
    clear_local_harness_run_records()
    empty_status = get_local_harness_run_store_status()
    assert empty_status["run_store_status"] == "in_memory_local_only"
    assert empty_status["run_store_record_count"] == 0
    assert empty_status["persistence_enabled"] is False

    run = trigger_local_harness_run("local-harness-known-faq-001")
    stored = get_local_harness_run_record(run["run_id"])

    assert stored == run
    assert get_local_harness_run_record("missing-run") is None
    assert get_local_harness_run_store_status()["run_store_record_count"] == 1

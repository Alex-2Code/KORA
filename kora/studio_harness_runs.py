"""Local-only run trigger scaffold for KORA Studio harness requests."""

from __future__ import annotations

from copy import deepcopy
from typing import Any
from uuid import uuid4

from kora.studio_harness_comparison import build_local_harness_comparison
from kora.studio_harness_events import LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY, build_local_harness_events
from kora.studio_harness_requests import get_local_harness_request_by_id
from kora.studio_report_viewer import get_report_viewer_status_fields

LOCAL_HARNESS_RUN_CLAIM_BOUNDARY = (
    "Local harness runs are generated only from approved synthetic deterministic request IDs. They do not "
    "execute models, call providers, download models, scan private data, list runtime models, or prove "
    "production behavior."
)

_LOCAL_HARNESS_RUNS: dict[str, dict[str, Any]] = {}


def _selected_request_summary(request: dict[str, Any]) -> dict[str, Any]:
    return {
        "request_id": request["request_id"],
        "input_text": request["input_text"],
        "task_family": request["task_family"],
        "expected_route_class": request["expected_route_class"],
        "expected_validation_result": request["expected_validation_result"],
        "expected_model_needed": request["expected_model_needed"],
        "claim_boundary": request["claim_boundary"],
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "download_connected": False,
    }


def clear_local_harness_run_records() -> None:
    """Clear in-memory run records for tests."""

    _LOCAL_HARNESS_RUNS.clear()


def trigger_local_harness_run(request_id: str) -> dict[str, Any]:
    """Generate a local harness run for an approved deterministic sample request."""

    selected_request = get_local_harness_request_by_id(request_id)
    if selected_request is None:
        raise ValueError(f"Unknown approved local harness request id: {request_id}")

    run_id = f"local-harness-trigger-{uuid4().hex}"
    harness_run = build_local_harness_events(selected_request, run_id=run_id)
    comparison = build_local_harness_comparison(selected_request)
    report_fields = get_report_viewer_status_fields(
        harness_run["counters_snapshot"],
        report_source="local_harness_summary",
    )
    generated_events = deepcopy(harness_run["events"])
    generated_counters = deepcopy(harness_run["counters_snapshot"])
    model_needed = bool(selected_request["expected_model_needed"])

    run_record = {
        "ok": True,
        "run_id": run_id,
        "request_id": selected_request["request_id"],
        "run_status": "completed",
        "run_state": "completed",
        "selected_request": _selected_request_summary(selected_request),
        "generated_events": generated_events,
        "generated_counters": generated_counters,
        "comparison_summary": {
            "comparison_status": comparison["comparison_status"],
            "comparison_source": comparison["comparison_source"],
            "request_id": comparison["request_id"],
            "metrics": deepcopy(comparison["metrics"]),
            "comparison_counters": deepcopy(comparison["comparison_counters"]),
            "claim_boundary": comparison["claim_boundary"],
            "provider_calls_enabled": False,
            "cloud_sync_enabled": False,
            "model_execution_connected": False,
            "download_connected": False,
        },
        "report_metadata_summary": {
            "report_viewer_status": report_fields["report_viewer_status"],
            "report_source": report_fields["report_viewer_placeholder"]["report_source"],
            "report_status": report_fields["report_viewer_placeholder"]["report_status"],
            "report_export_status": report_fields["report_export_status"],
            "claim_boundary": report_fields["report_viewer_claim_boundary"],
            "export_claim_boundary": report_fields["report_export_claim_boundary"],
            "arbitrary_local_file_scan_enabled": False,
            "upload_enabled": False,
            "generated_report_commit_enabled": False,
        },
        "model_needed_boundary_status": "execution_not_connected" if model_needed else "not_needed",
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "download_connected": False,
        "runtime_model_list_connected": False,
        "private_directory_scan_enabled": False,
        "claim_boundary": LOCAL_HARNESS_RUN_CLAIM_BOUNDARY,
        "event_claim_boundary": LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY,
    }
    _LOCAL_HARNESS_RUNS[run_id] = deepcopy(run_record)
    return deepcopy(run_record)


def get_local_harness_run_record(run_id: str) -> dict[str, Any] | None:
    """Return an in-memory local harness run record by id."""

    record = _LOCAL_HARNESS_RUNS.get(run_id)
    return deepcopy(record) if record is not None else None


def get_local_harness_run_store_status() -> dict[str, Any]:
    """Return claim-safe in-memory run store metadata."""

    return {
        "run_store_status": "in_memory_local_only",
        "run_store_record_count": len(_LOCAL_HARNESS_RUNS),
        "persistence_enabled": False,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "download_connected": False,
        "claim_boundary": LOCAL_HARNESS_RUN_CLAIM_BOUNDARY,
    }

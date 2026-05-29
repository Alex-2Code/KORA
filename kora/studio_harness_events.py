"""Local deterministic event builder for the KORA Studio harness."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from kora.studio_execution_fixture import EXECUTION_EVENT_SCHEMA_FIELDS
from kora.studio_harness_requests import (
    LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
    get_local_harness_request_by_id,
    validate_local_harness_request,
)

LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY = (
    "Local harness events are generated from synthetic deterministic requests. They do not execute models, "
    "call providers, download models, scan private data, or prove production behavior."
)


def _zero_counters() -> dict[str, Any]:
    return {
        "total_requests": 1,
        "baseline_model_calls": 1,
        "kora_model_calls": 0,
        "avoided_model_calls": 0,
        "avoided_model_call_rate": 0.0,
        "deterministic_routes": 0,
        "structured_lookup_routes": 0,
        "policy_routes": 0,
        "model_escalations": 0,
        "validation_pass_count": 0,
        "validation_fail_count": 0,
        "error_count": 0,
        "fallback_count": 0,
    }


def build_local_harness_counters(request: dict[str, Any]) -> dict[str, Any]:
    """Build deterministic counters for a local harness request."""

    counters = _zero_counters()
    route_class = request["expected_route_class"]
    validation_result = request["expected_validation_result"]
    model_needed = request["expected_model_needed"]

    if route_class == "structured_lookup":
        counters["structured_lookup_routes"] = 1
    elif route_class == "policy":
        counters["policy_routes"] = 1
    elif route_class == "deterministic_code":
        counters["deterministic_routes"] = 1

    if validation_result == "pass":
        counters["validation_pass_count"] = 1
    elif validation_result == "fail":
        counters["validation_fail_count"] = 1

    if model_needed:
        counters["model_escalations"] = 1
        counters["fallback_count"] = 1
    elif validation_result == "pass":
        counters["avoided_model_calls"] = 1
        counters["avoided_model_call_rate"] = 1.0

    return counters


def _event(
    *,
    run_id: str,
    request: dict[str, Any],
    stage_id: str,
    stage_name: str,
    route_class: str,
    status: str,
    latency_ms: int,
    stage_offset_ms: int,
    model_called: bool = False,
    deterministic_route_used: bool = False,
    structured_lookup_used: bool = False,
    validation_result: str = "not_applicable",
    counters_snapshot: dict[str, Any] | None = None,
    error_code: str | None = None,
    error_message: str | None = None,
) -> dict[str, Any]:
    started_at = f"2026-05-29T00:00:00.{stage_offset_ms:03d}Z"
    completed_at = f"2026-05-29T00:00:00.{stage_offset_ms + latency_ms:03d}Z"
    return {
        "run_id": run_id,
        "request_id": request["request_id"],
        "stage_id": stage_id,
        "stage_name": stage_name,
        "route_class": route_class,
        "status": status,
        "started_at": started_at,
        "completed_at": completed_at,
        "latency_ms": latency_ms,
        "model_called": model_called,
        "deterministic_route_used": deterministic_route_used,
        "structured_lookup_used": structured_lookup_used,
        "validation_result": validation_result,
        "adapter_name": "local_deterministic_harness",
        "adapter_mode": "local_fixture",
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "counters_snapshot": deepcopy(counters_snapshot or {}),
        "error_code": error_code,
        "error_message": error_message,
    }


def build_local_harness_events(request: dict[str, Any] | str) -> dict[str, Any]:
    """Convert a local harness request into claim-safe execution events."""

    if isinstance(request, str):
        selected_request = get_local_harness_request_by_id(request)
        if selected_request is None:
            raise ValueError(f"Unknown local harness request id: {request}")
    else:
        selected_request = deepcopy(request)

    if not validate_local_harness_request(selected_request):
        raise ValueError("Local harness request is missing required claim-safe fields")

    run_id = f"local-harness-run-{selected_request['request_id']}"
    route_class = selected_request["expected_route_class"]
    validation_result = selected_request["expected_validation_result"]
    model_needed = selected_request["expected_model_needed"]
    deterministic_route_used = route_class in {"deterministic_code", "structured_lookup", "policy"}
    structured_lookup_used = route_class == "structured_lookup"
    counters = build_local_harness_counters(selected_request)

    events = [
        _event(
            run_id=run_id,
            request=selected_request,
            stage_id="request_received",
            stage_name="Request received",
            route_class="input",
            status="completed",
            latency_ms=3,
            stage_offset_ms=0,
            counters_snapshot={"total_requests": 1, "baseline_model_calls": 1},
        ),
        _event(
            run_id=run_id,
            request=selected_request,
            stage_id="route_selected",
            stage_name="Route selected",
            route_class=route_class,
            status="completed",
            latency_ms=4,
            stage_offset_ms=3,
            deterministic_route_used=deterministic_route_used,
            structured_lookup_used=structured_lookup_used,
            counters_snapshot={
                "expected_route_class": route_class,
                "expected_model_needed": model_needed,
            },
        ),
        _event(
            run_id=run_id,
            request=selected_request,
            stage_id="deterministic_check",
            stage_name="Deterministic route check",
            route_class=route_class,
            status="completed" if deterministic_route_used else "skipped",
            latency_ms=5,
            stage_offset_ms=7,
            deterministic_route_used=deterministic_route_used,
            structured_lookup_used=structured_lookup_used,
            counters_snapshot={
                "deterministic_routes": counters["deterministic_routes"],
                "policy_routes": counters["policy_routes"],
                "structured_lookup_routes": counters["structured_lookup_routes"],
            },
        ),
    ]

    if structured_lookup_used:
        events.append(
            _event(
                run_id=run_id,
                request=selected_request,
                stage_id="structured_lookup",
                stage_name="Structured lookup",
                route_class="structured_lookup",
                status="completed",
                latency_ms=6,
                stage_offset_ms=12,
                deterministic_route_used=True,
                structured_lookup_used=True,
                counters_snapshot={"structured_lookup_routes": 1},
            )
        )

    events.append(
        _event(
            run_id=run_id,
            request=selected_request,
            stage_id="validation",
            stage_name="Validation",
            route_class="validation",
            status="completed" if validation_result in {"pass", "fail"} else "skipped",
            latency_ms=4,
            stage_offset_ms=18,
            deterministic_route_used=deterministic_route_used,
            structured_lookup_used=structured_lookup_used,
            validation_result=validation_result,
            counters_snapshot={
                "validation_pass_count": counters["validation_pass_count"],
                "validation_fail_count": counters["validation_fail_count"],
            },
        )
    )

    if model_needed:
        events.append(
            _event(
                run_id=run_id,
                request=selected_request,
                stage_id="model_needed_boundary",
                stage_name="Model needed boundary",
                route_class="local_model",
                status="execution_not_connected",
                latency_ms=0,
                stage_offset_ms=22,
                validation_result=validation_result,
                counters_snapshot={
                    "model_escalations": counters["model_escalations"],
                    "fallback_count": counters["fallback_count"],
                    "kora_model_calls": 0,
                },
            )
        )
    else:
        events.append(
            _event(
                run_id=run_id,
                request=selected_request,
                stage_id="model_fallback_skipped",
                stage_name="Model fallback skipped",
                route_class="local_model",
                status="skipped",
                latency_ms=0,
                stage_offset_ms=22,
                deterministic_route_used=deterministic_route_used,
                structured_lookup_used=structured_lookup_used,
                validation_result=validation_result,
                counters_snapshot={
                    "kora_model_calls": 0,
                    "avoided_model_calls": counters["avoided_model_calls"],
                },
            )
        )

    events.append(
        _event(
            run_id=run_id,
            request=selected_request,
            stage_id="final_counters",
            stage_name="Final counters",
            route_class="summary",
            status="completed",
            latency_ms=0,
            stage_offset_ms=22,
            deterministic_route_used=deterministic_route_used,
            structured_lookup_used=structured_lookup_used,
            validation_result=validation_result,
            counters_snapshot=counters,
        )
    )

    return {
        "run_id": run_id,
        "request_id": selected_request["request_id"],
        "request": selected_request,
        "events": events,
        "counters_snapshot": counters,
        "status": "completed",
        "local_harness_event_schema_fields": list(EXECUTION_EVENT_SCHEMA_FIELDS),
        "claim_boundary": LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY,
        "request_claim_boundary": LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "download_connected": False,
    }


def validate_local_harness_event(event: dict[str, Any]) -> bool:
    """Return whether a local harness event follows the Execution Viewer schema."""

    if not all(field in event for field in EXECUTION_EVENT_SCHEMA_FIELDS):
        return False
    if event.get("provider_calls_enabled") is not False:
        return False
    if event.get("cloud_sync_enabled") is not False:
        return False
    if event.get("model_called") is not False:
        return False
    return True

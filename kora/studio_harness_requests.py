"""Local deterministic request set for the KORA Studio harness."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

LOCAL_HARNESS_REQUESTS_FIXTURE_PATH = "docs/kora-studio/fixtures/local-harness-requests.sample.json"
LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY = (
    "Local harness requests are synthetic deterministic samples. They do not execute models, call providers, "
    "download models, scan private data, or prove production behavior."
)
LOCAL_HARNESS_REQUEST_SCHEMA_FIELDS = [
    "request_id",
    "input_text",
    "task_family",
    "expected_route_class",
    "expected_validation_result",
    "expected_model_needed",
    "claim_boundary",
]

LOCAL_HARNESS_REQUESTS: list[dict[str, Any]] = [
    {
        "request_id": "local-harness-json-required-fields-001",
        "input_text": 'Format {"ticket_id":"T-100","priority":"high","channel":"email"} and validate required fields.',
        "task_family": "json_required_fields",
        "expected_route_class": "deterministic_code",
        "expected_validation_result": "pass",
        "expected_model_needed": False,
        "claim_boundary": LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
        "expected_checks": ["valid_json", "required_fields_present"],
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
    },
    {
        "request_id": "local-harness-policy-rule-001",
        "input_text": "Classify whether a refund request within 14 days routes to the standard refund policy.",
        "task_family": "policy_rule_classification",
        "expected_route_class": "policy",
        "expected_validation_result": "pass",
        "expected_model_needed": False,
        "claim_boundary": LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
        "expected_checks": ["known_policy_window", "route_policy_refund_standard"],
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
    },
    {
        "request_id": "local-harness-known-faq-001",
        "input_text": "What is the support response for account access help?",
        "task_family": "known_faq_lookup",
        "expected_route_class": "structured_lookup",
        "expected_validation_result": "pass",
        "expected_model_needed": False,
        "claim_boundary": LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
        "expected_checks": ["faq_key_found", "answer_template_present"],
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
    },
    {
        "request_id": "local-harness-structured-normalize-001",
        "input_text": "Normalize customer record: name=ALBERT KIM; email=A.KIM@EXAMPLE.COM; tier=Pro.",
        "task_family": "structured_record_normalization",
        "expected_route_class": "deterministic_code",
        "expected_validation_result": "pass",
        "expected_model_needed": False,
        "claim_boundary": LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
        "expected_checks": ["lowercase_email", "titlecase_name", "tier_preserved"],
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
    },
    {
        "request_id": "local-harness-ambiguous-model-needed-001",
        "input_text": "Write a nuanced customer apology for an unusual situation with incomplete context.",
        "task_family": "ambiguous_generation_boundary",
        "expected_route_class": "model_needed_boundary",
        "expected_validation_result": "not_applicable",
        "expected_model_needed": True,
        "claim_boundary": LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
        "expected_checks": ["ambiguous_context", "model_needed_boundary_only"],
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
    },
]


def get_local_harness_requests() -> list[dict[str, Any]]:
    """Return synthetic local deterministic harness requests."""

    return deepcopy(LOCAL_HARNESS_REQUESTS)


def validate_local_harness_request(request: dict[str, Any]) -> bool:
    """Return whether a local harness request includes required claim-safe fields."""

    if not all(field in request for field in LOCAL_HARNESS_REQUEST_SCHEMA_FIELDS):
        return False
    if not isinstance(request["expected_model_needed"], bool):
        return False
    if request.get("provider_calls_enabled") is not False:
        return False
    if request.get("cloud_sync_enabled") is not False:
        return False
    if request.get("model_execution_connected") is not False:
        return False
    if request.get("claim_boundary") != LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY:
        return False
    return True


def get_local_harness_request_by_id(request_id: str) -> dict[str, Any] | None:
    """Return a local harness request by id, if present."""

    for request in LOCAL_HARNESS_REQUESTS:
        if request["request_id"] == request_id:
            return deepcopy(request)
    return None


def get_local_harness_request_summary() -> dict[str, Any]:
    """Return request-set metadata for /status and docs without running the harness."""

    requests = get_local_harness_requests()
    return {
        "local_harness_request_status": "static_local_deterministic_request_set",
        "local_harness_request_count": len(requests),
        "local_harness_request_schema_fields": list(LOCAL_HARNESS_REQUEST_SCHEMA_FIELDS),
        "local_harness_request_families": sorted({request["task_family"] for request in requests}),
        "local_harness_model_needed_request_count": sum(1 for request in requests if request["expected_model_needed"]),
        "local_harness_requests_fixture_path": LOCAL_HARNESS_REQUESTS_FIXTURE_PATH,
        "local_harness_request_claim_boundary": LOCAL_HARNESS_REQUEST_CLAIM_BOUNDARY,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "download_connected": False,
    }

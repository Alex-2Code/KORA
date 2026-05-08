import json
import re
from pathlib import Path


WORKLOAD_PATH = Path("experiments/workloads/customer_support_triage_synthetic_v1.json")


def _load_workload() -> dict:
    return json.loads(WORKLOAD_PATH.read_text(encoding="utf-8"))


def test_customer_support_triage_workload_is_valid_json() -> None:
    workload = _load_workload()

    assert workload["workload_id"] == "customer_support_triage_synthetic_v1"
    assert workload["version"] == 1
    assert workload["privacy_class"] == "synthetic"
    assert isinstance(workload["requests"], list)


def test_customer_support_triage_workload_route_counts() -> None:
    requests = _load_workload()["requests"]

    deterministic_count = sum(
        request["expected_route"] == "deterministic" for request in requests
    )
    model_required_count = sum(
        request["expected_route"] == "model_required" for request in requests
    )

    assert len(requests) == 12
    assert deterministic_count == 8
    assert model_required_count == 4


def test_customer_support_triage_workload_required_fields() -> None:
    required_fields = {
        "request_id",
        "input",
        "route_class",
        "expected_route",
        "deterministic_handler",
        "validation_rule",
        "expected_response_type",
        "notes",
    }

    for request in _load_workload()["requests"]:
        assert set(request) == required_fields
        assert request["request_id"].startswith("cst-")
        assert request["route_class"] in {
            "deterministic_faq",
            "deterministic_policy",
            "structured_lookup",
            "model_required",
        }
        assert request["expected_route"] in {"deterministic", "model_required"}


def test_customer_support_triage_workload_has_no_obvious_private_data() -> None:
    text = WORKLOAD_PATH.read_text(encoding="utf-8")
    email_pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    phone_pattern = re.compile(r"(?:\+?\d[\d .-]{8,}\d)")

    assert not email_pattern.search(text)
    assert not phone_pattern.search(text)
    assert "ORDER-EXAMPLE-" in text
    assert "INVOICE-EXAMPLE-" in text

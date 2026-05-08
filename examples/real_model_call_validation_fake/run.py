"""Local no-network model-call validation example.

This example exercises the provider-neutral model-call adapter boundary with
synthetic data only. It is intended to validate local model-call counters before
real local or remote provider adapters are added.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Any, Literal

from kora.model_call import (
    DeterministicFakeModelCallAdapter,
    ModelCallRequest,
    ModelCallResponse,
    ModelCallSummary,
)

Route = Literal["deterministic", "model_required"]

CLAIM_BOUNDARY = (
    "This local/no-network validation example tests the measured model-call "
    "counter path. It is not real provider validation, real API-cost validation, "
    "production validation, production cost reduction proof, broad workload "
    "superiority proof, or energy reduction evidence."
)


@dataclass(frozen=True)
class SyntheticRequest:
    request_id: str
    input: str
    expected_route: Route
    expected_output: str | None
    privacy_class: str = "synthetic"


WORKLOAD: tuple[SyntheticRequest, ...] = (
    SyntheticRequest(
        request_id="req-001",
        input="Return the current order status label for delivered.",
        expected_route="deterministic",
        expected_output="status:delivered",
    ),
    SyntheticRequest(
        request_id="req-002",
        input="Normalize the refund-policy category.",
        expected_route="deterministic",
        expected_output="category:refund_policy",
    ),
    SyntheticRequest(
        request_id="req-003",
        input="Route a billing receipt request.",
        expected_route="deterministic",
        expected_output="route:billing_receipt",
    ),
    SyntheticRequest(
        request_id="req-004",
        input="Classify a password reset request.",
        expected_route="deterministic",
        expected_output="route:account_recovery",
    ),
    SyntheticRequest(
        request_id="req-005",
        input="Identify a shipping-address update.",
        expected_route="deterministic",
        expected_output="route:shipping_update",
    ),
    SyntheticRequest(
        request_id="req-006",
        input="Return a canned support-hours answer.",
        expected_route="deterministic",
        expected_output="answer:support_hours",
    ),
    SyntheticRequest(
        request_id="req-007",
        input="Draft a nuanced apology for a delayed enterprise shipment.",
        expected_route="model_required",
        expected_output=None,
    ),
    SyntheticRequest(
        request_id="req-008",
        input="Summarize an ambiguous customer escalation note.",
        expected_route="model_required",
        expected_output=None,
    ),
    SyntheticRequest(
        request_id="req-009",
        input="Generate a context-aware response for a billing dispute.",
        expected_route="model_required",
        expected_output=None,
    ),
    SyntheticRequest(
        request_id="req-010",
        input="Explain an edge-case refund decision in plain language.",
        expected_route="model_required",
        expected_output=None,
    ),
)


def _model_request(item: SyntheticRequest) -> ModelCallRequest:
    return ModelCallRequest(
        request_id=item.request_id,
        prompt=item.input,
        privacy_class=item.privacy_class,
        metadata={"expected_route": item.expected_route},
    )


def _run_direct_baseline(
    workload: tuple[SyntheticRequest, ...],
    adapter: DeterministicFakeModelCallAdapter,
) -> list[ModelCallResponse]:
    return [adapter.call(_model_request(item)) for item in workload]


def _run_deterministic_handler(item: SyntheticRequest) -> str:
    if item.expected_output is None:
        raise ValueError(f"deterministic request {item.request_id} has no expected output")
    return item.expected_output


def _run_kora_controlled_path(
    workload: tuple[SyntheticRequest, ...],
    adapter: DeterministicFakeModelCallAdapter,
) -> tuple[list[ModelCallResponse], int, int, int, int, int]:
    model_responses: list[ModelCallResponse] = []
    deterministic_routes = 0
    model_escalations = 0
    validation_pass_count = 0
    validation_fail_count = 0
    error_count = 0

    for item in workload:
        try:
            if item.expected_route == "deterministic":
                deterministic_routes += 1
                output = _run_deterministic_handler(item)
                if output == item.expected_output:
                    validation_pass_count += 1
                else:
                    validation_fail_count += 1
                continue

            model_escalations += 1
            response = adapter.call(_model_request(item))
            model_responses.append(response)
            if response.output:
                validation_pass_count += 1
            else:
                validation_fail_count += 1
        except Exception:
            error_count += 1

    return (
        model_responses,
        deterministic_routes,
        model_escalations,
        validation_pass_count,
        validation_fail_count,
        error_count,
    )


def build_fake_model_call_validation_summary(
    *,
    offline: bool = True,
    workload: tuple[SyntheticRequest, ...] = WORKLOAD,
) -> dict[str, Any]:
    if not offline:
        raise ValueError("real_model_call_validation_fake supports --offline only")

    baseline_adapter = DeterministicFakeModelCallAdapter()
    kora_adapter = DeterministicFakeModelCallAdapter()

    baseline_responses = _run_direct_baseline(workload, baseline_adapter)
    (
        kora_responses,
        deterministic_routes,
        model_escalations,
        validation_pass_count,
        validation_fail_count,
        error_count,
    ) = _run_kora_controlled_path(workload, kora_adapter)

    baseline_summary = ModelCallSummary.from_responses(baseline_responses)
    kora_summary = ModelCallSummary.from_responses(kora_responses, error_count=error_count)
    total_requests = len(workload)
    avoided_model_calls = baseline_summary.model_calls - kora_summary.model_calls
    avoided_model_call_rate = (
        avoided_model_calls / baseline_summary.model_calls
        if baseline_summary.model_calls
        else 0.0
    )

    return {
        "ok": error_count == 0 and validation_fail_count == 0,
        "mode": "local_no_network_model_call_validation",
        "offline": True,
        "adapter": "deterministic local validation adapter",
        "provider": "local_validation",
        "model": "deterministic-local",
        "total_requests": total_requests,
        "baseline_model_calls": baseline_summary.model_calls,
        "kora_model_calls": kora_summary.model_calls,
        "avoided_model_calls": avoided_model_calls,
        "avoided_model_call_rate": avoided_model_call_rate,
        "deterministic_routes": deterministic_routes,
        "model_escalations": model_escalations,
        "validation_pass_count": validation_pass_count,
        "validation_fail_count": validation_fail_count,
        "error_count": error_count,
        "fallback_count": 0,
        "input_tokens_total": kora_summary.input_tokens_total,
        "output_tokens_total": kora_summary.output_tokens_total,
        "baseline_input_tokens_total": baseline_summary.input_tokens_total,
        "baseline_output_tokens_total": baseline_summary.output_tokens_total,
        "latency_total_ms": kora_summary.latency_total_ms,
        "privacy_class": "synthetic",
        "raw_prompts_emitted": False,
        "raw_responses_emitted": False,
        "claim_boundary": CLAIM_BOUNDARY,
        "notes": [
            "Synthetic workload only.",
            "Direct baseline records local validation model-call events for every request.",
            "KORA-controlled path handles deterministic routes without local validation model-call events.",
            "Model-required routes use the deterministic local validation adapter through the provider-neutral boundary.",
            "No external APIs, network access, provider credentials, raw prompts, or raw provider responses are used.",
        ],
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the local no-network model-call validation example."
    )
    parser.add_argument("--offline", action="store_true", help="required; run without network calls")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.offline:
        raise SystemExit("real_model_call_validation_fake requires --offline.")

    summary = build_fake_model_call_validation_summary(offline=True)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

"""Provider-neutral model-call measurement primitives."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Protocol


def _estimate_tokens(text: str) -> int:
    """Return a stable, conservative token estimate for local validation."""
    return len(text.split()) if text.strip() else 0


@dataclass(frozen=True)
class ModelCallRequest:
    """Provider-neutral model-call request for validation harnesses."""

    request_id: str
    prompt: str
    metadata: dict[str, Any] = field(default_factory=dict)
    privacy_class: str = "synthetic"


@dataclass(frozen=True)
class ModelCallResponse:
    """Provider-neutral model-call response with measurement counters."""

    request_id: str
    output: str
    model_calls: int
    latency_ms: float | None
    input_tokens: int | None
    output_tokens: int | None
    provider: str | None
    model: str | None
    metadata: dict[str, Any] = field(default_factory=dict)


class ModelCallAdapter(Protocol):
    """Protocol implemented by model-call adapters used in validation."""

    def call(self, request: ModelCallRequest) -> ModelCallResponse:
        """Execute one model-call request and return measured counters."""


class DeterministicFakeModelCallAdapter:
    """Local no-network adapter for deterministic validation tests."""

    provider = "fake"
    model = "deterministic-fake"

    def call(self, request: ModelCallRequest) -> ModelCallResponse:
        start = time.perf_counter()
        output = f"fake:{request.request_id}:{request.prompt.strip()[:80]}"
        latency_ms = (time.perf_counter() - start) * 1000.0
        return ModelCallResponse(
            request_id=request.request_id,
            output=output,
            model_calls=1,
            latency_ms=latency_ms,
            input_tokens=_estimate_tokens(request.prompt),
            output_tokens=_estimate_tokens(output),
            provider=self.provider,
            model=self.model,
            metadata={
                "privacy_class": request.privacy_class,
                "adapter": self.provider,
                "network": "none",
                "deterministic": True,
            },
        )


class BlockedModelCallAdapter:
    """Adapter that fails closed when real provider use is not configured."""

    def call(self, request: ModelCallRequest) -> ModelCallResponse:
        del request
        raise RuntimeError(
            "Real model-call adapter is not configured. Use an explicit local "
            "or remote adapter in a validation harness."
        )


@dataclass(frozen=True)
class ModelCallSummary:
    """Aggregate model-call counters for validation reports."""

    total_requests: int
    model_calls: int
    input_tokens_total: int | None
    output_tokens_total: int | None
    latency_total_ms: float | None
    error_count: int

    @classmethod
    def from_responses(
        cls,
        responses: list[ModelCallResponse],
        *,
        error_count: int = 0,
    ) -> "ModelCallSummary":
        input_tokens = [response.input_tokens for response in responses]
        output_tokens = [response.output_tokens for response in responses]
        latencies = [response.latency_ms for response in responses]
        return cls(
            total_requests=len(responses) + error_count,
            model_calls=sum(response.model_calls for response in responses),
            input_tokens_total=(
                sum(token for token in input_tokens if token is not None)
                if all(token is not None for token in input_tokens)
                else None
            ),
            output_tokens_total=(
                sum(token for token in output_tokens if token is not None)
                if all(token is not None for token in output_tokens)
                else None
            ),
            latency_total_ms=(
                sum(latency for latency in latencies if latency is not None)
                if all(latency is not None for latency in latencies)
                else None
            ),
            error_count=error_count,
        )

"""Dry-run provider fixture validation.

This module validates documentation-safe provider fixture metadata for future
real-provider validation planning. It does not construct provider requests,
load credentials, call network APIs, or execute local runtimes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

SAFE_PROVIDER_FIXTURE_MODES = ("dry_run", "fixture")

_COUNTER_FIELDS = (
    "baseline_candidate_events",
    "kora_routed_events",
    "avoided_model_call_events",
    "provider_attempted_events",
    "provider_blocked_events",
)


class ProviderFixtureValidationError(ValueError):
    """Raised when a provider fixture violates the dry-run contract."""


@dataclass(frozen=True)
class ProviderFixtureDryRunContract:
    """Validated provider fixture metadata for dry-run-only checks."""

    fixture_version: str
    provider_label: str
    model_label: str
    mode: str
    request_id: str
    baseline_candidate_events: int
    kora_routed_events: int
    avoided_model_call_events: int
    provider_attempted_events: int
    provider_blocked_events: int
    no_network: bool
    no_provider_call: bool
    contains_real_provider_response: bool
    contains_customer_data: bool
    contains_secret_material: bool
    notes: list[str] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, fixture: Mapping[str, Any]) -> "ProviderFixtureDryRunContract":
        """Validate fixture metadata and return a dry-run contract object."""

        return validate_provider_fixture(fixture)

    def report_fields(self) -> dict[str, Any]:
        """Return aggregate report fields safe for reviewer-facing summaries."""

        return {
            "fixture_contract_status": "passed",
            "fixture_version": self.fixture_version,
            "provider_label": self.provider_label,
            "model_label": self.model_label,
            "mode": self.mode,
            "request_id": self.request_id,
            "baseline_candidate_events": self.baseline_candidate_events,
            "kora_routed_events": self.kora_routed_events,
            "avoided_model_call_events": self.avoided_model_call_events,
            "provider_attempted_events": self.provider_attempted_events,
            "provider_blocked_events": self.provider_blocked_events,
            "no_network": self.no_network,
            "no_provider_call": self.no_provider_call,
            "contains_real_provider_response": self.contains_real_provider_response,
            "contains_customer_data": self.contains_customer_data,
            "contains_secret_material": self.contains_secret_material,
            "notes": list(self.notes),
        }


def validate_provider_fixture(
    fixture: Mapping[str, Any],
) -> ProviderFixtureDryRunContract:
    """Validate a provider fixture without attempting provider execution."""

    if not isinstance(fixture, Mapping):
        raise ProviderFixtureValidationError("Provider fixture must be a mapping.")

    mode = _required_string(fixture, "mode")
    if mode not in SAFE_PROVIDER_FIXTURE_MODES:
        supported = ", ".join(SAFE_PROVIDER_FIXTURE_MODES)
        raise ProviderFixtureValidationError(
            f"Provider fixture mode {mode!r} is unsupported. Supported: {supported}."
        )

    no_network = _required_bool(fixture, "no_network")
    if no_network is not True:
        raise ProviderFixtureValidationError("Provider fixture must set no_network=true.")

    no_provider_call = _required_bool(fixture, "no_provider_call")
    if no_provider_call is not True:
        raise ProviderFixtureValidationError(
            "Provider fixture must set no_provider_call=true."
        )

    contains_real_provider_response = _required_bool(
        fixture, "contains_real_provider_response"
    )
    if contains_real_provider_response is not False:
        raise ProviderFixtureValidationError(
            "Provider fixture must not contain real provider responses."
        )

    contains_customer_data = _required_bool(fixture, "contains_customer_data")
    if contains_customer_data is not False:
        raise ProviderFixtureValidationError(
            "Provider fixture must not contain customer data."
        )

    contains_secret_material = _required_bool(fixture, "contains_secret_material")
    if contains_secret_material is not False:
        raise ProviderFixtureValidationError(
            "Provider fixture must not contain secret material."
        )

    counters = {field_name: _required_counter(fixture, field_name) for field_name in _COUNTER_FIELDS}
    if counters["provider_attempted_events"] != 0:
        raise ProviderFixtureValidationError(
            "Dry-run provider fixtures must keep provider_attempted_events at 0."
        )

    notes = _optional_notes(fixture.get("notes", []))

    return ProviderFixtureDryRunContract(
        fixture_version=_required_string(fixture, "fixture_version"),
        provider_label=_required_string(fixture, "provider_label"),
        model_label=_required_string(fixture, "model_label"),
        mode=mode,
        request_id=_required_string(fixture, "request_id"),
        baseline_candidate_events=counters["baseline_candidate_events"],
        kora_routed_events=counters["kora_routed_events"],
        avoided_model_call_events=counters["avoided_model_call_events"],
        provider_attempted_events=counters["provider_attempted_events"],
        provider_blocked_events=counters["provider_blocked_events"],
        no_network=no_network,
        no_provider_call=no_provider_call,
        contains_real_provider_response=contains_real_provider_response,
        contains_customer_data=contains_customer_data,
        contains_secret_material=contains_secret_material,
        notes=notes,
    )


def _required_string(fixture: Mapping[str, Any], field_name: str) -> str:
    value = fixture.get(field_name)
    if not isinstance(value, str) or not value.strip():
        raise ProviderFixtureValidationError(
            f"Provider fixture field {field_name!r} must be a non-empty string."
        )
    return value


def _required_bool(fixture: Mapping[str, Any], field_name: str) -> bool:
    value = fixture.get(field_name)
    if not isinstance(value, bool):
        raise ProviderFixtureValidationError(
            f"Provider fixture field {field_name!r} must be a boolean."
        )
    return value


def _required_counter(fixture: Mapping[str, Any], field_name: str) -> int:
    value = fixture.get(field_name)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ProviderFixtureValidationError(
            f"Provider fixture counter {field_name!r} must be an integer."
        )
    if value < 0:
        raise ProviderFixtureValidationError(
            f"Provider fixture counter {field_name!r} must be non-negative."
        )
    return value


def _optional_notes(value: Any) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(note, str) for note in value):
        raise ProviderFixtureValidationError(
            "Provider fixture field 'notes' must be a list of strings."
        )
    return list(value)

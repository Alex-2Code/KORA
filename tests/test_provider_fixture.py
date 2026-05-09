import pytest

from kora.provider_fixture import (
    ProviderFixtureDryRunContract,
    ProviderFixtureValidationError,
    validate_provider_fixture,
)


def valid_fixture() -> dict[str, object]:
    return {
        "fixture_version": "0.1",
        "provider_label": "example-provider",
        "model_label": "example-model",
        "mode": "dry_run",
        "request_id": "dry_run_request_001",
        "baseline_candidate_events": 2,
        "kora_routed_events": 1,
        "avoided_model_call_events": 1,
        "provider_attempted_events": 0,
        "provider_blocked_events": 2,
        "no_network": True,
        "no_provider_call": True,
        "contains_real_provider_response": False,
        "contains_customer_data": False,
        "contains_secret_material": False,
        "notes": ["Synthetic metadata only."],
    }


def test_valid_provider_fixture_passes() -> None:
    contract = validate_provider_fixture(valid_fixture())

    assert isinstance(contract, ProviderFixtureDryRunContract)
    assert contract.mode == "dry_run"
    assert contract.provider_label == "example-provider"
    assert contract.model_label == "example-model"
    assert contract.provider_attempted_events == 0
    assert contract.provider_blocked_events == 2
    assert contract.no_network is True
    assert contract.no_provider_call is True


def test_fixture_mode_alias_passes() -> None:
    fixture = valid_fixture()
    fixture["mode"] = "fixture"

    contract = ProviderFixtureDryRunContract.from_mapping(fixture)

    assert contract.mode == "fixture"


@pytest.mark.parametrize(
    ("field_name", "value", "message"),
    [
        ("no_network", False, "no_network=true"),
        ("no_provider_call", False, "no_provider_call=true"),
        (
            "contains_real_provider_response",
            True,
            "must not contain real provider responses",
        ),
        ("contains_customer_data", True, "must not contain customer data"),
        ("contains_secret_material", True, "must not contain secret material"),
    ],
)
def test_provider_fixture_safety_flags_fail_closed(
    field_name: str,
    value: object,
    message: str,
) -> None:
    fixture = valid_fixture()
    fixture[field_name] = value

    with pytest.raises(ProviderFixtureValidationError, match=message):
        validate_provider_fixture(fixture)


def test_provider_attempted_events_must_remain_zero() -> None:
    fixture = valid_fixture()
    fixture["provider_attempted_events"] = 1

    with pytest.raises(ProviderFixtureValidationError, match="provider_attempted_events"):
        validate_provider_fixture(fixture)


@pytest.mark.parametrize(
    "field_name",
    [
        "baseline_candidate_events",
        "kora_routed_events",
        "avoided_model_call_events",
        "provider_attempted_events",
        "provider_blocked_events",
    ],
)
def test_provider_fixture_negative_counters_fail(field_name: str) -> None:
    fixture = valid_fixture()
    fixture[field_name] = -1

    with pytest.raises(ProviderFixtureValidationError, match="non-negative"):
        validate_provider_fixture(fixture)


def test_provider_fixture_boolean_counter_fails() -> None:
    fixture = valid_fixture()
    fixture["avoided_model_call_events"] = True

    with pytest.raises(ProviderFixtureValidationError, match="must be an integer"):
        validate_provider_fixture(fixture)


def test_provider_fixture_unknown_mode_fails() -> None:
    fixture = valid_fixture()
    fixture["mode"] = "remote_provider"

    with pytest.raises(ProviderFixtureValidationError, match="unsupported"):
        validate_provider_fixture(fixture)


def test_provider_fixture_missing_required_string_fails() -> None:
    fixture = valid_fixture()
    fixture["provider_label"] = ""

    with pytest.raises(ProviderFixtureValidationError, match="provider_label"):
        validate_provider_fixture(fixture)


def test_provider_fixture_notes_must_be_strings() -> None:
    fixture = valid_fixture()
    fixture["notes"] = ["safe", 123]

    with pytest.raises(ProviderFixtureValidationError, match="notes"):
        validate_provider_fixture(fixture)


def test_provider_fixture_report_fields_are_aggregate_and_safe() -> None:
    contract = validate_provider_fixture(valid_fixture())

    report_fields = contract.report_fields()

    assert report_fields["fixture_contract_status"] == "passed"
    assert report_fields["provider_label"] == "example-provider"
    assert report_fields["provider_attempted_events"] == 0
    assert report_fields["contains_real_provider_response"] is False
    assert "prompt" not in report_fields
    assert "response" not in report_fields
    assert "api_key" not in report_fields

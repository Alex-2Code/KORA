import importlib.util
import os
import subprocess
import sys
from pathlib import Path


def _load_example_module():
    script_path = Path("examples/customer_support_triage_fake_validation/run.py")
    spec = importlib.util.spec_from_file_location(
        "customer_support_triage_fake_validation_run", script_path
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load customer_support_triage_fake_validation module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[str(spec.name)] = module
    spec.loader.exec_module(module)
    return module


def test_customer_support_triage_fake_validation_loads_workload() -> None:
    module = _load_example_module()

    workload = module.load_workload()

    assert workload["workload_id"] == "customer_support_triage_synthetic_v1"
    assert workload["privacy_class"] == "synthetic"
    assert len(workload["requests"]) == 12


def test_customer_support_triage_fake_validation_summary_counts() -> None:
    module = _load_example_module()

    summary = module.build_customer_support_triage_fake_validation_summary(offline=True)

    assert summary["ok"] is True
    assert summary["mode"] == "customer_support_triage_local_validation"
    assert summary["workload_id"] == "customer_support_triage_synthetic_v1"
    assert summary["privacy_class"] == "synthetic"
    assert summary["provider"] == "local_validation"
    assert summary["model"] == "deterministic-local"
    assert summary["total_requests"] == 12
    assert summary["baseline_model_calls"] == 12
    assert summary["kora_model_calls"] == 4
    assert summary["avoided_model_calls"] == 8
    assert round(summary["avoided_model_call_rate"], 4) == 0.6667
    assert summary["deterministic_routes"] == 8
    assert summary["model_escalations"] == 4
    assert summary["validation_pass_count"] == 12
    assert summary["validation_fail_count"] == 0
    assert summary["error_count"] == 0
    assert summary["fallback_count"] == 0


def test_customer_support_triage_fake_validation_requires_no_provider_environment(
    monkeypatch,
) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    module = _load_example_module()

    summary = module.build_customer_support_triage_fake_validation_summary(offline=True)

    assert summary["ok"] is True
    assert "OPENAI_API_KEY" not in os.environ
    assert "ANTHROPIC_API_KEY" not in os.environ


def test_customer_support_triage_fake_validation_does_not_emit_raw_inputs_or_outputs() -> None:
    module = _load_example_module()

    summary = module.build_customer_support_triage_fake_validation_summary(offline=True)

    assert summary["raw_prompts_emitted"] is False
    assert summary["raw_responses_emitted"] is False
    assert "raw provider responses" in summary["notes"][-1]


def test_customer_support_triage_fake_validation_rejects_non_offline_mode() -> None:
    module = _load_example_module()

    try:
        module.build_customer_support_triage_fake_validation_summary(offline=False)
    except ValueError as exc:
        assert "--offline only" in str(exc)
    else:
        raise AssertionError("expected offline-only guard")


def test_customer_support_triage_fake_validation_cli_runs() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "kora",
            "run",
            "customer_support_triage_fake_validation",
            "--",
            "--offline",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0
    assert '"mode": "customer_support_triage_local_validation"' in completed.stdout
    assert '"baseline_model_calls": 12' in completed.stdout
    assert '"kora_model_calls": 4' in completed.stdout

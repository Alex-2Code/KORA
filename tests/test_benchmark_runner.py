import json
from pathlib import Path

import pytest

from experiments.run_benchmark import (
    DeterministicOutputMismatch,
    load_workload,
    run_direct_baseline,
    run_dry_run,
    run_kora_controlled,
    validate_expected_outputs,
)


WORKLOAD_PATH = Path("experiments/workloads/deterministic_heavy_v0.json")
V1_100_WORKLOAD_PATH = Path("experiments/workloads/deterministic_heavy_v1_100.json")


def test_workload_json_can_be_loaded() -> None:
    workload = load_workload(WORKLOAD_PATH)

    assert workload["name"] == "deterministic_heavy_v0"
    assert isinstance(workload["tasks"], list)
    assert len(workload["tasks"]) == 20


def test_dry_run_result_counts_workload(tmp_path: Path) -> None:
    output_path = tmp_path / "deterministic_heavy_v0.dry_run.json"

    result = run_dry_run(WORKLOAD_PATH, output_path)

    assert result["benchmark_name"] == "deterministic_heavy_v0"
    assert result["mode"] == "dry-run"
    assert result["total_tasks"] == 20
    assert result["requires_model_true"] == 4
    assert result["requires_model_false"] == 16
    assert set(result["category_counts"]) == {
        "arithmetic",
        "cache_lookup",
        "json_validation",
        "routing_decision",
        "schema_check",
        "string_normalization",
    }


def test_dry_run_writes_output_json(tmp_path: Path) -> None:
    output_path = tmp_path / "result.json"

    run_dry_run(WORKLOAD_PATH, output_path)

    assert output_path.exists()
    saved = json.loads(output_path.read_text(encoding="utf-8"))
    assert saved["status"] == "ok"
    assert saved["total_tasks"] == 20


def test_direct_baseline_result_counts_simulated_model_invocations(tmp_path: Path) -> None:
    output_path = tmp_path / "deterministic_heavy_v0.direct_baseline.json"

    result = run_direct_baseline(WORKLOAD_PATH, output_path)

    assert result["benchmark_name"] == "deterministic_heavy_v0"
    assert result["mode"] == "direct-baseline"
    assert result["total_tasks"] == 20
    assert result["simulated_model_invocations"] == 20
    assert result["deterministic_tasks_sent_to_model"] == 16
    assert result["fallback_candidate_tasks_sent_to_model"] == 4


def test_direct_baseline_writes_output_json(tmp_path: Path) -> None:
    output_path = tmp_path / "direct_baseline.json"

    run_direct_baseline(WORKLOAD_PATH, output_path)

    assert output_path.exists()
    saved = json.loads(output_path.read_text(encoding="utf-8"))
    assert saved["status"] == "ok"
    assert saved["mode"] == "direct-baseline"
    assert saved["simulated_model_invocations"] == 20


def test_kora_controlled_result_counts_avoided_model_invocations(tmp_path: Path) -> None:
    output_path = tmp_path / "deterministic_heavy_v0.kora_controlled.json"

    result = run_kora_controlled(WORKLOAD_PATH, output_path)

    assert result["benchmark_name"] == "deterministic_heavy_v0"
    assert result["mode"] == "kora-controlled"
    assert result["total_tasks"] == 20
    assert result["deterministic_resolutions"] == 16
    assert result["fallback_candidates"] == 4
    assert result["deterministic_output_checks"] == 16
    assert result["deterministic_output_mismatches"] == 0
    assert result["fallback_candidates_skipped_for_output_check"] == 4
    assert result["simulated_model_invocations"] == 4
    assert result["avoided_model_invocations_vs_direct_baseline"] == 16
    assert result["avoided_model_invocation_rate"] == 0.8


def test_kora_controlled_writes_output_json(tmp_path: Path) -> None:
    output_path = tmp_path / "kora_controlled.json"

    run_kora_controlled(WORKLOAD_PATH, output_path)

    assert output_path.exists()
    saved = json.loads(output_path.read_text(encoding="utf-8"))
    assert saved["status"] == "ok"
    assert saved["mode"] == "kora-controlled"
    assert saved["simulated_model_invocations"] == 4


def test_expected_output_validation_accepts_matching_deterministic_task() -> None:
    workload = {
        "tasks": [
            {
                "id": "arithmetic_pass",
                "category": "arithmetic",
                "input": {"left": 2, "right": 3, "operation": "multiply"},
                "expected_output": 6,
                "requires_model": False,
            },
            {
                "id": "fallback_skip",
                "category": "arithmetic",
                "input": {"left": 2, "right": 3, "operation": "multiply"},
                "expected_output": {"fallback_required": True},
                "requires_model": True,
            },
        ]
    }

    result = validate_expected_outputs(workload)

    assert result == {
        "deterministic_output_checks": 1,
        "deterministic_output_mismatches": 0,
        "fallback_candidates_skipped_for_output_check": 1,
    }


def test_expected_output_validation_rejects_mismatched_deterministic_task() -> None:
    workload = {
        "tasks": [
            {
                "id": "arithmetic_mismatch",
                "category": "arithmetic",
                "input": {"left": 2, "right": 3, "operation": "multiply"},
                "expected_output": 5,
                "requires_model": False,
            }
        ]
    }

    with pytest.raises(DeterministicOutputMismatch, match="arithmetic_mismatch"):
        validate_expected_outputs(workload)


def test_expected_output_validation_reports_unsupported_deterministic_category() -> None:
    workload = {
        "tasks": [
            {
                "id": "unsupported_category_case",
                "category": "unknown_deterministic_type",
                "input": {"value": 1},
                "expected_output": {"value": 1},
                "requires_model": False,
            }
        ]
    }

    with pytest.raises(ValueError, match="unsupported_category_case category: unknown_deterministic_type"):
        validate_expected_outputs(workload)


def test_expected_output_validation_reports_malformed_deterministic_input_type() -> None:
    workload = {
        "tasks": [
            {
                "id": "malformed_input_case",
                "category": "arithmetic",
                "input": "not-an-object",
                "expected_output": 3,
                "requires_model": False,
            }
        ]
    }

    with pytest.raises(ValueError, match="malformed_input_case category arithmetic must contain object input"):
        validate_expected_outputs(workload)


def test_expected_output_validation_skips_fallback_even_with_unsupported_category() -> None:
    workload = {
        "tasks": [
            {
                "id": "fallback_unsupported_skip",
                "category": "unknown_deterministic_type",
                "input": "not-an-object",
                "expected_output": {"fallback_required": True},
                "requires_model": True,
            }
        ]
    }

    result = validate_expected_outputs(workload)

    assert result == {
        "deterministic_output_checks": 0,
        "deterministic_output_mismatches": 0,
        "fallback_candidates_skipped_for_output_check": 1,
    }


def test_v1_100_benchmark_evidence_counters_remain_stable(tmp_path: Path) -> None:
    output_path = tmp_path / "deterministic_heavy_v1_100.kora_controlled.json"

    result = run_kora_controlled(V1_100_WORKLOAD_PATH, output_path)

    assert result["total_tasks"] == 100
    assert result["requires_model_false"] == 80
    assert result["requires_model_true"] == 20
    assert result["simulated_model_invocations"] == 20
    assert result["avoided_model_invocations_vs_direct_baseline"] == 80
    assert result["avoided_model_invocation_rate"] == 0.8
    assert result["deterministic_output_checks"] == 80
    assert result["deterministic_output_mismatches"] == 0
    assert result["fallback_candidates_skipped_for_output_check"] == 20

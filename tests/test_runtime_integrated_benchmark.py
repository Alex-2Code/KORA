import importlib.util
import json
from pathlib import Path


def _load_runtime_benchmark_module():
    script_path = Path("examples/runtime_integrated_benchmark/run.py")
    spec = importlib.util.spec_from_file_location("runtime_integrated_benchmark_run", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load runtime_integrated_benchmark module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_runtime_integrated_benchmark_counts_v1_100() -> None:
    module = _load_runtime_benchmark_module()

    result = module.build_runtime_integrated_summary(offline=True)

    assert result["ok"] is True
    assert result["total_tasks"] == 100
    assert result["deterministic_route_count"] == 80
    assert result["fallback_or_model_candidate_route_count"] == 20
    assert result["simulated_baseline_model_invocations"] == 100
    assert result["kora_controlled_model_invocations"] == 20
    assert result["avoided_simulated_model_invocations"] == 80
    assert result["avoided_simulated_model_invocation_rate"] == 0.8
    assert result["deterministic_outputs_checked"] == 80
    assert result["mismatch_count"] == 0
    assert result["runtime_path_execution_status"] == "ok"
    assert result["telemetry_event_count"] == 100


def test_runtime_integrated_benchmark_writes_json(tmp_path: Path) -> None:
    module = _load_runtime_benchmark_module()
    output_path = tmp_path / "runtime_integrated_benchmark.json"

    result = module.build_runtime_integrated_summary(offline=True, json_out=output_path)

    assert result["summary_output_path"] == str(output_path)
    assert output_path.exists()
    saved = json.loads(output_path.read_text(encoding="utf-8"))
    assert saved["mode"] == "runtime-integrated-benchmark"
    assert saved["kora_controlled_model_invocations"] == 20
    assert len(saved["events"]) == 100
    assert "production cost reduction proof" in saved["claim_boundary"]

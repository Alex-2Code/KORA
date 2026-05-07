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


def _load_runtime_report_module():
    script_path = Path("examples/runtime_integrated_benchmark/report.py")
    spec = importlib.util.spec_from_file_location("runtime_integrated_benchmark_report", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load runtime_integrated_benchmark report module")
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


def test_runtime_integrated_benchmark_renders_evidence_packet() -> None:
    module = _load_runtime_benchmark_module()
    result = module.build_runtime_integrated_summary(offline=True)

    packet = module.render_evidence_packet(result)

    assert "# KORA v0.3.0-alpha initial runtime-path benchmark evidence packet" in packet
    assert "| Total tasks | `100` |" in packet
    assert "| KORA-controlled model invocations | `20` |" in packet
    assert "| Avoided simulated model invocations | `80` |" in packet
    assert "| Avoided simulated model invocation rate | `80%` |" in packet
    assert "| `ADAPTER` | `20` |" in packet
    assert "| `DETERMINISTIC` | `80` |" in packet
    assert "No external API, network access, or API key is required." in packet
    assert "Generated JSON and Markdown outputs are reproducible local outputs." in packet
    assert "full runtime-integrated benchmark evidence" in packet
    assert (
        "python3 -m kora run runtime_integrated_benchmark -- "
        "--offline --json-out /tmp/kora_runtime_integrated_benchmark.json"
    ) in packet


def test_runtime_integrated_benchmark_report_from_json(tmp_path: Path) -> None:
    benchmark_module = _load_runtime_benchmark_module()
    report_module = _load_runtime_report_module()
    json_path = tmp_path / "runtime_integrated_benchmark.json"
    md_path = tmp_path / "runtime_integrated_benchmark_report.md"

    benchmark_module.build_runtime_integrated_summary(offline=True, json_out=json_path)
    packet = report_module.write_evidence_packet(
        json_path,
        md_path,
        runtime_json_command=(
            "python3 -m kora run runtime_integrated_benchmark -- "
            "--offline --json-out /tmp/kora_runtime_integrated_benchmark_task167.json"
        ),
        report_command=(
            "python3 examples/runtime_integrated_benchmark/report.py "
            "--input /tmp/kora_runtime_integrated_benchmark_task167.json "
            "--md-out /tmp/kora_runtime_integrated_benchmark_task167.md"
        ),
    )

    assert md_path.exists()
    saved = md_path.read_text(encoding="utf-8")
    assert saved == packet
    assert "KORA-controlled execution avoided 80 of 100 simulated model invocations" in saved
    assert "| Total tasks | `100` |" in saved
    assert "| Deterministic route count | `80` |" in saved
    assert "| Fallback/model-candidate route count | `20` |" in saved
    assert "| Simulated baseline model invocations | `100` |" in saved
    assert "| KORA-controlled model invocations | `20` |" in saved
    assert "| Avoided simulated model invocations | `80` |" in saved
    assert "| Avoided simulated model invocation rate | `80%` |" in saved
    assert "| Deterministic outputs checked | `80` |" in saved
    assert "| Mismatch count | `0` |" in saved
    assert "| Runtime path execution status | `ok` |" in saved
    assert "| Telemetry event count | `100` |" in saved
    assert "| Total LLM calls | `20` |" in saved
    assert "| Events OK | `100` |" in saved
    assert "This packet does not claim production cost reduction proof" in saved
    assert "This is not production benchmark evidence." in saved
    assert "This does not prove real API-cost reduction." in saved
    assert "This does not prove production cost reduction." in saved
    assert "This does not prove broad workload superiority." in saved
    assert "This does not prove energy reduction." in saved
    assert "This is not full runtime-integrated benchmark evidence." in saved

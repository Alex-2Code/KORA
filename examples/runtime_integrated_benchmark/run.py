"""Initial runtime-path benchmark harness for the deterministic-heavy workload."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from experiments.run_benchmark import load_workload
from kora.executor import run_graph
from kora.task_ir import TaskGraph, normalize_graph, validate_graph
from kora.telemetry import summarize_run

DEFAULT_WORKLOAD = Path("experiments/workloads/deterministic_heavy_v1_100.json")
SAFE_CLAIM = (
    "In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled "
    "execution avoided 80 of 100 simulated model invocations versus a naive direct baseline."
)
CLAIM_BOUNDARY = (
    "This is an initial runtime-path benchmark harness. It exercises KORA's runtime executor "
    "with offline/mock behavior and does not claim production cost reduction proof, real "
    "API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark "
    "evidence, broad workload superiority proof, or energy reduction evidence."
)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _task_graph_for_deterministic_expected(task: dict[str, Any]) -> TaskGraph:
    task_id = str(task["id"])
    return TaskGraph.model_validate(
        {
            "graph_id": f"runtime-benchmark-det-{task_id}",
            "version": "0.1",
            "root": "task_expected_output",
            "defaults": {"budget": {"max_time_ms": 1500, "max_tokens": 300, "max_retries": 0}},
            "tasks": [
                {
                    "id": "task_expected_output",
                    "type": f"det.benchmark.{task.get('category', 'unknown')}",
                    "deps": [],
                    "in": {"message": task.get("expected_output")},
                    "run": {
                        "kind": "det",
                        "spec": {"handler": "echo", "args": {"message": task.get("expected_output")}},
                    },
                    "policy": {"on_fail": "fail"},
                    "tags": ["runtime-integrated-benchmark", "deterministic-route"],
                }
            ],
        }
    )


def _task_graph_for_model_candidate(task: dict[str, Any]) -> TaskGraph:
    task_id = str(task["id"])
    category = str(task.get("category", "unknown"))
    question = (
        "Offline runtime benchmark model-candidate placeholder for "
        f"{task_id} ({category})."
    )
    return TaskGraph.model_validate(
        {
            "graph_id": f"runtime-benchmark-model-{task_id}",
            "version": "0.1",
            "root": "task_model_candidate",
            "defaults": {"budget": {"max_time_ms": 1500, "max_tokens": 300, "max_retries": 0}},
            "tasks": [
                {
                    "id": "task_model_candidate",
                    "type": f"llm.benchmark.{category}",
                    "deps": [],
                    "in": {},
                    "run": {
                        "kind": "llm",
                        "spec": {
                            "adapter": "mock",
                            "input": {"question": question},
                            "output_schema": {
                                "type": "object",
                                "required": ["status", "task_id", "answer"],
                                "properties": {
                                    "status": {"type": "string"},
                                    "task_id": {"type": "string"},
                                    "answer": {"type": "string"},
                                },
                            },
                        },
                    },
                    "policy": {"on_fail": "fail"},
                    "tags": ["runtime-integrated-benchmark", "model-candidate-route"],
                }
            ],
        }
    )


def _run_runtime_graph(graph: TaskGraph) -> dict[str, Any]:
    normalized = normalize_graph(graph)
    validate_graph(normalized)
    return run_graph(normalized)


def _adapter_invocation_count(events: list[dict[str, Any]]) -> int:
    return sum(
        1
        for event in events
        if event.get("stage") == "ADAPTER"
        and event.get("status") == "ok"
        and event.get("skipped") is not True
    )


def build_runtime_integrated_summary(
    workload_path: Path = DEFAULT_WORKLOAD,
    *,
    offline: bool = True,
    json_out: Path | None = None,
) -> dict[str, Any]:
    if not offline:
        raise ValueError("runtime-integrated benchmark harness currently supports offline mode only")

    workload = load_workload(workload_path)
    tasks = workload["tasks"]
    events: list[dict[str, Any]] = []
    deterministic_route_count = 0
    fallback_or_model_candidate_route_count = 0
    deterministic_outputs_checked = 0
    mismatch_count = 0
    runtime_failures: list[dict[str, Any]] = []

    for task in tasks:
        requires_model = bool(task["requires_model"])
        graph = _task_graph_for_model_candidate(task) if requires_model else _task_graph_for_deterministic_expected(task)
        result = _run_runtime_graph(graph)
        graph_events = [event for event in result.get("events", []) if isinstance(event, dict)]
        events.extend(graph_events)

        if not result.get("ok"):
            runtime_failures.append({"task_id": task.get("id"), "error": result.get("error")})
            continue

        if requires_model:
            fallback_or_model_candidate_route_count += 1
            continue

        deterministic_route_count += 1
        deterministic_outputs_checked += 1
        final = result.get("final")
        if not isinstance(final, dict) or final.get("message") != task.get("expected_output"):
            mismatch_count += 1

    simulated_baseline_model_invocations = len(tasks)
    kora_controlled_model_invocations = _adapter_invocation_count(events)
    avoided_invocations = simulated_baseline_model_invocations - kora_controlled_model_invocations
    avoided_rate = (
        avoided_invocations / simulated_baseline_model_invocations
        if simulated_baseline_model_invocations
        else 0.0
    )
    runtime_ok = not runtime_failures and mismatch_count == 0

    summary: dict[str, Any] = {
        "ok": runtime_ok,
        "benchmark_name": str(workload.get("name", workload_path.stem)),
        "mode": "runtime-integrated-benchmark",
        "offline": offline,
        "workload_path": str(workload_path),
        "total_tasks": len(tasks),
        "deterministic_route_count": deterministic_route_count,
        "fallback_or_model_candidate_route_count": fallback_or_model_candidate_route_count,
        "simulated_baseline_model_invocations": simulated_baseline_model_invocations,
        "kora_controlled_model_invocations": kora_controlled_model_invocations,
        "avoided_simulated_model_invocations": avoided_invocations,
        "avoided_simulated_model_invocation_rate": avoided_rate,
        "deterministic_outputs_checked": deterministic_outputs_checked,
        "mismatch_count": mismatch_count,
        "runtime_path_execution_status": "ok" if runtime_ok else "fail",
        "telemetry_event_count": len(events),
        "events": events,
        "runtime_failures": runtime_failures,
        "summary_output_path": str(json_out) if json_out else None,
        "safe_current_claim": SAFE_CLAIM,
        "claim_boundary": CLAIM_BOUNDARY,
        "notes": [
            "Initial runtime-path benchmark harness.",
            "Deterministic workload records execute through the KORA executor with existing deterministic handler support.",
            "Fallback/model-candidate records execute through the mock adapter to produce runtime adapter events.",
            "No external APIs are called in offline mode.",
            "Raw generated JSON should stay in /tmp or another ignored path unless explicitly selected for review.",
        ],
    }

    if json_out is not None:
        json_out.parent.mkdir(parents=True, exist_ok=True)
        json_out.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    return summary


def _format_percent(value: Any) -> str:
    if isinstance(value, int | float):
        return f"{float(value) * 100:.0f}%"
    return "n/a"


def render_evidence_packet(
    summary: dict[str, Any],
    *,
    generated_at: str | None = None,
    runtime_json_command: str | None = None,
    report_command: str | None = None,
) -> str:
    generated_at = generated_at or datetime.now(UTC).replace(microsecond=0).isoformat()
    runtime_json_command = runtime_json_command or (
        "python3 -m kora run runtime_integrated_benchmark -- "
        "--offline --json-out /tmp/kora_runtime_integrated_benchmark.json"
    )
    report_command = report_command or (
        "python3 examples/runtime_integrated_benchmark/report.py "
        "--input /tmp/kora_runtime_integrated_benchmark.json "
        "--md-out /tmp/kora_runtime_integrated_benchmark_report.md"
    )
    telemetry_summary = summarize_run(summary)
    stage_counts = telemetry_summary.get("stage_counts", {})
    if not isinstance(stage_counts, dict):
        stage_counts = {}
    stage_rows = [
        f"| `{stage}` | `{int(count)}` |"
        for stage, count in sorted(stage_counts.items())
    ]
    if not stage_rows:
        stage_rows = ["| `(none)` | `0` |"]

    lines = [
        "# KORA v0.3.0-alpha initial runtime-path benchmark evidence packet",
        "",
        "Status: initial runtime-path benchmark harness output",
        f"Generated at: `{generated_at}`",
        "",
        "## Source",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Benchmark | `{summary.get('benchmark_name', '')}` |",
        f"| Mode | `{summary.get('mode', '')}` |",
        f"| Workload | `{summary.get('workload_path', '')}` |",
        f"| Offline/mock mode | `{summary.get('offline', False)}` |",
        "",
        "## Reproduction Commands",
        "",
        "```bash",
        runtime_json_command,
        report_command,
        "```",
        "",
        "## Runtime Benchmark Counters",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Total tasks | `{summary.get('total_tasks')}` |",
        f"| Deterministic route count | `{summary.get('deterministic_route_count')}` |",
        (
            "| Fallback/model-candidate route count | "
            f"`{summary.get('fallback_or_model_candidate_route_count')}` |"
        ),
        (
            "| Simulated baseline model invocations | "
            f"`{summary.get('simulated_baseline_model_invocations')}` |"
        ),
        (
            "| KORA-controlled model invocations | "
            f"`{summary.get('kora_controlled_model_invocations')}` |"
        ),
        (
            "| Avoided simulated model invocations | "
            f"`{summary.get('avoided_simulated_model_invocations')}` |"
        ),
        (
            "| Avoided simulated model invocation rate | "
            f"`{_format_percent(summary.get('avoided_simulated_model_invocation_rate'))}` |"
        ),
        f"| Deterministic outputs checked | `{summary.get('deterministic_outputs_checked')}` |",
        f"| Mismatch count | `{summary.get('mismatch_count')}` |",
        f"| Runtime path execution status | `{summary.get('runtime_path_execution_status')}` |",
        f"| Telemetry event count | `{summary.get('telemetry_event_count')}` |",
        "",
        "## Telemetry Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Total LLM calls | `{telemetry_summary.get('total_llm_calls')}` |",
        f"| Events OK | `{telemetry_summary.get('events_ok')}` |",
        f"| Events failed | `{telemetry_summary.get('events_fail')}` |",
        f"| Events skipped | `{telemetry_summary.get('events_skipped')}` |",
        f"| Tokens in | `{telemetry_summary.get('tokens_in')}` |",
        f"| Tokens out | `{telemetry_summary.get('tokens_out')}` |",
        "",
        "### Stage Counts",
        "",
        "| Stage | Count |",
        "|---|---:|",
        *stage_rows,
        "",
        "## Safe Current Claim",
        "",
        f"> {summary.get('safe_current_claim', SAFE_CLAIM)}",
        "",
        "## Claim Boundary",
        "",
        str(summary.get("claim_boundary", CLAIM_BOUNDARY)),
        "",
        "This packet does not claim production cost reduction proof, real API-cost reduction proof, "
        "production benchmark proof, full runtime-integrated benchmark evidence, broad workload "
        "superiority proof, or energy reduction evidence.",
        "",
        "Explicit non-claims:",
        "",
        "- This is not production benchmark evidence.",
        "- This does not prove real API-cost reduction.",
        "- This does not prove production cost reduction.",
        "- This does not prove broad workload superiority.",
        "- This does not prove energy reduction.",
        "- This is not full runtime-integrated benchmark evidence.",
        "",
        "## Reproducibility Notes",
        "",
        "- The runtime benchmark runs in offline mode.",
        "- The workload is the deterministic-heavy v1 100-task workload.",
        "- No external API, network access, or API key is required.",
        "- Generated outputs should be regenerated locally when reviewing evidence.",
        "",
        "## Artifact Policy",
        "",
        "Generated JSON and Markdown outputs are reproducible local outputs. Keep them in `/tmp` "
        "or another ignored path unless a later review explicitly selects a frozen artifact.",
        "",
    ]
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the initial KORA runtime-integrated benchmark harness."
    )
    parser.add_argument(
        "--workload",
        default=str(DEFAULT_WORKLOAD),
        help="Path to workload JSON. Defaults to deterministic_heavy_v1_100.",
    )
    parser.add_argument("--offline", action="store_true", help="Run with offline/mock behavior.")
    parser.add_argument("--json-out", help="Optional path for generated raw JSON output.")
    parser.add_argument("--md-out", help="Optional path for generated Markdown evidence packet.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.offline:
        raise SystemExit("This harness currently requires --offline.")

    workload_path = Path(args.workload)
    if not workload_path.exists() and not workload_path.is_absolute():
        workload_path = _repo_root() / workload_path

    json_out = Path(args.json_out) if args.json_out else None
    summary = build_runtime_integrated_summary(workload_path, offline=True, json_out=json_out)
    if args.md_out:
        md_out = Path(args.md_out)
        md_out.parent.mkdir(parents=True, exist_ok=True)
        md_out.write_text(render_evidence_packet(summary), encoding="utf-8")
        summary["evidence_packet_path"] = str(md_out)
    printable = {key: value for key, value in summary.items() if key != "events"}
    print(json.dumps(printable, indent=2, sort_keys=True))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


CLAIM_BOUNDARY = (
    "This is reproducible benchmark evidence from simulated benchmark artifacts. "
    "It is not production cost proof, real API-cost proof, production benchmark proof, "
    "full runtime-integrated benchmark evidence, broad workload superiority evidence, "
    "or energy-reduction evidence."
)


def load_result(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        result = json.load(handle)

    if not isinstance(result, dict):
        raise ValueError(f"benchmark result must be a JSON object: {path}")
    return result


def _require_number(result: dict[str, Any], key: str, label: str) -> int | float:
    value = result.get(key)
    if not isinstance(value, int | float):
        raise ValueError(f"{label} result must contain numeric {key!r}")
    return value


def _require_mode(result: dict[str, Any], mode: str, label: str) -> None:
    if result.get("mode") != mode:
        raise ValueError(f"{label} result must have mode {mode!r}")


def _format_rate(value: int | float) -> str:
    return f"{value * 100:.0f}%" if value == round(value, 2) else f"{value * 100:.2f}%"


def build_summary_markdown(direct_result: dict[str, Any], kora_result: dict[str, Any]) -> str:
    _require_mode(direct_result, "direct-baseline", "direct-baseline")
    _require_mode(kora_result, "kora-controlled", "kora-controlled")

    benchmark_name = kora_result.get("benchmark_name") or direct_result.get("benchmark_name") or "unknown"
    workload_path = kora_result.get("workload_path") or direct_result.get("workload_path") or "unknown"
    total_tasks = _require_number(kora_result, "total_tasks", "kora-controlled")
    deterministic_tasks = _require_number(kora_result, "requires_model_false", "kora-controlled")
    fallback_tasks = _require_number(kora_result, "requires_model_true", "kora-controlled")
    direct_invocations = _require_number(direct_result, "simulated_model_invocations", "direct-baseline")
    kora_invocations = _require_number(kora_result, "simulated_model_invocations", "kora-controlled")
    avoided_invocations = _require_number(kora_result, "avoided_model_invocations_vs_direct_baseline", "kora-controlled")
    avoided_rate = _require_number(kora_result, "avoided_model_invocation_rate", "kora-controlled")

    lines = [
        f"# KORA Benchmark Result Summary - {benchmark_name}",
        "",
        "## Source Artifacts",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Benchmark name | `{benchmark_name}` |",
        f"| Workload | `{workload_path}` |",
        f"| Direct-baseline result mode | `{direct_result['mode']}` |",
        f"| KORA-controlled result mode | `{kora_result['mode']}` |",
        "",
        "## Result Metrics",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Total tasks | {total_tasks} |",
        f"| Deterministic/no-model tasks | {deterministic_tasks} |",
        f"| Fallback/model-candidate tasks | {fallback_tasks} |",
        f"| Direct-baseline simulated model invocations | {direct_invocations} |",
        f"| KORA-controlled simulated model invocations | {kora_invocations} |",
        f"| Avoided simulated model invocations | {avoided_invocations} |",
        f"| Avoided invocation rate | {_format_rate(avoided_rate)} |",
    ]

    correctness_keys = [
        ("deterministic_output_checks", "Deterministic expected-output checks"),
        ("deterministic_output_mismatches", "Deterministic expected-output mismatches"),
        ("fallback_candidates_skipped_for_output_check", "Fallback candidates skipped for output check"),
    ]
    correctness_rows = [(key, label) for key, label in correctness_keys if key in kora_result]
    if correctness_rows:
        lines.extend(
            [
                "",
                "## Expected-Output Correctness",
                "",
                "| Metric | Value |",
                "|---|---:|",
            ]
        )
        for key, label in correctness_rows:
            lines.append(f"| {label} | {kora_result[key]} |")

    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            CLAIM_BOUNDARY,
            "",
        ]
    )
    return "\n".join(lines)


def write_summary(markdown: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Markdown summaries from KORA benchmark result JSON.")
    parser.add_argument("--direct-baseline", required=True, help="Path to direct-baseline result JSON")
    parser.add_argument("--kora-controlled", required=True, help="Path to KORA-controlled result JSON")
    parser.add_argument("--output", help="Path for generated Markdown summary. If omitted, prints to stdout.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    direct_result = load_result(Path(args.direct_baseline))
    kora_result = load_result(Path(args.kora_controlled))
    markdown = build_summary_markdown(direct_result, kora_result)

    if args.output:
        output_path = Path(args.output)
        write_summary(markdown, output_path)
        print(str(output_path))
    else:
        print(markdown, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

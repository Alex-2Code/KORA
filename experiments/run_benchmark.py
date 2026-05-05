from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


SUPPORTED_MODES = {"direct-baseline", "dry-run", "kora-controlled"}


class DeterministicOutputMismatch(ValueError):
    """Raised when a deterministic workload task does not match its expected output."""


def _normalize_whitespace(value: str) -> str:
    return " ".join(value.strip().lower().split())


def _resolve_arithmetic(input_data: dict[str, Any]) -> Any:
    operation = input_data.get("operation")

    if "left" in input_data and "right" in input_data:
        left = input_data["left"]
        right = input_data["right"]
        if operation == "add":
            return left + right
        if operation == "subtract":
            return left - right
        if operation == "multiply":
            return left * right

    values = input_data.get("values")
    if operation == "add" and isinstance(values, list):
        return {"result": sum(values)}
    if operation == "multiply" and isinstance(values, list):
        result = 1
        for value in values:
            result *= value
        return {"result": result}
    if operation == "percent_change":
        old = input_data["old"]
        new = input_data["new"]
        return {"result": ((new - old) / old) * 100, "unit": "percent"}
    if operation == "divide":
        denominator = input_data["denominator"]
        if denominator == 0:
            return {"error": "division_by_zero"}
        return {"result": input_data["numerator"] / denominator}

    raise ValueError(f"unsupported deterministic arithmetic input: {input_data!r}")


def _resolve_string_normalization(input_data: dict[str, Any]) -> Any:
    text = input_data["text"]
    style = input_data.get("style")
    normalization = input_data.get("normalization")

    if normalization == "strip_lower_join_spaces":
        return " ".join(part.strip().lower() for part in text.split("-"))
    if style == "slug":
        slug = "".join(character.lower() if character.isalnum() else "-" for character in text).strip("-")
        return {"text": slug}
    if style == "email_domain":
        return {"domain": text.split("@", maxsplit=1)[1]}
    return {"text": _normalize_whitespace(text)}


def _resolve_json_validation(input_data: dict[str, Any]) -> dict[str, Any]:
    payload = input_data["payload"]

    if input_data.get("parse") is True:
        parsed = json.loads(payload)
        return {"valid_json": True, **parsed}

    if "required_fields" in input_data:
        required = input_data["required_fields"]
        missing = [field for field in required if field not in payload]
        return {"valid": not missing, "missing": missing}

    required_keys = input_data["required_keys"]
    missing_keys = [key for key in required_keys if key not in payload]
    return {"valid": not missing_keys, "missing_keys": missing_keys}


def _resolve_routing_decision(input_data: dict[str, Any]) -> dict[str, Any]:
    if "kind" in input_data and "priority" in input_data:
        kind = input_data["kind"]
        priority = input_data["priority"]
        route = "security_review" if kind == "security" or priority == "high" else f"{kind}_queue"
        return {"route": route}

    request_type = input_data.get("request_type")
    if request_type == "telemetry_summary" and input_data.get("has_run_json") is True:
        return {"route": "telemetry"}
    if request_type == "run_example":
        return {"route": "examples.run", "example": input_data["example"]}

    raise ValueError(f"unsupported deterministic routing input: {input_data!r}")


def _resolve_cache_lookup(input_data: dict[str, Any]) -> dict[str, Any]:
    key = input_data["key"]
    cache = input_data.get("cache", {"alpha": "cached-alpha", "beta": "cached-beta", "gamma": "cached-gamma"})
    return {"hit": key in cache, "value": cache.get(key)}


def _resolve_schema_check(input_data: dict[str, Any]) -> dict[str, Any]:
    if "enum" in input_data:
        status = input_data["object"].get("status")
        return {"valid": status in input_data["enum"], "field": "status"}

    if input_data.get("schema") == "task_event_minimal":
        task_id = input_data["object"].get("task_id")
        if isinstance(task_id, str):
            return {"valid": True}
        return {"valid": False, "errors": ["task_id_type"]}

    raise ValueError(f"unsupported deterministic schema input: {input_data!r}")


def _resolve_date_normalization(input_data: dict[str, Any]) -> str:
    if input_data.get("input_format") == "M/D/YYYY" and input_data.get("output_format") == "YYYY-MM-DD":
        return datetime.strptime(input_data["date"], "%m/%d/%Y").strftime("%Y-%m-%d")
    raise ValueError(f"unsupported deterministic date normalization input: {input_data!r}")


def _resolve_unit_conversion(input_data: dict[str, Any]) -> dict[str, Any]:
    if input_data.get("from") == "m" and input_data.get("to") == "cm":
        return {"value": input_data["value"] * 100, "unit": "cm"}
    raise ValueError(f"unsupported deterministic unit conversion input: {input_data!r}")


def _resolve_config_validation(input_data: dict[str, Any]) -> dict[str, Any]:
    config = input_data["config"]
    return {"valid": 0 <= config["retries"] <= 3 and config["timeout_ms"] <= 3000}


def _resolve_policy_rule_match(input_data: dict[str, Any]) -> dict[str, Any]:
    allowed = not (input_data["region"] == "eu" and input_data["data_class"] == "restricted")
    return {"allowed": allowed}


DETERMINISTIC_RESOLVERS = {
    "arithmetic": _resolve_arithmetic,
    "string_normalization": _resolve_string_normalization,
    "json_validation": _resolve_json_validation,
    "routing_decision": _resolve_routing_decision,
    "cache_lookup": _resolve_cache_lookup,
    "schema_check": _resolve_schema_check,
    "date_normalization": _resolve_date_normalization,
    "unit_conversion": _resolve_unit_conversion,
    "config_validation": _resolve_config_validation,
    "policy_rule_match": _resolve_policy_rule_match,
}


def load_workload(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        workload = json.load(handle)

    tasks = workload.get("tasks")
    if not isinstance(tasks, list):
        raise ValueError("workload must contain a 'tasks' list")

    return workload


def summarize_workload(workload: dict[str, Any]) -> dict[str, Any]:
    tasks = workload["tasks"]
    category_counts = Counter()
    requires_model_true = 0
    requires_model_false = 0

    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise ValueError(f"task at index {index} must be an object")

        category = task.get("category")
        if not isinstance(category, str) or not category:
            raise ValueError(f"task at index {index} must contain a non-empty category")
        category_counts[category] += 1

        requires_model = task.get("requires_model")
        if requires_model is True:
            requires_model_true += 1
        elif requires_model is False:
            requires_model_false += 1
        else:
            raise ValueError(f"task at index {index} must contain boolean requires_model")

    return {
        "total_tasks": len(tasks),
        "category_counts": dict(sorted(category_counts.items())),
        "requires_model_true": requires_model_true,
        "requires_model_false": requires_model_false,
    }


def resolve_deterministic_task(task: dict[str, Any]) -> Any:
    task_id = task.get("id", "<unknown>")
    category = task.get("category")
    if not isinstance(category, str) or not category:
        raise ValueError(f"deterministic task {task_id} must contain a non-empty string category")

    resolver = DETERMINISTIC_RESOLVERS.get(category)
    if resolver is None:
        raise ValueError(f"no deterministic resolver for task {task_id} category: {category}")

    input_data = task.get("input")
    if not isinstance(input_data, dict):
        raise ValueError(f"deterministic task {task_id} category {category} must contain object input")

    try:
        return resolver(input_data)
    except ValueError as exc:
        raise ValueError(f"deterministic task {task_id} category {category} failed: {exc}") from exc


def validate_expected_outputs(workload: dict[str, Any]) -> dict[str, int]:
    checked = 0
    skipped_fallback_candidates = 0

    for index, task in enumerate(workload["tasks"]):
        if not isinstance(task, dict):
            raise ValueError(f"task at index {index} must be an object")

        if task["requires_model"] is True:
            skipped_fallback_candidates += 1
            continue

        actual_output = resolve_deterministic_task(task)
        expected_output = task.get("expected_output")
        if actual_output != expected_output:
            task_id = task.get("id", f"index {index}")
            raise DeterministicOutputMismatch(
                f"deterministic expected output mismatch for task {task_id}: "
                f"expected {expected_output!r}, got {actual_output!r}"
            )
        checked += 1

    return {
        "deterministic_output_checks": checked,
        "deterministic_output_mismatches": 0,
        "fallback_candidates_skipped_for_output_check": skipped_fallback_candidates,
    }


def build_dry_run_result(workload: dict[str, Any], workload_path: Path) -> dict[str, Any]:
    summary = summarize_workload(workload)

    return {
        "benchmark_name": workload.get("name", workload_path.stem),
        "mode": "dry-run",
        "workload_path": str(workload_path),
        **summary,
        "status": "ok",
        "notes": [
            "Dry-run only: no direct baseline execution was performed.",
            "Dry-run only: no KORA-controlled execution was performed.",
        ],
    }


def build_direct_baseline_result(workload: dict[str, Any], workload_path: Path) -> dict[str, Any]:
    summary = summarize_workload(workload)

    return {
        "benchmark_name": workload.get("name", workload_path.stem),
        "mode": "direct-baseline",
        "workload_path": str(workload_path),
        **summary,
        "simulated_model_invocations": summary["total_tasks"],
        "deterministic_tasks_sent_to_model": summary["requires_model_false"],
        "fallback_candidate_tasks_sent_to_model": summary["requires_model_true"],
        "status": "ok",
        "notes": [
            "Simulated naive baseline: every task is counted as one model invocation.",
            "No real model calls or external APIs were used.",
            "No KORA-controlled execution was performed.",
        ],
    }


def build_kora_controlled_result(workload: dict[str, Any], workload_path: Path) -> dict[str, Any]:
    summary = summarize_workload(workload)
    correctness_summary = validate_expected_outputs(workload)
    direct_baseline_invocations = summary["total_tasks"]
    simulated_model_invocations = summary["requires_model_true"]
    avoided_invocations = direct_baseline_invocations - simulated_model_invocations
    avoided_rate = avoided_invocations / direct_baseline_invocations if direct_baseline_invocations else 0.0

    return {
        "benchmark_name": workload.get("name", workload_path.stem),
        "mode": "kora-controlled",
        "workload_path": str(workload_path),
        **summary,
        "deterministic_resolutions": summary["requires_model_false"],
        "fallback_candidates": summary["requires_model_true"],
        **correctness_summary,
        "simulated_model_invocations": simulated_model_invocations,
        "avoided_model_invocations_vs_direct_baseline": avoided_invocations,
        "avoided_model_invocation_rate": avoided_rate,
        "status": "ok",
        "notes": [
            "Simulated deterministic-first KORA-controlled mode based on workload metadata.",
            "Tasks with requires_model=false are counted as deterministic resolutions.",
            "Tasks with requires_model=true are counted as fallback/model-invocation candidates.",
            "No real model calls, external APIs, or full KORA runtime integration were used.",
        ],
    }


def write_result(result: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")


def run_dry_run(workload_path: Path, output_path: Path) -> dict[str, Any]:
    workload = load_workload(workload_path)
    result = build_dry_run_result(workload, workload_path)
    write_result(result, output_path)
    return result


def run_direct_baseline(workload_path: Path, output_path: Path) -> dict[str, Any]:
    workload = load_workload(workload_path)
    result = build_direct_baseline_result(workload, workload_path)
    write_result(result, output_path)
    return result


def run_kora_controlled(workload_path: Path, output_path: Path) -> dict[str, Any]:
    workload = load_workload(workload_path)
    result = build_kora_controlled_result(workload, workload_path)
    write_result(result, output_path)
    return result


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run KORA benchmark skeleton modes.")
    parser.add_argument("--workload", required=True, help="Path to workload JSON")
    parser.add_argument("--output", required=True, help="Path for result JSON")
    parser.add_argument("--mode", required=True, choices=sorted(SUPPORTED_MODES), help="Benchmark mode")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    workload_path = Path(args.workload)
    output_path = Path(args.output)

    if args.mode == "dry-run":
        result = run_dry_run(workload_path, output_path)
    elif args.mode == "direct-baseline":
        result = run_direct_baseline(workload_path, output_path)
    elif args.mode == "kora-controlled":
        result = run_kora_controlled(workload_path, output_path)
    else:
        raise ValueError(f"unsupported mode: {args.mode}")

    print(
        json.dumps(
            {
                "status": result["status"],
                "benchmark_name": result["benchmark_name"],
                "mode": result["mode"],
                "total_tasks": result["total_tasks"],
                "output": str(output_path),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

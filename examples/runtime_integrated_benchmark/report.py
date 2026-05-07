"""Render a Markdown evidence packet from runtime benchmark JSON."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


def _load_runtime_benchmark_module():
    script_path = Path(__file__).with_name("run.py")
    repo_root = Path(__file__).resolve().parents[2]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    spec = importlib.util.spec_from_file_location("runtime_integrated_benchmark_run", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load runtime_integrated_benchmark module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_runtime_benchmark_json(path: Path) -> dict[str, Any]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("runtime benchmark JSON must contain a JSON object")
    return obj


def write_evidence_packet(
    input_path: Path,
    md_out: Path,
    *,
    runtime_json_command: str | None = None,
    report_command: str | None = None,
) -> str:
    summary = load_runtime_benchmark_json(input_path)
    runtime_benchmark = _load_runtime_benchmark_module()
    packet = runtime_benchmark.render_evidence_packet(
        summary,
        runtime_json_command=runtime_json_command,
        report_command=report_command,
    )
    md_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.write_text(packet, encoding="utf-8")
    return packet


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a KORA runtime benchmark Markdown evidence packet from JSON."
    )
    parser.add_argument("--input", required=True, help="runtime benchmark JSON input path")
    parser.add_argument("--md-out", required=True, help="Markdown evidence packet output path")
    parser.add_argument(
        "--runtime-json-command",
        help="command shown in the report for regenerating the runtime benchmark JSON",
    )
    parser.add_argument(
        "--report-command",
        help="command shown in the report for regenerating this Markdown report",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    input_path = Path(args.input)
    md_out = Path(args.md_out)
    write_evidence_packet(
        input_path,
        md_out,
        runtime_json_command=args.runtime_json_command,
        report_command=args.report_command,
    )
    print(f"Saved runtime benchmark evidence packet: {md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

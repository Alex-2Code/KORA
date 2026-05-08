"""Markdown reports for local no-network validation summaries."""

from __future__ import annotations

from typing import Any


BOUNDARY_TEXT = (
    "This report describes local no-network validation using a deterministic "
    "local validation adapter. It is not real provider validation, real "
    "API-cost reduction evidence, production validation, production "
    "cost-reduction proof, or energy-reduction evidence."
)

COUNTER_KEYS = (
    "total_requests",
    "baseline_model_calls",
    "kora_model_calls",
    "avoided_model_calls",
    "avoided_model_call_rate",
    "deterministic_routes",
    "model_escalations",
    "validation_pass_count",
    "validation_fail_count",
    "error_count",
    "fallback_count",
    "input_tokens_total",
    "output_tokens_total",
)


def _display(value: Any) -> str:
    if value is None:
        return "N/A"
    if isinstance(value, float):
        return f"{value:.4f}" if value == value else "N/A"
    return str(value)


def _summary_line(label: str, value: Any) -> str:
    return f"- {label}: `{_display(value)}`"


def render_local_validation_markdown(summary: dict[str, Any]) -> str:
    """Render a claim-safe Markdown report from local validation counters."""

    workload = summary.get("workload_id") or summary.get("workload_path") or "synthetic local workload"
    command = summary.get("command")
    notes = summary.get("notes")

    lines = [
        "# Local No-Network Validation Report",
        "",
        "## Summary",
        "",
        _summary_line("Workload", workload),
        _summary_line("Mode", summary.get("mode")),
        _summary_line("Provider", summary.get("provider")),
        _summary_line("Model", summary.get("model")),
        _summary_line("Privacy class", summary.get("privacy_class")),
        _summary_line("Total requests", summary.get("total_requests")),
        _summary_line("Baseline model calls", summary.get("baseline_model_calls")),
        _summary_line("KORA-controlled model calls", summary.get("kora_model_calls")),
        _summary_line("Avoided model calls", summary.get("avoided_model_calls")),
        _summary_line("Avoided model-call rate", summary.get("avoided_model_call_rate")),
        _summary_line("Deterministic routes", summary.get("deterministic_routes")),
        _summary_line("Model escalations", summary.get("model_escalations")),
        _summary_line("Validation pass count", summary.get("validation_pass_count")),
        _summary_line("Validation fail count", summary.get("validation_fail_count")),
        _summary_line("Error count", summary.get("error_count")),
        _summary_line("Fallback count", summary.get("fallback_count")),
        "",
        "## Counters",
        "",
        "| Counter | Value |",
        "|---|---:|",
    ]

    for key in COUNTER_KEYS:
        if key in summary:
            lines.append(f"| `{key}` | {_display(summary.get(key))} |")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            BOUNDARY_TEXT,
            "",
            "This report must not include raw prompts, raw provider responses, secrets, or private user data.",
            "",
            "## Reproduction",
            "",
        ]
    )

    if command:
        lines.extend(["```bash", str(command), "```"])
    else:
        lines.append("- Command: `N/A`")

    lines.extend(["", "## Notes", ""])
    if isinstance(notes, list) and notes:
        lines.extend(f"- {note}" for note in notes)
    else:
        lines.append("- No additional notes provided.")

    return "\n".join(lines).rstrip() + "\n"

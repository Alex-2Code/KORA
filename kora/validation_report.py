"""Markdown reports for local no-network validation summaries."""

from __future__ import annotations

from typing import Any


BOUNDARY_TEXT = (
    "This report describes local/no-network validation using a selected "
    "local adapter, including the deterministic local validation adapter. "
    "It is not real provider validation, real API-cost reduction evidence, "
    "production validation, production cost-reduction proof, or "
    "energy-reduction evidence."
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

NON_CLAIMS = (
    "no production cost reduction proof",
    "no real API-cost reduction proof",
    "no production benchmark proof",
    "no full runtime-integrated real-provider benchmark evidence",
    "no broad workload superiority proof",
    "no energy reduction evidence",
    "no formal government validation",
    "no signed partner validation unless actually signed and documented",
    "no guaranteed adoption or funding",
)


def _display(value: Any) -> str:
    if value is None:
        return "N/A"
    if isinstance(value, float):
        return f"{value:.4f}" if value == value else "N/A"
    return str(value)


def _summary_line(label: str, value: Any) -> str:
    return f"- {label}: `{_display(value)}`"


def _bool_status(value: Any) -> str:
    if value is True:
        return "yes"
    if value is False:
        return "no"
    return "N/A"


def render_local_validation_markdown(summary: dict[str, Any]) -> str:
    """Render a claim-safe Markdown report from local validation counters."""

    workload = (
        summary.get("workload_id")
        or summary.get("workload_path")
        or "synthetic local workload"
    )
    command = summary.get("command")
    notes = summary.get("notes")
    provider_fixture = summary.get("provider_fixture_dry_run_contract")

    lines = [
        "# Local No-Network Validation Report",
        "",
        "## Report Metadata",
        "",
        _summary_line(
            "Report type",
            summary.get("report_type", "local_no_network_validation_packet"),
        ),
        _summary_line("Generated at", summary.get("generated_at", "N/A")),
        _summary_line("Mode", summary.get("mode")),
        _summary_line("Adapter kind", summary.get("adapter")),
        _summary_line("Provider label", summary.get("provider")),
        _summary_line("Model label", summary.get("model")),
        _summary_line("Offline", _bool_status(summary.get("offline"))),
        _summary_line("No network", _bool_status(summary.get("no_network"))),
        _summary_line(
            "No real provider call",
            _bool_status(summary.get("no_provider_call")),
        ),
        _summary_line(
            "Fail-closed status",
            summary.get("fail_closed_status", "not_applicable"),
        ),
        "",
        "## Summary",
        "",
        _summary_line("Workload", workload),
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
            "## Adapter Selection Result",
            "",
            _summary_line("Adapter kind", summary.get("adapter")),
            _summary_line("Provider label", summary.get("provider")),
            _summary_line("Model label", summary.get("model")),
            _summary_line(
                "Local/no-network status",
                _bool_status(summary.get("no_network")),
            ),
            _summary_line(
                "Real provider calls attempted",
                "no" if summary.get("no_provider_call") is True else "N/A",
            ),
            "",
            "## Provider Fixture Dry-Run Contract",
            "",
        ]
    )

    if isinstance(provider_fixture, dict):
        lines.extend(
            [
                _summary_line("Status", "available"),
                _summary_line("Mode", provider_fixture.get("mode")),
                _summary_line("Provider label", provider_fixture.get("provider_label")),
                _summary_line("Model label", provider_fixture.get("model_label")),
                _summary_line(
                    "Baseline candidate events",
                    provider_fixture.get("baseline_candidate_events"),
                ),
                _summary_line(
                    "KORA routed events",
                    provider_fixture.get("kora_routed_events"),
                ),
                _summary_line(
                    "Avoided model-call events",
                    provider_fixture.get("avoided_model_call_events"),
                ),
                _summary_line(
                    "Provider attempted events",
                    provider_fixture.get("provider_attempted_events"),
                ),
                _summary_line(
                    "Provider blocked events",
                    provider_fixture.get("provider_blocked_events"),
                ),
                _summary_line("No network", _bool_status(provider_fixture.get("no_network"))),
                _summary_line(
                    "No provider call",
                    _bool_status(provider_fixture.get("no_provider_call")),
                ),
                _summary_line(
                    "Contains real provider response",
                    _bool_status(provider_fixture.get("contains_real_provider_response")),
                ),
                _summary_line(
                    "Contains customer data",
                    _bool_status(provider_fixture.get("contains_customer_data")),
                ),
                _summary_line(
                    "Contains secret material",
                    _bool_status(provider_fixture.get("contains_secret_material")),
                ),
            ]
        )
    else:
        lines.append("- Status: `not provided`")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            BOUNDARY_TEXT,
            "",
            (
                "This report must not include raw prompts, raw provider responses, "
                "secrets, or private user data."
            ),
            "",
            "- No real provider call.",
            "- No network call.",
            "- No API-cost evidence.",
            "- No production benchmark evidence.",
            "- No energy evidence.",
            "",
            "## Interpretation",
            "",
            (
                "KORA's local no-network validation examples show that KORA can "
                "measure avoided model-call events in synthetic workloads."
            ),
            "",
            (
                "The counters in this report are aggregate local/no-network "
                "validation counters. They separate direct baseline candidate "
                "events, KORA-routed model-call events, and avoided model-call "
                "events in synthetic workloads."
            ),
            "",
            "## Explicit Non-Claims",
            "",
            *[f"- {non_claim}" for non_claim in NON_CLAIMS],
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

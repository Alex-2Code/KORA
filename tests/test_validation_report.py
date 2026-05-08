import subprocess
import sys
from pathlib import Path

from kora.validation_report import render_local_validation_markdown


def _summary() -> dict[str, object]:
    return {
        "mode": "customer_support_triage_local_validation",
        "workload_id": "customer_support_triage_synthetic_v1",
        "provider": "local_validation",
        "model": "deterministic-local",
        "privacy_class": "synthetic",
        "total_requests": 12,
        "baseline_model_calls": 12,
        "kora_model_calls": 4,
        "avoided_model_calls": 8,
        "avoided_model_call_rate": 2 / 3,
        "deterministic_routes": 8,
        "model_escalations": 4,
        "validation_pass_count": 12,
        "validation_fail_count": 0,
        "error_count": 0,
        "fallback_count": 0,
        "input_tokens_total": 50,
        "output_tokens_total": 50,
        "command": "python3 -m kora run customer_support_triage_fake_validation -- --offline",
        "notes": ["Synthetic workload only."],
    }


def test_render_local_validation_markdown_includes_core_sections() -> None:
    markdown = render_local_validation_markdown(_summary())

    assert "# Local No-Network Validation Report" in markdown
    assert "## Summary" in markdown
    assert "## Counters" in markdown
    assert "## Boundary" in markdown
    assert "## Reproduction" in markdown
    assert "## Notes" in markdown


def test_render_local_validation_markdown_includes_required_counters() -> None:
    markdown = render_local_validation_markdown(_summary())

    assert "| `total_requests` | 12 |" in markdown
    assert "| `baseline_model_calls` | 12 |" in markdown
    assert "| `kora_model_calls` | 4 |" in markdown
    assert "| `avoided_model_calls` | 8 |" in markdown
    assert "| `avoided_model_call_rate` | 0.6667 |" in markdown
    assert "| `input_tokens_total` | 50 |" in markdown
    assert "| `output_tokens_total` | 50 |" in markdown


def test_render_local_validation_markdown_is_claim_safe() -> None:
    markdown = render_local_validation_markdown(_summary())

    assert "local no-network validation" in markdown
    assert "deterministic local validation adapter" in markdown
    assert "not real provider validation" in markdown
    assert "real API-cost reduction evidence" in markdown
    assert "production validation" in markdown
    assert "energy-reduction evidence" in markdown
    assert "raw prompts" in markdown
    assert "raw provider responses" in markdown
    assert "private user data" in markdown


def test_render_local_validation_markdown_does_not_emit_raw_payloads() -> None:
    markdown = render_local_validation_markdown(_summary())

    assert "raw_prompt" not in markdown
    assert "raw_response" not in markdown
    assert "OPENAI_API_KEY" not in markdown
    assert "ANTHROPIC_API_KEY" not in markdown


def test_customer_support_example_writes_markdown_report(tmp_path: Path) -> None:
    report_path = tmp_path / "customer_support_validation.md"

    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "kora",
            "run",
            "customer_support_triage_fake_validation",
            "--",
            "--offline",
            "--report-md",
            str(report_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0
    report = report_path.read_text(encoding="utf-8")
    assert "# Local No-Network Validation Report" in report
    assert "| `total_requests` | 12 |" in report
    assert "| `kora_model_calls` | 4 |" in report
    assert "customer_support_triage_local_validation" in report
    assert "local_validation" in report


def test_real_model_call_example_writes_markdown_report(tmp_path: Path) -> None:
    report_path = tmp_path / "local_validation.md"

    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "kora",
            "run",
            "real_model_call_validation_fake",
            "--",
            "--offline",
            "--report-md",
            str(report_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0
    report = report_path.read_text(encoding="utf-8")
    assert "# Local No-Network Validation Report" in report
    assert "| `total_requests` | 10 |" in report
    assert "| `kora_model_calls` | 4 |" in report
    assert "local_no_network_model_call_validation" in report
    assert "deterministic-local" in report

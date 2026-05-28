from __future__ import annotations

import os
import subprocess
import sys

from kora.cli import main as cli_main
from kora.studio_status import get_studio_status, render_studio_status_text

APPROVED_BOOST_MESSAGE = "Less waiting. Better answers. No hardware upgrade."
TECHNICAL_EXPLANATION = (
    "KORA Boost handles simple work through fast paths and saves model power "
    "for the tasks that need it."
)


def _run_kora_studio(*args: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.pop("OPENAI_API_KEY", None)
    env.pop("ANTHROPIC_API_KEY", None)
    return subprocess.run(
        [sys.executable, "-m", "kora", "studio", *args],
        check=False,
        capture_output=True,
        text=True,
        env=env,
    )


def test_kora_studio_help_works() -> None:
    completed = _run_kora_studio("--help")

    assert completed.returncode == 0
    assert "KORA Studio" in completed.stdout
    assert "--no-browser" in completed.stdout
    assert "--open-browser" in completed.stdout
    assert "--serve" in completed.stdout
    assert "--host" in completed.stdout
    assert "--port" in completed.stdout


def test_kora_studio_status_command_is_safe_noop() -> None:
    completed = _run_kora_studio("--status")

    assert completed.returncode == 0
    assert "KORA Studio is in local preview mode." in completed.stdout
    assert APPROVED_BOOST_MESSAGE in completed.stdout
    assert TECHNICAL_EXPLANATION in completed.stdout
    assert "Server preview: available with python3 -m kora studio." in completed.stdout
    assert "Status-only command: python3 -m kora studio --status." in completed.stdout
    assert "Browser launch: enabled by default; use --no-browser to suppress it." in completed.stdout
    assert "Provider calls: disabled. No provider calls are made." in completed.stdout
    assert "Cloud sync: disabled. No cloud sync is performed." in completed.stdout
    assert "API keys: not required." in completed.stdout
    assert "Docs: docs/kora-studio/README.md" in completed.stdout
    assert "Fixtures: docs/kora-studio/fixtures/" in completed.stdout
    assert completed.stderr == ""


def test_kora_studio_default_launches_server_with_browser(monkeypatch) -> None:
    calls: list[dict[str, object]] = []

    def fake_run_studio_server(*, host: str, port: int, open_browser: bool) -> None:
        calls.append({"host": host, "port": port, "open_browser": open_browser})

    monkeypatch.setattr("kora.cli.run_studio_server", fake_run_studio_server)

    assert cli_main(["studio"]) == 0
    assert calls == [{"host": "127.0.0.1", "port": 8765, "open_browser": True}]


def test_kora_studio_no_browser_suppresses_browser_open(monkeypatch) -> None:
    calls: list[dict[str, object]] = []

    def fake_run_studio_server(*, host: str, port: int, open_browser: bool) -> None:
        calls.append({"host": host, "port": port, "open_browser": open_browser})

    monkeypatch.setattr("kora.cli.run_studio_server", fake_run_studio_server)

    assert cli_main(["studio", "--no-browser", "--port", "8766"]) == 0
    assert calls == [{"host": "127.0.0.1", "port": 8766, "open_browser": False}]


def test_kora_studio_serve_remains_compatible(monkeypatch) -> None:
    calls: list[dict[str, object]] = []

    def fake_run_studio_server(*, host: str, port: int, open_browser: bool) -> None:
        calls.append({"host": host, "port": port, "open_browser": open_browser})

    monkeypatch.setattr("kora.cli.run_studio_server", fake_run_studio_server)

    assert cli_main(["studio", "--serve"]) == 0
    assert calls == [{"host": "127.0.0.1", "port": 8765, "open_browser": True}]


def test_get_studio_status_is_local_preview() -> None:
    status = get_studio_status()

    assert status["status"] == "preview"
    assert status["implementation"] == "local_server_preview"
    assert status["v0_1_demo_status"] == "local_fixture_preview"
    assert "Report Viewer Placeholder" in status["v0_1_demo_surfaces"]
    assert status["server_available"] is True
    assert status["server_skeleton_available"] is True
    assert status["server_skeleton_command"] == "python3 -m kora studio"
    assert status["browser_launch_available"] is True
    assert status["provider_calls_enabled"] is False
    assert status["cloud_sync_enabled"] is False
    assert status["local_runtime_required"] is False
    assert status["docs_path"] == "docs/kora-studio/README.md"
    assert status["fixtures_path"] == "docs/kora-studio/fixtures/"
    assert status["kora_boost_message"] == APPROVED_BOOST_MESSAGE


def test_render_studio_status_text_includes_boundaries() -> None:
    text = render_studio_status_text(get_studio_status())

    assert text.endswith("\n")
    assert "local server preview scaffold" in text
    assert "fixture-backed demo surfaces" in text
    assert "No provider calls are made" in text
    assert "No cloud sync is performed" in text
    assert "Local runtime: not required" in text


def test_kora_studio_status_does_not_start_or_validate_server_host() -> None:
    completed = _run_kora_studio("--status", "--host", "0.0.0.0")

    assert completed.returncode == 0


def test_kora_studio_rejects_non_localhost_launch_host() -> None:
    completed = _run_kora_studio("--serve", "--host", "0.0.0.0")

    assert completed.returncode == 2
    assert "local-only" in completed.stderr
    assert completed.stdout == ""

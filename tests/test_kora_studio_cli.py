from __future__ import annotations

import os
import subprocess
import sys

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
    assert "planning/preview status" in completed.stdout
    assert "--no-browser" in completed.stdout
    assert "--open-browser" in completed.stdout
    assert "--serve" in completed.stdout
    assert "--host" in completed.stdout
    assert "--port" in completed.stdout


def test_kora_studio_status_command_is_safe_noop() -> None:
    completed = _run_kora_studio()

    assert completed.returncode == 0
    assert "KORA Studio is in planning/preview mode." in completed.stdout
    assert APPROVED_BOOST_MESSAGE in completed.stdout
    assert TECHNICAL_EXPLANATION in completed.stdout
    assert "Server skeleton: available with python3 -m kora studio --serve." in completed.stdout
    assert "no local server is started yet." in completed.stdout
    assert "Provider calls: disabled. No provider calls are made." in completed.stdout
    assert "API keys: not required." in completed.stdout
    assert "Docs: docs/kora-studio/README.md" in completed.stdout
    assert "Fixtures: docs/kora-studio/fixtures/" in completed.stdout
    assert completed.stderr == ""


def test_kora_studio_inert_browser_flags_do_not_launch_browser() -> None:
    completed = _run_kora_studio("--open-browser", "--no-browser")

    assert completed.returncode == 0
    assert "Browser launch: not implemented yet." in completed.stdout
    assert "Server skeleton: available with python3 -m kora studio --serve." in completed.stdout
    assert "no local server is started yet." in completed.stdout


def test_get_studio_status_is_planning_skeleton() -> None:
    status = get_studio_status()

    assert status["status"] == "planning"
    assert status["implementation"] == "cli_skeleton"
    assert status["server_available"] is False
    assert status["server_skeleton_available"] is True
    assert status["server_skeleton_command"] == "python3 -m kora studio --serve"
    assert status["browser_launch_available"] is False
    assert status["provider_calls_enabled"] is False
    assert status["local_runtime_required"] is False
    assert status["docs_path"] == "docs/kora-studio/README.md"
    assert status["fixtures_path"] == "docs/kora-studio/fixtures/"
    assert status["kora_boost_message"] == APPROVED_BOOST_MESSAGE


def test_render_studio_status_text_includes_boundaries() -> None:
    text = render_studio_status_text(get_studio_status())

    assert text.endswith("\n")
    assert "CLI skeleton" in text
    assert "local server skeleton" in text
    assert "No provider calls are made" in text
    assert "Local runtime: not required" in text


def test_kora_studio_rejects_non_localhost_serve_host() -> None:
    completed = _run_kora_studio("--serve", "--host", "0.0.0.0")

    assert completed.returncode == 2
    assert "local-only" in completed.stderr
    assert completed.stdout == ""

"""Planning-stage status helpers for the KORA Studio CLI skeleton."""

from __future__ import annotations

from typing import Any

KORA_BOOST_MESSAGE = "Less waiting. Better answers. No hardware upgrade."
KORA_BOOST_TECHNICAL_EXPLANATION = (
    "KORA Boost handles simple work through fast paths and saves model power "
    "for the tasks that need it."
)
DOCS_PATH = "docs/kora-studio/README.md"
FIXTURES_PATH = "docs/kora-studio/fixtures/"


def get_studio_status() -> dict[str, Any]:
    """Return static planning-stage status for KORA Studio."""

    return {
        "status": "planning",
        "implementation": "cli_skeleton",
        "server_available": False,
        "server_skeleton_available": True,
        "server_skeleton_command": "python3 -m kora studio --serve",
        "browser_launch_available": False,
        "provider_calls_enabled": False,
        "local_runtime_required": False,
        "docs_path": DOCS_PATH,
        "fixtures_path": FIXTURES_PATH,
        "kora_boost_message": KORA_BOOST_MESSAGE,
        "kora_boost_technical_explanation": KORA_BOOST_TECHNICAL_EXPLANATION,
    }


def render_studio_status_text(status: dict[str, Any]) -> str:
    """Render KORA Studio planning-stage status for CLI output."""

    lines = [
        "KORA Studio is in planning/preview mode.",
        str(status["kora_boost_message"]),
        str(status["kora_boost_technical_explanation"]),
        "Current status: CLI skeleton with optional local server skeleton.",
        "Server skeleton: available with python3 -m kora studio --serve.",
        "Default status command: no local server is started yet.",
        "Browser launch: not implemented yet.",
        "Provider calls: disabled. No provider calls are made.",
        "Local runtime: not required for this command.",
        "API keys: not required.",
        f"Docs: {status['docs_path']}",
        f"Fixtures: {status['fixtures_path']}",
    ]
    return "\n".join(lines) + "\n"

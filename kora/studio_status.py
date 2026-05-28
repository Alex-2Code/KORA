"""Preview status helpers for the KORA Studio local demo scaffold."""

from __future__ import annotations

from typing import Any

KORA_BOOST_MESSAGE = "Less waiting. Better answers. No hardware upgrade."
KORA_BOOST_TECHNICAL_EXPLANATION = (
    "KORA Boost handles simple work through fast paths and saves model power "
    "for the tasks that need it."
)
DOCS_PATH = "docs/kora-studio/README.md"
FIXTURES_PATH = "docs/kora-studio/fixtures/"
V0_1_DEMO_SURFACES = [
    "Launch/local-only status",
    "Your Computer",
    "Model Capability Estimate",
    "Runtime Status",
    "Catalog vs Installed",
    "Setup Guidance",
    "Disabled Download/Run Actions",
    "KORA Boost Boundary",
    "Execution Viewer",
    "Standard Mode vs KORA Boost",
    "Report Viewer Placeholder",
]


def get_studio_status() -> dict[str, Any]:
    """Return static preview status for KORA Studio."""

    return {
        "status": "preview",
        "implementation": "local_server_preview",
        "v0_1_demo_status": "local_fixture_preview",
        "v0_1_demo_surfaces": list(V0_1_DEMO_SURFACES),
        "server_available": True,
        "server_skeleton_available": True,
        "server_skeleton_command": "python3 -m kora studio",
        "browser_launch_available": True,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "local_runtime_required": False,
        "docs_path": DOCS_PATH,
        "fixtures_path": FIXTURES_PATH,
        "kora_boost_message": KORA_BOOST_MESSAGE,
        "kora_boost_technical_explanation": KORA_BOOST_TECHNICAL_EXPLANATION,
    }


def render_studio_status_text(status: dict[str, Any]) -> str:
    """Render KORA Studio preview status for CLI output."""

    lines = [
        "KORA Studio is in local preview mode.",
        "Positioning: local-first AI Task Execution Router workspace.",
        "KORA Studio routes local AI workflows; it is not an LM Studio replacement or generic local chatbot.",
        str(status["kora_boost_message"]),
        str(status["kora_boost_technical_explanation"]),
        "KORA does not remove RAM/VRAM/unified-memory or model-loading requirements.",
        "Provider/cloud/distributed routes: disabled by default unless explicitly enabled.",
        "Current status: local server preview scaffold with fixture-backed demo surfaces.",
        "Server preview: available with python3 -m kora studio.",
        "Status-only command: python3 -m kora studio --status.",
        "Browser launch: enabled by default; use --no-browser to suppress it.",
        "Provider calls: disabled. No provider calls are made.",
        "Cloud sync: disabled. No cloud sync is performed.",
        "Local runtime: not required for this command.",
        "API keys: not required.",
        f"Docs: {status['docs_path']}",
        f"Fixtures: {status['fixtures_path']}",
    ]
    return "\n".join(lines) + "\n"

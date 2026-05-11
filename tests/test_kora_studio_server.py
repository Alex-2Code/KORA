from __future__ import annotations

import json
import os
import threading
import urllib.request

import pytest
from http.server import ThreadingHTTPServer

from kora.studio_server import (
    DEFAULT_STUDIO_HOST,
    DEFAULT_STUDIO_PORT,
    create_studio_request_handler,
    get_studio_health_payload,
    get_studio_server_status,
    get_studio_status_payload,
    is_allowed_studio_host,
    render_studio_placeholder_html,
    render_studio_server_status_text,
)

APPROVED_BOOST_MESSAGE = "Less waiting. Better answers. No hardware upgrade."
TECHNICAL_EXPLANATION = (
    "KORA Boost handles simple work through fast paths and saves model power "
    "for the tasks that need it."
)


def test_import_does_not_start_server_or_require_api_keys(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    assert os.environ.get("OPENAI_API_KEY") is None
    assert os.environ.get("ANTHROPIC_API_KEY") is None
    assert DEFAULT_STUDIO_HOST == "127.0.0.1"
    assert DEFAULT_STUDIO_PORT == 8765


def test_allowed_studio_hosts_are_local_only() -> None:
    assert is_allowed_studio_host("127.0.0.1") is True
    assert is_allowed_studio_host("localhost") is True
    assert is_allowed_studio_host("0.0.0.0") is False
    assert is_allowed_studio_host("::1") is False


def test_get_studio_server_status_fields() -> None:
    status = get_studio_server_status()

    assert status["ok"] is True
    assert status["service"] == "kora-studio"
    assert status["status"] == "preview"
    assert status["server"] == "local-only"
    assert status["host"] == "127.0.0.1"
    assert status["port"] == 8765
    assert status["provider_calls_enabled"] is False
    assert status["browser_launch_available"] is False
    assert status["ollama_calls_enabled"] is False
    assert status["local_runtime_required"] is False
    assert status["no_server_side_provider_calls"] is True
    assert status["docs_path"] == "docs/kora-studio/README.md"
    assert status["fixtures_path"] == "docs/kora-studio/fixtures/"
    assert status["kora_boost_message"] == APPROVED_BOOST_MESSAGE
    assert status["kora_boost_technical_explanation"] == TECHNICAL_EXPLANATION


def test_health_and_status_payloads_are_claim_safe() -> None:
    health = get_studio_health_payload()
    status = get_studio_status_payload()

    assert health == {
        "ok": True,
        "service": "kora-studio",
        "status": "preview",
        "server": "local-only",
        "provider_calls_enabled": False,
        "browser_launch_available": False,
    }
    assert status["provider_calls_enabled"] is False
    assert status["no_server_side_provider_calls"] is True
    assert status["kora_boost_message"] == APPROVED_BOOST_MESSAGE


def test_render_studio_server_status_text_includes_boundaries() -> None:
    text = render_studio_server_status_text(get_studio_server_status())

    assert "Local URL: http://127.0.0.1:8765/" in text
    assert "preview/local-only" in text
    assert "No provider calls are made" in text
    assert "No Ollama calls are made" in text
    assert "API keys: not required" in text


def test_request_handler_serves_health_status_and_placeholder() -> None:
    handler = create_studio_request_handler(lambda: get_studio_server_status(port=0))
    try:
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    except PermissionError:
        pytest.skip("localhost binding is not available in this sandbox")
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}"
    try:
        with urllib.request.urlopen(f"{base_url}/health", timeout=2) as response:
            health = json.loads(response.read().decode("utf-8"))
        with urllib.request.urlopen(f"{base_url}/status", timeout=2) as response:
            status = json.loads(response.read().decode("utf-8"))
        with urllib.request.urlopen(f"{base_url}/", timeout=2) as response:
            html = response.read().decode("utf-8")
    finally:
        server.shutdown()
        thread.join(timeout=2)
        server.server_close()

    assert health["ok"] is True
    assert health["service"] == "kora-studio"
    assert status["server"] == "local-only"
    assert status["provider_calls_enabled"] is False
    assert status["ollama_calls_enabled"] is False
    content_type = response.headers.get("Content-Type", "")

    assert "text/html" in content_type
    assert "KORA Studio" in html
    assert APPROVED_BOOST_MESSAGE in html
    assert "Preview / Local-only" in html
    assert "Local v0.1 Skeleton" in html
    assert "deterministic-first local workflow exploration" in html
    assert "/health" in html
    assert "/status" in html
    assert "Provider calls: disabled" in html
    assert "Model/runtime integration: not connected" in html
    assert "Browser launch: disabled" in html
    assert "Ollama integration: not connected" in html
    assert "No production/API-cost/energy claims" in html
    assert "provider calls enabled" not in html.lower()
    assert "production cost reduction" not in html.lower()
    assert "real api-cost reduction" not in html.lower()
    assert "energy reduction" not in html.lower()


def test_static_preview_html_content_is_safe_and_complete() -> None:
    html = render_studio_placeholder_html(get_studio_server_status())

    assert html.startswith("<!doctype html>")
    assert "KORA Studio" in html
    assert "Local v0.1 Skeleton" in html
    assert "Preview / Local-only" in html
    assert APPROVED_BOOST_MESSAGE in html
    assert TECHNICAL_EXPLANATION in html
    assert "deterministic-first local workflow exploration" in html
    assert "Status Cards" in html
    assert "Server: local" in html
    assert "Provider calls: disabled" in html
    assert "Model/runtime integration: not connected" in html
    assert "Browser launch: disabled" in html
    assert "Ollama integration: not connected" in html
    assert "Endpoint Panel" in html
    assert "/health" in html
    assert "/status" in html
    assert "Workflow Preview" in html
    assert "Request" in html
    assert "Deterministic checks" in html
    assert "Local status" in html
    assert "Future runtime integration placeholder" in html
    assert "Placeholder only; no runtime execution occurs on this page" in html
    assert "Limitations Panel" in html
    assert "No production/API-cost/energy claims" in html
    assert "No full frontend yet" in html
    assert "No browser launch" in html
    assert "No provider calls" in html
    assert "No model/runtime integration yet" in html
    assert "No Ollama integration" in html
    assert "docs/kora-studio/README.md" in html
    assert "docs/kora-studio/fixtures/" in html
    assert "Local-only skeleton" in html
    assert "OPENAI_API_KEY" not in html
    assert "ANTHROPIC_API_KEY" not in html
    assert "provider calls enabled" not in html.lower()
    assert "production cost reduction" not in html.lower()
    assert "real api-cost reduction" not in html.lower()
    assert "energy reduction" not in html.lower()
    assert "<script" not in html.lower()
    assert "src=" not in html.lower()
    assert 'href="http' not in html.lower()
    assert "https://" not in html.lower()
    assert "localstorage" not in html.lower()
    assert "sessionstorage" not in html.lower()
    assert "fetch(" not in html.lower()
    assert "xmlhttprequest" not in html.lower()
    assert "navigator.sendbeacon" not in html.lower()

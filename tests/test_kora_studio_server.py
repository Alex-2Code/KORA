from __future__ import annotations

import json
import os
import threading
import urllib.request
from pathlib import Path

import pytest
from http.server import ThreadingHTTPServer

from kora.studio_server import (
    DEFAULT_STUDIO_HOST,
    DEFAULT_STUDIO_PORT,
    create_studio_request_handler,
    get_studio_url,
    get_studio_health_payload,
    get_studio_server_status,
    get_studio_status_payload,
    is_allowed_studio_host,
    open_studio_browser,
    render_studio_placeholder_html,
    render_studio_server_status_text,
    run_studio_server,
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
    assert status["studio_status"]["service"] == "kora-studio"
    assert status["studio_status"]["status"] == "preview"
    assert status["studio_status"]["implementation"] == "local_server_skeleton"
    assert status["studio_status"]["positioning"] == "local-first AI Task Execution Router workspace"
    assert status["studio_status"]["v0_2_status"]["milestone"] == "v0.2"
    assert status["studio_status"]["v0_2_status"]["readiness"] == "in_progress"
    assert "local preview/demo readiness milestone" in status["studio_status"]["v0_2_status"]["claim_boundary"]
    assert status["v0_2_status"] == status["studio_status"]["v0_2_status"]
    assert status["v0_1_readiness_status"] == "local_fixture_demo_ready"
    assert "Report Viewer Placeholder" in status["v0_1_demo_surfaces"]
    assert "local fixture-backed AI Task Execution Router demo scaffold" in status["v0_1_claim_boundary"]
    assert status["server"] == "local-only"
    assert status["host"] == "127.0.0.1"
    assert status["port"] == 8765
    assert status["launch_boundary"] == {
        "host": "127.0.0.1",
        "port": 8765,
        "url": "http://127.0.0.1:8765/",
        "server": "local-only",
        "allowed_hosts": ["127.0.0.1", "localhost"],
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "browser_launch_available": True,
        "api_key_required": False,
        "claim_boundary": (
            "The Studio preview is localhost-only by default. Provider calls and cloud sync are disabled, "
            "and no API key is required for the default local preview."
        ),
    }
    assert status["provider_calls_enabled"] is False
    assert status["cloud_sync_enabled"] is False
    assert status["system_profile"]["default_host"] == "127.0.0.1"
    assert status["system_profile"]["default_port"] == 8765
    assert status["system_profile"]["provider_calls_enabled"] is False
    assert status["system_profile"]["cloud_sync_enabled"] is False
    assert status["model_capability_estimate"]["recommended_local_chat_tier"]
    assert "estimates until validated" in status["model_capability_estimate"]["claim_boundary"]
    assert status["model_catalog_status"] == "static_local_scaffold"
    assert status["recommended_models"]
    first_model = status["recommended_models"][0]
    assert first_model["download_action_enabled"] is False
    assert first_model["run_action_enabled"] is False
    assert first_model["download_action_label"] == "Download not connected yet"
    assert first_model["run_action_label"] == "Run not connected yet"
    assert first_model["disabled_actions_route_to_guidance"] is True
    assert first_model["setup_guidance_path"] == "docs/kora-studio/kora-studio-runtime-setup-guidance.md"
    assert "estimates until validated" in status["model_catalog_claim_boundary"]
    assert "Download and execution are not connected yet" in status["model_catalog_claim_boundary"]
    assert status["runtime_status"]
    first_runtime = status["runtime_status"][0]
    assert first_runtime["service_reachable"] is False
    assert first_runtime["service_check_status"] == "not_checked"
    assert first_runtime["service_url"] == "http://127.0.0.1:11434/"
    assert first_runtime["service_probe_timeout_ms"] <= 500
    assert "localhost-only check" in first_runtime["service_probe_claim_boundary"]
    assert first_runtime["installed_model_detection_enabled"] is False
    assert first_runtime["installed_model_detection_status"] == "not_connected"
    assert first_runtime["installed_models_count"] == 0
    assert status["installed_models_summary"]["detection_status"] == "not_connected"
    assert status["installed_models_summary"]["installed_model_detection_status"] == "not_connected"
    assert status["installed_models_summary"]["installed_model_detection_enabled"] is False
    assert status["installed_models_summary"]["installed_models_count"] == 0
    assert "Catalog examples are not the same as installed models" in status["catalog_runtime_distinction"]
    assert status["setup_guidance_status"] == "informational_scaffold"
    assert status["setup_guidance_url"] == "docs/kora-studio/kora-studio-runtime-setup-guidance.md"
    assert status["disabled_actions_route_to_guidance"] is True
    assert status["disabled_action_state"] == {
        "download_connected": False,
        "run_connected": False,
        "model_execution_connected": False,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "disabled_actions_route_to_guidance": True,
        "setup_guidance_url": "docs/kora-studio/kora-studio-runtime-setup-guidance.md",
        "claim_boundary": (
            "Download and run actions remain disabled until explicitly connected. Disabled actions point to "
            "informational setup guidance, not to an active installer or model runner."
        ),
    }
    assert "not to an active installer" in status["setup_guidance_claim_boundary"]
    assert status["execution_viewer_status"] == "fixture_mock_scaffold"
    assert status["execution_viewer_fixture_event_count"] == 6
    assert status["execution_viewer_fixture_events"][0]["stage_id"] == "request_received"
    assert status["execution_viewer_fixture_events"][-1]["stage_id"] == "final_counters"
    assert status["execution_viewer_fixture_events"][-1]["counters_snapshot"]["avoided_model_calls"] == 1
    assert "local fixture/mock data" in status["execution_viewer_claim_boundary"]
    assert status["model_execution_connected"] is False
    assert status["download_connected"] is False
    assert status["standard_vs_kora_comparison_status"] == "fixture_mock_scaffold"
    assert status["standard_vs_kora_metrics"]["baseline_model_calls"] == 1
    assert status["standard_vs_kora_metrics"]["kora_model_calls"] == 0
    assert status["standard_vs_kora_metrics"]["avoided_model_calls"] == 1
    assert status["standard_vs_kora_metrics"]["deterministic_routes"] == 1
    assert status["standard_vs_kora_metrics"]["model_escalations"] == 0
    assert status["standard_vs_kora_metrics"]["validation_pass_count"] == 1
    assert len(status["standard_vs_kora_metric_cards"]) == 6
    assert "fixture/mock comparison" in status["standard_vs_kora_claim_boundary"]
    assert status["report_viewer_status"] == "fixture_metadata_placeholder"
    assert status["report_viewer_placeholder"]["report_fixture_path"] == (
        "docs/kora-studio/fixtures/report-viewer-metadata.sample.json"
    )
    assert status["report_viewer_placeholder"]["arbitrary_local_file_scan_enabled"] is False
    assert status["report_viewer_placeholder"]["upload_enabled"] is False
    assert status["report_viewer_placeholder"]["generated_report_commit_enabled"] is False
    assert status["report_viewer_placeholder"]["counters"]["avoided_model_calls"] == 8
    assert status["report_export_status"] == "placeholder_not_connected"
    assert status["report_export_placeholder"]["export_action_enabled"] is False
    assert "local fixture metadata only" in status["report_viewer_claim_boundary"]
    assert set(status["claim_boundaries"]) == {
        "studio",
        "launch",
        "model_capability",
        "model_catalog",
        "runtime_setup_guidance",
        "disabled_actions",
        "execution_viewer",
        "standard_vs_kora",
        "report_viewer",
    }
    assert "not a production release" in status["claim_boundaries"]["studio"]
    assert "localhost-only" in status["claim_boundaries"]["launch"]
    assert "estimates until validated" in status["claim_boundaries"]["model_capability"]
    assert "Download and execution are not connected yet" in status["claim_boundaries"]["model_catalog"]
    assert "No model is downloaded" in status["claim_boundaries"]["runtime_setup_guidance"]
    assert "remain disabled" in status["claim_boundaries"]["disabled_actions"]
    assert "local fixture/mock data" in status["claim_boundaries"]["execution_viewer"]
    assert "fixture/mock comparison" in status["claim_boundaries"]["standard_vs_kora"]
    assert "local fixture metadata only" in status["claim_boundaries"]["report_viewer"]
    assert status["first_run_section_order"] == [
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
    assert status["browser_launch_available"] is True
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
        "cloud_sync_enabled": False,
        "browser_launch_available": True,
    }
    assert status["provider_calls_enabled"] is False
    assert status["cloud_sync_enabled"] is False
    assert "system_profile" in status
    assert "model_capability_estimate" in status
    assert "recommended_models" in status
    assert status["model_catalog_status"] == "static_local_scaffold"
    assert "runtime_status" in status
    assert "installed_models_summary" in status
    assert status["installed_models_summary"]["installed_model_detection_enabled"] is False
    assert status["setup_guidance_status"] == "informational_scaffold"
    assert status["disabled_actions_route_to_guidance"] is True
    assert status["execution_viewer_status"] == "fixture_mock_scaffold"
    assert status["execution_viewer_fixture_event_count"] == 6
    assert status["model_execution_connected"] is False
    assert status["standard_vs_kora_comparison_status"] == "fixture_mock_scaffold"
    assert status["standard_vs_kora_metrics"]["avoided_model_calls"] == 1
    assert status["report_viewer_status"] == "fixture_metadata_placeholder"
    assert status["report_export_status"] == "placeholder_not_connected"
    assert status["no_server_side_provider_calls"] is True
    assert status["kora_boost_message"] == APPROVED_BOOST_MESSAGE


def test_status_payload_exposes_v0_2_contract_fields() -> None:
    status = get_studio_status_payload()

    required_top_level_fields = {
        "studio_status",
        "launch_boundary",
        "system_profile",
        "model_capability_estimate",
        "runtime_status",
        "installed_models_summary",
        "model_catalog_status",
        "recommended_models",
        "setup_guidance_status",
        "disabled_action_state",
        "execution_viewer_status",
        "execution_viewer_fixture_events",
        "standard_vs_kora_comparison_status",
        "standard_vs_kora_comparison",
        "standard_vs_kora_metrics",
        "report_viewer_status",
        "report_viewer_placeholder",
        "provider_calls_enabled",
        "cloud_sync_enabled",
        "claim_boundaries",
        "first_run_section_order",
    }
    assert required_top_level_fields <= set(status)

    assert status["studio_status"]["v0_2_status"]["first_run_section_order"] == status["first_run_section_order"]
    assert status["launch_boundary"]["provider_calls_enabled"] is False
    assert status["launch_boundary"]["cloud_sync_enabled"] is False
    assert status["disabled_action_state"]["download_connected"] is False
    assert status["disabled_action_state"]["run_connected"] is False
    assert status["disabled_action_state"]["model_execution_connected"] is False
    assert status["execution_viewer_status"] == "fixture_mock_scaffold"
    assert status["standard_vs_kora_comparison_status"] == "fixture_mock_scaffold"
    assert status["report_viewer_status"] == "fixture_metadata_placeholder"
    assert status["provider_calls_enabled"] is False
    assert status["cloud_sync_enabled"] is False


def test_render_studio_server_status_text_includes_boundaries() -> None:
    text = render_studio_server_status_text(get_studio_server_status())

    assert "Launching KORA Studio" in text
    assert "Local URL:" in text
    assert "http://127.0.0.1:8765/" in text
    assert "Local-only" in text
    assert "Provider calls: disabled" in text
    assert "Cloud sync: disabled" in text
    assert "Press Ctrl+C to stop" in text


def test_render_studio_server_status_text_includes_no_browser_state() -> None:
    text = render_studio_server_status_text(get_studio_server_status(), open_browser=False)

    assert "Local URL:" in text
    assert "http://127.0.0.1:8765/" in text
    assert "Browser launch: disabled by --no-browser." in text


def test_render_studio_server_status_text_includes_browser_failure_fallback() -> None:
    text = render_studio_server_status_text(
        get_studio_server_status(),
        open_browser=True,
        browser_opened=False,
    )

    assert "Browser launch failed. Open this URL manually:" in text
    assert "http://127.0.0.1:8765/" in text


def test_open_studio_browser_is_mockable_and_failure_safe() -> None:
    opened_urls: list[str] = []

    assert open_studio_browser("http://127.0.0.1:8765/", lambda url: (opened_urls.append(url), False)[1]) is False
    assert opened_urls == ["http://127.0.0.1:8765/"]

    def raise_error(url: str) -> bool:
        raise RuntimeError(f"cannot open {url}")

    assert open_studio_browser("http://127.0.0.1:8765/", raise_error) is False
    assert open_studio_browser("http://127.0.0.1:8765/", lambda url: True) is True


def test_run_studio_server_opens_browser_by_default(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    opened_urls: list[str] = []
    created_servers: list[object] = []

    class FakeServer:
        def __init__(self, address: tuple[str, int], handler: object) -> None:
            self.address = address
            self.handler = handler
            created_servers.append(self)

        def serve_forever(self) -> None:
            raise KeyboardInterrupt

        def server_close(self) -> None:
            return None

    monkeypatch.setattr("kora.studio_server.ThreadingHTTPServer", FakeServer)

    run_studio_server(browser_opener=lambda url: opened_urls.append(url) is None or True)

    assert opened_urls == [get_studio_url()]
    assert created_servers
    assert getattr(created_servers[0], "address") == ("127.0.0.1", 8765)
    output = capsys.readouterr().out
    assert "Launching KORA Studio" in output
    assert "Provider calls: disabled" in output
    assert "Cloud sync: disabled" in output


def test_run_studio_server_no_browser_suppresses_browser_open(monkeypatch: pytest.MonkeyPatch) -> None:
    opened_urls: list[str] = []

    class FakeServer:
        def __init__(self, address: tuple[str, int], handler: object) -> None:
            self.address = address
            self.handler = handler

        def serve_forever(self) -> None:
            raise KeyboardInterrupt

        def server_close(self) -> None:
            return None

    monkeypatch.setattr("kora.studio_server.ThreadingHTTPServer", FakeServer)

    run_studio_server(open_browser=False, browser_opener=lambda url: opened_urls.append(url) is None or True)

    assert opened_urls == []


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
    assert status["cloud_sync_enabled"] is False
    assert "system_profile" in status
    assert "model_capability_estimate" in status
    assert "recommended_models" in status
    assert status["model_catalog_claim_boundary"]
    assert "runtime_status" in status
    assert status["installed_models_summary"]["installed_models_detected"] is False
    assert status["ollama_calls_enabled"] is False
    content_type = response.headers.get("Content-Type", "")

    assert "text/html" in content_type
    assert "KORA Studio" in html
    assert APPROVED_BOOST_MESSAGE in html
    assert "Preview / Local-only" in html
    assert "Local Preview Scaffold" in html
    assert "deterministic-first local workflow exploration" in html
    assert "/health" in html
    assert "/status" in html
    assert "Provider calls: disabled" in html
    assert "Cloud sync: disabled" in html
    assert "Your Computer" in html
    assert "Model Capability Estimate" in html
    assert "Catalog vs Installed" in html
    assert "Physically runnable local candidates" in html
    assert "Larger-model workflow candidates" in html
    assert "Model recommendations are estimates until validated on this machine" in html
    assert "Download and execution are not connected yet" in html
    assert "Download" in html
    assert "Run" in html
    assert "Disabled Download/Run Actions" in html
    assert "Download action" in html
    assert "Run action" in html
    assert "Download not connected yet" in html
    assert "Run not connected yet" in html
    assert "Setup Guidance" in html
    assert "Disabled actions point to guidance, not to an active installer" in html
    assert "No model is downloaded" in html
    assert "No model is executed" in html
    assert "Provider/cloud routes are disabled by default" in html
    assert "docs/kora-studio/kora-studio-runtime-setup-guidance.md" in html
    assert "Runtime Status" in html
    assert "Installed locally" in html
    assert "Service reachability is a localhost-only check" in html
    assert "No model execution occurs during this check" in html
    assert "Installed model detection is not connected yet" in html
    assert "No private model directories are scanned" in html
    assert "No runtime model list command is called by default" in html
    assert "Download and run actions remain disabled" in html
    assert "Catalog vs Installed" in html
    assert "Catalog examples are not installed models" in html
    assert "Estimated local model tier" in html
    assert "KORA Boost Boundary" in html
    assert "KORA does not remove RAM/VRAM/unified-memory requirements" in html
    assert "Model/runtime integration: not connected" in html
    assert "Browser launch: available" in html
    assert "Ollama integration: not connected" in html
    assert "No production/API-cost/energy claims" in html
    assert "Report Viewer Placeholder" in html
    assert "Local No-Network Validation Report" in html
    assert "docs/kora-studio/fixtures/report-viewer-metadata.sample.json" in html
    assert "No arbitrary local file scan is performed" in html
    assert "No cloud upload is connected" in html
    assert "Export not connected yet" in html
    assert "Fixture summary only" in html
    assert "No new benchmark evidence is created" in html
    assert "provider calls enabled" not in html.lower()
    assert "production cost reduction" not in html.lower()
    assert "real api-cost reduction" not in html.lower()
    assert "energy reduction" not in html.lower()


def test_static_preview_html_content_is_safe_and_complete() -> None:
    html = render_studio_placeholder_html(get_studio_server_status())

    assert html.startswith("<!doctype html>")
    assert "KORA Studio" in html
    assert "Local Preview Scaffold" in html
    assert "Preview / Local-only" in html
    assert APPROVED_BOOST_MESSAGE in html
    assert TECHNICAL_EXPLANATION in html
    assert "deterministic-first local workflow exploration" in html
    assert "Launch / Local-only Status" in html
    assert "First-run order" in html
    assert "Server: local" in html
    assert "Provider calls: disabled" in html
    assert "Cloud sync: disabled" in html
    assert "Your Computer" in html
    assert "Model Capability Estimate" in html
    assert "Catalog vs Installed" in html
    assert "Catalog examples" in html
    assert "static_local_scaffold" in html
    assert "Download and execution are not connected yet" in html
    assert "Disabled Download/Run Actions" in html
    assert "Download action" in html
    assert "Run action" in html
    assert "Download not connected yet" in html
    assert "Run not connected yet" in html
    assert "Setup Guidance" in html
    assert "Disabled actions point to guidance, not to an active installer" in html
    assert "No model is downloaded" in html
    assert "No model is executed" in html
    assert "Runtime Status" in html
    assert "Installed model detection" in html
    assert "Runtime executable detection is local-only" in html
    assert "Service reachability is a localhost-only check" in html
    assert "No model execution occurs during this check" in html
    assert "Installed model detection is not connected yet" in html
    assert "No private model directories are scanned" in html
    assert "No runtime model list command is called by default" in html
    assert "Download and run actions remain disabled" in html
    assert "Catalog examples are not installed models" in html
    assert "Estimated local model tier" in html
    assert "Unknown until validated" in html or "depending on runtime" in html
    assert "KORA does not remove RAM/VRAM/unified-memory requirements" in html
    assert "Standard Mode vs KORA Boost" in html
    assert "Fixture/mock comparison only" in html
    assert "Baseline model calls" in html
    assert "KORA model calls" in html
    assert "Avoided model calls" in html
    assert "Deterministic routes" in html
    assert "Model escalations" in html
    assert "Validation passes" in html
    assert "No cost or energy claim is made" in html
    assert "Model/runtime integration: not connected" in html
    assert "Browser launch: available" in html
    assert "Ollama integration: not connected" in html
    assert "Endpoint Panel" in html
    assert "/health" in html
    assert "/status" in html
    assert "Execution Viewer" in html
    assert "Fixture/mock events only" in html
    assert "No real model execution" in html
    assert "No provider calls" in html
    assert "No model downloads" in html
    assert "Request received" in html
    assert "Deterministic route check" in html
    assert "Structured lookup" in html
    assert "Validation pass" in html
    assert "Model fallback skipped" in html
    assert "Final counters" in html
    assert "No runtime execution occurs on this page" in html
    assert "Report Viewer Placeholder" in html
    assert "Report metadata" in html
    assert "Export placeholder" in html
    assert "Boundary warnings" in html
    assert "No arbitrary local file scan is performed" in html
    assert "No cloud upload is connected" in html
    assert "Export not connected yet" in html
    assert "No new benchmark evidence is created" in html
    assert "Limitations Panel" in html
    assert "No production/API-cost/energy claims" in html
    assert "No full frontend yet" in html
    assert "Browser launch is local-only" in html
    assert "No provider calls" in html
    assert "No model/runtime integration yet" in html
    assert "No Ollama integration" in html
    assert "docs/kora-studio/README.md" in html
    assert "docs/kora-studio/fixtures/" in html
    assert "Local-only skeleton" in html
    assert "OPENAI_API_KEY" not in html
    assert "ANTHROPIC_API_KEY" not in html
    assert "provider calls enabled" not in html.lower()
    assert "download now" not in html.lower()
    assert "run now" not in html.lower()
    assert "install now" not in html.lower()
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

    ordered_sections = [
        "Launch / Local-only Status",
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
    positions = [html.index(f"<h2>{section}</h2>") for section in ordered_sections]
    assert positions == sorted(positions)


def test_runtime_setup_guidance_doc_is_claim_safe() -> None:
    doc = Path("docs/kora-studio/kora-studio-runtime-setup-guidance.md").read_text()

    assert "Setup guidance is informational in this scaffold" in doc
    assert "Disabled actions point to guidance, not to an active installer" in doc
    assert "No model is downloaded" in doc
    assert "No model is executed" in doc
    assert "No private model directories are scanned" in doc
    assert "No runtime model list command is called" in doc
    assert "No provider call is made" in doc
    assert "Provider and cloud routes are disabled by default" in doc

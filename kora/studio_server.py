"""Local-only KORA Studio server skeleton."""

from __future__ import annotations

import html
import json
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Callable

from kora.studio_execution_fixture import get_execution_viewer_fixture_summary, get_standard_vs_kora_status_fields
from kora.studio_harness_events import LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY, build_local_harness_events
from kora.studio_harness_requests import get_local_harness_request_summary, get_local_harness_requests
from kora.studio_model_catalog import MODEL_CATALOG_CLAIM_BOUNDARY, SETUP_GUIDANCE_PATH, recommend_catalog_models
from kora.studio_report_viewer import get_report_viewer_status_fields
from kora.studio_runtime_status import get_runtime_status, summarize_installed_models
from kora.studio_status import get_studio_status
from kora.studio_system_profile import estimate_model_capability, get_system_profile

DEFAULT_STUDIO_HOST = "127.0.0.1"
DEFAULT_STUDIO_PORT = 8765
ALLOWED_STUDIO_HOSTS = {"127.0.0.1", "localhost"}
SETUP_GUIDANCE_CLAIM_BOUNDARY = (
    "Setup guidance is informational in this scaffold. Disabled actions point to guidance, not to an active "
    "installer. No model is downloaded, no model is executed, no provider call is made, and cloud routes remain "
    "disabled by default."
)

StatusProvider = Callable[[], dict[str, Any]]
BrowserOpener = Callable[[str], bool]


def is_allowed_studio_host(host: str) -> bool:
    """Return whether a Studio server host is explicitly local-only."""

    return host in ALLOWED_STUDIO_HOSTS


def get_studio_server_status(host: str = DEFAULT_STUDIO_HOST, port: int = DEFAULT_STUDIO_PORT) -> dict[str, Any]:
    """Return static local server skeleton status without starting a server."""

    studio_status = get_studio_status()
    system_profile = get_system_profile(default_host=host, default_port=port)
    model_capability_estimate = estimate_model_capability(system_profile)
    runtime_status = get_runtime_status()
    installed_models_summary = summarize_installed_models(runtime_status)
    recommended_models = recommend_catalog_models(system_profile, model_capability_estimate, runtime_status)
    execution_viewer_fixture = get_execution_viewer_fixture_summary()
    standard_vs_kora_fixture = get_standard_vs_kora_status_fields()
    report_viewer_fixture = get_report_viewer_status_fields()
    local_harness_requests = get_local_harness_requests()
    local_harness_request_summary = get_local_harness_request_summary()
    local_harness_sample_run = build_local_harness_events(local_harness_requests[0])
    local_harness_counters = dict(local_harness_sample_run["counters_snapshot"])
    local_harness_status = {
        "status": "local_deterministic_harness_available",
        "event_source_status": "status_sample_only",
        "run_trigger_status": "not_connected",
        "sample_request_count": len(local_harness_requests),
        "sample_run_id": local_harness_sample_run["run_id"],
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "download_connected": False,
        "claim_boundary": LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY,
    }
    first_run_section_order = [
        "Launch/local-only status",
        "Your Computer",
        "Model Capability Estimate",
        "Runtime Status",
        "Catalog vs Installed",
        "Setup Guidance",
        "Disabled Download/Run Actions",
        "KORA Boost Boundary",
        "Local Harness Preview",
        "Execution Viewer",
        "Standard Mode vs KORA Boost",
        "Report Viewer Placeholder",
    ]
    launch_boundary = {
        "host": host,
        "port": port,
        "url": get_studio_url(host=host, port=port),
        "server": "local-only",
        "allowed_hosts": sorted(ALLOWED_STUDIO_HOSTS),
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "browser_launch_available": True,
        "api_key_required": False,
        "claim_boundary": (
            "The Studio preview is localhost-only by default. Provider calls and cloud sync are disabled, "
            "and no API key is required for the default local preview."
        ),
    }
    disabled_action_state = {
        "download_connected": False,
        "run_connected": False,
        "model_execution_connected": False,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "disabled_actions_route_to_guidance": True,
        "setup_guidance_url": SETUP_GUIDANCE_PATH,
        "claim_boundary": (
            "Download and run actions remain disabled until explicitly connected. Disabled actions point to "
            "informational setup guidance, not to an active installer or model runner."
        ),
    }
    v0_2_status = {
        "milestone": "v0.2",
        "status": "first_run_preview",
        "readiness": "local_preview_demo_ready",
        "description": "Local first-run setup preview for the AI Task Execution Router demo.",
        "first_run_section_order": list(first_run_section_order),
        "claim_boundary": (
            "v0.2 is a local preview/demo readiness milestone, not a production release. Execution data is "
            "fixture/mock only until live harness wiring is implemented."
        ),
    }
    studio_status_block = {
        "service": "kora-studio",
        "status": "preview",
        "implementation": "local_server_skeleton",
        "positioning": "local-first AI Task Execution Router workspace",
        "v0_1_readiness_status": "local_fixture_demo_ready",
        "v0_2_status": v0_2_status,
    }
    claim_boundaries = {
        "studio": v0_2_status["claim_boundary"],
        "launch": launch_boundary["claim_boundary"],
        "model_capability": str(model_capability_estimate.get("claim_boundary", "")),
        "model_catalog": MODEL_CATALOG_CLAIM_BOUNDARY,
        "runtime_setup_guidance": SETUP_GUIDANCE_CLAIM_BOUNDARY,
        "disabled_actions": disabled_action_state["claim_boundary"],
        "execution_viewer": str(execution_viewer_fixture.get("execution_viewer_claim_boundary", "")),
        "standard_vs_kora": str(standard_vs_kora_fixture.get("standard_vs_kora_claim_boundary", "")),
        "report_viewer": str(report_viewer_fixture.get("report_viewer_claim_boundary", "")),
        "local_harness": LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY,
    }
    return {
        "ok": True,
        "service": "kora-studio",
        "status": "preview",
        "implementation": "local_server_skeleton",
        "studio_status": studio_status_block,
        "launch_boundary": launch_boundary,
        "v0_2_status": v0_2_status,
        "v0_1_readiness_status": "local_fixture_demo_ready",
        "v0_1_demo_surfaces": list(first_run_section_order),
        "v0_1_claim_boundary": (
            "KORA Studio v0.1 is a local fixture-backed AI Task Execution Router demo scaffold. It is not "
            "production-ready, does not execute models, does not download models, does not call providers, "
            "and does not enable cloud sync."
        ),
        "server": "local-only",
        "host": host,
        "port": port,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "system_profile": system_profile.to_dict(),
        "model_capability_estimate": model_capability_estimate,
        "model_catalog_status": "static_local_scaffold",
        "recommended_models": recommended_models,
        "model_catalog_claim_boundary": MODEL_CATALOG_CLAIM_BOUNDARY,
        "runtime_status": runtime_status,
        "installed_models_summary": installed_models_summary,
        "catalog_runtime_distinction": (
            "Catalog examples are not the same as installed models. Installed model detection is not connected by "
            "default. Download and execution are not connected yet."
        ),
        "setup_guidance_status": "informational_scaffold",
        "setup_guidance_url": SETUP_GUIDANCE_PATH,
        "setup_guidance_claim_boundary": SETUP_GUIDANCE_CLAIM_BOUNDARY,
        "disabled_actions_route_to_guidance": True,
        "disabled_action_state": disabled_action_state,
        "local_harness_status": local_harness_status,
        "local_harness_request_summary": local_harness_request_summary,
        "local_harness_requests": local_harness_requests,
        "local_harness_sample_run": local_harness_sample_run,
        "local_harness_counters": local_harness_counters,
        "local_harness_claim_boundary": LOCAL_HARNESS_EVENT_CLAIM_BOUNDARY,
        **execution_viewer_fixture,
        **standard_vs_kora_fixture,
        **report_viewer_fixture,
        "claim_boundaries": claim_boundaries,
        "first_run_section_order": first_run_section_order,
        "browser_launch_available": True,
        "ollama_calls_enabled": False,
        "local_runtime_required": False,
        "no_server_side_provider_calls": True,
        "docs_path": studio_status["docs_path"],
        "fixtures_path": studio_status["fixtures_path"],
        "kora_boost_message": studio_status["kora_boost_message"],
        "kora_boost_technical_explanation": studio_status["kora_boost_technical_explanation"],
    }


def get_studio_health_payload() -> dict[str, Any]:
    """Return the /health response payload."""

    return {
        "ok": True,
        "service": "kora-studio",
        "status": "preview",
        "server": "local-only",
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "browser_launch_available": True,
    }


def get_studio_status_payload(host: str = DEFAULT_STUDIO_HOST, port: int = DEFAULT_STUDIO_PORT) -> dict[str, Any]:
    """Return the /status response payload."""

    return get_studio_server_status(host=host, port=port)


def get_studio_url(host: str = DEFAULT_STUDIO_HOST, port: int = DEFAULT_STUDIO_PORT) -> str:
    """Return the local KORA Studio URL."""

    return f"http://{host}:{port}/"


def open_studio_browser(url: str, browser_opener: BrowserOpener = webbrowser.open) -> bool:
    """Open the Studio URL with a mockable browser opener."""

    try:
        return bool(browser_opener(url))
    except Exception:
        return False


def render_studio_server_status_text(
    status: dict[str, Any],
    *,
    open_browser: bool = True,
    browser_opened: bool | None = None,
) -> str:
    """Render local server skeleton startup status for CLI output."""

    url = get_studio_url(str(status["host"]), int(status["port"]))
    lines = [
        "Launching KORA Studio...",
        "",
        "Local URL:",
        url,
        "",
        "Mode:",
        "Local-only",
        "Provider calls: disabled",
        "Cloud sync: disabled",
        "",
        "Press Ctrl+C to stop.",
    ]
    if open_browser and browser_opened is False:
        lines.extend(["", "Browser launch failed. Open this URL manually:", url])
    elif not open_browser:
        lines.extend(["", "Browser launch: disabled by --no-browser."])
    return "\n".join(lines) + "\n"


def render_studio_placeholder_html(status: dict[str, Any]) -> str:
    """Render the static KORA Studio preview page."""

    docs_path = html.escape(str(status["docs_path"]), quote=True)
    fixtures_path = html.escape(str(status["fixtures_path"]), quote=True)
    boost_message = html.escape(str(status["kora_boost_message"]), quote=True)
    boost_explanation = html.escape(str(status["kora_boost_technical_explanation"]), quote=True)
    system_profile = status.get("system_profile", {})
    model_capability = status.get("model_capability_estimate", {})
    os_name = html.escape(str(system_profile.get("os_name", "unknown")), quote=True)
    machine = html.escape(str(system_profile.get("machine", "unknown")), quote=True)
    memory = system_profile.get("total_memory_gb")
    memory_text = "unknown" if memory is None else f"{memory} GB"
    memory_text = html.escape(memory_text, quote=True)
    memory_status = html.escape(str(system_profile.get("memory_detection_status", "unknown")), quote=True)
    ollama_status = "detected" if system_profile.get("ollama_detected") is True else "not detected"
    llama_cpp_status = "detected" if system_profile.get("llama_cpp_detected") is True else "not detected"
    recommended_tier = html.escape(
        str(model_capability.get("recommended_local_chat_tier", "unknown")),
        quote=True,
    )
    physical_notes = html.escape(
        str(model_capability.get("physically_runnable_model_notes", "Unknown until validated.")),
        quote=True,
    )
    workflow_notes = html.escape(
        str(model_capability.get("larger_model_workflow_notes", "")),
        quote=True,
    )
    claim_boundary = html.escape(
        str(model_capability.get("claim_boundary", "Recommendations are estimates until validated on this machine.")),
        quote=True,
    )
    recommended_models = status.get("recommended_models", [])
    catalog_status = html.escape(str(status.get("model_catalog_status", "static_local_scaffold")), quote=True)
    catalog_boundary = html.escape(
        str(status.get("model_catalog_claim_boundary", MODEL_CATALOG_CLAIM_BOUNDARY)),
        quote=True,
    )
    runnable_models = [
        item
        for item in recommended_models
        if isinstance(item, dict) and item.get("candidate_type") == "physically_runnable_local_candidate"
    ]
    workflow_models = [
        item
        for item in recommended_models
        if isinstance(item, dict) and item.get("candidate_type") == "larger_model_workflow_candidate"
    ]
    unknown_models = [
        item for item in recommended_models if isinstance(item, dict) and item.get("candidate_type") == "unknown_needs_validation"
    ]
    local_candidate = runnable_models[0] if runnable_models else (unknown_models[0] if unknown_models else {})
    workflow_candidate = workflow_models[0] if workflow_models else {}
    local_candidate_name = html.escape(str(local_candidate.get("display_name", "Unknown until validated")), quote=True)
    local_candidate_note = html.escape(
        str(local_candidate.get("recommendation_note", "Model recommendations are estimates until validated on this machine.")),
        quote=True,
    )
    local_download_label = html.escape(str(local_candidate.get("download_action_label", "Download not connected yet")), quote=True)
    local_run_label = html.escape(str(local_candidate.get("run_action_label", "Run not connected yet")), quote=True)
    local_download_reason = html.escape(str(local_candidate.get("download_action_reason", "")), quote=True)
    local_run_reason = html.escape(str(local_candidate.get("run_action_reason", "")), quote=True)
    local_action_boundary = html.escape(
        str(
            local_candidate.get(
                "action_claim_boundary",
                "Model actions are disabled planning scaffolds. Catalog examples are not installed models.",
            )
        ),
        quote=True,
    )
    workflow_candidate_name = html.escape(str(workflow_candidate.get("display_name", "Larger workflow example")), quote=True)
    workflow_candidate_note = html.escape(
        str(
            workflow_candidate.get(
                "recommendation_note",
                "Larger-model workflows may become more practical when deterministic work avoids the model path.",
            )
        ),
        quote=True,
    )
    runtime_status = status.get("runtime_status", [])
    installed_summary = status.get("installed_models_summary", {})
    first_runtime = runtime_status[0] if isinstance(runtime_status, list) and runtime_status else {}
    runtime_name = html.escape(str(first_runtime.get("display_name", "Unknown runtime")), quote=True)
    runtime_detected = "detected" if first_runtime.get("executable_detected") is True else "not detected"
    service_status = html.escape(str(first_runtime.get("service_check_status", "not_checked")), quote=True)
    service_url = html.escape(str(first_runtime.get("service_url") or "not configured"), quote=True)
    service_boundary = html.escape(
        str(
            first_runtime.get(
                "service_probe_claim_boundary",
                "Service reachability is a localhost-only check. It does not execute models.",
            )
        ),
        quote=True,
    )
    installed_status = html.escape(str(installed_summary.get("detection_status", "not_checked")), quote=True)
    installed_enabled = (
        "enabled" if installed_summary.get("installed_model_detection_enabled") is True else "disabled"
    )
    installed_enabled = html.escape(installed_enabled, quote=True)
    installed_method = html.escape(str(installed_summary.get("installed_model_detection_method", "not_connected")), quote=True)
    installed_count = html.escape(str(installed_summary.get("installed_models_count", 0)), quote=True)
    installed_boundary = html.escape(
        str(
            installed_summary.get(
                "claim_boundary",
                "Installed model detection is local-only and disabled by default. Catalog examples are not installed models.",
            )
        ),
        quote=True,
    )
    setup_guidance_status = html.escape(str(status.get("setup_guidance_status", "informational_scaffold")), quote=True)
    setup_guidance_url = html.escape(str(status.get("setup_guidance_url", SETUP_GUIDANCE_PATH)), quote=True)
    setup_guidance_boundary = html.escape(
        str(status.get("setup_guidance_claim_boundary", SETUP_GUIDANCE_CLAIM_BOUNDARY)),
        quote=True,
    )
    execution_events = [
        item for item in status.get("execution_viewer_fixture_events", []) if isinstance(item, dict)
    ]
    execution_status = html.escape(str(status.get("execution_viewer_status", "fixture_mock_scaffold")), quote=True)
    execution_event_count = html.escape(str(status.get("execution_viewer_fixture_event_count", len(execution_events))), quote=True)
    execution_schema_count = html.escape(
        str(len(status.get("execution_viewer_event_schema_fields", []))),
        quote=True,
    )
    execution_boundary = html.escape(
        str(
            status.get(
                "execution_viewer_claim_boundary",
                "Execution Viewer events are local fixture/mock data and do not execute models.",
            )
        ),
        quote=True,
    )
    standard_vs_kora_status = html.escape(str(status.get("standard_vs_kora_comparison_status", "fixture_mock_scaffold")), quote=True)
    standard_vs_kora_boundary = html.escape(
        str(
            status.get(
                "standard_vs_kora_claim_boundary",
                "Standard Mode vs KORA Boost comparison data is local fixture/mock data.",
            )
        ),
        quote=True,
    )
    comparison = status.get("standard_vs_kora_comparison", {})
    comparison_modes = comparison.get("modes", []) if isinstance(comparison, dict) else []
    standard_mode = next(
        (item for item in comparison_modes if isinstance(item, dict) and item.get("mode") == "standard"),
        {},
    )
    kora_mode = next(
        (item for item in comparison_modes if isinstance(item, dict) and item.get("mode") == "kora_boost"),
        {},
    )
    standard_route_summary = html.escape(str(standard_mode.get("route_summary", "")), quote=True)
    kora_route_summary = html.escape(str(kora_mode.get("route_summary", "")), quote=True)
    metric_cards = [
        item for item in status.get("standard_vs_kora_metric_cards", []) if isinstance(item, dict)
    ]
    standard_vs_kora_metric_items = "".join(
        "<div class=\"card\">"
        f"<h3>{html.escape(str(card.get('label', 'Metric')), quote=True)}</h3>"
        f"<p class=\"status-value\">{html.escape(str(card.get('value', 0)), quote=True)}</p>"
        f"<p>{html.escape(str(card.get('claim_safety_note', 'Local fixture/mock comparison data only.')), quote=True)}</p>"
        "</div>"
        for card in metric_cards
    )
    execution_event_items = "".join(
        "<li>"
        f"{html.escape(str(event.get('stage_name', 'Unknown stage')), quote=True)} "
        f"({html.escape(str(event.get('route_class', 'unknown')), quote=True)} / "
        f"{html.escape(str(event.get('status', 'unknown')), quote=True)})"
        "</li>"
        for event in execution_events
    )
    report_viewer = status.get("report_viewer_placeholder", {})
    report_export = status.get("report_export_placeholder", {})
    report_viewer_status = html.escape(str(status.get("report_viewer_status", "fixture_metadata_placeholder")), quote=True)
    report_title = html.escape(str(report_viewer.get("report_title", "Local report fixture")), quote=True)
    report_fixture_path = html.escape(str(report_viewer.get("report_fixture_path", "")), quote=True)
    report_path_display = html.escape(str(report_viewer.get("report_path_display", "not loaded")), quote=True)
    report_boundary = html.escape(str(status.get("report_viewer_claim_boundary", "")), quote=True)
    report_export_status = html.escape(str(status.get("report_export_status", "placeholder_not_connected")), quote=True)
    report_export_label = html.escape(str(report_export.get("export_action_label", "Export not connected yet")), quote=True)
    report_export_reason = html.escape(str(report_export.get("export_action_reason", "")), quote=True)
    report_export_boundary = html.escape(str(status.get("report_export_claim_boundary", "")), quote=True)
    report_sections = "".join(
        f"<li>{html.escape(str(item), quote=True)}</li>"
        for item in report_viewer.get("sections", [])
    )
    report_warnings = "".join(
        f"<li>{html.escape(str(item), quote=True)}</li>"
        for item in report_viewer.get("boundary_warnings", [])
    )
    report_counters = report_viewer.get("counters", {}) if isinstance(report_viewer, dict) else {}
    report_counter_items = "".join(
        "<div class=\"card\">"
        f"<h3>{html.escape(str(key), quote=True)}</h3>"
        f"<p class=\"status-value\">{html.escape(str(value), quote=True)}</p>"
        "<p>Fixture metadata only.</p>"
        "</div>"
        for key, value in report_counters.items()
        if key in {"total_requests", "baseline_model_calls", "kora_model_calls", "avoided_model_calls"}
    )
    section_order_items = "".join(
        f"<li>{html.escape(str(item), quote=True)}</li>"
        for item in status.get(
            "first_run_section_order",
            [
                "Launch/local-only status",
                "Your Computer",
                "Model Capability Estimate",
                "Runtime Status",
                "Catalog vs Installed",
                "Setup Guidance",
                "Disabled Download/Run Actions",
                "KORA Boost Boundary",
                "Local Harness Preview",
                "Execution Viewer",
                "Standard Mode vs KORA Boost",
                "Report Viewer Placeholder",
            ],
        )
    )
    local_harness_status = status.get("local_harness_status", {})
    local_harness_requests = [
        item for item in status.get("local_harness_requests", []) if isinstance(item, dict)
    ]
    local_harness_sample_run = status.get("local_harness_sample_run", {})
    local_harness_counters = status.get("local_harness_counters", {})
    local_harness_status_text = html.escape(str(local_harness_status.get("status", "not_connected")), quote=True)
    local_harness_event_source = html.escape(str(local_harness_status.get("event_source_status", "not_connected")), quote=True)
    local_harness_run_trigger = html.escape(str(local_harness_status.get("run_trigger_status", "not_connected")), quote=True)
    local_harness_request_count = html.escape(
        str(local_harness_status.get("sample_request_count", len(local_harness_requests))),
        quote=True,
    )
    local_harness_boundary = html.escape(str(status.get("local_harness_claim_boundary", "")), quote=True)
    sample_request = local_harness_sample_run.get("request", {}) if isinstance(local_harness_sample_run, dict) else {}
    sample_request_id = html.escape(
        str(sample_request.get("request_id", local_harness_sample_run.get("request_id", "unknown"))),
        quote=True,
    )
    sample_input = html.escape(str(sample_request.get("input_text", "No sample request selected.")), quote=True)
    sample_family = html.escape(str(sample_request.get("task_family", "unknown")), quote=True)
    sample_route = html.escape(str(sample_request.get("expected_route_class", "unknown")), quote=True)
    sample_validation = html.escape(str(sample_request.get("expected_validation_result", "unknown")), quote=True)
    sample_model_needed = html.escape(str(sample_request.get("expected_model_needed", "unknown")), quote=True)
    local_harness_request_items = "".join(
        "<li>"
        f"{html.escape(str(request.get('request_id', 'unknown')), quote=True)} "
        f"({html.escape(str(request.get('task_family', 'unknown')), quote=True)} / "
        f"{html.escape(str(request.get('expected_route_class', 'unknown')), quote=True)})"
        "</li>"
        for request in local_harness_requests
    )
    local_harness_event_items = "".join(
        "<li>"
        f"{html.escape(str(event.get('stage_name', 'Unknown stage')), quote=True)} "
        f"({html.escape(str(event.get('route_class', 'unknown')), quote=True)} / "
        f"{html.escape(str(event.get('status', 'unknown')), quote=True)})"
        "</li>"
        for event in local_harness_sample_run.get("events", [])
        if isinstance(event, dict)
    )
    local_harness_counter_items = "".join(
        "<div class=\"card\">"
        f"<h3>{html.escape(str(key), quote=True)}</h3>"
        f"<p class=\"status-value\">{html.escape(str(local_harness_counters.get(key, 0)), quote=True)}</p>"
        "<p>Local deterministic harness output.</p>"
        "</div>"
        for key in [
            "total_requests",
            "baseline_model_calls",
            "kora_model_calls",
            "avoided_model_calls",
            "deterministic_routes",
            "model_escalations",
            "validation_pass_count",
        ]
    )

    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>KORA Studio</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #071014;
      --panel: #0d1b22;
      --panel-2: #10242d;
      --panel-3: #0a171d;
      --text: #edf7fa;
      --muted: #9fb3bd;
      --cyan: #32d1e6;
      --amber: #f0b44c;
      --green: #57d68d;
      --line: #24424d;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }}
    main {{
      width: min(1120px, calc(100% - 40px));
      margin: 0 auto;
      padding: 42px 0 34px;
    }}
    header {{
      border: 1px solid var(--line);
      background: linear-gradient(180deg, var(--panel), var(--panel-2));
      border-radius: 8px;
      padding: 28px;
    }}
    .topline {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 22px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      border: 1px solid var(--green);
      color: var(--green);
      border-radius: 999px;
      padding: 6px 12px;
      font-size: 13px;
      font-weight: 700;
      white-space: nowrap;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(34px, 6vw, 58px);
      letter-spacing: 0;
      line-height: 1.05;
    }}
    h2 {{
      margin: 0 0 14px;
      font-size: 20px;
      letter-spacing: 0;
    }}
    h3 {{
      margin: 0 0 6px;
      font-size: 15px;
      letter-spacing: 0;
    }}
    p {{ margin: 0; }}
    a {{ color: var(--cyan); }}
    code {{
      color: var(--amber);
      background: #071014;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 2px 6px;
      overflow-wrap: anywhere;
    }}
    .subtitle {{
      color: var(--muted);
      font-size: 17px;
      max-width: 760px;
    }}
    .boost {{
      color: var(--cyan);
      font-size: 24px;
      font-weight: 800;
      margin-top: 18px;
    }}
    .technical {{
      color: var(--muted);
      max-width: 820px;
      margin-top: 10px;
      font-size: 16px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-top: 18px;
    }}
    section, .card {{
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 8px;
      padding: 18px;
    }}
    .status-card {{
      min-height: 118px;
      background: var(--panel-3);
    }}
    .status-card p {{ color: var(--muted); }}
    .status-value {{
      color: var(--green);
      font-weight: 800;
      margin-top: 8px;
    }}
    .status-value.disabled {{ color: var(--amber); }}
    .workflow {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
    }}
    .step {{
      border: 1px solid var(--line);
      background: var(--panel-3);
      border-radius: 8px;
      padding: 14px;
      min-height: 130px;
    }}
    .step-number {{
      color: var(--cyan);
      font-size: 13px;
      font-weight: 800;
      margin-bottom: 8px;
    }}
    ul {{
      margin: 0;
      padding-left: 20px;
      color: var(--muted);
    }}
    li + li {{ margin-top: 8px; }}
    .section-stack {{
      display: grid;
      gap: 18px;
      margin-top: 18px;
    }}
    .footer {{
      color: var(--muted);
      border-top: 1px solid var(--line);
      margin-top: 22px;
      padding-top: 16px;
      font-size: 14px;
    }}
    @media (max-width: 760px) {{
      main {{ width: min(100% - 24px, 1120px); padding-top: 24px; }}
      header {{ padding: 20px; }}
      .topline {{ align-items: flex-start; flex-direction: column; }}
      .workflow {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <div class=\"topline\">
        <strong>Local Preview Scaffold</strong>
        <span class=\"badge\">Preview / Local-only</span>
      </div>
      <h1>KORA Studio</h1>
      <p class=\"subtitle\">A static AI Task Execution Router prototype for deterministic-first local workflow exploration. KORA Studio routes local AI workflows, not just local models.</p>
      <p class=\"boost\">{boost_message}</p>
      <p class=\"technical\">{boost_explanation}</p>
      <p class=\"technical\">Standard Mode sends every step to the model. KORA Boost routes deterministic and structured tasks to CPU/local fast paths first, so the model becomes one execution path, not the default path.</p>
    </header>

    <section aria-label=\"Launch Local-only Status\" style=\"margin-top: 18px;\">
      <h2>Launch / Local-only Status</h2>
      <div class=\"grid\">
        <div class=\"status-card card\"><h3>Server</h3><p class=\"status-value\">Server: local</p><p>Bound to the local Studio skeleton.</p></div>
        <div class=\"status-card card\"><h3>Provider Calls</h3><p class=\"status-value disabled\">Provider calls: disabled</p><p>No remote provider requests are made.</p></div>
        <div class=\"status-card card\"><h3>Cloud Sync</h3><p class=\"status-value disabled\">Cloud sync: disabled</p><p>No cloud sync is performed.</p></div>
        <div class=\"status-card card\"><h3>Model Runtime</h3><p class=\"status-value disabled\">Model/runtime integration: not connected</p><p>Future runtime work must distinguish physically runnable local models from workflow-usable models.</p></div>
        <div class=\"status-card card\"><h3>Browser Launch</h3><p class=\"status-value\">Browser launch: available</p><p>The CLI opens the local page by default; use <code>--no-browser</code> to suppress it.</p></div>
        <div class=\"status-card card\"><h3>Ollama</h3><p class=\"status-value disabled\">Ollama integration: not connected</p><p>No Ollama model calls happen here.</p></div>
      </div>
      <div class=\"card\" style=\"margin-top: 16px;\"><h3>First-run order</h3><ol>{section_order_items}</ol></div>
    </section>

    <div class=\"section-stack\">
      <section>
        <h2>Your Computer</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>System Profile</h3><p>OS: {os_name}</p><p>Machine: {machine}</p><p>Memory: {memory_text} ({memory_status})</p></div>
          <div class=\"card\"><h3>Local Runtime Detection</h3><p>Ollama: {ollama_status}</p><p>llama.cpp: {llama_cpp_status}</p><p>No runtime APIs are called by this preview.</p></div>
        </div>
      </section>

      <section>
        <h2>Model Capability Estimate</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Estimated local model tier</h3><p>{recommended_tier}</p><p>{physical_notes}</p></div>
          <div class=\"card\"><h3>Workflow feasibility</h3><p>{workflow_notes}</p><p>{claim_boundary}</p></div>
        </div>
      </section>

      <section>
        <h2>Runtime Status</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Runtime detected</h3><p>{runtime_name}: {runtime_detected}</p><p>Runtime executable detection is local-only.</p></div>
          <div class=\"card\"><h3>Service reachability</h3><p>Runtime reachable: {service_status}</p><p>Service URL: {service_url}</p><p>Service reachability is a localhost-only check.</p><p>No model execution occurs during this check.</p><p>{service_boundary}</p></div>
          <div class=\"card\"><h3>Installed model detection</h3><p>Detection enabled: {installed_enabled}</p><p>Detection method: {installed_method}</p><p>Installed model detection is not connected yet.</p></div>
        </div>
      </section>

      <section>
        <h2>Catalog vs Installed</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Catalog examples</h3><p>{catalog_status}</p><p>Catalog examples are curated examples, not installed models.</p></div>
          <div class=\"card\"><h3>Physically runnable local candidates</h3><p>{local_candidate_name}</p><p>{local_candidate_note}</p></div>
          <div class=\"card\"><h3>Larger-model workflow candidates</h3><p>{workflow_candidate_name}</p><p>{workflow_candidate_note}</p></div>
          <div class=\"card\"><h3>Installed locally</h3><p>Installed model detection: {installed_status}</p><p>Installed count: {installed_count}</p><p>No private model directories are scanned.</p><p>No runtime model list command is called by default.</p></div>
          <div class=\"card\"><h3>Catalog boundary</h3><p>{catalog_boundary}</p><p>{installed_boundary}</p></div>
        </div>
      </section>

      <section>
        <h2>Setup Guidance</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Guidance status</h3><p>{setup_guidance_status}</p><p>Disabled actions point to guidance, not to an active installer.</p><p><code>{setup_guidance_url}</code></p></div>
          <div class=\"card\"><h3>Setup boundary</h3><p>No model is downloaded.</p><p>No model is executed.</p><p>No provider call is made.</p><p>Provider/cloud routes are disabled by default.</p></div>
          <div class=\"card\"><h3>Runtime readiness</h3><p>Runtime executable detection is not model execution readiness.</p><p>Catalog examples are not installed models.</p><p>{setup_guidance_boundary}</p></div>
        </div>
      </section>

      <section>
        <h2>Disabled Download/Run Actions</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Download action</h3><p><span class=\"badge\">{local_download_label}</span></p><p>{local_download_reason}</p><p>Download remains disabled until explicitly connected.</p></div>
          <div class=\"card\"><h3>Run action</h3><p><span class=\"badge\">{local_run_label}</span></p><p>{local_run_reason}</p><p>Run remains disabled until explicitly connected.</p></div>
          <div class=\"card\"><h3>Action boundary</h3><p>Download and run actions remain disabled.</p><p>{local_action_boundary}</p><p>No install, download, or model execution action is active in this preview.</p></div>
        </div>
      </section>

      <section>
        <h2>KORA Boost Boundary</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Standard Mode</h3><p>Standard Mode sends every step to the model.</p><p>In this preview, model execution is not connected.</p></div>
          <div class=\"card\"><h3>KORA Boost</h3><p>KORA Boost routes deterministic and structured tasks to CPU/local fast paths first.</p><p>Larger-model workflows may become more practical when deterministic work avoids the model path.</p></div>
          <div class=\"card\"><h3>Boundary</h3><p>KORA does not remove model memory requirements.</p><p>Provider/cloud routes are disabled by default.</p></div>
        </div>
      </section>

      <section>
        <h2>Local Harness Preview</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Harness status</h3><p>{local_harness_status_text}</p><p>Event source: {local_harness_event_source}</p><p>Run trigger: {local_harness_run_trigger}</p><p>Available sample requests: {local_harness_request_count}</p></div>
          <div class=\"card\"><h3>Sample request</h3><p><code>{sample_request_id}</code></p><p>{sample_input}</p><p>Family: {sample_family}</p><p>Expected route: {sample_route}</p><p>Validation: {sample_validation}</p><p>Model needed: {sample_model_needed}</p></div>
          <div class=\"card\"><h3>Boundary</h3><p>{local_harness_boundary}</p><p>Model-needed boundaries do not execute models in this milestone.</p><p>No provider call, download, or cloud sync is connected.</p></div>
        </div>
        <div class=\"grid\" style=\"margin-top: 16px;\">
          <div class=\"card\"><h3>Available local deterministic sample requests</h3><ul>{local_harness_request_items}</ul></div>
          <div class=\"card\"><h3>Harness event stages</h3><ul>{local_harness_event_items}</ul></div>
        </div>
        <div class=\"grid\">{local_harness_counter_items}</div>
      </section>

      <section>
        <h2>Execution Viewer</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Fixture status</h3><p>{execution_status}</p><p>Fixture/mock events only.</p><p>No real model execution.</p><p>No provider calls.</p><p>No model downloads.</p></div>
          <div class=\"card\"><h3>Event schema</h3><p>Schema fields: {execution_schema_count}</p><p>Fixture events: {execution_event_count}</p><p>{execution_boundary}</p></div>
          <div class=\"card\"><h3>Fixture stages</h3><ul>{execution_event_items}</ul></div>
        </div>
        <div class=\"workflow\" style=\"margin-top: 16px;\">
          <div class=\"step\"><p class=\"step-number\">01</p><h3>Request received</h3><p>Local fixture request is received by the Execution Viewer scaffold.</p></div>
          <div class=\"step\"><p class=\"step-number\">02</p><h3>Deterministic route check</h3><p>Fixture route selection checks deterministic code before the model path.</p></div>
          <div class=\"step\"><p class=\"step-number\">03</p><h3>Structured lookup and validation pass</h3><p>Fixture structured lookup succeeds and validation passes.</p></div>
          <div class=\"step\"><p class=\"step-number\">04</p><h3>Model fallback skipped / Final counters</h3><p>Fixture counters show the model path skipped after validation. No runtime execution occurs on this page.</p></div>
        </div>
      </section>

      <section>
        <h2>Standard Mode vs KORA Boost</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Comparison status</h3><p>{standard_vs_kora_status}</p><p>Fixture/mock comparison only.</p><p>No model execution occurs.</p></div>
          <div class=\"card\"><h3>Standard Mode</h3><p>{standard_route_summary}</p><p>Model call counted in fixture baseline: 1</p></div>
          <div class=\"card\"><h3>KORA Boost</h3><p>{kora_route_summary}</p><p>Model call counted in fixture KORA path: 0</p></div>
          <div class=\"card\"><h3>Claim boundary</h3><p>{standard_vs_kora_boundary}</p><p>No cost or energy claim is made.</p></div>
        </div>
        <div class=\"grid\">{standard_vs_kora_metric_items}</div>
      </section>

      <section>
        <h2>Report Viewer Placeholder</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3>Report metadata</h3><p>{report_viewer_status}</p><p>{report_title}</p><p><code>{report_fixture_path}</code></p><p>Displayed path: <code>{report_path_display}</code></p></div>
          <div class=\"card\"><h3>Local-only boundary</h3><p>No arbitrary local file scan is performed.</p><p>No cloud upload is connected.</p><p>No provider calls are made.</p><p>Fixture summary only.</p></div>
          <div class=\"card\"><h3>Export placeholder</h3><p>{report_export_status}</p><p><span class=\"badge\">{report_export_label}</span></p><p>{report_export_reason}</p><p>{report_export_boundary}</p></div>
          <div class=\"card\"><h3>Claim boundary</h3><p>{report_boundary}</p><p>No new benchmark evidence is created.</p></div>
        </div>
        <div class=\"grid\">
          <div class=\"card\"><h3>Report sections</h3><ul>{report_sections}</ul></div>
          <div class=\"card\"><h3>Boundary warnings</h3><ul>{report_warnings}</ul></div>
        </div>
        <div class=\"grid\">{report_counter_items}</div>
      </section>

      <section>
        <h2>Endpoint Panel</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3><a href=\"/health\">/health</a></h3><p>Returns local health status JSON for the preview server.</p></div>
          <div class=\"card\"><h3><a href=\"/status\">/status</a></h3><p>Returns local preview status, system profile, model capability estimate, KORA Boost copy, docs paths, and fixture paths.</p></div>
        </div>
      </section>

      <section>
        <h2>Limitations Panel</h2>
        <ul>
          <li>No full frontend yet</li>
          <li>No provider calls</li>
          <li>No model/runtime integration yet</li>
          <li>Browser launch is local-only and can be disabled with <code>--no-browser</code></li>
          <li>No Ollama integration</li>
          <li>No production/API-cost/energy claims</li>
          <li>No claim that KORA removes model memory requirements</li>
          <li>External/provider/distributed routes disabled by default</li>
        </ul>
      </section>

      <section>
        <h2>Local References</h2>
        <ul>
          <li><code>{docs_path}</code></li>
          <li><code>{fixtures_path}</code></li>
        </ul>
      </section>
    </div>

    <p class=\"footer\">Local-only skeleton. Claim-safe AI Task Execution Router preview; KORA does not make large models smaller or remove memory requirements.</p>
  </main>
</body>
</html>
"""


def create_studio_request_handler(status_provider: StatusProvider | None = None) -> type[BaseHTTPRequestHandler]:
    """Create a request handler class for the local Studio preview server."""

    provider = status_provider or get_studio_server_status

    class StudioRequestHandler(BaseHTTPRequestHandler):
        server_version = "KORAStudioPreview/0.1"

        def log_message(self, format: str, *args: object) -> None:  # noqa: A002
            return

        def _write_json(self, payload: dict[str, Any], status_code: int = 200) -> None:
            body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
            self.send_response(status_code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _write_html(self, html: str, status_code: int = 200) -> None:
            body = html.encode("utf-8")
            self.send_response(status_code)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:
            status = provider()
            if self.path == "/health":
                self._write_json(get_studio_health_payload())
                return
            if self.path == "/status":
                self._write_json(status)
                return
            if self.path == "/":
                self._write_html(render_studio_placeholder_html(status))
                return
            self._write_json({"ok": False, "error": "not_found"}, status_code=404)

        def do_POST(self) -> None:
            self._write_json({"ok": False, "error": "post_not_supported"}, status_code=405)

    return StudioRequestHandler


def run_studio_server(
    host: str = DEFAULT_STUDIO_HOST,
    port: int = DEFAULT_STUDIO_PORT,
    *,
    open_browser: bool = True,
    browser_opener: BrowserOpener = webbrowser.open,
) -> None:
    """Run the local-only KORA Studio preview server until interrupted."""

    if not is_allowed_studio_host(host):
        raise ValueError("KORA Studio server is local-only; use 127.0.0.1 or localhost.")

    status = get_studio_server_status(host=host, port=port)
    handler = create_studio_request_handler(lambda: get_studio_server_status(host=host, port=port))
    server = ThreadingHTTPServer((host, port), handler)
    browser_opened = open_studio_browser(get_studio_url(host, port), browser_opener) if open_browser else None
    try:
        print(
            render_studio_server_status_text(
                status,
                open_browser=open_browser,
                browser_opened=browser_opened,
            ),
            end="",
            flush=True,
        )
        server.serve_forever()
    except KeyboardInterrupt:
        print("KORA Studio local server stopped.", flush=True)
    finally:
        server.server_close()

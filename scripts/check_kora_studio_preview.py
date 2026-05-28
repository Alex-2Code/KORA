#!/usr/bin/env python3
"""Local-only smoke check for the KORA Studio preview server.

This helper checks an already-running localhost Studio preview. It does not
start services, call providers, download models, execute models, or scan local
model directories.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Callable
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import urlopen

DEFAULT_BASE_URL = "http://127.0.0.1:8765"
UrlOpen = Callable[..., Any]


class SmokeCheckError(RuntimeError):
    """Raised when the local preview smoke check fails."""


def _normalise_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


def _require_local_url(base_url: str) -> None:
    parsed = urlparse(base_url)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost"}:
        raise SmokeCheckError("KORA Studio smoke check only accepts http://127.0.0.1 or http://localhost URLs.")


def _read_url(base_url: str, path: str, *, timeout: float, opener: UrlOpen = urlopen) -> tuple[int, str, str]:
    url = f"{_normalise_base_url(base_url)}{path}"
    try:
        with opener(url, timeout=timeout) as response:
            status = int(getattr(response, "status", 0))
            content_type = str(response.headers.get("Content-Type", ""))
            body = response.read().decode("utf-8")
    except URLError as exc:
        raise SmokeCheckError(f"Unable to reach {url}: {exc}") from exc
    except OSError as exc:
        raise SmokeCheckError(f"Unable to read {url}: {exc}") from exc
    return status, content_type, body


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SmokeCheckError(message)


def check_preview(base_url: str = DEFAULT_BASE_URL, *, timeout: float = 2.0, opener: UrlOpen = urlopen) -> list[str]:
    """Check local KORA Studio preview endpoints and return human-readable results."""

    base_url = _normalise_base_url(base_url)
    _require_local_url(base_url)

    results: list[str] = []

    health_status, health_content_type, health_body = _read_url(base_url, "/health", timeout=timeout, opener=opener)
    _require(health_status == 200, f"/health returned HTTP {health_status}")
    _require("application/json" in health_content_type, "/health did not return JSON")
    health = json.loads(health_body)
    _require(health.get("server") == "local-only", "/health does not report local-only server mode")
    _require(health.get("provider_calls_enabled") is False, "/health does not report provider calls disabled")
    _require(health.get("cloud_sync_enabled") is False, "/health does not report cloud sync disabled")
    results.append("/health ok")

    status_code, status_content_type, status_body = _read_url(base_url, "/status", timeout=timeout, opener=opener)
    _require(status_code == 200, f"/status returned HTTP {status_code}")
    _require("application/json" in status_content_type, "/status did not return JSON")
    status = json.loads(status_body)
    required_status_fields = {
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
        "standard_vs_kora_comparison_status",
        "report_viewer_status",
        "provider_calls_enabled",
        "cloud_sync_enabled",
        "claim_boundaries",
    }
    missing_fields = sorted(required_status_fields - set(status))
    _require(not missing_fields, f"/status missing fields: {', '.join(missing_fields)}")
    _require(status.get("provider_calls_enabled") is False, "/status does not report provider calls disabled")
    _require(status.get("cloud_sync_enabled") is False, "/status does not report cloud sync disabled")
    _require(status["disabled_action_state"].get("download_connected") is False, "/status reports download connected")
    _require(status["disabled_action_state"].get("run_connected") is False, "/status reports run connected")
    _require(
        status["disabled_action_state"].get("model_execution_connected") is False,
        "/status reports model execution connected",
    )
    _require(status.get("execution_viewer_status") == "fixture_mock_scaffold", "/status execution viewer is not fixture")
    _require(
        status.get("standard_vs_kora_comparison_status") == "fixture_mock_scaffold",
        "/status comparison is not fixture",
    )
    _require(
        status.get("report_viewer_status") == "fixture_metadata_placeholder",
        "/status report viewer is not placeholder",
    )
    results.append("/status ok")

    root_status, root_content_type, root_body = _read_url(base_url, "/", timeout=timeout, opener=opener)
    _require(root_status == 200, f"/ returned HTTP {root_status}")
    _require("text/html" in root_content_type, "/ did not return HTML")
    required_html_markers = [
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
        "Provider calls: disabled",
        "Cloud sync: disabled",
        "No model is downloaded",
        "No model is executed",
    ]
    missing_markers = [marker for marker in required_html_markers if marker not in root_body]
    _require(not missing_markers, f"/ missing markers: {', '.join(missing_markers)}")
    _require("Download now" not in root_body, "/ includes an active download phrase")
    _require("Run now" not in root_body, "/ includes an active run phrase")
    _require("Install now" not in root_body, "/ includes an active install phrase")
    results.append("/ ok")

    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Smoke-check an already-running local KORA Studio preview.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Local Studio base URL.")
    parser.add_argument("--timeout", type=float, default=2.0, help="Per-request timeout in seconds.")
    args = parser.parse_args(argv)

    try:
        results = check_preview(args.base_url, timeout=args.timeout)
    except SmokeCheckError as exc:
        print(f"KORA Studio preview smoke check failed: {exc}", file=sys.stderr)
        return 1

    print("KORA Studio preview smoke check passed.")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

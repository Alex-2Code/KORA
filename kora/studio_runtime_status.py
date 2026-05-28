"""Local-only KORA Studio runtime availability scaffold."""

from __future__ import annotations

import shutil
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable
from copy import deepcopy
from typing import Any

ExecutableDetector = Callable[[str], str | None]
ServiceProbe = Callable[[str, int], dict[str, Any]]

DEFAULT_SERVICE_PROBE_TIMEOUT_MS = 250
LOCAL_SERVICE_HOSTS = {"127.0.0.1", "localhost"}

RUNTIME_STATUS_CLAIM_BOUNDARY = (
    "Runtime status is local-only and fail-closed. Catalog examples are not the same as installed models. "
    "Download and execution are not connected yet."
)
SERVICE_PROBE_CLAIM_BOUNDARY = (
    "Service reachability is a localhost-only check. It does not execute models, list models, download models, "
    "or prove runtime execution readiness."
)

RUNTIME_CANDIDATES = [
    {
        "runtime_id": "ollama",
        "display_name": "Ollama",
        "commands": ["ollama"],
        "detection_method": "local_executable_path",
        "service_url": "http://127.0.0.1:11434/",
        "service_probe_method": "localhost_http_root_probe",
    },
    {
        "runtime_id": "llama_cpp",
        "display_name": "llama.cpp",
        "commands": ["llama-cli", "llama"],
        "detection_method": "local_executable_path",
        "service_url": None,
        "service_probe_method": "not_configured",
    },
    {
        "runtime_id": "mock",
        "display_name": "Mock runtime",
        "commands": [],
        "detection_method": "built_in_mock_placeholder",
        "service_url": None,
        "service_probe_method": "mock_local_probe",
    },
]


def probe_local_http_service(
    service_url: str,
    timeout_ms: int = DEFAULT_SERVICE_PROBE_TIMEOUT_MS,
    *,
    opener: Callable[..., Any] = urllib.request.urlopen,
) -> dict[str, Any]:
    """Probe a localhost HTTP service without model execution or private model enumeration."""

    parsed = urllib.parse.urlparse(service_url)
    if parsed.scheme != "http" or parsed.hostname not in LOCAL_SERVICE_HOSTS:
        return {
            "service_reachable": False,
            "service_check_status": "blocked_non_localhost",
            "service_probe_error": "only localhost HTTP service probes are allowed",
        }

    request = urllib.request.Request(service_url, method="GET")
    try:
        with opener(request, timeout=max(timeout_ms, 1) / 1000) as response:
            status_code = getattr(response, "status", 200)
        return {
            "service_reachable": int(status_code) < 500,
            "service_check_status": "reachable" if int(status_code) < 500 else "unreachable",
            "service_probe_error": None,
        }
    except (OSError, TimeoutError, urllib.error.URLError) as exc:
        return {
            "service_reachable": False,
            "service_check_status": "unreachable",
            "service_probe_error": exc.__class__.__name__,
        }
    except Exception as exc:  # pragma: no cover - defensive fail-closed guard for custom openers.
        return {
            "service_reachable": False,
            "service_check_status": "probe_error",
            "service_probe_error": exc.__class__.__name__,
        }


def _service_probe_status(
    candidate: dict[str, Any],
    *,
    probe_services: bool,
    service_probe: ServiceProbe | None,
    timeout_ms: int,
) -> dict[str, Any]:
    base = {
        "service_reachable": False,
        "service_check_status": "not_checked",
        "service_url": candidate.get("service_url"),
        "service_probe_method": candidate.get("service_probe_method", "not_configured"),
        "service_probe_timeout_ms": timeout_ms,
        "service_probe_error": None,
        "service_probe_claim_boundary": SERVICE_PROBE_CLAIM_BOUNDARY,
    }
    if not probe_services:
        return base
    if candidate["runtime_id"] == "mock":
        return {
            **base,
            "service_reachable": True,
            "service_check_status": "reachable",
            "service_probe_error": None,
        }
    service_url = candidate.get("service_url")
    if not isinstance(service_url, str) or not service_url:
        return {
            **base,
            "service_check_status": "not_configured",
            "service_probe_error": "no_safe_local_endpoint_configured",
        }

    probe = service_probe or probe_local_http_service
    try:
        result = probe(service_url, timeout_ms)
    except Exception as exc:
        return {
            **base,
            "service_check_status": "probe_error",
            "service_probe_error": exc.__class__.__name__,
        }

    return {
        **base,
        "service_reachable": bool(result.get("service_reachable")),
        "service_check_status": str(result.get("service_check_status", "unreachable")),
        "service_probe_error": result.get("service_probe_error"),
    }


def get_runtime_status(
    which: ExecutableDetector = shutil.which,
    *,
    probe_services: bool = False,
    service_probe: ServiceProbe | None = None,
    service_probe_timeout_ms: int = DEFAULT_SERVICE_PROBE_TIMEOUT_MS,
) -> list[dict[str, Any]]:
    """Return runtime status without starting services or executing models."""

    statuses: list[dict[str, Any]] = []
    for candidate in RUNTIME_CANDIDATES:
        commands = candidate["commands"]
        executable_path = None
        if commands:
            executable_path = next((which(command) for command in commands if which(command)), None)
        executable_detected = executable_path is not None or candidate["runtime_id"] == "mock"
        service_status = _service_probe_status(
            candidate,
            probe_services=probe_services,
            service_probe=service_probe,
            timeout_ms=service_probe_timeout_ms,
        )
        statuses.append(
            {
                "runtime_id": candidate["runtime_id"],
                "display_name": candidate["display_name"],
                "executable_detected": executable_detected,
                "executable_path": executable_path,
                **service_status,
                "installed_models_detected": False,
                "installed_models": [],
                "installed_model_detection_status": "not_checked",
                "detection_method": candidate["detection_method"],
                "detection_status": "detected" if executable_detected else "not_detected",
                "claim_boundary": RUNTIME_STATUS_CLAIM_BOUNDARY,
            }
        )
    return statuses


def summarize_installed_models(runtime_status: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize installed model detection without claiming unavailable data."""

    installed_models: list[dict[str, Any]] = []
    for runtime in runtime_status:
        models = runtime.get("installed_models", [])
        if isinstance(models, list):
            for model in models:
                if isinstance(model, dict):
                    installed_models.append(deepcopy(model))

    return {
        "installed_models_detected": bool(installed_models),
        "installed_models": installed_models,
        "installed_model_count": len(installed_models),
        "detection_status": "not_checked" if not installed_models else "detected",
        "installed_model_detection_status": "not_checked" if not installed_models else "detected",
        "claim_boundary": (
            "Installed model detection is local-only and may be unknown. Catalog examples are not installed models."
        ),
    }


def runtime_status_by_id(runtime_status: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Index runtime status by runtime id."""

    return {
        str(item["runtime_id"]): item
        for item in runtime_status
        if isinstance(item, dict) and "runtime_id" in item
    }

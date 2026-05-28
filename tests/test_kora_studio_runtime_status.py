from __future__ import annotations

from kora.studio_runtime_status import (
    RUNTIME_STATUS_CLAIM_BOUNDARY,
    get_runtime_status,
    probe_local_http_service,
    summarize_installed_models,
)


def test_runtime_status_returns_safe_default_fields() -> None:
    statuses = get_runtime_status(which=lambda command: None)

    assert {item["runtime_id"] for item in statuses} == {"ollama", "llama_cpp", "mock"}
    for status in statuses:
        assert "runtime_id" in status
        assert "display_name" in status
        assert status["service_reachable"] is False
        assert status["service_check_status"] == "not_checked"
        assert "service_url" in status
        assert status["service_probe_timeout_ms"] <= 500
        assert "localhost-only check" in status["service_probe_claim_boundary"]
        assert status["installed_models_detected"] is False
        assert status["installed_models"] == []
        assert status["installed_model_detection_status"] == "not_checked"
        assert status["claim_boundary"] == RUNTIME_STATUS_CLAIM_BOUNDARY


def test_runtime_executable_detection_can_be_mocked() -> None:
    def fake_which(command: str) -> str | None:
        return f"/mock/bin/{command}" if command == "ollama" else None

    statuses = get_runtime_status(which=fake_which)
    by_id = {item["runtime_id"]: item for item in statuses}

    assert by_id["ollama"]["executable_detected"] is True
    assert by_id["ollama"]["executable_path"] == "/mock/bin/ollama"
    assert by_id["ollama"]["service_reachable"] is False
    assert by_id["llama_cpp"]["executable_detected"] is False
    assert by_id["mock"]["executable_detected"] is True


def test_local_http_probe_blocks_non_localhost_urls() -> None:
    result = probe_local_http_service("https://example.com", opener=lambda request, timeout: None)

    assert result["service_reachable"] is False
    assert result["service_check_status"] == "blocked_non_localhost"
    assert "localhost" in result["service_probe_error"]


def test_runtime_service_probe_is_mockable_and_timeout_bound() -> None:
    seen: list[tuple[str, int]] = []

    def fake_probe(service_url: str, timeout_ms: int) -> dict:
        seen.append((service_url, timeout_ms))
        return {
            "service_reachable": True,
            "service_check_status": "reachable",
            "service_probe_error": None,
        }

    statuses = get_runtime_status(
        which=lambda command: "/mock/bin/ollama" if command == "ollama" else None,
        probe_services=True,
        service_probe=fake_probe,
        service_probe_timeout_ms=200,
    )
    by_id = {item["runtime_id"]: item for item in statuses}

    assert seen == [("http://127.0.0.1:11434/", 200)]
    assert by_id["ollama"]["service_reachable"] is True
    assert by_id["ollama"]["service_check_status"] == "reachable"
    assert by_id["ollama"]["service_probe_timeout_ms"] == 200
    assert by_id["mock"]["service_reachable"] is True
    assert by_id["mock"]["service_check_status"] == "reachable"
    assert by_id["llama_cpp"]["service_reachable"] is False
    assert by_id["llama_cpp"]["service_check_status"] == "not_configured"
    assert by_id["llama_cpp"]["service_probe_error"] == "no_safe_local_endpoint_configured"


def test_runtime_service_probe_failure_is_fail_closed() -> None:
    def failing_probe(service_url: str, timeout_ms: int) -> dict:
        raise TimeoutError("probe timed out")

    statuses = get_runtime_status(
        which=lambda command: "/mock/bin/ollama" if command == "ollama" else None,
        probe_services=True,
        service_probe=failing_probe,
    )
    by_id = {item["runtime_id"]: item for item in statuses}

    assert by_id["ollama"]["service_reachable"] is False
    assert by_id["ollama"]["service_check_status"] == "probe_error"
    assert by_id["ollama"]["service_probe_error"] == "TimeoutError"
    assert by_id["ollama"]["installed_models_detected"] is False
    assert by_id["ollama"]["installed_models"] == []


def test_installed_model_summary_does_not_claim_models_by_default() -> None:
    summary = summarize_installed_models(get_runtime_status(which=lambda command: None))

    assert summary["installed_models_detected"] is False
    assert summary["installed_models"] == []
    assert summary["installed_model_count"] == 0
    assert summary["detection_status"] == "not_checked"
    assert summary["installed_model_detection_status"] == "not_checked"
    assert "Catalog examples are not installed models" in summary["claim_boundary"]

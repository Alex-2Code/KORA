from __future__ import annotations

from kora.studio_system_profile import (
    StudioSystemProfile,
    detect_runtime_candidates,
    estimate_model_capability,
    get_system_profile,
)


def test_system_profile_returns_safe_default_fields() -> None:
    profile = get_system_profile(which=lambda command: None, total_memory_gb=None)
    data = profile.to_dict()

    assert data["os_name"]
    assert data["os_version"]
    assert data["machine"]
    assert data["processor"]
    assert data["python_version"]
    assert data["total_memory_gb"] is None
    assert data["memory_detection_status"] == "unknown"
    assert data["ollama_detected"] is False
    assert data["llama_cpp_detected"] is False
    assert data["default_host"] == "127.0.0.1"
    assert data["default_port"] == 8765
    assert data["provider_calls_enabled"] is False
    assert data["cloud_sync_enabled"] is False
    assert data["profile_status"] in {"detected", "detected_with_unknowns"}


def test_executable_detection_can_be_mocked() -> None:
    def fake_which(command: str) -> str | None:
        return f"/mock/bin/{command}" if command == "ollama" else None

    candidates, ollama_detected, llama_cpp_detected = detect_runtime_candidates(fake_which)

    assert ollama_detected is True
    assert llama_cpp_detected is False
    assert candidates[0]["name"] == "ollama"
    assert candidates[0]["detected"] is True
    assert candidates[0]["command"] == "ollama"
    assert candidates[1]["name"] == "llama.cpp"
    assert candidates[1]["detected"] is False


def test_model_capability_unknown_memory_fallback() -> None:
    profile = get_system_profile(which=lambda command: None, total_memory_gb=None)
    estimate = estimate_model_capability(profile)

    assert estimate["recommended_local_chat_tier"] == "unknown"
    assert estimate["recommendation_status"] == "unknown"
    assert estimate["confidence"] == "low"
    assert "estimates until validated" in estimate["claim_boundary"]
    assert "does not remove RAM/VRAM/unified-memory requirements" in estimate["claim_boundary"]


def test_model_capability_memory_tier_heuristic() -> None:
    cases = [
        (4, "small/mini local models only"),
        (8, "3B-7B quantized tier"),
        (16, "7B-8B quantized tier"),
        (32, "7B-13B quantized tier"),
        (64, "13B+ may be possible depending on runtime and quantization"),
    ]

    for memory_gb, expected_tier in cases:
        profile = get_system_profile(which=lambda command: None, total_memory_gb=memory_gb)
        estimate = estimate_model_capability(profile)
        assert estimate["recommended_local_chat_tier"] == expected_tier
        assert estimate["recommendation_status"] == "estimated"
        assert estimate["confidence"] == "medium"
        assert "validat" in estimate["physically_runnable_model_notes"] or "depending on runtime" in estimate[
            "physically_runnable_model_notes"
        ]


def test_model_capability_output_avoids_forbidden_claims() -> None:
    profile = StudioSystemProfile(
        os_name="Darwin",
        os_version="unknown",
        machine="arm64",
        processor="unknown",
        python_version="3.13",
        total_memory_gb=64,
        memory_detection_status="detected",
        runtime_candidates=[],
        ollama_detected=False,
        llama_cpp_detected=False,
        local_storage_status="writable",
        default_host="127.0.0.1",
        default_port=8765,
        provider_calls_enabled=False,
        cloud_sync_enabled=False,
        profile_status="detected",
    )
    text = " ".join(str(value) for value in estimate_model_capability(profile).values()).lower()

    assert "runs 70b locally" not in text
    assert "equal to a 70b" not in text
    assert "all open-source llms are supported" not in text
    assert "cost reduction proven" not in text
    assert "energy reduction proven" not in text

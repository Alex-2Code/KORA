"""Local-only KORA Studio system profile and capability estimate helpers."""

from __future__ import annotations

import os
import platform
import shutil
import sys
from collections.abc import Callable
from dataclasses import asdict, dataclass
from typing import Any

DEFAULT_PROFILE_HOST = "127.0.0.1"
DEFAULT_PROFILE_PORT = 8765
UNKNOWN = "unknown"

ExecutableDetector = Callable[[str], str | None]


@dataclass(frozen=True)
class StudioSystemProfile:
    """Claim-safe local system profile for KORA Studio preview surfaces."""

    os_name: str
    os_version: str
    machine: str
    processor: str
    python_version: str
    total_memory_gb: float | None
    memory_detection_status: str
    runtime_candidates: list[dict[str, Any]]
    ollama_detected: bool
    llama_cpp_detected: bool
    local_storage_status: str
    default_host: str
    default_port: int
    provider_calls_enabled: bool
    cloud_sync_enabled: bool
    profile_status: str

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-ready representation."""

        return asdict(self)


def _safe_text(value: str | None) -> str:
    return value if value else UNKNOWN


def detect_total_memory_gb() -> tuple[float | None, str]:
    """Detect total physical memory using local OS metadata only."""

    if not hasattr(os, "sysconf"):
        return None, "unknown"

    try:
        page_size = os.sysconf("SC_PAGE_SIZE")
        page_count = os.sysconf("SC_PHYS_PAGES")
    except (OSError, ValueError):
        return None, "unknown"

    if not isinstance(page_size, int) or not isinstance(page_count, int):
        return None, "unknown"
    if page_size <= 0 or page_count <= 0:
        return None, "unknown"

    memory_gb = (page_size * page_count) / (1024**3)
    return round(memory_gb, 2), "detected"


def detect_runtime_candidates(which: ExecutableDetector = shutil.which) -> tuple[list[dict[str, Any]], bool, bool]:
    """Detect local runtime command availability without starting runtimes."""

    runtime_specs = [
        ("ollama", ["ollama"]),
        ("llama.cpp", ["llama-cli", "llama"]),
    ]
    candidates: list[dict[str, Any]] = []
    detected_by_name: dict[str, bool] = {}

    for name, commands in runtime_specs:
        detected_command = next((command for command in commands if which(command)), None)
        detected = detected_command is not None
        detected_by_name[name] = detected
        candidates.append(
            {
                "name": name,
                "detected": detected,
                "detection_method": "local_executable_path",
                "command": detected_command,
                "status": "detected" if detected else "not_detected",
            }
        )

    return candidates, detected_by_name["ollama"], detected_by_name["llama.cpp"]


def detect_local_storage_status(path: str | os.PathLike[str] = ".") -> str:
    """Return whether the current local workspace path appears writable."""

    try:
        return "writable" if os.access(path, os.W_OK) else "not_writable"
    except OSError:
        return "unknown"


def get_system_profile(
    *,
    default_host: str = DEFAULT_PROFILE_HOST,
    default_port: int = DEFAULT_PROFILE_PORT,
    which: ExecutableDetector = shutil.which,
    total_memory_gb: float | None | object = UNKNOWN,
    memory_detection_status: str | None = None,
) -> StudioSystemProfile:
    """Build a local-only system profile with fail-closed unknown fields."""

    if total_memory_gb == UNKNOWN:
        detected_memory_gb, detected_memory_status = detect_total_memory_gb()
    else:
        detected_memory_gb = total_memory_gb if isinstance(total_memory_gb, (int, float)) else None
        detected_memory_status = memory_detection_status or ("detected" if detected_memory_gb is not None else "unknown")

    runtime_candidates, ollama_detected, llama_cpp_detected = detect_runtime_candidates(which)
    unknowns = [
        not _safe_text(platform.version()) or _safe_text(platform.version()) == UNKNOWN,
        detected_memory_gb is None,
    ]
    profile_status = "detected_with_unknowns" if any(unknowns) else "detected"

    return StudioSystemProfile(
        os_name=_safe_text(platform.system()),
        os_version=_safe_text(platform.version()),
        machine=_safe_text(platform.machine()),
        processor=_safe_text(platform.processor()),
        python_version=_safe_text(sys.version.split()[0]),
        total_memory_gb=detected_memory_gb,
        memory_detection_status=detected_memory_status,
        runtime_candidates=runtime_candidates,
        ollama_detected=ollama_detected,
        llama_cpp_detected=llama_cpp_detected,
        local_storage_status=detect_local_storage_status(),
        default_host=default_host,
        default_port=default_port,
        provider_calls_enabled=False,
        cloud_sync_enabled=False,
        profile_status=profile_status,
    )


def estimate_model_capability(profile: StudioSystemProfile | dict[str, Any]) -> dict[str, Any]:
    """Return a claim-safe local model capability estimate."""

    profile_dict = profile.to_dict() if isinstance(profile, StudioSystemProfile) else profile
    memory_gb = profile_dict.get("total_memory_gb")

    if not isinstance(memory_gb, (int, float)):
        recommended_tier = "unknown"
        physical_notes = "Estimated local model tier is unknown until memory and runtime are validated."
        confidence = "low"
        recommendation_status = "unknown"
    elif memory_gb < 8:
        recommended_tier = "small/mini local models only"
        physical_notes = "This machine appears best suited for small or mini local models until validated."
        confidence = "medium"
        recommendation_status = "estimated"
    elif memory_gb < 16:
        recommended_tier = "3B-7B quantized tier"
        physical_notes = "This machine may be suited for 3B-7B quantized local models, depending on runtime and validation."
        confidence = "medium"
        recommendation_status = "estimated"
    elif memory_gb < 32:
        recommended_tier = "7B-8B quantized tier"
        physical_notes = "This machine may be suited for 7B-8B quantized local models, depending on runtime and validation."
        confidence = "medium"
        recommendation_status = "estimated"
    elif memory_gb < 64:
        recommended_tier = "7B-13B quantized tier"
        physical_notes = "This machine may be suited for 7B-13B quantized local models, depending on runtime and validation."
        confidence = "medium"
        recommendation_status = "estimated"
    else:
        recommended_tier = "13B+ may be possible depending on runtime and quantization"
        physical_notes = "Larger local models may be possible only when memory, runtime, quantization, and validation support them."
        confidence = "medium"
        recommendation_status = "estimated"

    return {
        "recommended_local_chat_tier": recommended_tier,
        "physically_runnable_model_notes": physical_notes,
        "larger_model_workflow_notes": (
            "KORA can make larger-model workflows more practical by routing deterministic work away from the model path."
        ),
        "recommendation_status": recommendation_status,
        "confidence": confidence,
        "claim_boundary": (
            "Recommendations are estimates until validated on this machine. "
            "KORA does not remove RAM/VRAM/unified-memory requirements."
        ),
    }

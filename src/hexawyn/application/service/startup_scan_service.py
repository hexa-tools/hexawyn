"""Startup-scan business logic — interpreting the control-plane scan result."""

from __future__ import annotations

_ERROR_NARRATIVE_SKIP = [
    "not available",
    "unavailable",
    "install hexawyn",
    "is down",
    "no node",
    "no pods",
    "0 pods",
    "Runtime not available",
    "startup scan requires",
    "empty and inactive",
]


def is_error_narrative(text: str) -> bool:
    """Return True when a narrative reads as an error/unavailable state."""
    text_lower = text.lower()
    return any(p.lower() in text_lower for p in _ERROR_NARRATIVE_SKIP)


def is_valid_startup_result(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True

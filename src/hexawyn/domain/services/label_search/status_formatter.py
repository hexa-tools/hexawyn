from __future__ import annotations

from hexawyn.domain.models.label_search import MatchedResourceResult

_UNHEALTHY_PHASES = frozenset(
    {
        "CrashLoop",
        "CrashLoopBackOff",
        "Error",
        "ImagePullBackOff",
        "Pending",
        "Unknown",
        "Terminating",
        "Failed",
    }
)


def is_pod_healthy(phase: str | None) -> bool | None:
    """`None` when the resource has no phase concept at all (non-pod kinds) —
    distinct from `False`, which means a real unhealthy pod status."""
    if phase is None:
        return None
    return phase not in _UNHEALTHY_PHASES


def summarize_health(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is False]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )

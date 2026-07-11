from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityIncidentRaw,
)


def compute_uptime_pct(incidents: list[ReliabilityIncidentRaw], period_minutes: int) -> float:
    """Compute availability as ``(1 - downtime / period) * 100``.

    Planned-maintenance windows are excluded from downtime. The result is
    clamped to [0, 100] and rounded to two decimals — this is the authoritative
    formula the semantic layer validates the LLM's uptime figure against.
    """
    if period_minutes <= 0:
        return 100.0
    downtime = sum(
        incident["downtime_minutes"]
        for incident in incidents
        if not incident["planned_maintenance"]
    )
    uptime = (1 - downtime / period_minutes) * 100
    return round(max(0.0, min(100.0, uptime)), 2)

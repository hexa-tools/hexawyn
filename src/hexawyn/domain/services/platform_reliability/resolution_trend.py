from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityIncidentRaw,
)

_TREND_TOLERANCE_PCT = 2.0


@dataclass(frozen=True)
class ResolutionResult:
    avg_resolution_minutes: int
    resolution_delta_pct: float
    resolution_trend: str


def compute_resolution(
    incidents: list[ReliabilityIncidentRaw], previous_avg: int | None
) -> ResolutionResult:
    """Compute the average resolution time and its trend vs the previous period.

    Faster resolution (a negative delta) is an improvement; slower is a
    degradation. Differences within +/- 2% are treated as stable.
    """
    avg = _average_resolution(incidents)
    delta_pct = _delta_pct(avg, previous_avg)
    return ResolutionResult(
        avg_resolution_minutes=avg,
        resolution_delta_pct=delta_pct,
        resolution_trend=_trend(delta_pct, previous_avg),
    )


def _average_resolution(incidents: list[ReliabilityIncidentRaw]) -> int:
    if not incidents:
        return 0
    total = sum(incident["resolution_minutes"] for incident in incidents)
    return round(total / len(incidents))


def _delta_pct(current: int, previous: int | None) -> float:
    if previous is None or previous <= 0:
        return 0.0
    return round((current - previous) / previous * 100, 1)


def _trend(delta_pct: float, previous: int | None) -> str:
    if previous is None:
        return "stable"
    if delta_pct < -_TREND_TOLERANCE_PCT:
        return "improving"
    if delta_pct > _TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"

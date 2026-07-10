from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorRawData,
)
from hexawyn.domain.models.cluster_operator_health import (
    HEALTH_DEGRADED,
    HEALTH_HEALTHY,
    HEALTH_PROGRESSING,
    HEALTH_UNKNOWN,
    ClusterOperatorHealthReport,
    ClusterOperatorStatus,
)

_CHRONIC_THRESHOLD_MINUTES = 15
_HEALTH_ORDER = {
    HEALTH_DEGRADED: 0,
    HEALTH_UNKNOWN: 1,
    HEALTH_PROGRESSING: 2,
    HEALTH_HEALTHY: 3,
}


class ClusterOperatorHealthService:
    """Domain service — classifies ClusterOperator health from raw conditions.

    Health precedence: an operator is degraded before progressing; an operator
    whose Available condition is Unknown is never healthy. Operators degraded
    for more than 15 minutes are chronic (vs transient).
    """

    def __init__(self, clock: Callable[[], datetime] | None = None) -> None:
        self._clock = clock or _utc_now

    def evaluate(self, operators: list[ClusterOperatorRawData]) -> ClusterOperatorHealthReport:
        statuses = [self._to_status(operator) for operator in operators]
        statuses.sort(key=lambda status: _HEALTH_ORDER.get(status.health, 99))

        degraded = sum(1 for status in statuses if status.health == HEALTH_DEGRADED)
        progressing = sum(1 for status in statuses if status.health == HEALTH_PROGRESSING)
        healthy = sum(1 for status in statuses if status.health == HEALTH_HEALTHY)

        return ClusterOperatorHealthReport(
            operators=statuses,
            total=len(statuses),
            healthy=healthy,
            degraded=degraded,
            progressing=progressing,
            all_healthy=healthy == len(statuses),
        )

    def _to_status(self, operator: ClusterOperatorRawData) -> ClusterOperatorStatus:
        health = self._classify(operator)
        duration_minutes = self._degraded_duration_minutes(operator.get("degraded_since"))
        return ClusterOperatorStatus(
            name=operator["name"],
            available=operator["available"],
            progressing=operator["progressing"],
            degraded=operator["degraded"],
            health=health,
            message=operator.get("message", ""),
            degraded_duration_minutes=duration_minutes,
            is_chronic=duration_minutes > _CHRONIC_THRESHOLD_MINUTES,
        )

    def _classify(self, operator: ClusterOperatorRawData) -> str:
        if operator.get("available_unknown"):
            return HEALTH_UNKNOWN
        if operator["degraded"]:
            return HEALTH_DEGRADED
        if operator["progressing"]:
            return HEALTH_PROGRESSING
        if operator["available"]:
            return HEALTH_HEALTHY
        return HEALTH_UNKNOWN

    def _degraded_duration_minutes(self, degraded_since: str | None) -> int:
        if not degraded_since:
            return 0
        try:
            started = datetime.fromisoformat(degraded_since.replace("Z", "+00:00"))
        except ValueError:
            return 0
        elapsed = self._clock() - started
        return max(0, int(elapsed.total_seconds() // 60))


def _utc_now() -> datetime:
    return datetime.now(UTC)

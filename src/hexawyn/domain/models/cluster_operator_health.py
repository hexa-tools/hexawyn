from __future__ import annotations

from dataclasses import dataclass, field

HEALTH_HEALTHY = "healthy"
HEALTH_DEGRADED = "degraded"
HEALTH_PROGRESSING = "progressing"
HEALTH_UNKNOWN = "unknown"


@dataclass(frozen=True)
class ClusterOperatorStatus:
    name: str
    available: bool
    progressing: bool
    degraded: bool
    health: str
    message: str
    degraded_duration_minutes: int
    is_chronic: bool


@dataclass
class ClusterOperatorHealthReport:
    operators: list[ClusterOperatorStatus] = field(default_factory=list)
    total: int = 0
    healthy: int = 0
    degraded: int = 0
    progressing: int = 0
    all_healthy: bool = True

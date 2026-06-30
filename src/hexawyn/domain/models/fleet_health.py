from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True)
class ClusterRawMetrics:
    context_name: str
    nodes_total: int
    nodes_not_ready: int
    pods_total: int
    pods_running: int
    pods_crashloop: int
    cpu_utilization: float | None  # 0.0–1.0, None if unknown
    memory_utilization: float | None  # 0.0–1.0, None if unknown
    certs_expiring_critical: int  # expiring in <= 7 days
    certs_expiring_warning: int  # expiring in <= 30 days
    security_violations: int  # privileged / non-compliant pods
    pipelines_failing: int  # failing Tekton pipeline runs
    prometheus_available: bool


@dataclass(frozen=True)
class CategoryReport:
    status: str  # "OK" | "WARNING" | "CRITICAL" | "UNKNOWN"
    key_metric: str  # human-readable summary metric
    top_issue: str | None


@dataclass(frozen=True)
class ClusterHealthReport:
    context_name: str
    reachable: bool
    unreachable_reason: str | None
    health_score: int | None  # None when unreachable
    health_status: str  # "healthy" | "degraded" | "critical" | "unreachable"
    categories: dict[str, CategoryReport]
    checked_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass
class FleetHealthReport:
    cluster_reports: list[ClusterHealthReport] = field(default_factory=list)
    fleet_score: int | None = None  # avg score of reachable clusters, None if all unreachable
    fleet_status: str = "unknown"  # worst status across reachable clusters
    reachable_count: int = 0
    unreachable_count: int = 0
    checked_at: datetime = field(default_factory=lambda: datetime.now(UTC))

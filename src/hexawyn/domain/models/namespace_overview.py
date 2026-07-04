from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class NamespaceHealthStatus(Enum):
    """Single-score namespace health, deliberately separate from the raw K8s
    namespace phase (Active/Terminating) — see `NamespaceOverviewReport.namespace_status`."""

    HEALTHY = "Healthy"
    DEGRADED = "Degraded"
    CRITICAL = "Critical"


@dataclass(frozen=True)
class NamespaceCounts:
    pods_total: int
    pods_running: int
    pods_failed: int
    deployments_total: int
    deployments_ready: int
    services_total: int


@dataclass(frozen=True)
class UnhealthyResource:
    name: str
    kind: str
    reason: str


@dataclass(frozen=True)
class NamespaceOverviewRequest:
    namespace: str
    max_tokens: int = 2000


@dataclass(frozen=True)
class NamespaceOverviewReport:
    """Compact, token-budgeted namespace health report — only unhealthy
    resources are named, never a raw resource dump."""

    namespace: str
    namespace_status: str
    counts: NamespaceCounts
    health_status: NamespaceHealthStatus
    root_cause: str = ""
    unhealthy_resources: list[UnhealthyResource] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    has_more_unhealthy: bool = False
    remaining_unhealthy_count: int = 0
    estimated_tokens: int = 0
    is_empty: bool = False
    summary: str = ""

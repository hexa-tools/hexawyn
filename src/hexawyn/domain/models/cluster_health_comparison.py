from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ClusterHealthSnapshot:
    cluster_name: str
    failing_pods: int
    total_pods: int
    cpu_utilization_pct: float
    memory_utilization_pct: float
    node_count: int
    nodes_not_ready: int
    active_incidents: int
    health_status: str
    in_maintenance: bool
    reachable: bool


@dataclass
class ComparisonReport:
    worse_cluster: str | None
    reason: str
    delta_failing_pods: int = 0
    delta_cpu_pct: float = 0.0
    delta_active_incidents: int = 0
    normalized_a_failing_per_100: float = 0.0
    normalized_b_failing_per_100: float = 0.0


@dataclass
class HealthComparisonResult:
    cluster_a: ClusterHealthSnapshot
    cluster_b: ClusterHealthSnapshot
    comparison: ComparisonReport

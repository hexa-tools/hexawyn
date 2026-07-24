from __future__ import annotations

from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.use_case.compare_cluster_health.command import CompareClusterHealthCommand
from hexawyn.application.use_case.compare_cluster_health.response import (
    CompareClusterHealthResponse,
)
from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot
from hexawyn.domain.models.fleet_health import ClusterRawMetrics
from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (
    compare,
)


class CompareClusterHealthUseCase:
    def __init__(self, fleet_health_port: FleetHealthPort) -> None:
        self._port = fleet_health_port

    def execute(self, command: CompareClusterHealthCommand) -> CompareClusterHealthResponse:
        raw_a = self._port.get_cluster_raw_metrics(command.cluster_a)
        raw_b = self._port.get_cluster_raw_metrics(command.cluster_b)
        snap_a = _to_snapshot(raw_a)
        snap_b = _to_snapshot(raw_b)
        result = compare(snap_a, snap_b)
        return CompareClusterHealthResponse(result=result)


def _to_snapshot(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )

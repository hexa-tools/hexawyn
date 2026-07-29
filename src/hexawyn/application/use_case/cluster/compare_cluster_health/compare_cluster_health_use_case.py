from __future__ import annotations

from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.use_case.cluster.compare_cluster_health.command import (  # noqa: E501
    CompareClusterHealthCommand,
)
from hexawyn.application.use_case.cluster.compare_cluster_health.response import (  # noqa: E501
    CompareClusterHealthResponse,
)
from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot
from hexawyn.domain.models.fleet_health import ClusterRawMetrics
from hexawyn.domain.services.cluster_health_comparison.cluster_health_comparison_service import (  # noqa: E501
    compare,
)


def _to_snapshot(
    name: str, metrics: ClusterRawMetrics, reachable: bool = True
) -> ClusterHealthSnapshot:
    return ClusterHealthSnapshot(
        cluster_name=name,
        failing_pods=metrics.pods_total - metrics.pods_running,
        total_pods=metrics.pods_total,
        cpu_utilization_pct=(metrics.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(metrics.memory_utilization or 0.0) * 100,
        node_count=metrics.nodes_total,
        nodes_not_ready=metrics.nodes_not_ready,
        active_incidents=0,
        health_status="healthy",
        in_maintenance=False,
        reachable=reachable,
    )


class CompareClusterHealthUseCase:
    def __init__(self, fleet_health_port: FleetHealthPort) -> None:
        self._port = fleet_health_port

    def execute(self, command: CompareClusterHealthCommand) -> CompareClusterHealthResponse:
        raw_a, reachable_a = self._fetch_or_default(command.cluster_a)
        raw_b, reachable_b = self._fetch_or_default(command.cluster_b)
        result = compare(
            _to_snapshot(command.cluster_a, raw_a, reachable_a),
            _to_snapshot(command.cluster_b, raw_b, reachable_b),
        )
        return CompareClusterHealthResponse(result=result)

    def _fetch_or_default(self, context_name: str) -> tuple[ClusterRawMetrics, bool]:
        try:
            return self._port.get_cluster_raw_metrics(context_name), True
        except Exception:
            return ClusterRawMetrics(
                context_name=context_name,
                nodes_total=0,
                nodes_not_ready=0,
                pods_total=0,
                pods_running=0,
                pods_crashloop=0,
                cpu_utilization=None,
                memory_utilization=None,
                certs_expiring_critical=0,
                certs_expiring_warning=0,
                security_violations=0,
                pipelines_failing=0,
                prometheus_available=False,
            ), False

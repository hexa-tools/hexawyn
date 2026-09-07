from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.compare_cluster_health.command import (
    CompareClusterHealthCommand,
)
from hexawyn.application.use_case.cluster.compare_cluster_health.compare_cluster_health_use_case import (  # noqa: E501
    CompareClusterHealthUseCase,
)
from hexawyn.application.use_case.cluster.compare_cluster_health.response import (
    CompareClusterHealthResponse,
)
from hexawyn.domain.models.fleet_health import ClusterRawMetrics


def _raw_metrics(context_name: str = "test") -> ClusterRawMetrics:
    return ClusterRawMetrics(
        context_name=context_name,
        nodes_total=5,
        nodes_not_ready=0,
        pods_total=20,
        pods_running=19,
        pods_crashloop=1,
        cpu_utilization=0.5,
        memory_utilization=0.6,
        certs_expiring_critical=0,
        certs_expiring_warning=2,
        security_violations=0,
        pipelines_failing=1,
        prometheus_available=True,
    )


class TestCompareClusterHealthUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_cluster_raw_metrics.return_value = _raw_metrics()

        use_case = CompareClusterHealthUseCase(fleet_health_port=port)
        result = use_case.execute(
            CompareClusterHealthCommand(cluster_a="prod-eu", cluster_b="prod-us")
        )

        assert isinstance(result, CompareClusterHealthResponse)

    def test_execute_one_cluster_unreachable(self) -> None:
        port = MagicMock()
        port.get_cluster_raw_metrics.side_effect = [
            _raw_metrics("prod-eu"),
            Exception("timeout"),
        ]

        use_case = CompareClusterHealthUseCase(fleet_health_port=port)
        result = use_case.execute(
            CompareClusterHealthCommand(cluster_a="prod-eu", cluster_b="prod-us")
        )

        assert isinstance(result, CompareClusterHealthResponse)

    def test_execute_both_clusters_unreachable(self) -> None:
        port = MagicMock()
        port.get_cluster_raw_metrics.side_effect = Exception("offline")

        use_case = CompareClusterHealthUseCase(fleet_health_port=port)
        result = use_case.execute(CompareClusterHealthCommand(cluster_a="a", cluster_b="b"))

        assert isinstance(result, CompareClusterHealthResponse)

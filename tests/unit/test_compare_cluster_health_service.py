from unittest.mock import MagicMock

from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_command import (  # noqa: E501
    CompareClusterHealthCommand,
)


class TestCompareClusterHealthService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_service_port import (  # noqa: E501
            CompareClusterHealthServicePort,
        )
        from hexawyn.application.service.compare_cluster_health_service import (
            CompareClusterHealthService,
        )

        service = CompareClusterHealthService(fleet_health_port=MagicMock(spec=FleetHealthPort))
        assert isinstance(service, CompareClusterHealthServicePort)

    def test_compare_returns_result(self) -> None:
        from hexawyn.application.service.compare_cluster_health_service import (
            CompareClusterHealthService,
        )

        port = MagicMock(spec=FleetHealthPort)
        port.get_cluster_raw_metrics.return_value = MagicMock(
            pods_total=0,
            pods_running=0,
            pods_crashloop=0,
            nodes_total=0,
            nodes_not_ready=0,
            cpu_utilization=None,
            memory_utilization=None,
            certs_expiring_critical=0,
            certs_expiring_warning=0,
            security_violations=0,
            pipelines_failing=0,
            prometheus_available=False,
            context_name="test",
        )
        service = CompareClusterHealthService(fleet_health_port=port)

        response = service.compare(CompareClusterHealthCommand(cluster_a="a", cluster_b="b"))
        assert response.result.comparison.worse_cluster is None

    def test_unreachable_cluster_fallback(self) -> None:
        from hexawyn.application.service.compare_cluster_health_service import (
            CompareClusterHealthService,
        )

        port = MagicMock(spec=FleetHealthPort)
        port.get_cluster_raw_metrics.side_effect = [
            RuntimeError("timeout"),
            MagicMock(
                pods_total=0,
                pods_running=0,
                pods_crashloop=0,
                nodes_total=0,
                nodes_not_ready=0,
                cpu_utilization=None,
                memory_utilization=None,
                certs_expiring_critical=0,
                certs_expiring_warning=0,
                security_violations=0,
                pipelines_failing=0,
                prometheus_available=False,
                context_name="prod-us",
            ),
        ]
        service = CompareClusterHealthService(fleet_health_port=port)

        response = service.compare(
            CompareClusterHealthCommand(cluster_a="prod-eu", cluster_b="prod-us")
        )
        assert response.result.cluster_a.reachable is False

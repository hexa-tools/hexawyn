from unittest.mock import MagicMock

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorRawData,
    ClusterOperatorStatusPort,
)
from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_command import (  # noqa: E501
    CheckClusterOperatorHealthCommand,
)


def _raw(name: str, degraded: bool = False) -> ClusterOperatorRawData:
    return ClusterOperatorRawData(
        name=name,
        available=True,
        progressing=False,
        degraded=degraded,
        available_unknown=False,
        message="etcd member not responding" if degraded else "",
        degraded_since=None,
    )


class TestCheckClusterOperatorHealthService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_service_port import (  # noqa: E501
            CheckClusterOperatorHealthServicePort,
        )
        from hexawyn.application.service.check_cluster_operator_health_service import (
            CheckClusterOperatorHealthService,
        )

        service = CheckClusterOperatorHealthService(
            operator_port=MagicMock(spec=ClusterOperatorStatusPort)
        )

        assert isinstance(service, CheckClusterOperatorHealthServicePort)

    def test_check_returns_report_from_port_data(self) -> None:
        from hexawyn.application.service.check_cluster_operator_health_service import (
            CheckClusterOperatorHealthService,
        )

        port = MagicMock(spec=ClusterOperatorStatusPort)
        port.list_cluster_operators.return_value = [_raw("etcd", degraded=True), _raw("dns")]
        service = CheckClusterOperatorHealthService(operator_port=port)

        response = service.check(CheckClusterOperatorHealthCommand())

        port.list_cluster_operators.assert_called_once_with()
        assert response.result.total == 2
        assert response.result.degraded == 1
        assert response.result.all_healthy is False

    def test_check_lets_domain_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.check_cluster_operator_health_service import (
            CheckClusterOperatorHealthService,
        )
        from hexawyn.domain.errors import ClusterOperatorCRDNotFoundError

        port = MagicMock(spec=ClusterOperatorStatusPort)
        port.list_cluster_operators.side_effect = ClusterOperatorCRDNotFoundError()
        service = CheckClusterOperatorHealthService(operator_port=port)

        with pytest.raises(ClusterOperatorCRDNotFoundError):
            service.check(CheckClusterOperatorHealthCommand())

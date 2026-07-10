from unittest.mock import MagicMock

from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_command import (  # noqa: E501
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_response import (  # noqa: E501
    CheckClusterOperatorHealthResponse,
)
from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_service_port import (  # noqa: E501
    CheckClusterOperatorHealthServicePort,
)
from hexawyn.domain.models.cluster_operator_health import ClusterOperatorHealthReport


class TestCheckClusterOperatorHealthUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.check_cluster_operator_health.check_cluster_operator_health_use_case import (  # noqa: E501
            CheckClusterOperatorHealthUseCase,
        )

        service = MagicMock(spec=CheckClusterOperatorHealthServicePort)
        expected = CheckClusterOperatorHealthResponse(
            result=ClusterOperatorHealthReport(total=32, healthy=30, degraded=1, progressing=1)
        )
        service.check.return_value = expected
        use_case = CheckClusterOperatorHealthUseCase(service=service)
        command = CheckClusterOperatorHealthCommand()

        response = use_case.execute(command)

        service.check.assert_called_once_with(command)
        assert response is expected
        assert response.result.total == 32

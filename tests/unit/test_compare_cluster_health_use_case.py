from unittest.mock import MagicMock

from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_command import (  # noqa: E501
    CompareClusterHealthCommand,
)
from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_response import (  # noqa: E501
    CompareClusterHealthResponse,
)
from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_service_port import (  # noqa: E501
    CompareClusterHealthServicePort,
)
from hexawyn.domain.models.cluster_health_comparison import HealthComparisonResult


class TestCompareClusterHealthUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.compare_cluster_health.compare_cluster_health_use_case import (  # noqa: E501
            CompareClusterHealthUseCase,
        )

        service = MagicMock(spec=CompareClusterHealthServicePort)
        expected = CompareClusterHealthResponse(result=MagicMock(spec=HealthComparisonResult))
        service.compare.return_value = expected
        use_case = CompareClusterHealthUseCase(service=service)

        response = use_case.execute(CompareClusterHealthCommand(cluster_a="a", cluster_b="b"))

        assert response is expected

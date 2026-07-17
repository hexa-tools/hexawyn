from unittest.mock import MagicMock

from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_command import (  # noqa: E501
    DiffClusterResourcesCommand,
)
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_response import (  # noqa: E501
    DiffClusterResourcesResponse,
)
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_service_port import (  # noqa: E501
    DiffClusterResourcesServicePort,
)
from hexawyn.domain.models.cluster_diff import ClusterDiffReport


class TestDiffClusterResourcesUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.diff_cluster_resources.diff_cluster_resources_use_case import (  # noqa: E501
            DiffClusterResourcesUseCase,
        )

        service = MagicMock(spec=DiffClusterResourcesServicePort)
        expected = DiffClusterResourcesResponse(
            result=ClusterDiffReport(source_cluster="staging", target_cluster="prod")
        )
        service.diff.return_value = expected
        use_case = DiffClusterResourcesUseCase(service=service)

        response = use_case.execute(
            DiffClusterResourcesCommand(source_context="staging", target_context="prod")
        )

        assert response is expected

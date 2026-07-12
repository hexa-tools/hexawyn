from unittest.mock import MagicMock

from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_command import (  # noqa: E501
    DiffClusterResourcesCommand,
)


class TestDiffClusterResourcesService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_service_port import (  # noqa: E501
            DiffClusterResourcesServicePort,
        )
        from hexawyn.application.service.diff_cluster_resources_service import (
            DiffClusterResourcesService,
        )

        service = DiffClusterResourcesService(cluster_diff_port=MagicMock(spec=ClusterDiffPort))
        assert isinstance(service, DiffClusterResourcesServicePort)

    def test_diff_returns_result(self) -> None:
        from hexawyn.application.service.diff_cluster_resources_service import (
            DiffClusterResourcesService,
        )

        port = MagicMock(spec=ClusterDiffPort)
        port.get_resource_inventory.side_effect = [
            {
                "cluster_name": "staging",
                "resources": [
                    {
                        "kind": "Deployment",
                        "name": "svc",
                        "namespace": "ns",
                        "image_tag": "v1",
                        "replicas": 1,
                        "is_secret": False,
                    }
                ],
            },
            {"cluster_name": "prod", "resources": []},
        ]
        service = DiffClusterResourcesService(cluster_diff_port=port)

        response = service.diff(
            DiffClusterResourcesCommand(source_context="staging", target_context="prod")
        )
        assert response.result.total_differences == 1

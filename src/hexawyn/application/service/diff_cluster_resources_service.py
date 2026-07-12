from __future__ import annotations

from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_command import (  # noqa: E501
    DiffClusterResourcesCommand,
)
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_response import (  # noqa: E501
    DiffClusterResourcesResponse,
)
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_service_port import (  # noqa: E501
    DiffClusterResourcesServicePort,
)
from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
    compute_diff,
)


class DiffClusterResourcesService(DiffClusterResourcesServicePort):
    def __init__(self, cluster_diff_port: ClusterDiffPort) -> None:
        self._port = cluster_diff_port

    def diff(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=result)

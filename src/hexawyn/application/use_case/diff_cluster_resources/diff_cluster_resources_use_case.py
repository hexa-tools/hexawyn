from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
from hexawyn.application.use_case.diff_cluster_resources.command import DiffClusterResourcesCommand
from hexawyn.application.use_case.diff_cluster_resources.response import (
    DiffClusterResourcesResponse,
)
from hexawyn.domain.services.cluster_diff.cluster_diff_service import compute_diff


class DiffClusterResourcesUseCase:
    def __init__(self, cluster_diff_port: ClusterDiffPort) -> None:
        self._port = cluster_diff_port

    def execute(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=result)

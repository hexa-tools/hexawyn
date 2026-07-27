from dataclasses import dataclass

from hexawyn.domain.models.cluster_diff import ClusterDiffReport


@dataclass
class DiffClusterResourcesResponse:
    result: ClusterDiffReport

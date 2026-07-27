from dataclasses import dataclass

from hexawyn.domain.models.cluster_operator_health import ClusterOperatorHealthReport


@dataclass
class CheckClusterOperatorHealthResponse:
    result: ClusterOperatorHealthReport

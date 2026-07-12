from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.cross_cluster_correlation import CrossClusterCorrelationReport


@dataclass
class DetectCrossClusterIncidentResponse:
    result: CrossClusterCorrelationReport

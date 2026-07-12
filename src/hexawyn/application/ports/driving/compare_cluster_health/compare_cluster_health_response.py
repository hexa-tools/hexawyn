from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.cluster_health_comparison import HealthComparisonResult


@dataclass
class CompareClusterHealthResponse:
    result: HealthComparisonResult

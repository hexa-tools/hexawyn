from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalComparisonResult,
    HistoricalPodInfo,
)


@dataclass
class QueryKubeArchiveResponse:
    total_resources: int = 0
    pods: list[HistoricalPodInfo] = field(default_factory=list)
    queried_timestamp: str | None = None
    comparison: HistoricalComparisonResult | None = None
    error: str | None = None

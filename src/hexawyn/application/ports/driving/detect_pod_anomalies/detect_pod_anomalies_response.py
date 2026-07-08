from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class PodAnomalyDict(TypedDict):
    pod_name: str
    namespace: str
    metric: str
    severity: str
    deviation_pct: float
    z_score: float | None
    isolation_forest_score: float | None
    detection_method: str
    current_value: float
    baseline_mean: float
    note: str


class ExcludedPodDict(TypedDict):
    pod_name: str
    namespace: str
    reason: str


@dataclass
class DetectPodAnomaliesResponse:
    namespace: str = ""
    total_pods: int = 0
    anomalies: list[PodAnomalyDict] = field(default_factory=list)
    excluded_pods: list[ExcludedPodDict] = field(default_factory=list)
    summary: str = ""
    error: str | None = None

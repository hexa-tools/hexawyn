from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class PodAnomalyDict(TypedDict):
    pod_name: str
    anomaly_type: str
    description: str
    severity: str


class ExcludedPodDict(TypedDict):
    pod_name: str
    reason: str


@dataclass
class DetectPodAnomaliesResponse:
    namespace: str = ""
    total_pods: int = 0
    anomalies: list[PodAnomalyDict] = field(default_factory=list)
    excluded_pods: list[ExcludedPodDict] = field(default_factory=list)
    summary: str = ""
    error: str | None = None

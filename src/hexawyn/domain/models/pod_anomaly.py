from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from hexawyn.domain.models.event import EventSeverity

PodMetric = Literal["cpu", "memory", "error_rate"]
DetectionMethod = Literal["zscore", "isolation_forest", "both"]


@dataclass(frozen=True)
class PodAnomaly:
    """An anomalous metric for one pod, ranked by severity against its own baseline."""

    pod_name: str
    namespace: str
    metric: PodMetric
    severity: EventSeverity
    deviation_pct: float
    z_score: float | None
    isolation_forest_score: float | None
    detection_method: DetectionMethod
    current_value: float
    baseline_mean: float
    note: str = ""


@dataclass(frozen=True)
class ExcludedPod:
    """A pod excluded from anomaly comparison, with an explanatory reason."""

    pod_name: str
    namespace: str
    reason: str


@dataclass(frozen=True)
class PodAnomalyDetectionRequest:
    namespace: str
    baseline_window_days: int = 7


@dataclass(frozen=True)
class PodAnomalyDetectionReport:
    """Full result: ranked anomalies, exclusions, and a summary."""

    namespace: str
    total_pods: int
    anomalies: list[PodAnomaly] = field(default_factory=list)
    excluded_pods: list[ExcludedPod] = field(default_factory=list)
    summary: str = ""

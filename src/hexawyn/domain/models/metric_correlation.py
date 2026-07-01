from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum

MIN_DATA_POINTS: int = 3
CORRELATION_THRESHOLD: float = 0.7


class CorrelationStatus(Enum):
    CORRELATED = "correlated"
    UNCORRELATED = "uncorrelated"
    INCONCLUSIVE = "inconclusive"


@dataclass(frozen=True)
class TimeSeries:
    label: str
    data_points: list[float]


@dataclass(frozen=True)
class CorrelationRequest:
    primary_service: str
    correlated_service: str
    time_window_minutes: int = 30


@dataclass(frozen=True)
class CorrelationResult:
    status: CorrelationStatus
    coefficient: float
    lag_index: int
    primary_label: str
    correlated_label: str
    hypothesis: str
    data_point_count: int
    reasons: list[str] = field(default_factory=list)

    @staticmethod
    def compute(
        request: CorrelationRequest,
        series_a: TimeSeries,
        series_b: TimeSeries,
    ) -> CorrelationResult:
        count = min(len(series_a.data_points), len(series_b.data_points))
        if count < MIN_DATA_POINTS:
            return CorrelationResult(
                status=CorrelationStatus.INCONCLUSIVE,
                coefficient=0.0,
                lag_index=0,
                primary_label=series_a.label,
                correlated_label=series_b.label,
                hypothesis="Insufficient data points for correlation analysis",
                data_point_count=count,
                reasons=[f"Only {count} data point(s) — minimum {MIN_DATA_POINTS} required"],
            )

        a = series_a.data_points[:count]
        b = series_b.data_points[:count]
        n = len(a)
        sum_a = sum(a)
        sum_b = sum(b)
        sum_ab = sum(a[i] * b[i] for i in range(n))
        sum_a2 = sum(a[i] * a[i] for i in range(n))
        sum_b2 = sum(b[i] * b[i] for i in range(n))
        denominator = math.sqrt((n * sum_a2 - sum_a * sum_a) * (n * sum_b2 - sum_b * sum_b))

        if abs(denominator) < 1e-10:
            coefficient = 0.0
        else:
            coefficient = (n * sum_ab - sum_a * sum_b) / denominator

        reasons: list[str] = []
        if coefficient >= CORRELATION_THRESHOLD:
            status = CorrelationStatus.CORRELATED
            hypothesis = (
                f"{series_b.label} spike likely contributing to {series_a.label} incidents "
                f"(correlation coefficient: {coefficient:.2f})"
            )
            reasons.append(f"Strong positive correlation: r={coefficient:.2f}")
        elif coefficient <= -CORRELATION_THRESHOLD:
            status = CorrelationStatus.UNCORRELATED
            hypothesis = (
                f"Inverse relationship: {series_b.label} decreases when {series_a.label} spikes "
                f"(r={coefficient:.2f})"
            )
            reasons.append(f"Negative correlation: r={coefficient:.2f}")
        elif abs(coefficient) < 0.3:
            status = CorrelationStatus.UNCORRELATED
            hypothesis = f"No significant correlation between {series_a.label} and {series_b.label}"
            reasons.append(f"Weak correlation: r={coefficient:.2f}")
        else:
            status = CorrelationStatus.INCONCLUSIVE
            hypothesis = f"Moderate correlation (r={coefficient:.2f}) — more data needed"
            reasons.append(f"Moderate correlation: r={coefficient:.2f}")

        return CorrelationResult(
            status=status,
            coefficient=round(coefficient, 4),
            lag_index=0,
            primary_label=series_a.label,
            correlated_label=series_b.label,
            hypothesis=hypothesis,
            data_point_count=count,
            reasons=reasons,
        )

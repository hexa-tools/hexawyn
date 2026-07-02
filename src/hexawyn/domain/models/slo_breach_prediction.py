from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RiskLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"


@dataclass(frozen=True)
class ServiceRisk:
    service_name: str
    current_p99_ms: float
    slo_threshold_ms: float
    trend_slope_ms_per_min: float
    projected_p99_ms: float
    breach_in_minutes: float | None
    risk: RiskLevel


@dataclass(frozen=True)
class SLOBreachPredictionRequest:
    prediction_window_minutes: int = 60
    history_window_minutes: int = 30


@dataclass(frozen=True)
class SLOBreachPredictionResult:
    prediction_window_minutes: int
    at_risk: list[ServiceRisk]
    safe_count: int

    @staticmethod
    def compute(
        request: SLOBreachPredictionRequest,
        raw_metrics: list[dict[str, object]],
    ) -> SLOBreachPredictionResult:
        at_risk: list[ServiceRisk] = []
        safe = 0

        for r in raw_metrics:
            current = float(str(r.get("current_p99", 0)))
            slo = float(str(r.get("slo", 0)))
            slope = float(str(r.get("slope", 0)))

            if slope <= 0:
                safe += 1
                continue

            projected = current + slope * request.prediction_window_minutes
            breach_min = (slo - current) / slope if slope > 0 else None
            if projected <= slo:
                risk = RiskLevel.LOW
            elif breach_min is not None and breach_min <= 30:
                risk = RiskLevel.HIGH
            elif breach_min is not None and breach_min <= request.prediction_window_minutes:
                risk = RiskLevel.MEDIUM
            else:
                risk = RiskLevel.LOW

            at_risk.append(
                ServiceRisk(
                    service_name=str(r.get("service", "")),
                    current_p99_ms=current,
                    slo_threshold_ms=slo,
                    trend_slope_ms_per_min=slope,
                    projected_p99_ms=round(projected, 2),
                    breach_in_minutes=round(breach_min, 1) if breach_min is not None else None,
                    risk=risk,
                )
            )

        at_risk.sort(key=lambda s: s.breach_in_minutes if s.breach_in_minutes is not None else 9999)
        return SLOBreachPredictionResult(
            prediction_window_minutes=request.prediction_window_minutes,
            at_risk=at_risk,
            safe_count=safe,
        )

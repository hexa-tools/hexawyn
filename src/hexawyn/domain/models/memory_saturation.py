from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

DEFAULT_NODE_CAPACITY_MB: float = 32768.0


class PredictionRisk(Enum):
    CRITICAL = "critical"
    AT_RISK = "at_risk"
    STABLE = "stable"
    OSCILLATING = "oscillating"


@dataclass(frozen=True)
class MemoryPrediction:
    pod_name: str
    namespace: str
    current_memory_mb: float
    limit_mb: float | None
    growth_rate_mb_per_min: float
    saturation_in_minutes: float | None
    otel_root_cause: str | None
    risk: PredictionRisk


@dataclass(frozen=True)
class MemorySaturationRequest:
    prediction_window_minutes: int = 30
    critical_threshold_minutes: int = 30


@dataclass(frozen=True)
class MemorySaturationResult:
    prediction_window_minutes: int
    critical_pods: list[MemoryPrediction]
    safe_pod_count: int

    @staticmethod
    def compute(
        request: MemorySaturationRequest,
        raw_pods: list[dict[str, object]],
    ) -> MemorySaturationResult:
        critical: list[MemoryPrediction] = []
        safe_count = 0
        for raw in raw_pods:
            current = float(str(raw.get("current_mb", 0)))
            limit = raw.get("limit_mb")
            limit_val: float | None = float(str(limit)) if limit is not None else None
            growth = float(str(raw.get("growth_rate_mb_per_min", 0)))

            if limit_val is not None and growth > 0:
                minutes_to_sat = (limit_val - current) / growth
            elif limit_val is not None and growth <= 0:
                minutes_to_sat = None
            else:
                minutes_to_sat = (
                    (DEFAULT_NODE_CAPACITY_MB - current) / growth if growth > 0 else None
                )

            risk = PredictionRisk.STABLE
            if minutes_to_sat is not None and minutes_to_sat <= request.critical_threshold_minutes:
                risk = PredictionRisk.CRITICAL if minutes_to_sat <= 15 else PredictionRisk.AT_RISK

            p = MemoryPrediction(
                pod_name=str(raw.get("name", "")),
                namespace=str(raw.get("namespace", "")),
                current_memory_mb=current,
                limit_mb=limit_val,
                growth_rate_mb_per_min=growth,
                saturation_in_minutes=round(minutes_to_sat, 1)
                if minutes_to_sat is not None
                else None,
                otel_root_cause=None,
                risk=risk,
            )
            if risk in (PredictionRisk.CRITICAL, PredictionRisk.AT_RISK):
                critical.append(p)
            else:
                safe_count += 1
        return MemorySaturationResult(
            prediction_window_minutes=request.prediction_window_minutes,
            critical_pods=critical,
            safe_pod_count=safe_count,
        )

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class SLOStatus(Enum):
    PASS = "pass"
    FAIL = "fail"
    NO_DATA = "no_data"


@dataclass(frozen=True)
class LatencyPercentiles:
    p50_ms: float
    p95_ms: float
    p99_ms: float
    sample_count: int


@dataclass(frozen=True)
class LatencyPercentileRequest:
    endpoint: str
    time_window_minutes: int = 120
    slo_threshold_ms: float = 500.0


@dataclass(frozen=True)
class P99Result:
    endpoint: str
    time_window_minutes: int
    p50_ms: float
    p95_ms: float
    p99_ms: float
    slo_threshold_ms: float
    slo_status: SLOStatus
    slo_delta_ms: float
    sample_count: int
    reasons: list[str] = field(default_factory=list)

    @staticmethod
    def compute(
        request: LatencyPercentileRequest,
        percentiles: LatencyPercentiles,
    ) -> P99Result:
        if percentiles.sample_count == 0:
            return P99Result(
                endpoint=request.endpoint,
                time_window_minutes=request.time_window_minutes,
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                slo_threshold_ms=request.slo_threshold_ms,
                slo_status=SLOStatus.NO_DATA,
                slo_delta_ms=0.0,
                sample_count=0,
                reasons=["No traces found for this endpoint in the time window"],
            )

        delta = percentiles.p99_ms - request.slo_threshold_ms
        status = SLOStatus.PASS if delta <= 0 else SLOStatus.FAIL
        reasons: list[str] = []
        if status == SLOStatus.FAIL:
            reasons.append(f"p99 exceeds SLO by {abs(delta):.0f}ms")
        else:
            reasons.append(f"p99 within SLO (margin: {abs(delta):.0f}ms)")
        return P99Result(
            endpoint=request.endpoint,
            time_window_minutes=request.time_window_minutes,
            p50_ms=percentiles.p50_ms,
            p95_ms=percentiles.p95_ms,
            p99_ms=percentiles.p99_ms,
            slo_threshold_ms=request.slo_threshold_ms,
            slo_status=status,
            slo_delta_ms=delta,
            sample_count=percentiles.sample_count,
            reasons=reasons,
        )

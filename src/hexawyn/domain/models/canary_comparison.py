from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

REGRESSION_THRESHOLD_PCT: float = 10.0
ERROR_THRESHOLD_PCT: float = 0.5
MIN_SAMPLE: int = 500


class CanaryVerdict(Enum):
    SAFE = "safe"
    REGRESSION = "regression"
    INSUFFICIENT_DATA = "insufficient_data"


class ConfidenceLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass(frozen=True)
class VersionMetrics:
    version: str
    request_count: int
    p50_ms: float
    p95_ms: float
    p99_ms: float
    error_rate_pct: float


@dataclass(frozen=True)
class CanaryComparisonRequest:
    service_name: str
    time_window_minutes: int = 30
    traffic_split_pct: float = 5.0
    min_sample_threshold: int = MIN_SAMPLE


@dataclass(frozen=True)
class ComparisonResult:
    canary_version: str
    stable_version: str
    verdict: CanaryVerdict
    confidence: ConfidenceLevel
    p99_delta_pct: float
    error_rate_delta_pct: float
    canary_count: int
    stable_count: int
    traffic_split_pct: float
    reasons: list[str] = field(default_factory=list)

    @staticmethod
    def _compute_delta(canary_val: float, stable_val: float) -> float:
        if stable_val == 0:
            return 0.0
        return ((canary_val - stable_val) / stable_val) * 100.0

    @staticmethod
    def compute(
        canary: VersionMetrics,
        stable: VersionMetrics,
        traffic_split_pct: float,
        min_sample_threshold: int,
    ) -> ComparisonResult:
        reasons: list[str] = []
        p99_delta = ComparisonResult._compute_delta(canary.p99_ms, stable.p99_ms)
        error_delta = ComparisonResult._compute_delta(canary.error_rate_pct, stable.error_rate_pct)

        confidence = ConfidenceLevel.HIGH
        if canary.request_count < min_sample_threshold:
            confidence = ConfidenceLevel.LOW
        elif traffic_split_pct < 20.0:  # noqa: PLR2004
            confidence = ConfidenceLevel.MEDIUM

        if canary.request_count == 0 and stable.request_count == 0:
            return ComparisonResult(
                canary_version=canary.version,
                stable_version=stable.version,
                verdict=CanaryVerdict.INSUFFICIENT_DATA,
                confidence=ConfidenceLevel.LOW,
                p99_delta_pct=0.0,
                error_rate_delta_pct=0.0,
                canary_count=0,
                stable_count=0,
                traffic_split_pct=traffic_split_pct,
                reasons=["No data for either version"],
            )

        has_regression = False
        if p99_delta > REGRESSION_THRESHOLD_PCT:
            has_regression = True
            reasons.append(f"p99 latency increased by {p99_delta:.1f}%")
        if error_delta > ERROR_THRESHOLD_PCT:
            has_regression = True
            reasons.append(f"error rate increased by {error_delta:.1f}%")

        verdict = CanaryVerdict.REGRESSION if has_regression else CanaryVerdict.SAFE
        return ComparisonResult(
            canary_version=canary.version,
            stable_version=stable.version,
            verdict=verdict,
            confidence=confidence,
            p99_delta_pct=p99_delta,
            error_rate_delta_pct=error_delta,
            canary_count=canary.request_count,
            stable_count=stable.request_count,
            traffic_split_pct=traffic_split_pct,
            reasons=reasons,
        )

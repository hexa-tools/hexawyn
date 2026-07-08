from __future__ import annotations

from dataclasses import dataclass

P99_REGRESSION_THRESHOLD_PCT: float = 20.0
ERROR_REGRESSION_THRESHOLD_PCT: float = 0.5


@dataclass(frozen=True)
class VersionMetrics:
    version: str
    p50_ms: float
    p95_ms: float
    p99_ms: float
    error_rate_pct: float
    request_count: int


@dataclass(frozen=True)
class RegressionFlag:
    metric: str
    baseline_value: float
    current_value: float
    delta_pct: float
    severity: str


@dataclass(frozen=True)
class VersionComparisonRequest:
    service_name: str
    time_window_minutes: int = 120
    p99_threshold_pct: float = P99_REGRESSION_THRESHOLD_PCT
    error_threshold_pct: float = ERROR_REGRESSION_THRESHOLD_PCT


@dataclass(frozen=True)
class VersionComparisonResult:
    service_name: str
    baseline_version: str
    current_version: str
    p50_delta_pct: float
    p95_delta_pct: float
    p99_delta_pct: float
    error_delta_pct: float
    flags: list[RegressionFlag]
    verdict: str

    @staticmethod
    def _delta(before: float, after: float) -> float:
        if before == 0:
            return 0.0
        return ((after - before) / before) * 100.0

    @staticmethod
    def compute(
        request: VersionComparisonRequest,
        baseline: VersionMetrics,
        current: VersionMetrics,
    ) -> VersionComparisonResult:
        p50_d = VersionComparisonResult._delta(baseline.p50_ms, current.p50_ms)
        p95_d = VersionComparisonResult._delta(baseline.p95_ms, current.p95_ms)
        p99_d = VersionComparisonResult._delta(baseline.p99_ms, current.p99_ms)
        err_d = current.error_rate_pct - baseline.error_rate_pct

        flags: list[RegressionFlag] = []
        if p99_d >= request.p99_threshold_pct:
            flags.append(
                RegressionFlag(
                    metric="p99",
                    baseline_value=baseline.p99_ms,
                    current_value=current.p99_ms,
                    delta_pct=round(p99_d, 1),
                    severity="critical",
                )
            )
        if err_d >= request.error_threshold_pct:
            flags.append(
                RegressionFlag(
                    metric="error_rate",
                    baseline_value=baseline.error_rate_pct,
                    current_value=current.error_rate_pct,
                    delta_pct=round(err_d, 1),
                    severity="warning",
                )
            )

        verdict = "regression_detected" if flags else "no_regression"
        return VersionComparisonResult(
            service_name=request.service_name,
            baseline_version=baseline.version,
            current_version=current.version,
            p50_delta_pct=p50_d,
            p95_delta_pct=p95_d,
            p99_delta_pct=p99_d,
            error_delta_pct=err_d,
            flags=flags,
            verdict=verdict,
        )

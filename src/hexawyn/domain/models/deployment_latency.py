from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

REGRESSION_THRESHOLD_PCT: float = 20.0
MIN_POST_DEPLOY_SAMPLES: int = 10


class RegressionVerdict(Enum):
    REGRESSION = "regression"
    NO_REGRESSION = "no_regression"
    INCONCLUSIVE = "inconclusive"
    IMPROVED = "improved"


@dataclass(frozen=True)
class WindowLatency:
    p50_ms: float
    p95_ms: float
    p99_ms: float
    sample_count: int


@dataclass(frozen=True)
class DeploymentComparisonRequest:
    service_name: str
    regression_threshold_pct: float = REGRESSION_THRESHOLD_PCT
    min_samples: int = MIN_POST_DEPLOY_SAMPLES


@dataclass(frozen=True)
class DeploymentComparisonResult:
    service_name: str
    verdict: RegressionVerdict
    p50_delta_pct: float
    p95_delta_pct: float
    p99_delta_pct: float
    before: WindowLatency
    after: WindowLatency
    suggestion: str | None
    reasons: list[str] = field(default_factory=list)

    @staticmethod
    def _delta(before: float, after: float) -> float:
        if before == 0:
            return 0.0
        return ((after - before) / before) * 100.0

    @staticmethod
    def compute(
        request: DeploymentComparisonRequest,
        before: WindowLatency,
        after: WindowLatency,
    ) -> DeploymentComparisonResult:
        p50_d = DeploymentComparisonResult._delta(before.p50_ms, after.p50_ms)
        p95_d = DeploymentComparisonResult._delta(before.p95_ms, after.p95_ms)
        p99_d = DeploymentComparisonResult._delta(before.p99_ms, after.p99_ms)

        if after.sample_count < request.min_samples:
            return DeploymentComparisonResult(
                service_name=request.service_name,
                verdict=RegressionVerdict.INCONCLUSIVE,
                p50_delta_pct=p50_d,
                p95_delta_pct=p95_d,
                p99_delta_pct=p99_d,
                before=before,
                after=after,
                suggestion="Insufficient post-deployment samples",
                reasons=[
                    f"Only {after.sample_count} samples after deployment (min: {request.min_samples})"  # noqa: E501
                ],
            )

        reasons: list[str] = []
        if p99_d >= request.regression_threshold_pct:
            verdict = RegressionVerdict.REGRESSION
            reasons.append(
                f"p99 increased by {p99_d:.1f}% (exceeds {request.regression_threshold_pct}% threshold)"  # noqa: E501
            )
            suggestion = f"p99 regression of {p99_d:.1f}% exceeds {request.regression_threshold_pct}% threshold; consider rollback"  # noqa: E501
        elif p99_d <= -request.regression_threshold_pct:
            verdict = RegressionVerdict.IMPROVED
            reasons.append(f"p99 improved by {abs(p99_d):.1f}%")
            suggestion = (
                f"Latency improved by {abs(p99_d):.1f}% after deployment — no action needed"
            )
        else:
            verdict = RegressionVerdict.NO_REGRESSION
            reasons.append(f"p99 change of {p99_d:.1f}% is within threshold")
            suggestion = None

        return DeploymentComparisonResult(
            service_name=request.service_name,
            verdict=verdict,
            p50_delta_pct=p50_d,
            p95_delta_pct=p95_d,
            p99_delta_pct=p99_d,
            before=before,
            after=after,
            suggestion=suggestion,
            reasons=reasons,
        )

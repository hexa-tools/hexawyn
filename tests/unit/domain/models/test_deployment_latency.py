from __future__ import annotations

from hexawyn.domain.models.deployment_latency import (
    DeploymentComparisonRequest,
    DeploymentComparisonResult,
    RegressionVerdict,
    WindowLatency,
)


class TestWindowLatency:
    def test_create(self) -> None:
        wl = WindowLatency(p50_ms=85.0, p95_ms=180.0, p99_ms=210.0, sample_count=5000)
        assert wl.p99_ms == 210.0


class TestDeploymentComparisonResult:
    def test_regression(self) -> None:
        before = WindowLatency(p50_ms=85.0, p95_ms=180.0, p99_ms=210.0, sample_count=5000)
        after = WindowLatency(p50_ms=92.0, p95_ms=310.0, p99_ms=450.0, sample_count=4000)
        result = DeploymentComparisonResult.compute(
            request=DeploymentComparisonRequest(service_name="payment-service"),
            before=before,
            after=after,
        )
        assert result.verdict == RegressionVerdict.REGRESSION
        assert result.p99_delta_pct > 100
        assert result.suggestion is not None

    def test_no_regression(self) -> None:
        before = WindowLatency(p50_ms=85.0, p95_ms=180.0, p99_ms=210.0, sample_count=5000)
        after = WindowLatency(p50_ms=88.0, p95_ms=190.0, p99_ms=225.0, sample_count=4000)
        result = DeploymentComparisonResult.compute(
            request=DeploymentComparisonRequest(service_name="svc"),
            before=before,
            after=after,
        )
        assert result.verdict == RegressionVerdict.NO_REGRESSION

    def test_insufficient_data(self) -> None:
        before = WindowLatency(p50_ms=85.0, p95_ms=180.0, p99_ms=210.0, sample_count=5000)
        after = WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=3)
        result = DeploymentComparisonResult.compute(
            request=DeploymentComparisonRequest(service_name="svc"),
            before=before,
            after=after,
        )
        assert result.verdict == RegressionVerdict.INCONCLUSIVE

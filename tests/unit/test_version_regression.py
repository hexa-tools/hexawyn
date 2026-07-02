from __future__ import annotations

from hexawyn.domain.models.version_regression import (
    VersionComparisonRequest,
    VersionComparisonResult,
    VersionMetrics,
)


class TestVersionMetrics:
    def test_create(self) -> None:
        vm = VersionMetrics(
            version="v1.2",
            p50_ms=45.0,
            p95_ms=120.0,
            p99_ms=150.0,
            error_rate_pct=0.1,
            request_count=5000,
        )
        assert vm.version == "v1.2"
        assert vm.p99_ms == 150.0


class TestVersionComparisonResult:
    def test_regression(self) -> None:
        baseline = VersionMetrics(
            version="v1.2",
            p50_ms=45.0,
            p95_ms=120.0,
            p99_ms=150.0,
            error_rate_pct=0.1,
            request_count=5000,
        )
        current = VersionMetrics(
            version="v1.3",
            p50_ms=52.0,
            p95_ms=250.0,
            p99_ms=380.0,
            error_rate_pct=0.8,
            request_count=4000,
        )
        result = VersionComparisonResult.compute(
            request=VersionComparisonRequest(service_name="recommendation-service"),
            baseline=baseline,
            current=current,
        )
        assert result.baseline_version == "v1.2"
        assert len(result.flags) >= 2
        assert any(f.metric == "p99" for f in result.flags)

    def test_no_regression(self) -> None:
        baseline = VersionMetrics(
            version="v1.2",
            p50_ms=45.0,
            p95_ms=120.0,
            p99_ms=150.0,
            error_rate_pct=0.1,
            request_count=5000,
        )
        current = VersionMetrics(
            version="v1.3",
            p50_ms=48.0,
            p95_ms=125.0,
            p99_ms=160.0,
            error_rate_pct=0.15,
            request_count=4000,
        )
        result = VersionComparisonResult.compute(
            request=VersionComparisonRequest(service_name="svc"),
            baseline=baseline,
            current=current,
        )
        assert len(result.flags) == 0

    def test_error_rate_regression(self) -> None:
        baseline = VersionMetrics(
            version="v1.2",
            p50_ms=45.0,
            p95_ms=120.0,
            p99_ms=150.0,
            error_rate_pct=0.1,
            request_count=5000,
        )
        current = VersionMetrics(
            version="v1.3",
            p50_ms=48.0,
            p95_ms=130.0,
            p99_ms=160.0,
            error_rate_pct=0.8,
            request_count=4000,
        )
        result = VersionComparisonResult.compute(
            request=VersionComparisonRequest(service_name="svc"),
            baseline=baseline,
            current=current,
        )
        assert len(result.flags) == 1
        assert result.flags[0].metric == "error_rate"

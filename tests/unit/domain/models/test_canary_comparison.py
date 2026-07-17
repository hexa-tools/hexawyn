from __future__ import annotations

from hexawyn.domain.models.canary_comparison import (
    CanaryComparisonRequest,
    CanaryVerdict,
    ComparisonResult,
    ConfidenceLevel,
    VersionMetrics,
)


class TestVersionMetrics:
    def test_create(self) -> None:
        vm = VersionMetrics(
            version="v2.4",
            request_count=500,
            p50_ms=120.0,
            p95_ms=350.0,
            p99_ms=480.0,
            error_rate_pct=2.1,
        )
        assert vm.version == "v2.4"
        assert vm.p99_ms == 480.0
        assert vm.error_rate_pct == 2.1


class TestCanaryComparisonRequest:
    def test_create(self) -> None:
        req = CanaryComparisonRequest(
            service_name="order-service",
            time_window_minutes=30,
            traffic_split_pct=5.0,
            min_sample_threshold=500,
        )
        assert req.service_name == "order-service"
        assert req.traffic_split_pct == 5.0
        assert req.min_sample_threshold == 500

    def test_defaults(self) -> None:
        req = CanaryComparisonRequest(service_name="svc")
        assert req.time_window_minutes == 30
        assert req.min_sample_threshold == 500


class TestComparisonResult:
    def test_canary_regression(self) -> None:
        stable = VersionMetrics(
            version="v2.3",
            request_count=9500,
            p50_ms=10.0,
            p95_ms=150.0,
            p99_ms=210.0,
            error_rate_pct=0.1,
        )
        canary = VersionMetrics(
            version="v2.4",
            request_count=500,
            p50_ms=15.0,
            p95_ms=380.0,
            p99_ms=480.0,
            error_rate_pct=2.1,
        )
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=5.0,
            min_sample_threshold=500,
        )
        assert result.verdict == CanaryVerdict.REGRESSION
        assert result.confidence == ConfidenceLevel.MEDIUM
        assert result.p99_delta_pct > 100
        assert result.error_rate_delta_pct > 1.0

    def test_canary_safe(self) -> None:
        stable = VersionMetrics(
            version="v2.3",
            request_count=9500,
            p50_ms=10.0,
            p95_ms=150.0,
            p99_ms=210.0,
            error_rate_pct=0.1,
        )
        canary = VersionMetrics(
            version="v2.4",
            request_count=8000,
            p50_ms=9.0,
            p95_ms=145.0,
            p99_ms=205.0,
            error_rate_pct=0.1,
        )
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=50.0,
            min_sample_threshold=500,
        )
        assert result.verdict == CanaryVerdict.SAFE
        assert result.confidence == ConfidenceLevel.HIGH

    def test_low_confidence(self) -> None:
        stable = VersionMetrics(
            version="v2.3",
            request_count=9500,
            p50_ms=10.0,
            p95_ms=150.0,
            p99_ms=210.0,
            error_rate_pct=0.1,
        )
        canary = VersionMetrics(
            version="v2.4",
            request_count=50,
            p50_ms=10.0,
            p95_ms=150.0,
            p99_ms=210.0,
            error_rate_pct=0.1,
        )
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=1.0,
            min_sample_threshold=500,
        )
        assert result.confidence == ConfidenceLevel.LOW

    def test_insufficient_data(self) -> None:
        stable = VersionMetrics(
            version="v2.3", request_count=0, p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, error_rate_pct=0.0
        )
        canary = VersionMetrics(
            version="v2.4", request_count=0, p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, error_rate_pct=0.0
        )
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=10.0,
            min_sample_threshold=500,
        )
        assert result.verdict == CanaryVerdict.INSUFFICIENT_DATA

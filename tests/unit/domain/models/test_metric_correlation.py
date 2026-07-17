from __future__ import annotations

from hexawyn.domain.models.metric_correlation import (
    CorrelationRequest,
    CorrelationResult,
    CorrelationStatus,
    TimeSeries,
)


class TestTimeSeries:
    def test_create(self) -> None:
        ts = TimeSeries(
            label="api-gateway-5xx", data_points=[0.01, 0.01, 0.45, 0.82, 0.91, 0.30, 0.02]
        )
        assert ts.label == "api-gateway-5xx"
        assert len(ts.data_points) == 7


class TestCorrelationResult:
    def test_correlated(self) -> None:
        a = TimeSeries(label="5xx", data_points=[0.01, 0.01, 0.45, 0.82, 0.91, 0.30, 0.02])
        b = TimeSeries(label="latency", data_points=[80.0, 85.0, 320.0, 750.0, 820.0, 410.0, 90.0])
        result = CorrelationResult.compute(
            request=CorrelationRequest(
                primary_service="api-gateway",
                correlated_service="auth-service",
                time_window_minutes=30,
            ),
            series_a=a,
            series_b=b,
        )
        assert result.status == CorrelationStatus.CORRELATED
        assert result.coefficient > 0.9

    def test_uncorrelated(self) -> None:
        a = TimeSeries(label="5xx", data_points=[1.0, 2.0, 1.0, 2.0, 1.0])
        b = TimeSeries(label="latency", data_points=[100.0, 100.0, 100.0, 100.0, 100.0])
        result = CorrelationResult.compute(
            request=CorrelationRequest(
                primary_service="svc-a", correlated_service="svc-b", time_window_minutes=10
            ),
            series_a=a,
            series_b=b,
        )
        assert result.status == CorrelationStatus.UNCORRELATED

    def test_insufficient_data(self) -> None:
        a = TimeSeries(label="5xx", data_points=[1.0])
        b = TimeSeries(label="latency", data_points=[100.0])
        result = CorrelationResult.compute(
            request=CorrelationRequest(
                primary_service="svc-a", correlated_service="svc-b", time_window_minutes=1
            ),
            series_a=a,
            series_b=b,
        )
        assert result.status == CorrelationStatus.INCONCLUSIVE

    def test_negative_correlation(self) -> None:
        a = TimeSeries(label="5xx", data_points=[0.9, 0.7, 0.5, 0.3, 0.1])
        b = TimeSeries(label="latency", data_points=[100.0, 300.0, 500.0, 700.0, 900.0])
        result = CorrelationResult.compute(
            request=CorrelationRequest(
                primary_service="svc-a", correlated_service="svc-b", time_window_minutes=5
            ),
            series_a=a,
            series_b=b,
        )
        assert result.status == CorrelationStatus.UNCORRELATED
        assert result.coefficient < -0.5

    def test_moderate_correlation_inconclusive(self) -> None:
        a = TimeSeries(label="5xx", data_points=[0.1, 0.5, 0.2, 0.8, 0.1, 0.6, 0.3])
        b = TimeSeries(
            label="latency", data_points=[150.0, 250.0, 300.0, 200.0, 400.0, 180.0, 350.0]
        )
        result = CorrelationResult.compute(
            request=CorrelationRequest(
                primary_service="svc-a", correlated_service="svc-b", time_window_minutes=5
            ),
            series_a=a,
            series_b=b,
        )
        assert result.status == CorrelationStatus.INCONCLUSIVE
        assert "moderate" in result.hypothesis.lower()

from __future__ import annotations

from unittest.mock import patch


class TestOtelCorrelationAdapterUnit:
    def test_returns_timeseries(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_correlation_adapter import (
            OTelPrometheusCorrelationAdapter,
        )
        from hexawyn.domain.models.metric_correlation import CorrelationRequest

        adapter = OTelPrometheusCorrelationAdapter()
        result = adapter.fetch_primary_series(
            CorrelationRequest(primary_service="svc-a", correlated_service="svc-b")
        )
        assert result.label == "primary"

    def test_empty_primary_service_returns_empty_series(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_correlation_adapter import (
            OTelPrometheusCorrelationAdapter,
        )
        from hexawyn.domain.models.metric_correlation import CorrelationRequest

        adapter = OTelPrometheusCorrelationAdapter()
        result = adapter.fetch_primary_series(
            CorrelationRequest(primary_service="", correlated_service="svc-b")
        )
        assert result.label == "primary"
        assert result.data_points == []

    def test_fetch_correlated_series_with_data(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_correlation_adapter import (
            OTelPrometheusCorrelationAdapter,
        )
        from hexawyn.domain.models.metric_correlation import CorrelationRequest

        mock_metrics = [
            {"value": 10.5, "labels": {"pod": "pod-a"}},
            {"value": 20.0, "labels": {"pod": "pod-b"}},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_correlation_adapter.query_prometheus_instant",
            return_value=mock_metrics,
        ):
            adapter = OTelPrometheusCorrelationAdapter()
            result = adapter.fetch_correlated_series(
                CorrelationRequest(primary_service="svc-a", correlated_service="svc-b")
            )
            assert result.label == "correlated"
            assert len(result.data_points) == 2  # noqa: PLR2004

    def test_fetch_correlated_series_empty_service(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_correlation_adapter import (
            OTelPrometheusCorrelationAdapter,
        )
        from hexawyn.domain.models.metric_correlation import CorrelationRequest

        adapter = OTelPrometheusCorrelationAdapter()
        result = adapter.fetch_correlated_series(
            CorrelationRequest(primary_service="svc-a", correlated_service="")
        )
        assert result.label == "correlated"
        assert result.data_points == []

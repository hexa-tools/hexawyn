# Auto-generated test for otel_correlation_adapter

from __future__ import annotations


class TestOtelCorrelationAdapterUnit:
    def test_returns_timeseries(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_correlation_adapter import (
            OTelPrometheusCorrelationAdapter,
        )
        from hexawyn.domain.models.metric_correlation import CorrelationRequest

        adapter = OTelPrometheusCorrelationAdapter()
        result = adapter.fetch_primary_series(
            CorrelationRequest(primary_service="svc-a", correlated_service="svc-b")
        )  # noqa: E501
        assert result.label == "primary"

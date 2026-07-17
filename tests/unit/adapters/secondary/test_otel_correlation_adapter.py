from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_correlation_adapter import (
    OTelPrometheusCorrelationAdapter,
)
from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.domain.models.metric_correlation import CorrelationRequest


class TestOTelCorrelationAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelPrometheusCorrelationAdapter(), MetricCorrelationPort)

    def test_fetch_primary_returns_empty(self) -> None:
        r = OTelPrometheusCorrelationAdapter().fetch_primary_series(CorrelationRequest("a", "b"))
        assert r.data_points == []

    def test_fetch_correlated_returns_empty(self) -> None:
        r = OTelPrometheusCorrelationAdapter().fetch_correlated_series(CorrelationRequest("a", "b"))
        assert r.data_points == []

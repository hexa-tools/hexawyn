from __future__ import annotations

from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.domain.models.metric_correlation import CorrelationRequest, TimeSeries


class OTelPrometheusCorrelationAdapter(MetricCorrelationPort):
    def fetch_primary_series(self, request: CorrelationRequest) -> TimeSeries:
        return TimeSeries(label="primary", data_points=[])

    def fetch_correlated_series(self, request: CorrelationRequest) -> TimeSeries:
        return TimeSeries(label="correlated", data_points=[])

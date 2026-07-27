from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import (
    query_prometheus_instant,
)
from hexawyn.application.ports.driven.metric_correlation_port import (
    MetricCorrelationPort,
)
from hexawyn.domain.models.metric_correlation import CorrelationRequest, TimeSeries


class OTelPrometheusCorrelationAdapter(MetricCorrelationPort):
    def fetch_primary_series(self, request: CorrelationRequest) -> TimeSeries:
        query = (
            f'rate(http_request_duration_seconds_count{{service="{request.primary_service}"}}[5m])'  # noqa: E501
        )
        if not request.primary_service:
            return TimeSeries(label="primary", data_points=[])

        metrics = query_prometheus_instant(query)
        data_points = [(m["value"], m["labels"].get("pod", "")) for m in metrics]
        return TimeSeries(label="primary", data_points=data_points)  # type: ignore

    def fetch_correlated_series(self, request: CorrelationRequest) -> TimeSeries:
        query = f'rate(http_request_duration_seconds_count{{service="{request.correlated_service}"}}[5m])'  # noqa: E501
        if not request.correlated_service:
            return TimeSeries(label="correlated", data_points=[])

        metrics = query_prometheus_instant(query)
        data_points = [(m["value"], m["labels"].get("pod", "")) for m in metrics]
        return TimeSeries(label="correlated", data_points=data_points)  # type: ignore

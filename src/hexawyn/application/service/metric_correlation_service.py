from __future__ import annotations

from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.application.ports.driving.metric_correlation.metric_correlation_command import (
    MetricCorrelationCommand,
)
from hexawyn.application.ports.driving.metric_correlation.metric_correlation_response import (
    MetricCorrelationResponse,
)
from hexawyn.application.ports.driving.metric_correlation.metric_correlation_service_port import (
    MetricCorrelationServicePort,
)
from hexawyn.domain.models.metric_correlation import CorrelationRequest, CorrelationResult


class MetricCorrelationService(MetricCorrelationServicePort):
    def __init__(self, port: MetricCorrelationPort) -> None:
        self._port = port

    def correlate(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,
            lag_index=r.lag_index,
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

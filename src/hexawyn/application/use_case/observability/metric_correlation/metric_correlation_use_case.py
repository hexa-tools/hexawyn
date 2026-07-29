from __future__ import annotations

from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.application.use_case.observability.metric_correlation.command import (
    MetricCorrelationCommand,
)
from hexawyn.application.use_case.observability.metric_correlation.response import (
    MetricCorrelationResponse,
)
from hexawyn.domain.models.metric_correlation import CorrelationRequest, CorrelationResult


class MetricCorrelationUseCase:
    def __init__(self, port: MetricCorrelationPort) -> None:
        self._port = port

    def execute(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
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
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

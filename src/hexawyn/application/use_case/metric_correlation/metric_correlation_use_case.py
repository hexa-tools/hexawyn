from __future__ import annotations

from hexawyn.application.ports.driving.metric_correlation.metric_correlation_command import (
    MetricCorrelationCommand,
)
from hexawyn.application.ports.driving.metric_correlation.metric_correlation_response import (
    MetricCorrelationResponse,
)
from hexawyn.application.ports.driving.metric_correlation.metric_correlation_service_port import (
    MetricCorrelationServicePort,
)


class MetricCorrelationUseCase:
    def __init__(self, service: MetricCorrelationServicePort) -> None:
        self._svc = service

    def execute(self, cmd: MetricCorrelationCommand) -> MetricCorrelationResponse:
        return self._svc.correlate(cmd)

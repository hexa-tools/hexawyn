from dataclasses import asdict

from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.application.use_case.metric_correlation.command import MetricCorrelationCommand
from hexawyn.application.use_case.metric_correlation.response import MetricCorrelationResponse


class MetricCorrelationUseCase:
    def __init__(self, port: MetricCorrelationPort) -> None:
        self._port = port

    def execute(self, c: MetricCorrelationCommand) -> MetricCorrelationResponse:
        results = self._port.correlate(
            service_name=c.service_name, lookback_minutes=c.lookback_minutes
        )
        return MetricCorrelationResponse(correlations=[asdict(r) for r in results])

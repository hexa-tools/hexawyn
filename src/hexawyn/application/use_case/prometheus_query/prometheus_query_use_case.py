from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.use_case.prometheus_query.command import PrometheusQueryCommand
from hexawyn.application.use_case.prometheus_query.response import PrometheusQueryResponse


class PrometheusQueryUseCase:
    def __init__(self, port: MetricsQueryPort) -> None:
        self._port = port

    def execute(self, command: PrometheusQueryCommand) -> PrometheusQueryResponse:
        return PrometheusQueryResponse()

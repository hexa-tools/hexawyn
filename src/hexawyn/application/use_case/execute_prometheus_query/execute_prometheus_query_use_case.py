from __future__ import annotations

from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_response import (
    ExecutePrometheusQueryResponse,
)
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_service_port import (
    ExecutePrometheusQueryServicePort,
)


class ExecutePrometheusQueryUseCase:
    def __init__(self, service: ExecutePrometheusQueryServicePort) -> None:
        self._svc = service

    def execute(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        return self._svc.execute(command)

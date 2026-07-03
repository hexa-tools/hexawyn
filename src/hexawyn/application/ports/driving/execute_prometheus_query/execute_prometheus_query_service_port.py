from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_response import (
    ExecutePrometheusQueryResponse,
)


class ExecutePrometheusQueryServicePort(ABC):
    @abstractmethod
    def execute(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse: ...

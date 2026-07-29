from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.execute_prometheus_query.command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.execute_prometheus_query.response import (
    ExecutePrometheusQueryResponse,
)


class ExecutePrometheusQueryServicePort(ABC):
    @abstractmethod
    def execute(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse: ...

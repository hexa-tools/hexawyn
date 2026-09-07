from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.execute_prometheus_query.command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.execute_prometheus_query.response import (
    ExecutePrometheusQueryResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ExecutePrometheusQueryServicePort(ABC):
    @abstractmethod
    def execute(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse: ...

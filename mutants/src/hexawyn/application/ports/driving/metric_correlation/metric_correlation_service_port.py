from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.metric_correlation.command import (
    MetricCorrelationCommand,
)
from hexawyn.application.use_case.observability.metric_correlation.response import (
    MetricCorrelationResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class MetricCorrelationServicePort(ABC):
    @abstractmethod
    def correlate(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse: ...

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.span_bottleneck_analysis.command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.observability.span_bottleneck_analysis.response import (
    SpanBottleneckAnalysisResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SpanBottleneckAnalysisServicePort(ABC):
    @abstractmethod
    def analyze(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse: ...

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.span_bottleneck_analysis.command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.observability.span_bottleneck_analysis.response import (
    SpanBottleneckAnalysisResponse,
)


class SpanBottleneckAnalysisServicePort(ABC):
    @abstractmethod
    def analyze(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse: ...

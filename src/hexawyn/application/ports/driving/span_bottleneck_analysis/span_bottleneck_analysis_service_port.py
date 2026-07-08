from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_response import (
    SpanBottleneckAnalysisResponse,
)


class SpanBottleneckAnalysisServicePort(ABC):
    @abstractmethod
    def analyze(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse: ...

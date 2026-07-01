from __future__ import annotations

from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_response import (
    SpanBottleneckAnalysisResponse,
)
from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_service_port import (
    SpanBottleneckAnalysisServicePort,
)


class SpanBottleneckAnalysisUseCase:
    def __init__(self, service: SpanBottleneckAnalysisServicePort) -> None:
        self._svc = service

    def execute(self, cmd: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        return self._svc.analyze(cmd)

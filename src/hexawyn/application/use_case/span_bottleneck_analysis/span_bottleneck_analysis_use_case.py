from dataclasses import asdict

from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.application.use_case.span_bottleneck_analysis.command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.span_bottleneck_analysis.response import (
    SpanBottleneckAnalysisResponse,
)


class SpanBottleneckAnalysisUseCase:
    def __init__(self, port: SpanBottleneckPort) -> None:
        self._port = port

    def execute(self, c: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        bottlenecks = self._port.find_bottlenecks(
            service_name=c.service_name, lookback_minutes=c.lookback_minutes
        )
        return SpanBottleneckAnalysisResponse(bottlenecks=[asdict(b) for b in bottlenecks])

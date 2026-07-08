from __future__ import annotations

from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_response import (
    SpanBottleneckAnalysisResponse,
)
from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_service_port import (
    SpanBottleneckAnalysisServicePort,
)
from hexawyn.domain.models.span_bottleneck import BottleneckRequest, BottleneckResult


class SpanBottleneckAnalysisService(SpanBottleneckAnalysisServicePort):
    def __init__(self, port: SpanBottleneckPort) -> None:
        self._port = port

    def analyze(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,
            redis_slowest=result.redis_breakdown.slowest_operation
            if result.redis_breakdown
            else None,
            reasons=result.reasons,
        )

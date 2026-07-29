from __future__ import annotations

from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.application.use_case.observability.span_bottleneck_analysis.command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.observability.span_bottleneck_analysis.response import (
    SpanBottleneckAnalysisResponse,
)
from hexawyn.domain.models.span_bottleneck import BottleneckRequest, BottleneckResult


class SpanBottleneckAnalysisUseCase:
    def __init__(self, port: SpanBottleneckPort) -> None:
        self._port = port

    def execute(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

from __future__ import annotations

from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.domain.models.span_bottleneck import BottleneckRequest, SpanBreakdown


class OTelSpanBreakdownAdapter(SpanBottleneckPort):
    def fetch_db_spans(self, request: BottleneckRequest) -> SpanBreakdown:
        return SpanBreakdown(
            category="db", avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
        )

    def fetch_redis_spans(self, request: BottleneckRequest) -> SpanBreakdown | None:
        return None

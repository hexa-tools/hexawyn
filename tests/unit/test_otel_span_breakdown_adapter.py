from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
    OTelSpanBreakdownAdapter,
)
from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.domain.models.span_bottleneck import BottleneckRequest


class TestOTelSpanBreakdownAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelSpanBreakdownAdapter(), SpanBottleneckPort)

    def test_fetch_db_returns_default(self) -> None:
        result = OTelSpanBreakdownAdapter().fetch_db_spans(BottleneckRequest())
        assert result.category == "db"
        assert result.avg_ms == 0.0

    def test_fetch_redis_returns_none(self) -> None:
        result = OTelSpanBreakdownAdapter().fetch_redis_spans(BottleneckRequest())
        assert result is None

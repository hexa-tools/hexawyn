# Auto-generated test for otel_span_breakdown_adapter

from __future__ import annotations


class TestOtelSpanBreakdownAdapterUnit:
    def test_returns_breakdown(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
            OTelSpanBreakdownAdapter,
        )
        from hexawyn.domain.models.span_bottleneck import BottleneckRequest

        adapter = OTelSpanBreakdownAdapter()
        result = adapter.fetch_db_spans(BottleneckRequest())
        assert result.category == "db"

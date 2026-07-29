from __future__ import annotations

from hexawyn.domain.models.redundant_calls import (
    RedundancyType,
    RedundantCallRequest,
    RedundantCallResult,
    SpanInfo,
)


class TestSpanInfo:
    def test_create(self) -> None:
        s = SpanInfo(
            span_name="SELECT * FROM products WHERE id = ?",
            service_name="db-service",
            duration_ms=15.0,
        )
        assert s.span_name == "SELECT * FROM products WHERE id = ?"


class TestRedundantCallResult:
    def test_n_plus_one(self) -> None:
        spans = [
            SpanInfo(
                span_name="SELECT * FROM products WHERE id = ?",
                service_name="db-service",
                duration_ms=15.0,
            )
            for _ in range(47)
        ]
        result = RedundantCallResult.compute(
            request=RedundantCallRequest(flow="web -> api -> db"),
            spans=spans,
        )
        assert len(result.patterns) >= 1
        n1 = [p for p in result.patterns if p.type == RedundancyType.N_PLUS_ONE]
        assert len(n1) == 1
        assert n1[0].occurrences == 47  # noqa: PLR2004

    def test_duplicate(self) -> None:
        spans = [
            SpanInfo(span_name="GET cache:user:123", service_name="api-service", duration_ms=2.0),
            SpanInfo(span_name="GET cache:user:123", service_name="api-service", duration_ms=3.0),
        ]
        result = RedundantCallResult.compute(
            request=RedundantCallRequest(flow="web -> api"),
            spans=spans,
        )
        assert any(p.type == RedundancyType.DUPLICATE for p in result.patterns)

    def test_no_redundancy(self) -> None:
        spans = [
            SpanInfo(span_name="SELECT * FROM orders", service_name="db-service", duration_ms=50.0),
            SpanInfo(
                span_name="SELECT * FROM products", service_name="db-service", duration_ms=30.0
            ),
        ]
        result = RedundantCallResult.compute(
            request=RedundantCallRequest(flow="web -> api"),
            spans=spans,
        )
        assert result.patterns == []

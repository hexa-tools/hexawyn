from __future__ import annotations

from hexawyn.domain.models.span_bottleneck import (
    BottleneckCategory,
    BottleneckConfidence,
    BottleneckRequest,
    BottleneckResult,
    SpanBreakdown,
)


class TestSpanBreakdown:
    def test_db_breakdown(self) -> None:
        b = SpanBreakdown(
            category="db",
            avg_ms=380.0,
            p95_ms=650.0,
            max_ms=1200.0,
            slowest_operation="SELECT * FROM orders WHERE user_id = ? LIMIT 1000",
        )
        assert b.category == "db"
        assert b.avg_ms == 380.0
        assert b.slowest_operation is not None

    def test_redis_breakdown(self) -> None:
        b = SpanBreakdown(
            category="redis",
            avg_ms=6.0,
            p95_ms=15.0,
            max_ms=45.0,
            slowest_operation="HGETALL session:user:123",
        )
        assert b.category == "redis"


class TestBottleneckResult:
    def test_db_bottleneck_high_confidence(self) -> None:
        db = SpanBreakdown(
            category="db",
            avg_ms=420.0,
            p95_ms=650.0,
            max_ms=1200.0,
            slowest_operation="SELECT * FROM orders",
        )
        redis = SpanBreakdown(
            category="redis", avg_ms=8.0, p95_ms=15.0, max_ms=45.0, slowest_operation="GET user:123"
        )
        result = BottleneckResult.compute(
            request=BottleneckRequest(time_window_minutes=30), db_spans=db, redis_spans=redis
        )
        assert result.bottleneck == BottleneckCategory.DB
        assert result.confidence == BottleneckConfidence.HIGH

    def test_redis_bottleneck(self) -> None:
        db = SpanBreakdown(
            category="db", avg_ms=50.0, p95_ms=80.0, max_ms=120.0, slowest_operation="SELECT 1"
        )
        redis = SpanBreakdown(
            category="redis",
            avg_ms=200.0,
            p95_ms=350.0,
            max_ms=500.0,
            slowest_operation="HGETALL big:key",
        )
        result = BottleneckResult.compute(
            request=BottleneckRequest(), db_spans=db, redis_spans=redis
        )
        assert result.bottleneck == BottleneckCategory.REDIS
        assert result.confidence == BottleneckConfidence.HIGH

    def test_no_bottleneck_both_fast(self) -> None:
        db = SpanBreakdown(
            category="db", avg_ms=5.0, p95_ms=10.0, max_ms=15.0, slowest_operation="SELECT 1"
        )
        redis = SpanBreakdown(
            category="redis", avg_ms=3.0, p95_ms=8.0, max_ms=12.0, slowest_operation="GET k"
        )
        result = BottleneckResult.compute(
            request=BottleneckRequest(), db_spans=db, redis_spans=redis
        )
        assert result.bottleneck == BottleneckCategory.NEITHER

    def test_db_only_no_redis_spans(self) -> None:
        db = SpanBreakdown(
            category="db",
            avg_ms=350.0,
            p95_ms=500.0,
            max_ms=800.0,
            slowest_operation="SELECT * FROM items",
        )
        result = BottleneckResult.compute(
            request=BottleneckRequest(), db_spans=db, redis_spans=None
        )
        assert result.bottleneck == BottleneckCategory.DB
        assert result.confidence == BottleneckConfidence.MEDIUM

    def test_medium_confidence(self) -> None:
        db = SpanBreakdown(
            category="db",
            avg_ms=120.0,
            p95_ms=200.0,
            max_ms=300.0,
            slowest_operation="SELECT * FROM x",
        )
        redis = SpanBreakdown(
            category="redis", avg_ms=40.0, p95_ms=100.0, max_ms=150.0, slowest_operation="GET y"
        )
        result = BottleneckResult.compute(
            request=BottleneckRequest(), db_spans=db, redis_spans=redis
        )
        assert result.confidence == BottleneckConfidence.MEDIUM

    def test_redis_medium_confidence(self) -> None:
        db = SpanBreakdown(
            category="db", avg_ms=40.0, p95_ms=80.0, max_ms=120.0, slowest_operation="SELECT 1"
        )
        redis = SpanBreakdown(
            category="redis",
            avg_ms=120.0,
            p95_ms=200.0,
            max_ms=300.0,
            slowest_operation="GET big:key",
        )
        result = BottleneckResult.compute(
            request=BottleneckRequest(), db_spans=db, redis_spans=redis
        )
        assert result.bottleneck == BottleneckCategory.REDIS
        assert result.confidence == BottleneckConfidence.MEDIUM

    def test_no_clear_bottleneck_close_ratio(self) -> None:
        db = SpanBreakdown(
            category="db", avg_ms=40.0, p95_ms=80.0, max_ms=120.0, slowest_operation="SELECT x"
        )
        redis = SpanBreakdown(
            category="redis", avg_ms=30.0, p95_ms=50.0, max_ms=80.0, slowest_operation="GET y"
        )
        result = BottleneckResult.compute(
            request=BottleneckRequest(), db_spans=db, redis_spans=redis
        )
        assert result.bottleneck == BottleneckCategory.NEITHER
        assert result.confidence == BottleneckConfidence.LOW

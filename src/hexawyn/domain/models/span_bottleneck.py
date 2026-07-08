from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

THRESHOLD_SLOW_MS: float = 20.0
HIGH_CONFIDENCE_RATIO: float = 4.0
MEDIUM_CONFIDENCE_RATIO: float = 2.0


class BottleneckCategory(Enum):
    DB = "db"
    REDIS = "redis"
    NEITHER = "neither"


class BottleneckConfidence(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass(frozen=True)
class SpanBreakdown:
    category: str
    avg_ms: float
    p95_ms: float
    max_ms: float
    slowest_operation: str | None


@dataclass(frozen=True)
class BottleneckRequest:
    time_window_minutes: int = 30


@dataclass(frozen=True)
class BottleneckResult:
    bottleneck: BottleneckCategory
    confidence: BottleneckConfidence
    db_breakdown: SpanBreakdown | None
    redis_breakdown: SpanBreakdown | None
    bottleneck_pct_of_total: float
    reasons: list[str] = field(default_factory=list)

    @staticmethod
    def compute(
        request: BottleneckRequest,
        db_spans: SpanBreakdown,
        redis_spans: SpanBreakdown | None = None,
    ) -> BottleneckResult:
        reasons: list[str] = []
        db_avg = db_spans.avg_ms
        redis_avg = redis_spans.avg_ms if redis_spans else 0.0
        total = db_avg + redis_avg

        if redis_spans is None:
            pct = 100.0 if total == 0 else (db_avg / total) * 100.0 if total > 0 else 100.0
            return BottleneckResult(
                bottleneck=BottleneckCategory.DB,
                confidence=BottleneckConfidence.MEDIUM,
                db_breakdown=db_spans,
                redis_breakdown=None,
                bottleneck_pct_of_total=pct,
                reasons=["Only DB spans found in traces"],
            )

        if db_avg <= THRESHOLD_SLOW_MS and redis_spans.avg_ms <= THRESHOLD_SLOW_MS:
            return BottleneckResult(
                bottleneck=BottleneckCategory.NEITHER,
                confidence=BottleneckConfidence.LOW,
                db_breakdown=db_spans,
                redis_breakdown=redis_spans,
                bottleneck_pct_of_total=0.0,
                reasons=["Both DB and Redis are fast (<20ms average)"],
            )

        ratio = db_avg / redis_avg if redis_avg > 0 else float("inf")

        if ratio >= HIGH_CONFIDENCE_RATIO:
            bottleneck = BottleneckCategory.DB
            confidence = BottleneckConfidence.HIGH
            reasons.append(f"DB is {ratio:.1f}x slower than Redis on average")
        elif ratio <= 1.0 / HIGH_CONFIDENCE_RATIO:
            bottleneck = BottleneckCategory.REDIS
            confidence = BottleneckConfidence.HIGH
            reasons.append(f"Redis is {(1.0 / ratio):.1f}x slower than DB on average")
        elif ratio >= MEDIUM_CONFIDENCE_RATIO:
            bottleneck = BottleneckCategory.DB
            confidence = BottleneckConfidence.MEDIUM
            reasons.append(f"DB is {ratio:.1f}x slower than Redis")
        elif ratio <= 1.0 / MEDIUM_CONFIDENCE_RATIO:
            bottleneck = BottleneckCategory.REDIS
            confidence = BottleneckConfidence.MEDIUM
            reasons.append(f"Redis is {(1.0 / ratio):.1f}x slower than DB")
        else:
            bottleneck = BottleneckCategory.NEITHER
            confidence = BottleneckConfidence.LOW
            reasons.append("No clear bottleneck — DB and Redis times are similar")

        pct = (db_avg / total) * 100.0 if total > 0 else 0.0
        return BottleneckResult(
            bottleneck=bottleneck,
            confidence=confidence,
            db_breakdown=db_spans,
            redis_breakdown=redis_spans,
            bottleneck_pct_of_total=pct,
            reasons=reasons,
        )

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import Enum

N_PLUS_ONE_THRESHOLD: int = 5
DUPLICATE_THRESHOLD: int = 2


class RedundancyType(Enum):
    N_PLUS_ONE = "n_plus_one"
    DUPLICATE = "duplicate"
    ROUND_TRIP = "round_trip"


@dataclass(frozen=True)
class SpanInfo:
    span_name: str
    service_name: str
    duration_ms: float


@dataclass(frozen=True)
class RedundancyPattern:
    type: RedundancyType
    operation: str
    occurrences: int
    wasted_ms: float
    suggestion: str


@dataclass(frozen=True)
class RedundantCallRequest:
    flow: str
    trace_id: str | None = None


@dataclass(frozen=True)
class RedundantCallResult:
    flow: str
    patterns: list[RedundancyPattern]
    total_redundant_calls: int
    calculated_waste_ms: float

    @staticmethod
    def compute(
        request: RedundantCallRequest,
        spans: list[SpanInfo],
    ) -> RedundantCallResult:
        patterns: list[RedundancyPattern] = []
        counter: Counter[str] = Counter()
        total_duration: dict[str, float] = {}

        for s in spans:
            counter[s.span_name] += 1
            if s.span_name not in total_duration:
                total_duration[s.span_name] = 0.0
            total_duration[s.span_name] += s.duration_ms

        total_redundant = 0
        total_waste = 0.0

        for name, count in counter.most_common():
            wasted = total_duration[name] - (total_duration[name] / count)
            if count >= N_PLUS_ONE_THRESHOLD:
                pattern = RedundancyPattern(
                    type=RedundancyType.N_PLUS_ONE,
                    operation=name,
                    occurrences=count,
                    wasted_ms=round(wasted, 2),
                    suggestion=f"Use IN clause, batch fetch, or cache. {count} individual calls detected.",  # noqa: E501
                )
                patterns.append(pattern)
                total_redundant += count
                total_waste += wasted
            elif count >= DUPLICATE_THRESHOLD:
                pattern = RedundancyPattern(
                    type=RedundancyType.DUPLICATE,
                    operation=name,
                    occurrences=count,
                    wasted_ms=round(wasted, 2),
                    suggestion=f"Avoid duplicate call — result could be cached. Called {count} times.",  # noqa: E501
                )
                patterns.append(pattern)
                total_redundant += count
                total_waste += wasted

        return RedundantCallResult(
            flow=request.flow,
            patterns=patterns,
            total_redundant_calls=total_redundant,
            calculated_waste_ms=round(total_waste, 2),
        )

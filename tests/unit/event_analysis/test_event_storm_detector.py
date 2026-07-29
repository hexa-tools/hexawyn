"""Unit tests for EventStormDetector — detects bursts of events in a short window."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.services.event_analysis.event_storm_detector import (
    EventStorm,
    EventStormDetector,
)

_BASE_TIME = datetime(2024, 1, 1, 14, 32, 0, tzinfo=UTC)


def _events_over_seconds(
    count: int, span_seconds: float, start: datetime = _BASE_TIME
) -> list[NamespaceEvent]:
    step = span_seconds / max(count - 1, 1)
    return [
        NamespaceEvent(
            event_type="Warning",
            reason="BackOff",
            message="BackOff",
            object=f"pod/worker-{i}",
            count=1,
            last_seen=(start + timedelta(seconds=i * step)).isoformat().replace("+00:00", "Z"),
        )
        for i in range(count)
    ]


class TestEventStormDetector:
    def test_storm_detected_when_burst_exceeds_threshold(self) -> None:
        """TC1: Event storm detected at 14:32 (80 events in 90s)."""
        events = _events_over_seconds(80, span_seconds=90)
        detector = EventStormDetector()

        storms = detector.detect(events)

        assert len(storms) == 1
        assert storms[0].event_count == 80  # noqa: PLR2004

    def test_no_storm_for_normal_low_volume_period(self) -> None:
        """TC3: Normal 6h period with low event volume → no storms detected."""
        events = _events_over_seconds(20, span_seconds=6 * 3600)
        detector = EventStormDetector()

        storms = detector.detect(events)

        assert storms == []

    def test_events_at_or_below_threshold_not_flagged(self) -> None:
        events = _events_over_seconds(50, span_seconds=90)
        detector = EventStormDetector()

        storms = detector.detect(events)

        assert storms == []

    def test_events_spread_beyond_window_not_flagged(self) -> None:
        events = _events_over_seconds(80, span_seconds=300)
        detector = EventStormDetector()

        storms = detector.detect(events)

        assert storms == []

    def test_out_of_order_timestamps_still_detected(self) -> None:
        """Edge case: event timestamps out of order → sorted before analysis."""
        events = _events_over_seconds(80, span_seconds=90)
        shuffled = list(reversed(events))
        detector = EventStormDetector()

        storms = detector.detect(shuffled)

        assert len(storms) == 1
        assert storms[0].event_count == 80  # noqa: PLR2004

    def test_empty_events_returns_no_storms(self) -> None:
        detector = EventStormDetector()

        storms = detector.detect([])

        assert storms == []

    def test_storm_is_dataclass_with_expected_fields(self) -> None:
        storm = EventStorm(
            start_time="2024-01-01T14:32:00+00:00",
            end_time="2024-01-01T14:33:30+00:00",
            event_count=80,
        )
        assert storm.event_count == 80  # noqa: PLR2004

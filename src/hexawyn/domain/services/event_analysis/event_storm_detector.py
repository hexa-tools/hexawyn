from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from hexawyn.domain.models.constants import AdvancedEventAnalyticsConstants
from hexawyn.domain.models.namespace_event import NamespaceEvent

_cfg = AdvancedEventAnalyticsConstants()


@dataclass(frozen=True)
class EventStorm:
    """A burst of events exceeding storm_min_events within storm_window_seconds."""

    start_time: str
    end_time: str
    event_count: int


class EventStormDetector:
    """Detects bursts of >N events within a short sliding time window.

    Sorts by timestamp first (events may arrive out of order), then slides
    a window forward — never backward — for an O(n) scan.
    """

    def __init__(self, min_events: int | None = None, window_seconds: int | None = None) -> None:
        self.min_events = min_events or _cfg.storm_min_events
        self.window_seconds = window_seconds or _cfg.storm_window_seconds

    def detect(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = 0
        while left < n:
            right = left
            while (
                right < n
                and (timestamps[right] - timestamps[left]).total_seconds() <= self.window_seconds
            ):
                right += 1
            count = right - left
            if count > self.min_events:
                storms.append(
                    EventStorm(
                        start_time=timestamps[left].isoformat(),
                        end_time=timestamps[right - 1].isoformat(),
                        event_count=count,
                    )
                )
                left = right
            else:
                left += 1
        return storms


def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from hexawyn.domain.models.constants import AdvancedEventAnalyticsConstants
from hexawyn.domain.models.namespace_event import NamespaceEvent

_cfg = AdvancedEventAnalyticsConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class EventStorm:
    """A burst of events exceeding storm_min_events within storm_window_seconds."""

    start_time: str
    end_time: str
    event_count: int
mutants_xǁEventStormDetectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁEventStormDetectorǁdetect__mutmut: MutantDict = {}  # type: ignore


class EventStormDetector:
    """Detects bursts of >N events within a short sliding time window.

    Sorts by timestamp first (events may arrive out of order), then slides
    a window forward — never backward — for an O(n) scan.
    """

    @_mutmut_mutated(mutants_xǁEventStormDetectorǁ__init____mutmut)
    def __init__(self, min_events: int | None = None, window_seconds: int | None = None) -> None:
        self.min_events = min_events or _cfg.storm_min_events
        self.window_seconds = window_seconds or _cfg.storm_window_seconds

    def xǁEventStormDetectorǁ__init____mutmut_orig(self, min_events: int | None = None, window_seconds: int | None = None) -> None:
        self.min_events = min_events or _cfg.storm_min_events
        self.window_seconds = window_seconds or _cfg.storm_window_seconds

    def xǁEventStormDetectorǁ__init____mutmut_1(self, min_events: int | None = None, window_seconds: int | None = None) -> None:
        self.min_events = None
        self.window_seconds = window_seconds or _cfg.storm_window_seconds

    def xǁEventStormDetectorǁ__init____mutmut_2(self, min_events: int | None = None, window_seconds: int | None = None) -> None:
        self.min_events = min_events and _cfg.storm_min_events
        self.window_seconds = window_seconds or _cfg.storm_window_seconds

    def xǁEventStormDetectorǁ__init____mutmut_3(self, min_events: int | None = None, window_seconds: int | None = None) -> None:
        self.min_events = min_events or _cfg.storm_min_events
        self.window_seconds = None

    def xǁEventStormDetectorǁ__init____mutmut_4(self, min_events: int | None = None, window_seconds: int | None = None) -> None:
        self.min_events = min_events or _cfg.storm_min_events
        self.window_seconds = window_seconds and _cfg.storm_window_seconds

    @_mutmut_mutated(mutants_xǁEventStormDetectorǁdetect__mutmut)
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

    def xǁEventStormDetectorǁdetect__mutmut_orig(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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

    def xǁEventStormDetectorǁdetect__mutmut_1(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = None
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

    def xǁEventStormDetectorǁdetect__mutmut_2(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(None)
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

    def xǁEventStormDetectorǁdetect__mutmut_3(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(None) for event in events)
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

    def xǁEventStormDetectorǁdetect__mutmut_4(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = None

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

    def xǁEventStormDetectorǁdetect__mutmut_5(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = None
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

    def xǁEventStormDetectorǁdetect__mutmut_6(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = None
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

    def xǁEventStormDetectorǁdetect__mutmut_7(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = 1
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

    def xǁEventStormDetectorǁdetect__mutmut_8(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = 0
        while left <= n:
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

    def xǁEventStormDetectorǁdetect__mutmut_9(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = 0
        while left < n:
            right = None
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

    def xǁEventStormDetectorǁdetect__mutmut_10(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = 0
        while left < n:
            right = left
            while (
                right < n or (timestamps[right] - timestamps[left]).total_seconds() <= self.window_seconds
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

    def xǁEventStormDetectorǁdetect__mutmut_11(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = 0
        while left < n:
            right = left
            while (
                right <= n
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

    def xǁEventStormDetectorǁdetect__mutmut_12(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = 0
        while left < n:
            right = left
            while (
                right < n
                and (timestamps[right] + timestamps[left]).total_seconds() <= self.window_seconds
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

    def xǁEventStormDetectorǁdetect__mutmut_13(self, events: list[NamespaceEvent]) -> list[EventStorm]:
        timestamps = sorted(_parse_timestamp(event.last_seen) for event in events)
        n = len(timestamps)

        storms: list[EventStorm] = []
        left = 0
        while left < n:
            right = left
            while (
                right < n
                and (timestamps[right] - timestamps[left]).total_seconds() < self.window_seconds
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

    def xǁEventStormDetectorǁdetect__mutmut_14(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                right = 1
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

    def xǁEventStormDetectorǁdetect__mutmut_15(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                right -= 1
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

    def xǁEventStormDetectorǁdetect__mutmut_16(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                right += 2
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

    def xǁEventStormDetectorǁdetect__mutmut_17(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
            count = None
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

    def xǁEventStormDetectorǁdetect__mutmut_18(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
            count = right + left
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

    def xǁEventStormDetectorǁdetect__mutmut_19(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
            if count >= self.min_events:
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

    def xǁEventStormDetectorǁdetect__mutmut_20(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                    None
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_21(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                        start_time=None,
                        end_time=timestamps[right - 1].isoformat(),
                        event_count=count,
                    )
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_22(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                        end_time=None,
                        event_count=count,
                    )
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_23(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                        event_count=None,
                    )
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_24(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                        end_time=timestamps[right - 1].isoformat(),
                        event_count=count,
                    )
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_25(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                        event_count=count,
                    )
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_26(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                        )
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_27(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                        end_time=timestamps[right + 1].isoformat(),
                        event_count=count,
                    )
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_28(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                        end_time=timestamps[right - 2].isoformat(),
                        event_count=count,
                    )
                )
                left = right
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_29(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                left = None
            else:
                left += 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_30(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                left = 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_31(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                left -= 1
        return storms

    def xǁEventStormDetectorǁdetect__mutmut_32(self, events: list[NamespaceEvent]) -> list[EventStorm]:
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
                left += 2
        return storms

mutants_xǁEventStormDetectorǁ__init____mutmut['_mutmut_orig'] = EventStormDetector.xǁEventStormDetectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁ__init____mutmut['xǁEventStormDetectorǁ__init____mutmut_1'] = EventStormDetector.xǁEventStormDetectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁ__init____mutmut['xǁEventStormDetectorǁ__init____mutmut_2'] = EventStormDetector.xǁEventStormDetectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁ__init____mutmut['xǁEventStormDetectorǁ__init____mutmut_3'] = EventStormDetector.xǁEventStormDetectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁ__init____mutmut['xǁEventStormDetectorǁ__init____mutmut_4'] = EventStormDetector.xǁEventStormDetectorǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁEventStormDetectorǁdetect__mutmut['_mutmut_orig'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_1'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_2'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_3'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_4'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_5'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_6'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_7'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_8'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_9'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_10'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_11'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_12'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_13'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_14'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_15'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_16'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_17'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_18'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_19'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_20'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_21'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_22'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_22 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_23'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_23 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_24'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_24 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_25'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_25 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_26'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_26 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_27'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_27 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_28'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_28 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_29'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_29 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_30'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_30 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_31'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_31 # type: ignore # mutmut generated
mutants_xǁEventStormDetectorǁdetect__mutmut['xǁEventStormDetectorǁdetect__mutmut_32'] = EventStormDetector.xǁEventStormDetectorǁdetect__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_timestamp__mutmut)
def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_orig(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_1(raw: str) -> datetime:
    return datetime.fromisoformat(None)


def x__parse_timestamp__mutmut_2(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace(None, "+00:00"))


def x__parse_timestamp__mutmut_3(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", None))


def x__parse_timestamp__mutmut_4(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("+00:00"))


def x__parse_timestamp__mutmut_5(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", ))


def x__parse_timestamp__mutmut_6(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("XXZXX", "+00:00"))


def x__parse_timestamp__mutmut_7(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("z", "+00:00"))


def x__parse_timestamp__mutmut_8(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "XX+00:00XX"))

mutants_x__parse_timestamp__mutmut['_mutmut_orig'] = x__parse_timestamp__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_1'] = x__parse_timestamp__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_2'] = x__parse_timestamp__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_3'] = x__parse_timestamp__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_4'] = x__parse_timestamp__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_5'] = x__parse_timestamp__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_6'] = x__parse_timestamp__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_7'] = x__parse_timestamp__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_8'] = x__parse_timestamp__mutmut_8 # type: ignore # mutmut generated

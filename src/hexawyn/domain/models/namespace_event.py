from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Urgency = Literal["high", "normal"]


@dataclass(frozen=True)
class NamespaceEvent:
    event_type: str
    reason: str
    message: str
    object: str
    count: int
    last_seen: str
    recurring: bool = False
    urgency: Urgency = "normal"
    object_exists: bool = True


@dataclass(frozen=True)
class GetNamespaceEventsRequest:
    namespace: str
    time_window_minutes: int = 15
    top_n: int = 20


@dataclass(frozen=True)
class GetNamespaceEventsResult:
    namespace: str
    time_window_minutes: int
    total_events: int
    events: list[NamespaceEvent] = field(default_factory=list)
    has_more: bool = False
    remaining_count: int = 0
    summary: str = ""

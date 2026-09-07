from dataclasses import dataclass, field
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class NamespaceEventDict(TypedDict):
    event_type: str
    reason: str
    message: str
    object: str
    count: int
    last_seen: str
    recurring: bool
    urgency: str
    object_exists: bool


@dataclass
class GetNamespaceEventsResponse:
    namespace: str
    time_window_minutes: int
    total_events: int
    has_more: bool = False
    remaining_count: int = 0
    summary: str = ""
    events: list[NamespaceEventDict] = field(default_factory=list)

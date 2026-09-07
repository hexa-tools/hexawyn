from dataclasses import dataclass, field
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CriticalIncidentDict(TypedDict):
    event_type: str
    reason: str
    message: str
    involved_object: str
    count: int
    last_seen: str
    likely_root_cause: str
    severity: str


@dataclass
class AnalyzeCriticalNamespaceEventsResponse:
    namespace: str = ""
    time_window_minutes: int = 0
    critical_events: list[CriticalIncidentDict] = field(default_factory=list)
    total_events: int = 0
    summary: str = ""
    critical_incidents: str = ""
    error: str | None = None

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class CriticalIncidentDict(TypedDict):
    reason: str
    involved_objects: list[str]
    event_count: int
    likely_root_cause: str
    runbook_id: str
    runbook_title: str
    runbook_steps: list[str]


@dataclass
class AnalyzeCriticalNamespaceEventsResponse:
    namespace: str = ""
    critical_incidents: list[CriticalIncidentDict] = field(default_factory=list)
    error: str | None = None

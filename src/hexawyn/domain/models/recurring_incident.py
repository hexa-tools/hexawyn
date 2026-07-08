from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ServiceIncidentSummary:
    service_name: str
    incident_count: int
    avg_duration_minutes: float
    most_common_cause: str
    recurrence_count: int
    is_recurring: bool
    recommendation: str


@dataclass
class RecurringIncidentReport:
    services: list[ServiceIncidentSummary] = field(default_factory=list)

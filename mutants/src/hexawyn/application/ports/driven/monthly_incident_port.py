from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class IncidentSnapshotData(TypedDict):
    incident_id: str
    service_name: str
    severity: str
    downtime_minutes: int
    timestamp: str
    resolved_at: str
    is_planned_maintenance: bool
    reopened: bool


class MonthlyIncidentPort(ABC):
    @abstractmethod
    def fetch_incidents(self, month: str) -> list[IncidentSnapshotData]: ...

from abc import ABC, abstractmethod
from typing import TypedDict


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

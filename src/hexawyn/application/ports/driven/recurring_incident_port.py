from abc import ABC, abstractmethod
from typing import TypedDict


class IncidentFrequencyData(TypedDict):
    incident_id: str
    service_name: str
    root_cause: str
    duration_minutes: int
    timestamp: str


class RecurringIncidentPort(ABC):
    @abstractmethod
    def fetch_incidents(self, window_days: int) -> list[IncidentFrequencyData]: ...

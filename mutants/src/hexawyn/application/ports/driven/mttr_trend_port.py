from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class IncidentResolutionData(TypedDict):
    incident_id: str
    service_name: str
    severity: str
    resolution_minutes: int
    resolved: bool
    root_cause: str


class MTTRTrendPort(ABC):
    @abstractmethod
    def fetch_incidents_by_month(self, month: str) -> list[IncidentResolutionData]: ...

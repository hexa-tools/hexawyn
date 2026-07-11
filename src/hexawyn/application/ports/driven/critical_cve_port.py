from abc import ABC, abstractmethod
from typing import TypedDict


class CveRaw(TypedDict):
    business_service_name: str
    severity: str
    count: int
    oldest_unresolved_days: int


class CriticalCvePort(ABC):
    @abstractmethod
    def get_critical_cves(self) -> list[CveRaw]: ...

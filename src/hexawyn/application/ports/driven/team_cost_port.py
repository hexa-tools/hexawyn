from abc import ABC, abstractmethod
from typing import TypedDict


class NamespaceResourceData(TypedDict):
    namespace: str
    team_label: str
    cpu_cores: float
    memory_gb: float
    storage_gb: float
    month: str
    days_active: int


class TeamCostPort(ABC):
    @abstractmethod
    def fetch_namespace_resources(self, month: str) -> list[NamespaceResourceData]: ...

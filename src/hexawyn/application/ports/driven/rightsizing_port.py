from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class WorkloadRawData(TypedDict):
    resource_name: str
    namespace: str
    kind: str  # "Deployment" | "StatefulSet"
    cpu_requested_cores: float
    memory_requested_mi: float
    cpu_actual_cores: float | None
    memory_actual_mi: float | None


class RightsizingPort(ABC):
    @abstractmethod
    def get_workload_rightsizing_data(self) -> list[WorkloadRawData]: ...

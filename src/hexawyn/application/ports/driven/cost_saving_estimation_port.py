from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class PodResourceData(TypedDict):
    pod_name: str
    namespace: str
    cpu_request_cores: float | None  # None if no request set
    memory_request_mi: float | None  # None if no request set
    cpu_limit_cores: float | None  # For "limits but no requests" edge case
    memory_limit_mi: float | None
    cpu_p95_cores: float | None  # From Prometheus (7d p95)
    memory_p95_mi: float | None  # From Prometheus (7d p95)
    cpu_max_cores: float | None  # For bursty detection proxy
    hpa_enabled: bool
    hpa_min_replicas: int | None


class CostSavingEstimationPort(ABC):
    @abstractmethod
    def get_pod_resource_data(self) -> list[PodResourceData]: ...

    @abstractmethod
    def get_previous_total_saving(self) -> float | None: ...

    @abstractmethod
    def store_total_saving(self, total_saving_usd: float) -> None: ...

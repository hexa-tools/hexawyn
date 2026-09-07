from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PodResourceSnapshotData(TypedDict):
    pod_name: str
    namespace: str
    month: str
    cpu_cores: float
    memory_gb: float


class ServiceCostPort(ABC):
    @abstractmethod
    def fetch_pod_resources(
        self, service_name: str, month: str
    ) -> list[PodResourceSnapshotData]: ...

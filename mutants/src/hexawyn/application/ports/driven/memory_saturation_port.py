from abc import ABC, abstractmethod

from hexawyn.domain.models.memory_saturation import (
    MemorySaturationRequest,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class MemorySaturationPort(ABC):
    @abstractmethod
    def fetch_memory_metrics(self, request: MemorySaturationRequest) -> list[dict[str, object]]: ...
    @abstractmethod
    def correlate_with_otel(self, pod_name: str, namespace: str) -> str | None: ...

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class NamespaceResourceAllocation(TypedDict):
    namespace: str
    total_cpu_cores: float
    total_memory_gb: float
    pod_count: int


@dataclass
class NamespaceResourceAllocationReport:
    allocations: list[NamespaceResourceAllocation] = field(default_factory=list)

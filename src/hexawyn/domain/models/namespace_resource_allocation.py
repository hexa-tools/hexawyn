from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class NamespaceResourceAllocation(TypedDict):
    namespace: str
    total_cpu_cores: float
    total_memory_gb: float
    pod_count: int


@dataclass
class NamespaceResourceAllocationReport:
    allocations: list[NamespaceResourceAllocation] = field(default_factory=list)

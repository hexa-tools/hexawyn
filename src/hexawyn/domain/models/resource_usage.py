from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class PodResourceUsage(TypedDict):
    name: str
    namespace: str
    cpu_requested_cores: float
    cpu_used_cores: float
    cpu_utilization_pct: float
    memory_requested_gb: float
    memory_used_gb: float
    memory_utilization_pct: float


class NamespaceResourceUsageSummary(TypedDict):
    namespace: str
    pod_count: int
    total_cpu_requested_cores: float
    total_cpu_used_cores: float
    total_cpu_utilization_pct: float
    total_memory_requested_gb: float
    total_memory_used_gb: float
    total_memory_utilization_pct: float


@dataclass
class ResourceUsageReport:
    pods: list[PodResourceUsage] = field(default_factory=list)
    namespace_summary: list[NamespaceResourceUsageSummary] = field(default_factory=list)
    metrics_server_available: bool = False
    source: str = ""

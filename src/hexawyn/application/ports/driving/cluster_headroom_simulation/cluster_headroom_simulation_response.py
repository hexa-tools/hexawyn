from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ClusterHeadroomSimulationResponse:
    current_cpu_utilization_percent: float = 0.0
    current_memory_utilization_percent: float = 0.0
    total_new_cpu_cores: float = 0.0
    total_new_memory_gb: float = 0.0
    post_cpu_utilization_percent: float = 0.0
    post_memory_utilization_percent: float = 0.0
    binding_constraint: str = ""
    verdict: str = ""
    recommended_additional_nodes: int = 0
    autoscaler_enabled: bool = False
    unschedulable_workloads: list[str] = field(default_factory=list)
    summary: str = ""
    error: str | None = None

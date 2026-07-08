from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

BindingConstraint = Literal["CPU", "Memory", "None"]
HeadroomVerdict = Literal["fits", "tight", "needs_nodes"]


@dataclass(frozen=True)
class ProposedWorkload:
    name: str
    cpu_request_per_pod: str
    memory_request_per_pod: str
    replicas: int = 2


@dataclass(frozen=True)
class ClusterHeadroomSnapshot:
    total_allocatable_cpu_cores: float
    total_allocatable_memory_gb: float
    used_cpu_cores: float
    used_memory_gb: float
    node_count: int
    largest_node_cpu_cores: float
    largest_node_memory_gb: float
    autoscaler_enabled: bool


@dataclass(frozen=True)
class HeadroomSimulationRequest:
    proposed_workloads: list[ProposedWorkload] = field(default_factory=list)


@dataclass(frozen=True)
class HeadroomSimulationReport:
    current_cpu_utilization_percent: float
    current_memory_utilization_percent: float
    total_new_cpu_cores: float
    total_new_memory_gb: float
    post_cpu_utilization_percent: float
    post_memory_utilization_percent: float
    binding_constraint: BindingConstraint
    verdict: HeadroomVerdict
    recommended_additional_nodes: int
    autoscaler_enabled: bool
    unschedulable_workloads: list[str]
    summary: str

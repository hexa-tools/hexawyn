from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

NodeType = Literal["compute_optimized", "memory_optimized", "balanced"]
BindingConstraint = Literal["CPU", "Memory", "None"]
ProvisioningVerdict = Literal["no_action", "provision", "autoscaler_handles"]
MultiplierSource = Literal["historical", "generic_fallback", "pessimistic", "provided"]

GENERIC_MULTIPLIER: float = 3.0
PESSIMISTIC_MULTIPLIER: float = 4.0


@dataclass(frozen=True)
class ClusterCapacitySnapshot:
    node_count: int
    allocatable_cpu_cores: float
    allocatable_memory_gb: float
    used_cpu_cores: float
    used_memory_gb: float
    autoscaler_enabled: bool


@dataclass
class SpikeProvisioningReport:
    traffic_multiplier: float
    multiplier_source: str
    verdict: str
    current_cpu_headroom_pct: float = 0.0
    current_memory_headroom_pct: float = 0.0
    projected_cpu_pct: float = 0.0
    projected_memory_pct: float = 0.0
    recommended_nodes: int = 0
    recommended_node_type: str = "balanced"
    binding_constraint: str = "None"
    autoscaler_sufficient: bool = False
    provisioning_deadline: str | None = None
    warning: str = ""

from dataclasses import dataclass


@dataclass
class SpikeProvisioningResult:
    verdict: str = ""
    traffic_multiplier: float = 0.0
    multiplier_source: str = ""
    current_cpu_headroom_pct: float = 0.0
    current_memory_headroom_pct: float = 0.0
    projected_cpu_pct: float = 0.0
    projected_memory_pct: float = 0.0
    recommended_nodes: int = 0
    recommended_node_type: str = ""
    binding_constraint: str = ""
    autoscaler_sufficient: bool = False
    provisioning_deadline: str = ""
    warning: str = ""


@dataclass
class PlanSpikeProvisioningResponse:
    result: SpikeProvisioningResult
    error: str | None = None

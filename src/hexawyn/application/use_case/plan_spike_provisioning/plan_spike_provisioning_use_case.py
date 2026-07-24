from __future__ import annotations

from datetime import datetime, timedelta

from hexawyn.application.ports.driven.spike_provisioning_port import SpikeProvisioningPort
from hexawyn.application.use_case.plan_spike_provisioning.command import (
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.use_case.plan_spike_provisioning.response import (
    PlanSpikeProvisioningResponse,
    SpikeProvisioningResult,
)


class PlanSpikeProvisioningUseCase:
    def __init__(self, port: SpikeProvisioningPort) -> None:
        self._port = port

    def execute(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        historical = self._port.get_historical_spike_multiplier()

        multiplier = command.traffic_multiplier or historical or 2.0
        source = (
            "provided"
            if command.traffic_multiplier
            else ("historical" if historical else "generic")
        )

        cpu_headroom_pct = (
            1 - capacity["used_cpu_cores"] / max(capacity["allocatable_cpu_cores"], 1)
        ) * 100
        mem_headroom_pct = (
            1 - capacity["used_memory_gb"] / max(capacity["allocatable_memory_gb"], 1)
        ) * 100

        projected_cpu = capacity["used_cpu_cores"] * multiplier
        projected_mem = capacity["used_memory_gb"] * multiplier
        projected_cpu_pct = (projected_cpu / max(capacity["allocatable_cpu_cores"], 1)) * 100
        projected_mem_pct = (projected_mem / max(capacity["allocatable_memory_gb"], 1)) * 100

        binding = "None"
        if (
            projected_cpu_pct > command.safe_threshold_pct
            or projected_mem_pct > command.safe_threshold_pct
        ):
            binding = "CPU" if projected_cpu_pct >= projected_mem_pct else "Memory"
            verdict = "action_required"
        elif cpu_headroom_pct < 15 or mem_headroom_pct < 15:
            verdict = "action_required"
        else:
            verdict = "no_action"

        recommended_nodes = 0
        if verdict == "action_required":
            deficit_cpu = max(0.0, projected_cpu - capacity["allocatable_cpu_cores"] * 0.85)
            deficit_mem = max(0.0, projected_mem - capacity["allocatable_memory_gb"] * 0.85)
            node_cpu = 4.0
            node_mem = 16.0
            nodes_cpu = int(deficit_cpu / node_cpu) + 1
            nodes_mem = int(deficit_mem / node_mem) + 1
            recommended_nodes = max(nodes_cpu, nodes_mem)

        node_type = (
            "compute_optimized" if cpu_headroom_pct < mem_headroom_pct else "memory_optimized"
        )
        deadline = (datetime.now() + timedelta(hours=command.provider_lead_time_hours)).isoformat()

        warning = ""
        if command.unpredictable:
            warning = "Traffic multiplier is unpredictable — consider buffer"
        if not capacity["autoscaler_enabled"]:
            warning += "; No cluster autoscaler detected — manual provisioning required"

        result = SpikeProvisioningResult(
            verdict=verdict,
            traffic_multiplier=round(multiplier, 2),
            multiplier_source=source,
            current_cpu_headroom_pct=round(cpu_headroom_pct, 2),
            current_memory_headroom_pct=round(mem_headroom_pct, 2),
            projected_cpu_pct=round(projected_cpu_pct, 2),
            projected_memory_pct=round(projected_mem_pct, 2),
            recommended_nodes=recommended_nodes,
            recommended_node_type=node_type,
            binding_constraint=binding,
            autoscaler_sufficient=capacity["autoscaler_enabled"],
            provisioning_deadline=deadline,
            warning=warning.strip("; "),
        )
        return PlanSpikeProvisioningResponse(result=result)

"""MCP tool: plan_spike_provisioning — decides whether to add nodes ahead of a
traffic spike (e.g. Black Friday), how many, of which type, and by when."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_command import (  # noqa: E501
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.use_case.plan_spike_provisioning.plan_spike_provisioning_use_case import (  # noqa: E501
    PlanSpikeProvisioningUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def plan_spike_provisioning(
    event_date: str,
    traffic_multiplier: float | None = None,
    provider_lead_time_hours: int = 24,
    safety_margin_days: int = 3,
    safe_threshold_pct: float = 85.0,
    unpredictable: bool = False,
) -> dict[str, object]:
    """Plan node provisioning ahead of a traffic spike.

    Returns current cluster headroom, the projected peak utilisation under the
    traffic multiplier, whether action is needed (or the autoscaler covers it),
    the recommended number and type of nodes to add (compute- vs
    memory-optimized), and a safe provisioning deadline that accounts for the
    cloud provider's node lead time.
    """
    from hexawyn.application.service.plan_spike_provisioning_service import (
        PlanSpikeProvisioningService,
    )
    from hexawyn.mcp.server import build_spike_provisioning_adapter

    try:
        adapter = build_spike_provisioning_adapter()
        service = PlanSpikeProvisioningService(spike_port=adapter)
        use_case = PlanSpikeProvisioningUseCase(service=service)
        response = use_case.execute(
            PlanSpikeProvisioningCommand(
                event_date=event_date,
                traffic_multiplier=traffic_multiplier,
                provider_lead_time_hours=provider_lead_time_hours,
                safety_margin_days=safety_margin_days,
                safe_threshold_pct=safe_threshold_pct,
                unpredictable=unpredictable,
            )
        )
        report = response.result
        return {
            "verdict": report.verdict,
            "traffic_multiplier": report.traffic_multiplier,
            "multiplier_source": report.multiplier_source,
            "current_cpu_headroom_pct": report.current_cpu_headroom_pct,
            "current_memory_headroom_pct": report.current_memory_headroom_pct,
            "projected_cpu_pct": report.projected_cpu_pct,
            "projected_memory_pct": report.projected_memory_pct,
            "recommended_nodes": report.recommended_nodes,
            "recommended_node_type": report.recommended_node_type,
            "binding_constraint": report.binding_constraint,
            "autoscaler_sufficient": report.autoscaler_sufficient,
            "provisioning_deadline": report.provisioning_deadline,
            "warning": report.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "verdict": "no_action",
            "traffic_multiplier": traffic_multiplier or 0.0,
            "multiplier_source": "provided",
            "current_cpu_headroom_pct": 0.0,
            "current_memory_headroom_pct": 0.0,
            "projected_cpu_pct": 0.0,
            "projected_memory_pct": 0.0,
            "recommended_nodes": 0,
            "recommended_node_type": "balanced",
            "binding_constraint": "None",
            "autoscaler_sufficient": False,
            "provisioning_deadline": None,
            "warning": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(plan_spike_provisioning)

"""MCP tool: cluster_headroom_simulation — simulates whether the cluster has
enough headroom for a list of proposed new workloads before deploying them."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_command import (
    ClusterHeadroomSimulationCommand,
    ProposedWorkloadDict,
)
from hexawyn.application.use_case.cluster_headroom_simulation.cluster_headroom_simulation_use_case import (
    ClusterHeadroomSimulationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cluster_headroom_simulation(
    proposed_workloads: list[ProposedWorkloadDict] | None = None,
) -> dict[str, object]:
    from hexawyn.application.service.cluster_headroom_simulation_service import (
        ClusterHeadroomSimulationService,
    )
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_headroom_simulation_adapter,
    )

    try:
        service = ClusterHeadroomSimulationService(
            metrics_port=build_cluster_resource_metrics_adapter(),
            headroom_port=build_headroom_simulation_adapter(),
        )
        r = ClusterHeadroomSimulationUseCase(service=service).execute(
            ClusterHeadroomSimulationCommand(proposed_workloads=proposed_workloads or [])
        )
        return {
            "current_cpu_utilization_percent": r.current_cpu_utilization_percent,
            "current_memory_utilization_percent": r.current_memory_utilization_percent,
            "total_new_cpu_cores": r.total_new_cpu_cores,
            "total_new_memory_gb": r.total_new_memory_gb,
            "post_cpu_utilization_percent": r.post_cpu_utilization_percent,
            "post_memory_utilization_percent": r.post_memory_utilization_percent,
            "binding_constraint": r.binding_constraint,
            "verdict": r.verdict,
            "recommended_additional_nodes": r.recommended_additional_nodes,
            "autoscaler_enabled": r.autoscaler_enabled,
            "unschedulable_workloads": r.unschedulable_workloads,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(cluster_headroom_simulation)

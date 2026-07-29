"""MCP tool: cluster_headroom_simulation — Simulate cluster headroom."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.cluster_headroom_simulation.cluster_headroom_simulation_use_case import (  # noqa: E501
    ClusterHeadroomSimulationUseCase,
)
from hexawyn.application.use_case.cluster.cluster_headroom_simulation.command import (
    ClusterHeadroomSimulationCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cluster_headroom_simulation() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_headroom_simulation_adapter,
    )

    try:
        use_case = ClusterHeadroomSimulationUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            headroom_port=build_headroom_simulation_adapter(),
        )
        response = use_case.simulate(ClusterHeadroomSimulationCommand())
        return {
            "current_cpu_utilization_percent": response.current_cpu_utilization_percent,
            "current_memory_utilization_percent": response.current_memory_utilization_percent,
            "total_new_cpu_cores": response.total_new_cpu_cores,
            "total_new_memory_gb": response.total_new_memory_gb,
            "post_cpu_utilization_percent": response.post_cpu_utilization_percent,
            "post_memory_utilization_percent": response.post_memory_utilization_percent,
            "binding_constraint": response.binding_constraint,
            "verdict": response.verdict,
            "recommended_additional_nodes": response.recommended_additional_nodes,
            "autoscaler_enabled": response.autoscaler_enabled,
            "unschedulable_workloads": response.unschedulable_workloads,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "current_cpu_utilization_percent": 0.0,
            "current_memory_utilization_percent": 0.0,
            "total_new_cpu_cores": 0.0,
            "total_new_memory_gb": 0.0,
            "post_cpu_utilization_percent": 0.0,
            "post_memory_utilization_percent": 0.0,
            "binding_constraint": "",
            "verdict": "",
            "recommended_additional_nodes": 0,
            "autoscaler_enabled": False,
            "unschedulable_workloads": None,
            "summary": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(cluster_headroom_simulation)

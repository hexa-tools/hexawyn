"""MCP tool: compare_cluster_health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.compare_cluster_health.command import CompareClusterHealthCommand
from hexawyn.application.use_case.compare_cluster_health.compare_cluster_health_use_case import (
    CompareClusterHealthUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot


def _snapshot_to_dict(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def compare_cluster_health(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(compare_cluster_health)

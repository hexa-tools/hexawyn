"""MCP tool: compare_cluster_health — side-by-side health comparison of two clusters."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_command import (  # noqa: E501
    CompareClusterHealthCommand,
)
from hexawyn.application.use_case.compare_cluster_health.compare_cluster_health_use_case import (  # noqa: E501
    CompareClusterHealthUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot


def compare_cluster_health(cluster_a: str, cluster_b: str) -> dict[str, object]:
    from hexawyn.application.service.compare_cluster_health_service import (
        CompareClusterHealthService,
    )
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        adapter = build_fleet_health_adapter()
        service = CompareClusterHealthService(fleet_health_port=adapter)
        use_case = CompareClusterHealthUseCase(service=service)
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        r = response.result
        return {
            "cluster_a": _serialize(r.cluster_a),
            "cluster_b": _serialize(r.cluster_b),
            "comparison": {
                "worse_cluster": r.comparison.worse_cluster,
                "reason": r.comparison.reason,
                "delta_failing_pods": r.comparison.delta_failing_pods,
                "delta_cpu_pct": r.comparison.delta_cpu_pct,
                "delta_active_incidents": r.comparison.delta_active_incidents,
                "normalized_a_failing_per_100": r.comparison.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": r.comparison.normalized_b_failing_per_100,
            },
            "error": None,
        }
    except Exception as exc:
        return {
            "cluster_a": _empty_snapshot(cluster_a),
            "cluster_b": _empty_snapshot(cluster_b),
            "comparison": {"worse_cluster": None, "reason": str(exc)},
            "error": str(exc),
        }


def _serialize(snap: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snap.cluster_name,
        "failing_pods": snap.failing_pods,
        "total_pods": snap.total_pods,
        "cpu_utilization_pct": snap.cpu_utilization_pct,
        "memory_utilization_pct": snap.memory_utilization_pct,
        "node_count": snap.node_count,
        "nodes_not_ready": snap.nodes_not_ready,
        "active_incidents": snap.active_incidents,
        "health_status": snap.health_status,
        "in_maintenance": snap.in_maintenance,
        "reachable": snap.reachable,
    }


def _empty_snapshot(name: str) -> dict[str, object]:
    return {
        "cluster_name": name,
        "failing_pods": 0,
        "total_pods": 0,
        "cpu_utilization_pct": 0.0,
        "memory_utilization_pct": 0.0,
        "node_count": 0,
        "nodes_not_ready": 0,
        "active_incidents": 0,
        "health_status": "unreachable",
        "in_maintenance": False,
        "reachable": False,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compare_cluster_health)

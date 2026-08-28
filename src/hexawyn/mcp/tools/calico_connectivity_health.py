"""MCP tool: calico_connectivity_health — Calico dataplane end-to-end health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_connectivity_health.calico_connectivity_health_use_case import (  # noqa: E501
    CalicoConnectivityHealthUseCase,
)
from hexawyn.application.use_case.calico.calico_connectivity_health.command import (
    CalicoConnectivityHealthCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _node_dict(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, "ready", False),
    }


def calico_connectivity_health() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_connectivity_health)

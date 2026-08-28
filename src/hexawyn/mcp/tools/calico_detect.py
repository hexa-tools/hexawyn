"""MCP tool: calico_detect — detect if Calico is the active CNI and its health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_detect.calico_detect_use_case import (
    CalicoDetectUseCase,
)
from hexawyn.application.use_case.calico.calico_detect.command import CalicoDetectCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _agent_dict(agent: object) -> dict[str, object]:
    """Project a CalicoNodeAgent into a plain, serialisable dict."""
    return {
        "node": getattr(agent, "node", None),
        "phase": getattr(getattr(agent, "phase", ""), "value", getattr(agent, "phase", "")),
        "ready": getattr(agent, "ready", False),
        "ready_replicas": getattr(agent, "ready_replicas", 0),
        "desired_replicas": getattr(agent, "desired_replicas", 0),
        "available_replicas": getattr(agent, "available_replicas", 0),
        "message": getattr(agent, "message", None),
    }


def _empty(error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "status": "not_installed",
        "not_installed_marker": "NOT_INSTALLED",
        "version": None,
        "mode": None,
        "namespace": None,
        "tigera_operator": False,
        "enterprise": False,
        "agents": [],
        "total_nodes": 0,
        "ready_agents": 0,
        "degraded_agents": 0,
        "degraded_summary": None,
        "error": error,
    }


def calico_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        adapter = build_calico_adapter()
        use_case = CalicoDetectUseCase(port=adapter)
        result = use_case.execute(CalicoDetectCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "not_installed_marker": result.not_installed_marker,
            "version": result.version,
            "mode": getattr(result.mode, "value", result.mode),
            "namespace": result.namespace,
            "tigera_operator": result.tigera_operator,
            "enterprise": result.enterprise,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "total_nodes": result.total_nodes,
            "ready_agents": result.ready_agents,
            "degraded_agents": result.degraded_agents,
            "degraded_summary": result.degraded_summary,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_detect)

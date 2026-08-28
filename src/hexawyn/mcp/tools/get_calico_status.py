"""MCP tool: get_calico_status — aggregated Calico datapath health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.get_calico_status.command import (
    GetCalicoStatusCommand,
)
from hexawyn.application.use_case.calico.get_calico_status.get_calico_status_use_case import (
    GetCalicoStatusUseCase,
)

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
        "not_installed_marker": "NOT_INSTALLED",
        "status": "not_installed",
        "ready_agents": 0,
        "total_agents": 0,
        "degraded_summary": None,
        "agents": [],
        "felix_errors": None,
        "felix_errors_available": False,
        "connectivity_status": None,
        "connectivity_available": False,
        "connectivity_detail": None,
        "error": error,
    }


def get_calico_status() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "status": result.status,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "degraded_summary": result.degraded_summary,
            "agents": [_agent_dict(agent) for agent in result.agents],
            "felix_errors": result.felix_errors,
            "felix_errors_available": result.felix_errors_available,
            "connectivity_status": result.connectivity_status,
            "connectivity_available": result.connectivity_available,
            "connectivity_detail": result.connectivity_detail,
            "error": result.error,
        }
    except Exception as exc:
        return _empty(error=str(exc))


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_calico_status)

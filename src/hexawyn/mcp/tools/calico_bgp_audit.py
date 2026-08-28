"""MCP tool: calico_bgp_audit — Calico BGP configuration and peer state."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_bgp_audit.calico_bgp_audit_use_case import (
    CalicoBgpAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_bgp_audit.command import CalicoBgpAuditCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _peer_dict(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def calico_bgp_audit() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_bgp_audit)

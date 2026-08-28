"""MCP tool: list_cilium_network_policies — Cilium network policy inventory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.list_cilium_network_policies.command import (
    ListCiliumNetworkPoliciesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_network_policies.list_cilium_network_policies_use_case import (  # noqa: E501
    ListCiliumNetworkPoliciesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_cilium_network_policies() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_cilium_network_policies)

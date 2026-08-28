"""MCP tool: list_calico_ip_pools — list Calico IPPools."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.list_calico_ip_pools.command import (
    ListCalicoIpPoolsCommand,
)
from hexawyn.application.use_case.calico.list_calico_ip_pools.list_calico_ip_pools_use_case import (
    ListCalicoIpPoolsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _pool_dict(pool: object) -> dict[str, object]:
    """Project a CalicoIPPool into a plain, serialisable dict."""
    return {
        "name": getattr(pool, "name", None),
        "cidr": getattr(pool, "cidr", None),
        "disabled": getattr(pool, "disabled", False),
        "nat_outgoing": getattr(pool, "nat_outgoing", False),
        "node_selector": getattr(pool, "node_selector", ""),
        "ipip_mode": getattr(pool, "ipip_mode", None),
        "vxlan_mode": getattr(pool, "vxlan_mode", None),
    }


def list_calico_ip_pools() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoIpPoolsUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoIpPoolsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "pools": [_pool_dict(pool) for pool in result.pools],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "pools": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_calico_ip_pools)

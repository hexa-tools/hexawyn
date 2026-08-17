"""MCP tool: get_namespace_resource_allocation — Rank namespaces by CPU/memory requests + pod count."""  # noqa: E501

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.command import (
    GetNamespaceResourceAllocationCommand,
)
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.get_namespace_resource_allocation_use_case import (  # noqa: E501
    GetNamespaceResourceAllocationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_namespace_resource_allocation() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_namespace_resource_allocation)

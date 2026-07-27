"""MCP tool: list_openshift_routes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.openshift.list_openshift_routes.command import (
    ListOpenshiftRoutesCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_routes.list_openshift_routes_use_case import (  # noqa: E501
    ListOpenshiftRoutesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_openshift_routes(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_openshift_routes)

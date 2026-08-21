"""MCP tool: list_ingresses."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.ingress.list_ingresses.command import (
    ListIngressesCommand,
)
from hexawyn.application.use_case.ingress.list_ingresses.list_ingresses_use_case import (
    ListIngressesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_ingresses(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_ingress_adapter

    try:
        use_case = ListIngressesUseCase(port=build_ingress_adapter())
        r = use_case.execute(ListIngressesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_ingresses)

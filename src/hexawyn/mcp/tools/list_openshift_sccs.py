"""MCP tool: list_openshift_sccs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.openshift.list_openshift_sccs.command import (
    ListOpenshiftSccsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_sccs.list_openshift_sccs_use_case import (  # noqa: E501
    ListOpenshiftSccsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_openshift_sccs() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_openshift_sccs)

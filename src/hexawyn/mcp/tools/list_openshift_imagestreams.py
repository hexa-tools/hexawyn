"""MCP tool: list_openshift_imagestreams."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.openshift.list_openshift_imagestreams.command import (
    ListOpenshiftImagestreamsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_imagestreams.list_openshift_imagestreams_use_case import (  # noqa: E501
    ListOpenshiftImagestreamsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_openshift_imagestreams(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftImagestreamsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftImagestreamsCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_openshift_imagestreams)

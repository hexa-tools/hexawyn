"""MCP tool: list_openshift_projects."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.openshift.list_openshift_projects.command import (
    ListOpenshiftProjectsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_projects.list_openshift_projects_use_case import (  # noqa: E501
    ListOpenshiftProjectsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_openshift_projects() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftProjectsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftProjectsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_openshift_projects)

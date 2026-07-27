"""MCP tool: gitops_apps_list."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_apps_list.command import GitopsAppsListCommand
from hexawyn.application.use_case.gitops.gitops_apps_list.gitops_apps_list_use_case import (
    GitopsAppsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_apps_list() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppsListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_apps_list)

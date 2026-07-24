"""MCP tool: gitops_sources_list."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops_sources_list.command import GitopsSourcesListCommand
from hexawyn.application.use_case.gitops_sources_list.gitops_sources_list_use_case import (
    GitopsSourcesListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_sources_list() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_sources_list)

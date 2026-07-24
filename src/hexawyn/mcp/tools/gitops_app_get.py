"""MCP tool: gitops_app_get."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops_app_get.command import GitopsAppGetCommand
from hexawyn.application.use_case.gitops_app_get.gitops_app_get_use_case import GitopsAppGetUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_get(name="test-name", namespace="test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppGetCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_get)

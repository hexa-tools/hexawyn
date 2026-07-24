"""MCP tool: gitops_source_get."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops_source_get.command import GitopsSourceGetCommand
from hexawyn.application.use_case.gitops_source_get.gitops_source_get_use_case import (
    GitopsSourceGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_source_get(name="test-name", namespace="test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourceGetUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourceGetCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_source_get)

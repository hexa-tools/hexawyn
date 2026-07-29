# mypy: ignore-errors
"""MCP tool: gitops_source_get."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_source_get.command import GitopsSourceGetCommand
from hexawyn.application.use_case.gitops.gitops_source_get.gitops_source_get_use_case import (
    GitopsSourceGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_source_get(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourceGetUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourceGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(gitops_source_get)

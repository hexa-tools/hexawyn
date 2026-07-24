"""MCP tool: gitops_app_status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops_app_status.command import GitopsAppStatusCommand
from hexawyn.application.use_case.gitops_app_status.gitops_app_status_use_case import (
    GitopsAppStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_status(name="test-name", namespace="test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppStatusUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppStatusCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_status)

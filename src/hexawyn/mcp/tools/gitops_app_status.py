# mypy: ignore-errors
"""MCP tool: gitops_app_status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_app_status.command import GitopsAppStatusCommand
from hexawyn.application.use_case.gitops.gitops_app_status.gitops_app_status_use_case import (
    GitopsAppStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_app_status(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppStatusUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppStatusCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(gitops_app_status)

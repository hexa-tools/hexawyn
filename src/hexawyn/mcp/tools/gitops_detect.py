"""MCP tool: gitops_detect."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops_detect.command import GitopsDetectCommand
from hexawyn.application.use_case.gitops_detect.gitops_detect_use_case import GitopsDetectUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def gitops_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsDetectUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_detect)

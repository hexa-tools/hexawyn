"""MCP tool: rollouts_list — List all Argo Rollouts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.rollouts_list.command import RolloutsListCommand
from hexawyn.application.use_case.workloads.rollouts_list.rollouts_list_use_case import (
    RolloutsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def rollouts_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(rollouts_list)

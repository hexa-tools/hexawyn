"""MCP tool: rollout_status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.rollout_status.command import RolloutStatusCommand
from hexawyn.application.use_case.rollout_status.rollout_status_use_case import RolloutStatusUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def rollout_status(name="test-name", namespace="test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutStatusUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutStatusCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(rollout_status)

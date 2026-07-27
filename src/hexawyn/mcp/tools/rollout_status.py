# mypy: ignore-errors
"""MCP tool: rollout_status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.rollout_status.command import RolloutStatusCommand
from hexawyn.application.use_case.workloads.rollout_status.rollout_status_use_case import (
    RolloutStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def rollout_status(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutStatusUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutStatusCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(rollout_status)

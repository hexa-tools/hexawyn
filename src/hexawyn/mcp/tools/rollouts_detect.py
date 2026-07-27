"""MCP tool: rollouts_detect."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.rollouts_detect.command import RolloutsDetectCommand
from hexawyn.application.use_case.workloads.rollouts_detect.rollouts_detect_use_case import (
    RolloutsDetectUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def rollouts_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(rollouts_detect)

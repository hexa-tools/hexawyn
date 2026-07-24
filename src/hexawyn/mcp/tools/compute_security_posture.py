"""MCP tool: compute_security_posture."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.compute_security_posture.command import (
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.compute_security_posture.compute_security_posture_use_case import (
    ComputeSecurityPostureUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_security_posture() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())
        _ = use_case.execute(ComputeSecurityPostureCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_security_posture)

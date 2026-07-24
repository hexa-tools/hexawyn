"""MCP tool: detect_missing_probes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.detect_missing_probes.command import DetectMissingProbesCommand
from hexawyn.application.use_case.detect_missing_probes.detect_missing_probes_use_case import (
    DetectMissingProbesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_missing_probes() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())
        _ = use_case.execute(DetectMissingProbesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_missing_probes)

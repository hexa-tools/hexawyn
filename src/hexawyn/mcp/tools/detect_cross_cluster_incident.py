"""MCP tool: detect_cross_cluster_incident."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.detect_cross_cluster_incident.command import (
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.use_case.detect_cross_cluster_incident.detect_cross_cluster_incident_use_case import (
    DetectCrossClusterIncidentUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_cross_cluster_incident() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectCrossClusterIncidentUseCase(incident_port=build_optimization_roi_adapter())
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_cross_cluster_incident)

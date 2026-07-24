"""MCP tool: detect_network_segmentation_gaps."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.detect_network_segmentation_gaps.command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.use_case.detect_network_segmentation_gaps.detect_network_segmentation_gaps_use_case import (
    DetectNetworkSegmentationGapsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_network_segmentation_gaps() -> dict[str, object]:
    from hexawyn.mcp.server import build_network_policy_audit_adapter

    try:
        use_case = DetectNetworkSegmentationGapsUseCase(port=build_network_policy_audit_adapter())
        _ = use_case.execute(DetectNetworkSegmentationGapsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_network_segmentation_gaps)

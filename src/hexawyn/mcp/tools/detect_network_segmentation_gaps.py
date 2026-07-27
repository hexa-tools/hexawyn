"""MCP tool: detect_network_segmentation_gaps."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.detect_network_segmentation_gaps_use_case import (  # noqa: E501
    DetectNetworkSegmentationGapsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_network_segmentation_gaps() -> dict[str, object]:
    """Detect namespaces with missing or insufficient NetworkPolicies.

    Returns findings per namespace including network status, risk level, and recommendations.
    """
    from hexawyn.mcp.server import build_network_policy_audit_adapter

    try:
        use_case = DetectNetworkSegmentationGapsUseCase(port=build_network_policy_audit_adapter())
        response = use_case.execute(DetectNetworkSegmentationGapsCommand())
        return {
            "findings": response.findings,
            "excluded_namespaces": response.excluded_namespaces,
            "total_namespaces_checked": response.total_namespaces_checked,
            "fully_open_count": response.fully_open_count,
            "partially_restricted_count": response.partially_restricted_count,
            "restricted_count": response.restricted_count,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "excluded_namespaces": [],
            "total_namespaces_checked": 0,
            "fully_open_count": 0,
            "partially_restricted_count": 0,
            "restricted_count": 0,
            "summary": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_network_segmentation_gaps)

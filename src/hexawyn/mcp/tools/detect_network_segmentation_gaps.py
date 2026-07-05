"""MCP tool: detect_network_segmentation_gaps — checks each namespace for
NetworkPolicy coverage, flags namespaces fully open to east-west traffic
(no ingress and no egress restriction), and recommends a default-deny
NetworkPolicy where needed."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.use_case.detect_network_segmentation_gaps.detect_network_segmentation_gaps_use_case import (
    DetectNetworkSegmentationGapsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_network_segmentation_gaps(namespaces: list[str] | None = None) -> dict[str, object]:
    from hexawyn.application.service.east_west_network_segmentation_service import (
        EastWestNetworkSegmentationService,
    )
    from hexawyn.mcp.server import build_network_policy_audit_adapter

    try:
        service = EastWestNetworkSegmentationService(
            network_policy_port=build_network_policy_audit_adapter()
        )
        r = DetectNetworkSegmentationGapsUseCase(service=service).execute(
            DetectNetworkSegmentationGapsCommand(namespaces=namespaces)
        )
        return {
            "findings": r.findings,
            "excluded_namespaces": r.excluded_namespaces,
            "total_namespaces_checked": r.total_namespaces_checked,
            "fully_open_count": r.fully_open_count,
            "partially_restricted_count": r.partially_restricted_count,
            "restricted_count": r.restricted_count,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_network_segmentation_gaps)

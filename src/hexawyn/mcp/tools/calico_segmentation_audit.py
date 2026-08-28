"""MCP tool: calico_segmentation_audit — Calico east-west matrix."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_segmentation_audit.calico_segmentation_audit_use_case import (  # noqa: E501
    CalicoSegmentationAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_segmentation_audit.command import (
    CalicoSegmentationAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _edge_dict(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def calico_segmentation_audit(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_segmentation_audit)

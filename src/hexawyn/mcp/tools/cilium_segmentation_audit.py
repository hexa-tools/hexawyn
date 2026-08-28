"""MCP tool: cilium_segmentation_audit — east-west reachability audit."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.cilium_segmentation_audit.cilium_segmentation_audit_use_case import (  # noqa: E501
    CiliumSegmentationAuditUseCase,
)
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.command import (
    CiliumSegmentationAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cilium_segmentation_audit() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumSegmentationAuditUseCase(port=adapter)
        result = use_case.execute(CiliumSegmentationAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "view": result.view,
            "total_identities": result.total_identities,
            "total_paths": result.total_paths,
            "uncovered_paths": result.uncovered_paths,
            "findings": result.findings,
            "summary": result.summary,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "view": "vanilla",
            "total_identities": 0,
            "total_paths": 0,
            "uncovered_paths": 0,
            "findings": [],
            "summary": "",
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(cilium_segmentation_audit)

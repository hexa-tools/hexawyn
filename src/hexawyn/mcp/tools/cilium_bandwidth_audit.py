"""MCP tool: cilium_bandwidth_audit — Cilium bandwidth manager audit."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.cilium_bandwidth_audit_use_case import (  # noqa: E501
    CiliumBandwidthAuditUseCase,
)
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.command import (
    CiliumBandwidthAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cilium_bandwidth_audit() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(cilium_bandwidth_audit)

"""MCP tool: keda_detect — Detect if KEDA is installed."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda_detect.command import KedaDetectCommand
from hexawyn.application.use_case.keda_detect.keda_detect_use_case import KedaDetectUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaDetectUseCase(keda_port=a)
        r = uc.execute(KedaDetectCommand())
        return {
            "installed": r.installed,
            "version": r.version,
            "namespace": r.namespace,
            "total_scaledobjects": r.total_scaledobjects,
            "ready_scaledobjects": r.ready_scaledobjects,
            "error_scaledobjects": r.error_scaledobjects,
            "scaled_to_zero_count": r.scaled_to_zero_count,
            "total_scaledjobs": r.total_scaledjobs,
            "managed_namespaces": r.managed_namespaces,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "version": None,
            "namespace": None,
            "total_scaledobjects": 0,
            "ready_scaledobjects": 0,
            "error_scaledobjects": 0,
            "scaled_to_zero_count": 0,
            "total_scaledjobs": 0,
            "managed_namespaces": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_detect)

"""MCP tool: detect_cilium_denials — detect Cilium policy denials via Hubble."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.detect_cilium_denials.command import (
    DetectCiliumDenialsCommand,
)
from hexawyn.application.use_case.cilium.detect_cilium_denials.detect_cilium_denials_use_case import (  # noqa: E501
    DetectCiliumDenialsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_cilium_denials(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_cilium_denials)

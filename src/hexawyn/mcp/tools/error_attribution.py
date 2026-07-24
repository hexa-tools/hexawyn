"""MCP tool: error_attribution — Identify which downstream service causes gateway errors."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.error_attribution.command import ErrorAttributionCommand
from hexawyn.application.use_case.error_attribution.error_attribution_use_case import (
    ErrorAttributionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def error_attribution(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(error_attribution)

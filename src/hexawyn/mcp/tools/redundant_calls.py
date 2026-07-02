"""MCP tool: redundant_calls — Detect redundant/N+1 calls in trace flows."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.redundant_calls.redundant_calls_command import (
    RedundantCallsCommand,
)
from hexawyn.application.use_case.redundant_calls.redundant_calls_use_case import (
    RedundantCallsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def redundant_calls(flow: str, trace_id: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.redundant_calls_service import RedundantCallsService
    from hexawyn.mcp.server import build_redundant_call_detection_adapter

    try:
        a = build_redundant_call_detection_adapter()
        r = RedundantCallsUseCase(service=RedundantCallsService(port=a)).execute(
            RedundantCallsCommand(flow=flow, trace_id=trace_id)
        )
        return {
            "flow": r.flow,
            "patterns": r.patterns,
            "total_redundant_calls": r.total_redundant_calls,
            "calculated_waste_ms": r.calculated_waste_ms,
            "error": r.error,
        }
    except Exception as exc:
        return {"flow": flow, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(redundant_calls)

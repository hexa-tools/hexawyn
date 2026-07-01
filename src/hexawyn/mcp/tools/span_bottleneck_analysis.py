"""MCP tool: span_bottleneck_analysis — DB vs Redis bottleneck detection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.span_bottleneck_analysis.span_bottleneck_analysis_use_case import (
    SpanBottleneckAnalysisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def span_bottleneck_analysis(time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.application.service.span_bottleneck_analysis_service import (
        SpanBottleneckAnalysisService,
    )
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        a = build_span_bottleneck_adapter()
        r = SpanBottleneckAnalysisUseCase(service=SpanBottleneckAnalysisService(port=a)).execute(
            SpanBottleneckAnalysisCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "bottleneck": r.bottleneck,
            "confidence": r.confidence,
            "bottleneck_pct_of_total": r.bottleneck_pct_of_total,
            "db_avg_ms": r.db_avg_ms,
            "redis_avg_ms": r.redis_avg_ms,
            "db_slowest": r.db_slowest,
            "redis_slowest": r.redis_slowest,
            "reasons": r.reasons,
            "error": r.error,
        }
    except Exception as exc:
        return {"bottleneck": "neither", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(span_bottleneck_analysis)

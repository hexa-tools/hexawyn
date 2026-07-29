"""MCP tool: span_bottleneck_analysis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.span_bottleneck_analysis.command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.observability.span_bottleneck_analysis.span_bottleneck_analysis_use_case import (  # noqa: E501
    SpanBottleneckAnalysisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def span_bottleneck_analysis() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(span_bottleneck_analysis)

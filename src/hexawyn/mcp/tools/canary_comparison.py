"""MCP tool: canary_comparison — Compare OTel metrics between canary and stable."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.canary_comparison.canary_comparison_use_case import (
    CanaryComparisonUseCase,
)
from hexawyn.application.use_case.pipelines.canary_comparison.command import CanaryComparisonCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def canary_comparison(
    service_name: str, time_window_minutes: int = 30, traffic_split_pct: float = 5.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_canary_comparison_adapter

    try:
        a = build_canary_comparison_adapter()
        uc = CanaryComparisonUseCase(canary_comparison_port=a)  # type: ignore
        r = uc.execute(
            CanaryComparisonCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                traffic_split_pct=traffic_split_pct,
            )
        )
        return {
            "service_name": r.service_name,
            "canary_version": r.canary_version,
            "stable_version": r.stable_version,
            "verdict": r.verdict,
            "confidence": r.confidence,
            "p99_delta_pct": r.p99_delta_pct,
            "error_rate_delta_pct": r.error_rate_delta_pct,
            "canary_count": r.canary_count,
            "stable_count": r.stable_count,
            "traffic_split_pct": r.traffic_split_pct,
            "reasons": r.reasons,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(canary_comparison)

"""MCP tool: version_regression — Detect latency/error regressions between service versions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.version_regression.command import VersionRegressionCommand
from hexawyn.application.use_case.version_regression.version_regression_use_case import (
    VersionRegressionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def version_regression(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(version_regression)

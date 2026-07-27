"""MCP tool: deployment_latency — Compare latency before/after deployment."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.deployment_latency.command import (
    DeploymentLatencyCommand,
)
from hexawyn.application.use_case.observability.deployment_latency.deployment_latency_use_case import (  # noqa: E501
    DeploymentLatencyUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def deployment_latency(
    service_name: str, regression_threshold_pct: float = 20.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_deployment_latency_comparison_adapter

    try:
        a = build_deployment_latency_comparison_adapter()
        r = DeploymentLatencyUseCase(port=a).execute(
            DeploymentLatencyCommand(
                service_name=service_name, regression_threshold_pct=regression_threshold_pct
            )
        )
        return {
            "service_name": r.service_name,
            "verdict": r.verdict,
            "p50_delta_pct": r.p50_delta_pct,
            "p95_delta_pct": r.p95_delta_pct,
            "p99_delta_pct": r.p99_delta_pct,
            "before_p99_ms": r.before_p99_ms,
            "after_p99_ms": r.after_p99_ms,
            "suggestion": r.suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(deployment_latency)

"""MCP tool: estimate_rightsizing_savings — FinOps rightsizing recommendations."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.use_case.estimate_rightsizing_savings.estimate_rightsizing_savings_use_case import (
    EstimateRightsizingSavingsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def estimate_rightsizing_savings(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(estimate_rightsizing_savings)

"""MCP tool: compute_mttr_trend — MTTR trend over last 3 months."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.compute_mttr_trend.command import (  # type: ignore
    ComputeMttrTrendCommand,
)
from hexawyn.application.use_case.workloads.compute_mttr_trend.compute_mttr_trend_use_case import (  # type: ignore
    ComputeMttrTrendUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_mttr_trend(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMttrTrendUseCase(port=adapter)
        response = use_case.execute(ComputeMttrTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "incident_count": s.incident_count,
                        "meets_benchmark": s.meets_benchmark,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "resolution_minutes": i.resolution_minutes,
                    "root_cause": i.root_cause,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_mttr_trend)

"""MCP tool: estimate_cost_saving — FinOps pod-level right-sizing cost savings."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.estimate_cost_saving.command import EstimateCostSavingCommand
from hexawyn.application.use_case.estimate_cost_saving.estimate_cost_saving_use_case import (
    EstimateCostSavingUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def estimate_cost_saving(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)
        response = use_case.execute(
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(estimate_cost_saving)

"""MCP tool: compute_optimization_roi — measures the ROI of a Kubernetes
optimization sprint (cost before/after, savings, top optimizations, and the
performance impact) for demonstrating business value."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.use_case.compute_optimization_roi.compute_optimization_roi_use_case import (  # noqa: E501
    ComputeOptimizationRoiUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.optimization_roi import OptimizationItem, PerformanceImpact


def compute_optimization_roi(sprint_id: str, traffic_growth_pct: float = 0.0) -> dict[str, object]:
    """Measure the ROI of an optimization sprint.

    Returns cost before and after the sprint, monthly and projected annual
    savings, the highest-impact optimizations, and the performance impact
    (flagging any cost/performance trade-off). Savings are normalized against
    traffic growth. When no pre-sprint baseline exists, returns guidance to
    establish one first rather than a misleading zero.
    """
    from hexawyn.application.service.compute_optimization_roi_service import (
        ComputeOptimizationRoiService,
    )
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        adapter = build_optimization_roi_adapter()
        service = ComputeOptimizationRoiService(roi_port=adapter)
        use_case = ComputeOptimizationRoiUseCase(service=service)
        response = use_case.execute(
            ComputeOptimizationRoiCommand(
                sprint_id=sprint_id, traffic_growth_pct=traffic_growth_pct
            )
        )
        report = response.result
        return {
            "has_baseline": report.has_baseline,
            "baseline_monthly_eur": report.baseline_monthly_eur,
            "current_monthly_eur": report.current_monthly_eur,
            "monthly_saving_eur": report.monthly_saving_eur,
            "annual_saving_eur": report.annual_saving_eur,
            "savings_pct": report.savings_pct,
            "optimizations": [_serialize_item(item) for item in report.optimizations],
            "top_optimization": (
                _serialize_item(report.top_optimization)
                if report.top_optimization is not None
                else None
            ),
            "performance_impacts": [
                _serialize_impact(impact) for impact in report.performance_impacts
            ],
            "has_regression": report.has_regression,
            "traffic_normalized": report.traffic_normalized,
            "traffic_growth_pct": report.traffic_growth_pct,
            "warning": report.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "has_baseline": True,
            "baseline_monthly_eur": 0.0,
            "current_monthly_eur": 0.0,
            "monthly_saving_eur": 0.0,
            "annual_saving_eur": 0.0,
            "savings_pct": 0.0,
            "optimizations": [],
            "top_optimization": None,
            "performance_impacts": [],
            "has_regression": False,
            "traffic_normalized": False,
            "traffic_growth_pct": traffic_growth_pct,
            "warning": "",
            "error": str(exc),
        }


def _serialize_item(item: OptimizationItem) -> dict[str, object]:
    return {
        "name": item.name,
        "category": item.category,
        "monthly_saving_eur": item.monthly_saving_eur,
        "description": item.description,
    }


def _serialize_impact(impact: PerformanceImpact) -> dict[str, object]:
    return {
        "metric": impact.metric,
        "before": impact.before,
        "after": impact.after,
        "improved": impact.improved,
        "regressed": impact.regressed,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_optimization_roi)

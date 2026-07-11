from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import SprintRoiData
from hexawyn.domain.models.optimization_roi import OptimizationRoiReport
from hexawyn.domain.services.optimization_roi.performance_analyzer import (
    analyze_performance,
    has_regression,
)
from hexawyn.domain.services.optimization_roi.roi_calculator import (
    compute_savings,
    rank_optimizations,
)

_NO_BASELINE_WARNING = (
    "No pre-sprint cost baseline was recorded — ROI cannot be measured. "
    "Establish a baseline before the next optimization sprint."
)
_REGRESSION_WARNING = (
    "Cost was reduced but a performance metric regressed — review this "
    "cost/performance trade-off before claiming the sprint a success."
)


class OptimizationRoiService:
    """Domain service — turns before/after sprint data into a ROI report:
    monthly and annual savings (traffic-normalized), the highest-impact
    optimizations, and the performance impact (including regressions)."""

    def compute(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["optimizations"])
        impacts = analyze_performance(data["performance_metrics"])
        regression = has_regression(impacts)

        return OptimizationRoiReport(
            baseline_monthly_eur=data["baseline_monthly_eur"],
            current_monthly_eur=data["current_monthly_eur"],
            monthly_saving_eur=savings.monthly_saving_eur,
            annual_saving_eur=savings.annual_saving_eur,
            savings_pct=savings.savings_pct,
            optimizations=optimizations,
            top_optimization=optimizations[0] if optimizations else None,
            performance_impacts=impacts,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

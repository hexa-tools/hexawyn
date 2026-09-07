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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOptimizationRoiServiceǁcompute__mutmut: MutantDict = {}  # type: ignore


class OptimizationRoiService:
    """Domain service — turns before/after sprint data into a ROI report:
    monthly and annual savings (traffic-normalized), the highest-impact
    optimizations, and the performance impact (including regressions)."""

    @_mutmut_mutated(mutants_xǁOptimizationRoiServiceǁcompute__mutmut)
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_orig(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_1(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if data["has_baseline"]:
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_2(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["XXhas_baselineXX"]:
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_3(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["HAS_BASELINE"]:
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_4(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=None, warning=_NO_BASELINE_WARNING)

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

    def xǁOptimizationRoiServiceǁcompute__mutmut_5(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=None)

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

    def xǁOptimizationRoiServiceǁcompute__mutmut_6(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(warning=_NO_BASELINE_WARNING)

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

    def xǁOptimizationRoiServiceǁcompute__mutmut_7(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, )

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

    def xǁOptimizationRoiServiceǁcompute__mutmut_8(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=True, warning=_NO_BASELINE_WARNING)

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

    def xǁOptimizationRoiServiceǁcompute__mutmut_9(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = None
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_10(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=None,
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_11(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=None,
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_12(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=None,
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_13(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_14(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_15(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_16(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["XXbaseline_monthly_eurXX"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_17(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["BASELINE_MONTHLY_EUR"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_18(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["XXcurrent_monthly_eurXX"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_19(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["CURRENT_MONTHLY_EUR"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_20(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = None
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_21(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(None)
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_22(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["XXoptimizationsXX"])
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_23(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["OPTIMIZATIONS"])
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_24(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["optimizations"])
        impacts = None
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_25(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["optimizations"])
        impacts = analyze_performance(None)
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_26(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["optimizations"])
        impacts = analyze_performance(data["XXperformance_metricsXX"])
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_27(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["optimizations"])
        impacts = analyze_performance(data["PERFORMANCE_METRICS"])
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_28(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["optimizations"])
        impacts = analyze_performance(data["performance_metrics"])
        regression = None

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

    def xǁOptimizationRoiServiceǁcompute__mutmut_29(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
        if not data["has_baseline"]:
            return OptimizationRoiReport(has_baseline=False, warning=_NO_BASELINE_WARNING)

        savings = compute_savings(
            baseline=data["baseline_monthly_eur"],
            current=data["current_monthly_eur"],
            traffic_growth_pct=traffic_growth_pct,
        )
        optimizations = rank_optimizations(data["optimizations"])
        impacts = analyze_performance(data["performance_metrics"])
        regression = has_regression(None)

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

    def xǁOptimizationRoiServiceǁcompute__mutmut_30(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            baseline_monthly_eur=None,
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_31(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            current_monthly_eur=None,
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_32(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            monthly_saving_eur=None,
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_33(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            annual_saving_eur=None,
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_34(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            savings_pct=None,
            optimizations=optimizations,
            top_optimization=optimizations[0] if optimizations else None,
            performance_impacts=impacts,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_35(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            optimizations=None,
            top_optimization=optimizations[0] if optimizations else None,
            performance_impacts=impacts,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_36(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            top_optimization=None,
            performance_impacts=impacts,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_37(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            performance_impacts=None,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_38(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            has_regression=None,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_39(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            traffic_normalized=None,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_40(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            traffic_growth_pct=None,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_41(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            has_baseline=None,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_42(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            warning=None,
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_43(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_44(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_45(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_46(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_47(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            optimizations=optimizations,
            top_optimization=optimizations[0] if optimizations else None,
            performance_impacts=impacts,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_48(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            top_optimization=optimizations[0] if optimizations else None,
            performance_impacts=impacts,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_49(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            performance_impacts=impacts,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_50(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_51(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_52(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_53(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_54(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_55(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            )

    def xǁOptimizationRoiServiceǁcompute__mutmut_56(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            baseline_monthly_eur=data["XXbaseline_monthly_eurXX"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_57(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            baseline_monthly_eur=data["BASELINE_MONTHLY_EUR"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_58(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            current_monthly_eur=data["XXcurrent_monthly_eurXX"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_59(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            current_monthly_eur=data["CURRENT_MONTHLY_EUR"],
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

    def xǁOptimizationRoiServiceǁcompute__mutmut_60(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            top_optimization=optimizations[1] if optimizations else None,
            performance_impacts=impacts,
            has_regression=regression,
            traffic_normalized=savings.traffic_normalized,
            traffic_growth_pct=traffic_growth_pct,
            has_baseline=True,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_61(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            has_baseline=False,
            warning=_REGRESSION_WARNING if regression else "",
        )

    def xǁOptimizationRoiServiceǁcompute__mutmut_62(self, data: SprintRoiData, traffic_growth_pct: float) -> OptimizationRoiReport:
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
            warning=_REGRESSION_WARNING if regression else "XXXX",
        )

mutants_xǁOptimizationRoiServiceǁcompute__mutmut['_mutmut_orig'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_1'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_2'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_3'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_4'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_5'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_6'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_7'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_8'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_9'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_10'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_11'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_12'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_13'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_14'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_15'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_16'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_17'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_18'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_19'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_20'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_21'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_22'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_23'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_24'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_25'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_26'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_27'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_28'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_29'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_30'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_31'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_32'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_33'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_34'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_35'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_36'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_37'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_38'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_39'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_40'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_41'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_42'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_43'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_44'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_45'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_46'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_47'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_48'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_49'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_50'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_51'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_52'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_53'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_54'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_55'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_56'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_57'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_58'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_59'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_60'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_61'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOptimizationRoiServiceǁcompute__mutmut['xǁOptimizationRoiServiceǁcompute__mutmut_62'] = OptimizationRoiService.xǁOptimizationRoiServiceǁcompute__mutmut_62 # type: ignore # mutmut generated

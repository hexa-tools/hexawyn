from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
)
from hexawyn.infrastructure.config.config_manager import load_config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut: MutantDict = {}  # type: ignore


class ConfigBudgetIntelligenceSource:
    @_mutmut_mutated(mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut)
    def fetch_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_orig(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_1(self, period: str) -> BudgetIntelligenceData:
        config = None
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_2(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = None
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_3(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get(None)
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_4(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("XXbusinessXX")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_5(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("BUSINESS")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_6(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = ""
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_7(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = None
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_8(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get(None)
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_9(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("XXcloud_budget_monthlyXX")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_10(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("CLOUD_BUDGET_MONTHLY")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_11(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = None
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_12(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(None)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_13(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=None,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_14(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=None,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_15(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=None,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_16(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_17(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_18(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_19(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=1.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )
    def xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_20(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=1.0,
            budget_monthly_eur=budget,
        )

mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['_mutmut_orig'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_1'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_2'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_3'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_4'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_5'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_6'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_7'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_8'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_9'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_10'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_11'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_12'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_13'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_14'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_15'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_16'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_17'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_18'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_19'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut['xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_20'] = ConfigBudgetIntelligenceSource.xǁConfigBudgetIntelligenceSourceǁfetch_budget_intelligence_data__mutmut_20 # type: ignore # mutmut generated
mutants_x__as_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float__mutmut)
def _as_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None


def x__as_float__mutmut_orig(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None


def x__as_float__mutmut_1(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(None)
    return None

mutants_x__as_float__mutmut['_mutmut_orig'] = x__as_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_1'] = x__as_float__mutmut_1 # type: ignore # mutmut generated

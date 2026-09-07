from __future__ import annotations

from hexawyn.application.ports.driven.budget_projection_port import (
    BudgetProjectionPort,
    MonthlyCostRaw,
)
from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort

_DAYS_PER_MONTH = 30
_COMPUTE_SHARE = 0.6
_STORAGE_SHARE = 0.25
_NETWORK_SHARE = 0.15


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁBudgetProjectionAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut: MutantDict = {}  # type: ignore


class BudgetProjectionAdapter(BudgetProjectionPort):
    """Aggregates the daily cost source into monthly history by category.

    Daily costs (from CostForecastPort) are grouped into calendar months and
    each month's total is attributed to compute / storage / network using a
    fixed cloud-typical split, keeping category attribution in the adapter so
    the domain stays agnostic.
    """

    @_mutmut_mutated(mutants_xǁBudgetProjectionAdapterǁ__init____mutmut)
    def __init__(self, cost_forecast_port: CostForecastPort) -> None:
        self._cost_forecast_port = cost_forecast_port

    def xǁBudgetProjectionAdapterǁ__init____mutmut_orig(self, cost_forecast_port: CostForecastPort) -> None:
        self._cost_forecast_port = cost_forecast_port

    def xǁBudgetProjectionAdapterǁ__init____mutmut_1(self, cost_forecast_port: CostForecastPort) -> None:
        self._cost_forecast_port = None

    @_mutmut_mutated(mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut)
    def get_monthly_cost_history(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_orig(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_1(self, months: int) -> list[MonthlyCostRaw]:
        daily = None
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_2(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(None)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_3(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months / _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_4(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = None
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_5(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = None
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_6(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(None)
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_7(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["XXdateXX"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_8(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["DATE"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_9(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is not None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_10(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                break
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_11(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = None

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_12(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) - entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_13(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(None, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_14(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, None) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_15(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_16(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, ) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_17(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 1.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_18(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["XXtotal_usdXX"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_19(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["TOTAL_USD"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_20(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(None, total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_21(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, None) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_22(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(total) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_23(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, ) for month, total in sorted(totals_by_month.items())]

    def xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_24(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(None)]

mutants_xǁBudgetProjectionAdapterǁ__init____mutmut['_mutmut_orig'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁ__init____mutmut['xǁBudgetProjectionAdapterǁ__init____mutmut_1'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['_mutmut_orig'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_1'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_2'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_3'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_4'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_5'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_6'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_7'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_8'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_9'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_10'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_11'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_12'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_13'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_14'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_15'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_16'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_17'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_18'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_19'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_20'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_21'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_22'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_23'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut['xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_24'] = BudgetProjectionAdapter.xǁBudgetProjectionAdapterǁget_monthly_cost_history__mutmut_24 # type: ignore # mutmut generated
mutants_x__month_of__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__month_of__mutmut)
def _month_of(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_orig(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_1(date: str) -> str | None:
    parts = None
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_2(date: str) -> str | None:
    parts = date.split(None)
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_3(date: str) -> str | None:
    parts = date.split("XX-XX")
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_4(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[0].isdigit() and not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_5(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 and not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_6(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) <= 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_7(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 3 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_8(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_9(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[1].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_10(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[0].isdigit() or parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_11(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[0].isdigit() or not parts[2].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def x__month_of__mutmut_12(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[1]}-{parts[1]}"


def x__month_of__mutmut_13(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[2]}"

mutants_x__month_of__mutmut['_mutmut_orig'] = x__month_of__mutmut_orig # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_1'] = x__month_of__mutmut_1 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_2'] = x__month_of__mutmut_2 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_3'] = x__month_of__mutmut_3 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_4'] = x__month_of__mutmut_4 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_5'] = x__month_of__mutmut_5 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_6'] = x__month_of__mutmut_6 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_7'] = x__month_of__mutmut_7 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_8'] = x__month_of__mutmut_8 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_9'] = x__month_of__mutmut_9 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_10'] = x__month_of__mutmut_10 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_11'] = x__month_of__mutmut_11 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_12'] = x__month_of__mutmut_12 # type: ignore # mutmut generated
mutants_x__month_of__mutmut['x__month_of__mutmut_13'] = x__month_of__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_monthly_raw__mutmut)
def _to_monthly_raw(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_orig(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_1(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=None,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_2(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=None,
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_3(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=None,
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_4(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=None,
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_5(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=None,
    )


def x__to_monthly_raw__mutmut_6(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_7(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_8(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_9(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_10(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        )


def x__to_monthly_raw__mutmut_11(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(None, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_12(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, None),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_13(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_14(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, ),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_15(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 3),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_16(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(None, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_17(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, None),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_18(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_19(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, ),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_20(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total / _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_21(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 3),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_22(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(None, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_23(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, None),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_24(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_25(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, ),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_26(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total / _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_27(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 3),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_28(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(None, 2),
    )


def x__to_monthly_raw__mutmut_29(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, None),
    )


def x__to_monthly_raw__mutmut_30(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(2),
    )


def x__to_monthly_raw__mutmut_31(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, ),
    )


def x__to_monthly_raw__mutmut_32(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total / _NETWORK_SHARE, 2),
    )


def x__to_monthly_raw__mutmut_33(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 3),
    )

mutants_x__to_monthly_raw__mutmut['_mutmut_orig'] = x__to_monthly_raw__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_1'] = x__to_monthly_raw__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_2'] = x__to_monthly_raw__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_3'] = x__to_monthly_raw__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_4'] = x__to_monthly_raw__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_5'] = x__to_monthly_raw__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_6'] = x__to_monthly_raw__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_7'] = x__to_monthly_raw__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_8'] = x__to_monthly_raw__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_9'] = x__to_monthly_raw__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_10'] = x__to_monthly_raw__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_11'] = x__to_monthly_raw__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_12'] = x__to_monthly_raw__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_13'] = x__to_monthly_raw__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_14'] = x__to_monthly_raw__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_15'] = x__to_monthly_raw__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_16'] = x__to_monthly_raw__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_17'] = x__to_monthly_raw__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_18'] = x__to_monthly_raw__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_19'] = x__to_monthly_raw__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_20'] = x__to_monthly_raw__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_21'] = x__to_monthly_raw__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_22'] = x__to_monthly_raw__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_23'] = x__to_monthly_raw__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_24'] = x__to_monthly_raw__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_25'] = x__to_monthly_raw__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_26'] = x__to_monthly_raw__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_27'] = x__to_monthly_raw__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_28'] = x__to_monthly_raw__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_29'] = x__to_monthly_raw__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_30'] = x__to_monthly_raw__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_31'] = x__to_monthly_raw__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_32'] = x__to_monthly_raw__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_monthly_raw__mutmut['x__to_monthly_raw__mutmut_33'] = x__to_monthly_raw__mutmut_33 # type: ignore # mutmut generated

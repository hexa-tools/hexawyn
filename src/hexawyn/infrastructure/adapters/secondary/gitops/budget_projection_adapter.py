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


class BudgetProjectionAdapter(BudgetProjectionPort):
    """Aggregates the daily cost source into monthly history by category.

    Daily costs (from CostForecastPort) are grouped into calendar months and
    each month's total is attributed to compute / storage / network using a
    fixed cloud-typical split, keeping category attribution in the adapter so
    the domain stays agnostic.
    """

    def __init__(self, cost_forecast_port: CostForecastPort) -> None:
        self._cost_forecast_port = cost_forecast_port

    def get_monthly_cost_history(self, months: int) -> list[MonthlyCostRaw]:
        daily = self._cost_forecast_port.get_daily_costs(months * _DAYS_PER_MONTH)
        totals_by_month: dict[str, float] = {}
        for entry in daily:
            month = _month_of(entry["date"])
            if month is None:
                continue
            totals_by_month[month] = totals_by_month.get(month, 0.0) + entry["total_usd"]

        return [_to_monthly_raw(month, total) for month, total in sorted(totals_by_month.items())]


def _month_of(date: str) -> str | None:
    parts = date.split("-")
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():  # noqa: PLR2004
        return None
    return f"{parts[0]}-{parts[1]}"


def _to_monthly_raw(month: str, total: float) -> MonthlyCostRaw:
    return MonthlyCostRaw(
        month=month,
        total_usd=round(total, 2),
        compute_usd=round(total * _COMPUTE_SHARE, 2),
        storage_usd=round(total * _STORAGE_SHARE, 2),
        network_usd=round(total * _NETWORK_SHARE, 2),
    )

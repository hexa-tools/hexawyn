from __future__ import annotations

from datetime import datetime

from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
from hexawyn.application.use_case.forecast_cost.command import ForecastCostCommand
from hexawyn.application.use_case.forecast_cost.response import (
    CostDriver,
    CostForecastResult,
    ForecastCostResponse,
)


class ForecastCostUseCase:
    def __init__(self, port: CostForecastPort) -> None:
        self._port = port

    def execute(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)

        now = datetime.now()
        month_str = f"{now.year}-{now.month:02d}"
        days_in_month = 30
        days_elapsed = min(len(daily_costs), command.historical_days)
        days_remaining = max(0, days_in_month - days_elapsed)

        current_spend = sum(d["total_usd"] for d in daily_costs)
        avg_daily = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        projected = current_spend + (avg_daily * days_remaining)

        trend_factor = 1.0
        if len(daily_costs) >= 3:
            recent = daily_costs[-3:]
            earlier = daily_costs[:3]
            if earlier and sum(e["total_usd"] for e in earlier) > 0:
                trend_factor = sum(r.total_usd for r in recent) / sum(e["total_usd"] for e in earlier)

        ns_totals: dict[str, float] = {}
        for d in daily_costs:
            for nc in d["namespace_costs"]:
                ns_totals[nc["name"]] = ns_totals.get(nc["name"], 0.0) + nc["cost_usd"]

        sorted_ns = sorted(ns_totals.items(), key=lambda x: x[1], reverse=True)
        total_all = sum(v for _, v in sorted_ns)
        drivers = [
            CostDriver(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(val, 2),
                percentage=round(val / total_all * 100, 1) if total_all > 0 else 0.0,
            )
            for name, val in sorted_ns[: command.top_n_drivers]
        ]

        forecast = CostForecastResult(
            cluster_name="default",
            month=month_str,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=round(projected, 2),
            previous_month_usd=None,
            month_over_month_delta=0.0,
            trend_factor=round(trend_factor, 2),
            top_cost_drivers=drivers,
            forecast_confidence="medium",
            historical_days_used=days_elapsed,
            data_source="estimated",
        )
        return ForecastCostResponse(forecast=forecast)

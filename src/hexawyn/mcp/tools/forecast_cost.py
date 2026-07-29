"""MCP tool: forecast_cost — FinOps cost predictive model."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.forecast_cost.command import (
    ForecastCostCommand,
)
from hexawyn.application.use_case.finops.forecast_cost.forecast_cost_use_case import (
    ForecastCostUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def forecast_cost(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
    """Project end-of-month Kubernetes cluster spend based on resource request trends.

    Args:
        historical_days: Days of cost history to use (7 = Free, 30/90 = Pro).
        top_n_drivers: Number of top cost drivers to surface (default: 3).
    """
    from hexawyn.mcp.server import build_cost_forecast_adapter

    try:
        adapter = build_cost_forecast_adapter()
        use_case = ForecastCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ForecastCostCommand(historical_days=historical_days, top_n_drivers=top_n_drivers)
        )
        f = response.forecast
        return {
            "cluster_name": f.cluster_name,
            "month": f.month,
            "days_elapsed": f.days_elapsed,
            "days_remaining": f.days_remaining,
            "current_spend_usd": f.current_spend_usd,
            "projected_total_usd": f.projected_total_usd,
            "previous_month_usd": f.previous_month_usd,
            "month_over_month_delta_pct": f.month_over_month_delta,
            "trend_factor": f.trend_factor,
            "top_cost_drivers": [
                {
                    "name": d.name,
                    "kind": d.kind,
                    "monthly_cost_usd": d.monthly_cost_usd,
                    "percentage": d.percentage,
                }
                for d in f.top_cost_drivers
            ],
            "forecast_confidence": f.forecast_confidence,
            "historical_days_used": f.historical_days_used,
            "data_source": f.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "cluster_name": "",
            "month": "",
            "days_elapsed": 0,
            "days_remaining": 0,
            "current_spend_usd": 0.0,
            "projected_total_usd": 0.0,
            "previous_month_usd": None,
            "month_over_month_delta_pct": 0.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(forecast_cost)

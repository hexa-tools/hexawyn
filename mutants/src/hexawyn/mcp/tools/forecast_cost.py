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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_forecast_cost__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_forecast_cost__mutmut)
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


def x_forecast_cost__mutmut_orig(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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


def x_forecast_cost__mutmut_1(historical_days: int = 8, top_n_drivers: int = 3) -> dict[str, object]:
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


def x_forecast_cost__mutmut_2(historical_days: int = 7, top_n_drivers: int = 4) -> dict[str, object]:
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


def x_forecast_cost__mutmut_3(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
    """Project end-of-month Kubernetes cluster spend based on resource request trends.

    Args:
        historical_days: Days of cost history to use (7 = Free, 30/90 = Pro).
        top_n_drivers: Number of top cost drivers to surface (default: 3).
    """
    from hexawyn.mcp.server import build_cost_forecast_adapter

    try:
        adapter = None
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


def x_forecast_cost__mutmut_4(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
    """Project end-of-month Kubernetes cluster spend based on resource request trends.

    Args:
        historical_days: Days of cost history to use (7 = Free, 30/90 = Pro).
        top_n_drivers: Number of top cost drivers to surface (default: 3).
    """
    from hexawyn.mcp.server import build_cost_forecast_adapter

    try:
        adapter = build_cost_forecast_adapter()
        use_case = None  # type: ignore
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


def x_forecast_cost__mutmut_5(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
    """Project end-of-month Kubernetes cluster spend based on resource request trends.

    Args:
        historical_days: Days of cost history to use (7 = Free, 30/90 = Pro).
        top_n_drivers: Number of top cost drivers to surface (default: 3).
    """
    from hexawyn.mcp.server import build_cost_forecast_adapter

    try:
        adapter = build_cost_forecast_adapter()
        use_case = ForecastCostUseCase(port=None)  # type: ignore
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


def x_forecast_cost__mutmut_6(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
    """Project end-of-month Kubernetes cluster spend based on resource request trends.

    Args:
        historical_days: Days of cost history to use (7 = Free, 30/90 = Pro).
        top_n_drivers: Number of top cost drivers to surface (default: 3).
    """
    from hexawyn.mcp.server import build_cost_forecast_adapter

    try:
        adapter = build_cost_forecast_adapter()
        use_case = ForecastCostUseCase(port=adapter)  # type: ignore
        response = None
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


def x_forecast_cost__mutmut_7(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            None
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


def x_forecast_cost__mutmut_8(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            ForecastCostCommand(historical_days=None, top_n_drivers=top_n_drivers)
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


def x_forecast_cost__mutmut_9(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            ForecastCostCommand(historical_days=historical_days, top_n_drivers=None)
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


def x_forecast_cost__mutmut_10(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            ForecastCostCommand(top_n_drivers=top_n_drivers)
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


def x_forecast_cost__mutmut_11(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            ForecastCostCommand(historical_days=historical_days, )
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


def x_forecast_cost__mutmut_12(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
        f = None
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


def x_forecast_cost__mutmut_13(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXcluster_nameXX": f.cluster_name,
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


def x_forecast_cost__mutmut_14(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "CLUSTER_NAME": f.cluster_name,
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


def x_forecast_cost__mutmut_15(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXmonthXX": f.month,
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


def x_forecast_cost__mutmut_16(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "MONTH": f.month,
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


def x_forecast_cost__mutmut_17(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXdays_elapsedXX": f.days_elapsed,
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


def x_forecast_cost__mutmut_18(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "DAYS_ELAPSED": f.days_elapsed,
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


def x_forecast_cost__mutmut_19(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXdays_remainingXX": f.days_remaining,
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


def x_forecast_cost__mutmut_20(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "DAYS_REMAINING": f.days_remaining,
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


def x_forecast_cost__mutmut_21(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXcurrent_spend_usdXX": f.current_spend_usd,
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


def x_forecast_cost__mutmut_22(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "CURRENT_SPEND_USD": f.current_spend_usd,
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


def x_forecast_cost__mutmut_23(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXprojected_total_usdXX": f.projected_total_usd,
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


def x_forecast_cost__mutmut_24(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "PROJECTED_TOTAL_USD": f.projected_total_usd,
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


def x_forecast_cost__mutmut_25(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXprevious_month_usdXX": f.previous_month_usd,
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


def x_forecast_cost__mutmut_26(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "PREVIOUS_MONTH_USD": f.previous_month_usd,
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


def x_forecast_cost__mutmut_27(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXmonth_over_month_delta_pctXX": f.month_over_month_delta,
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


def x_forecast_cost__mutmut_28(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "MONTH_OVER_MONTH_DELTA_PCT": f.month_over_month_delta,
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


def x_forecast_cost__mutmut_29(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXtrend_factorXX": f.trend_factor,
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


def x_forecast_cost__mutmut_30(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "TREND_FACTOR": f.trend_factor,
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


def x_forecast_cost__mutmut_31(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXtop_cost_driversXX": [
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


def x_forecast_cost__mutmut_32(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "TOP_COST_DRIVERS": [
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


def x_forecast_cost__mutmut_33(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
                    "XXnameXX": d.name,
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


def x_forecast_cost__mutmut_34(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
                    "NAME": d.name,
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


def x_forecast_cost__mutmut_35(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
                    "XXkindXX": d.kind,
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


def x_forecast_cost__mutmut_36(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
                    "KIND": d.kind,
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


def x_forecast_cost__mutmut_37(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
                    "XXmonthly_cost_usdXX": d.monthly_cost_usd,
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


def x_forecast_cost__mutmut_38(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
                    "MONTHLY_COST_USD": d.monthly_cost_usd,
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


def x_forecast_cost__mutmut_39(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
                    "XXpercentageXX": d.percentage,
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


def x_forecast_cost__mutmut_40(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
                    "PERCENTAGE": d.percentage,
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


def x_forecast_cost__mutmut_41(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXforecast_confidenceXX": f.forecast_confidence,
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


def x_forecast_cost__mutmut_42(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "FORECAST_CONFIDENCE": f.forecast_confidence,
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


def x_forecast_cost__mutmut_43(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXhistorical_days_usedXX": f.historical_days_used,
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


def x_forecast_cost__mutmut_44(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "HISTORICAL_DAYS_USED": f.historical_days_used,
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


def x_forecast_cost__mutmut_45(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXdata_sourceXX": f.data_source,
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


def x_forecast_cost__mutmut_46(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "DATA_SOURCE": f.data_source,
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


def x_forecast_cost__mutmut_47(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXerrorXX": None,
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


def x_forecast_cost__mutmut_48(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "ERROR": None,
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


def x_forecast_cost__mutmut_49(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXcluster_nameXX": "",
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


def x_forecast_cost__mutmut_50(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "CLUSTER_NAME": "",
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


def x_forecast_cost__mutmut_51(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "cluster_name": "XXXX",
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


def x_forecast_cost__mutmut_52(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXmonthXX": "",
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


def x_forecast_cost__mutmut_53(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "MONTH": "",
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


def x_forecast_cost__mutmut_54(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "month": "XXXX",
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


def x_forecast_cost__mutmut_55(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXdays_elapsedXX": 0,
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


def x_forecast_cost__mutmut_56(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "DAYS_ELAPSED": 0,
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


def x_forecast_cost__mutmut_57(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "days_elapsed": 1,
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


def x_forecast_cost__mutmut_58(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXdays_remainingXX": 0,
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


def x_forecast_cost__mutmut_59(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "DAYS_REMAINING": 0,
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


def x_forecast_cost__mutmut_60(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "days_remaining": 1,
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


def x_forecast_cost__mutmut_61(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXcurrent_spend_usdXX": 0.0,
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


def x_forecast_cost__mutmut_62(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "CURRENT_SPEND_USD": 0.0,
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


def x_forecast_cost__mutmut_63(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "current_spend_usd": 1.0,
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


def x_forecast_cost__mutmut_64(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXprojected_total_usdXX": 0.0,
            "previous_month_usd": None,
            "month_over_month_delta_pct": 0.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_65(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "PROJECTED_TOTAL_USD": 0.0,
            "previous_month_usd": None,
            "month_over_month_delta_pct": 0.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_66(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "projected_total_usd": 1.0,
            "previous_month_usd": None,
            "month_over_month_delta_pct": 0.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_67(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXprevious_month_usdXX": None,
            "month_over_month_delta_pct": 0.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_68(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "PREVIOUS_MONTH_USD": None,
            "month_over_month_delta_pct": 0.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_69(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXmonth_over_month_delta_pctXX": 0.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_70(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "MONTH_OVER_MONTH_DELTA_PCT": 0.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_71(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "month_over_month_delta_pct": 1.0,
            "trend_factor": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_72(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXtrend_factorXX": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_73(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "TREND_FACTOR": 1.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_74(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "trend_factor": 2.0,
            "top_cost_drivers": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_75(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXtop_cost_driversXX": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_76(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "TOP_COST_DRIVERS": [],
            "forecast_confidence": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_77(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXforecast_confidenceXX": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_78(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "FORECAST_CONFIDENCE": "low",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_79(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "forecast_confidence": "XXlowXX",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_80(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "forecast_confidence": "LOW",
            "historical_days_used": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_81(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXhistorical_days_usedXX": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_82(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "HISTORICAL_DAYS_USED": 0,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_83(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "historical_days_used": 1,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_84(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXdata_sourceXX": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_85(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "DATA_SOURCE": "estimated",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_86(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "data_source": "XXestimatedXX",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_87(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "data_source": "ESTIMATED",
            "error": str(exc),
        }


def x_forecast_cost__mutmut_88(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "XXerrorXX": str(exc),
        }


def x_forecast_cost__mutmut_89(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "ERROR": str(exc),
        }


def x_forecast_cost__mutmut_90(historical_days: int = 7, top_n_drivers: int = 3) -> dict[str, object]:
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
            "error": str(None),
        }

mutants_x_forecast_cost__mutmut['_mutmut_orig'] = x_forecast_cost__mutmut_orig # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_1'] = x_forecast_cost__mutmut_1 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_2'] = x_forecast_cost__mutmut_2 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_3'] = x_forecast_cost__mutmut_3 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_4'] = x_forecast_cost__mutmut_4 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_5'] = x_forecast_cost__mutmut_5 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_6'] = x_forecast_cost__mutmut_6 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_7'] = x_forecast_cost__mutmut_7 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_8'] = x_forecast_cost__mutmut_8 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_9'] = x_forecast_cost__mutmut_9 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_10'] = x_forecast_cost__mutmut_10 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_11'] = x_forecast_cost__mutmut_11 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_12'] = x_forecast_cost__mutmut_12 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_13'] = x_forecast_cost__mutmut_13 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_14'] = x_forecast_cost__mutmut_14 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_15'] = x_forecast_cost__mutmut_15 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_16'] = x_forecast_cost__mutmut_16 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_17'] = x_forecast_cost__mutmut_17 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_18'] = x_forecast_cost__mutmut_18 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_19'] = x_forecast_cost__mutmut_19 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_20'] = x_forecast_cost__mutmut_20 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_21'] = x_forecast_cost__mutmut_21 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_22'] = x_forecast_cost__mutmut_22 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_23'] = x_forecast_cost__mutmut_23 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_24'] = x_forecast_cost__mutmut_24 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_25'] = x_forecast_cost__mutmut_25 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_26'] = x_forecast_cost__mutmut_26 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_27'] = x_forecast_cost__mutmut_27 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_28'] = x_forecast_cost__mutmut_28 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_29'] = x_forecast_cost__mutmut_29 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_30'] = x_forecast_cost__mutmut_30 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_31'] = x_forecast_cost__mutmut_31 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_32'] = x_forecast_cost__mutmut_32 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_33'] = x_forecast_cost__mutmut_33 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_34'] = x_forecast_cost__mutmut_34 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_35'] = x_forecast_cost__mutmut_35 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_36'] = x_forecast_cost__mutmut_36 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_37'] = x_forecast_cost__mutmut_37 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_38'] = x_forecast_cost__mutmut_38 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_39'] = x_forecast_cost__mutmut_39 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_40'] = x_forecast_cost__mutmut_40 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_41'] = x_forecast_cost__mutmut_41 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_42'] = x_forecast_cost__mutmut_42 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_43'] = x_forecast_cost__mutmut_43 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_44'] = x_forecast_cost__mutmut_44 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_45'] = x_forecast_cost__mutmut_45 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_46'] = x_forecast_cost__mutmut_46 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_47'] = x_forecast_cost__mutmut_47 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_48'] = x_forecast_cost__mutmut_48 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_49'] = x_forecast_cost__mutmut_49 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_50'] = x_forecast_cost__mutmut_50 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_51'] = x_forecast_cost__mutmut_51 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_52'] = x_forecast_cost__mutmut_52 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_53'] = x_forecast_cost__mutmut_53 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_54'] = x_forecast_cost__mutmut_54 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_55'] = x_forecast_cost__mutmut_55 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_56'] = x_forecast_cost__mutmut_56 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_57'] = x_forecast_cost__mutmut_57 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_58'] = x_forecast_cost__mutmut_58 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_59'] = x_forecast_cost__mutmut_59 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_60'] = x_forecast_cost__mutmut_60 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_61'] = x_forecast_cost__mutmut_61 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_62'] = x_forecast_cost__mutmut_62 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_63'] = x_forecast_cost__mutmut_63 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_64'] = x_forecast_cost__mutmut_64 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_65'] = x_forecast_cost__mutmut_65 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_66'] = x_forecast_cost__mutmut_66 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_67'] = x_forecast_cost__mutmut_67 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_68'] = x_forecast_cost__mutmut_68 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_69'] = x_forecast_cost__mutmut_69 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_70'] = x_forecast_cost__mutmut_70 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_71'] = x_forecast_cost__mutmut_71 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_72'] = x_forecast_cost__mutmut_72 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_73'] = x_forecast_cost__mutmut_73 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_74'] = x_forecast_cost__mutmut_74 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_75'] = x_forecast_cost__mutmut_75 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_76'] = x_forecast_cost__mutmut_76 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_77'] = x_forecast_cost__mutmut_77 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_78'] = x_forecast_cost__mutmut_78 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_79'] = x_forecast_cost__mutmut_79 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_80'] = x_forecast_cost__mutmut_80 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_81'] = x_forecast_cost__mutmut_81 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_82'] = x_forecast_cost__mutmut_82 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_83'] = x_forecast_cost__mutmut_83 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_84'] = x_forecast_cost__mutmut_84 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_85'] = x_forecast_cost__mutmut_85 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_86'] = x_forecast_cost__mutmut_86 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_87'] = x_forecast_cost__mutmut_87 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_88'] = x_forecast_cost__mutmut_88 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_89'] = x_forecast_cost__mutmut_89 # type: ignore # mutmut generated
mutants_x_forecast_cost__mutmut['x_forecast_cost__mutmut_90'] = x_forecast_cost__mutmut_90 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(forecast_cost)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(forecast_cost)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated

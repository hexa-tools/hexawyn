from __future__ import annotations

from hexawyn.domain.models.cost_forecast import CostForecast, ResourceCost

_TREND_WINDOW = 3  # days used to compute recent trend


class CostForecastEngine:
    """Pure domain service — no infra deps, no try/catch."""

    def forecast(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )


def _compute_current_spend(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def _compute_trend(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def _month_over_month_delta(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, 2)


def _top_drivers(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0

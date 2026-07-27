from __future__ import annotations

import math

from hexawyn.application.ports.driven.engineer_workload_port import MonthNightData
from hexawyn.domain.models.engineer_workload import NightInterventionReport


def compute_night_intervention_report(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def _average(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def _compute_trend(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def _build_summary(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )

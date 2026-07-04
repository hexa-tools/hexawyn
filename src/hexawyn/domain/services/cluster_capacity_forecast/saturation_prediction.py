from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(frozen=True)
class SaturationPrediction:
    days_to_saturation: int | None
    saturation_date: str | None
    capped_horizon: bool


def predict_saturation(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )

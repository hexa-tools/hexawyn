from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from statistics import mean

from hexawyn.domain.models.constants import HotNodeAnalysisConstants

_cfg = HotNodeAnalysisConstants()


@dataclass(frozen=True)
class HotStatus:
    is_hot: bool
    avg_percent: float
    hot_hours: int
    business_hours_pattern: bool


def compute_hot_status(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=0, business_hours_pattern=False)

    values = [value for _, value in series]
    hot_points = [(timestamp, value) for timestamp, value in series if value > threshold_pct]
    hot_hours = len(hot_points)
    is_hot = (hot_hours / len(series) * 100) >= duration_pct

    return HotStatus(
        is_hot=is_hot,
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def _is_business_hours_pattern(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = sum(1 for timestamp in hot_timestamps if _is_business_hour(timestamp))
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def _is_business_hour(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end

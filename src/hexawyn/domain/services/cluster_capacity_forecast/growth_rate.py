from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, median

from hexawyn.domain.models.constants import ClusterCapacityForecastConstants

_cfg = ClusterCapacityForecastConstants()
_MIN_POINTS_FOR_JUMP_DETECTION = 4
_SPIKE_RATIO_THRESHOLD = 2.0


@dataclass(frozen=True)
class GrowthRateResult:
    slope_per_day: float
    window_days_used: int
    capacity_jump_detected: bool
    spike_caveat: bool


def detect_capacity_jump(daily_values: list[float]) -> int | None:
    """Flags a single, discrete step change (e.g. a node joining mid-window)
    — deliberately distinct from a sustained multi-day acceleration (which is
    a `spike_caveat`, not a capacity jump). Exactly one outlier delta must
    exist; more than one means the series is genuinely trending, not
    step-shifted."""
    if len(daily_values) < _MIN_POINTS_FOR_JUMP_DETECTION:
        return None

    deltas = _deltas(daily_values)
    abs_deltas = [abs(delta) for delta in deltas]
    baseline = median(abs_deltas)
    threshold = _cfg.jump_outlier_multiplier * baseline

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def compute_growth_rate(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def _is_outlier(delta: float, threshold: float, baseline: float) -> bool:
    return delta > threshold if baseline > 0 else delta > 0


def _deltas(values: list[float]) -> list[float]:
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


def _least_squares_slope(series: list[float]) -> float:
    n = len(series)
    if n < 2:
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def _has_recent_spike(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:
        return abs(recent_avg) > 1e-9
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)

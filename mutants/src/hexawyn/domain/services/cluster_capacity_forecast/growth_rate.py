from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, median

from hexawyn.domain.models.constants import ClusterCapacityForecastConstants

_cfg = ClusterCapacityForecastConstants()
_MIN_POINTS_FOR_JUMP_DETECTION = 4
_SPIKE_RATIO_THRESHOLD = 2.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class GrowthRateResult:
    slope_per_day: float
    window_days_used: int
    capacity_jump_detected: bool
    spike_caveat: bool
mutants_x_detect_capacity_jump__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_capacity_jump__mutmut)
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


def x_detect_capacity_jump__mutmut_orig(daily_values: list[float]) -> int | None:
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


def x_detect_capacity_jump__mutmut_1(daily_values: list[float]) -> int | None:
    """Flags a single, discrete step change (e.g. a node joining mid-window)
    — deliberately distinct from a sustained multi-day acceleration (which is
    a `spike_caveat`, not a capacity jump). Exactly one outlier delta must
    exist; more than one means the series is genuinely trending, not
    step-shifted."""
    if len(daily_values) <= _MIN_POINTS_FOR_JUMP_DETECTION:
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


def x_detect_capacity_jump__mutmut_2(daily_values: list[float]) -> int | None:
    """Flags a single, discrete step change (e.g. a node joining mid-window)
    — deliberately distinct from a sustained multi-day acceleration (which is
    a `spike_caveat`, not a capacity jump). Exactly one outlier delta must
    exist; more than one means the series is genuinely trending, not
    step-shifted."""
    if len(daily_values) < _MIN_POINTS_FOR_JUMP_DETECTION:
        return None

    deltas = None
    abs_deltas = [abs(delta) for delta in deltas]
    baseline = median(abs_deltas)
    threshold = _cfg.jump_outlier_multiplier * baseline

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_3(daily_values: list[float]) -> int | None:
    """Flags a single, discrete step change (e.g. a node joining mid-window)
    — deliberately distinct from a sustained multi-day acceleration (which is
    a `spike_caveat`, not a capacity jump). Exactly one outlier delta must
    exist; more than one means the series is genuinely trending, not
    step-shifted."""
    if len(daily_values) < _MIN_POINTS_FOR_JUMP_DETECTION:
        return None

    deltas = _deltas(None)
    abs_deltas = [abs(delta) for delta in deltas]
    baseline = median(abs_deltas)
    threshold = _cfg.jump_outlier_multiplier * baseline

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_4(daily_values: list[float]) -> int | None:
    """Flags a single, discrete step change (e.g. a node joining mid-window)
    — deliberately distinct from a sustained multi-day acceleration (which is
    a `spike_caveat`, not a capacity jump). Exactly one outlier delta must
    exist; more than one means the series is genuinely trending, not
    step-shifted."""
    if len(daily_values) < _MIN_POINTS_FOR_JUMP_DETECTION:
        return None

    deltas = _deltas(daily_values)
    abs_deltas = None
    baseline = median(abs_deltas)
    threshold = _cfg.jump_outlier_multiplier * baseline

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_5(daily_values: list[float]) -> int | None:
    """Flags a single, discrete step change (e.g. a node joining mid-window)
    — deliberately distinct from a sustained multi-day acceleration (which is
    a `spike_caveat`, not a capacity jump). Exactly one outlier delta must
    exist; more than one means the series is genuinely trending, not
    step-shifted."""
    if len(daily_values) < _MIN_POINTS_FOR_JUMP_DETECTION:
        return None

    deltas = _deltas(daily_values)
    abs_deltas = [abs(None) for delta in deltas]
    baseline = median(abs_deltas)
    threshold = _cfg.jump_outlier_multiplier * baseline

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_6(daily_values: list[float]) -> int | None:
    """Flags a single, discrete step change (e.g. a node joining mid-window)
    — deliberately distinct from a sustained multi-day acceleration (which is
    a `spike_caveat`, not a capacity jump). Exactly one outlier delta must
    exist; more than one means the series is genuinely trending, not
    step-shifted."""
    if len(daily_values) < _MIN_POINTS_FOR_JUMP_DETECTION:
        return None

    deltas = _deltas(daily_values)
    abs_deltas = [abs(delta) for delta in deltas]
    baseline = None
    threshold = _cfg.jump_outlier_multiplier * baseline

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_7(daily_values: list[float]) -> int | None:
    """Flags a single, discrete step change (e.g. a node joining mid-window)
    — deliberately distinct from a sustained multi-day acceleration (which is
    a `spike_caveat`, not a capacity jump). Exactly one outlier delta must
    exist; more than one means the series is genuinely trending, not
    step-shifted."""
    if len(daily_values) < _MIN_POINTS_FOR_JUMP_DETECTION:
        return None

    deltas = _deltas(daily_values)
    abs_deltas = [abs(delta) for delta in deltas]
    baseline = median(None)
    threshold = _cfg.jump_outlier_multiplier * baseline

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_8(daily_values: list[float]) -> int | None:
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
    threshold = None

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_9(daily_values: list[float]) -> int | None:
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
    threshold = _cfg.jump_outlier_multiplier / baseline

    outlier_indices = [
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_10(daily_values: list[float]) -> int | None:
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

    outlier_indices = None
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_11(daily_values: list[float]) -> int | None:
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
        index for index, delta in enumerate(None) if _is_outlier(delta, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_12(daily_values: list[float]) -> int | None:
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
        index for index, delta in enumerate(abs_deltas) if _is_outlier(None, threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_13(daily_values: list[float]) -> int | None:
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
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, None, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_14(daily_values: list[float]) -> int | None:
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
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, None)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_15(daily_values: list[float]) -> int | None:
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
        index for index, delta in enumerate(abs_deltas) if _is_outlier(threshold, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_16(daily_values: list[float]) -> int | None:
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
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, baseline)
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_17(daily_values: list[float]) -> int | None:
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
        index for index, delta in enumerate(abs_deltas) if _is_outlier(delta, threshold, )
    ]
    if len(outlier_indices) != 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_18(daily_values: list[float]) -> int | None:
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
    if len(outlier_indices) == 1:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_19(daily_values: list[float]) -> int | None:
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
    if len(outlier_indices) != 2:
        return None
    return outlier_indices[0] + 1


def x_detect_capacity_jump__mutmut_20(daily_values: list[float]) -> int | None:
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
    return outlier_indices[0] - 1


def x_detect_capacity_jump__mutmut_21(daily_values: list[float]) -> int | None:
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
    return outlier_indices[1] + 1


def x_detect_capacity_jump__mutmut_22(daily_values: list[float]) -> int | None:
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
    return outlier_indices[0] + 2

mutants_x_detect_capacity_jump__mutmut['_mutmut_orig'] = x_detect_capacity_jump__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_1'] = x_detect_capacity_jump__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_2'] = x_detect_capacity_jump__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_3'] = x_detect_capacity_jump__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_4'] = x_detect_capacity_jump__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_5'] = x_detect_capacity_jump__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_6'] = x_detect_capacity_jump__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_7'] = x_detect_capacity_jump__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_8'] = x_detect_capacity_jump__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_9'] = x_detect_capacity_jump__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_10'] = x_detect_capacity_jump__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_11'] = x_detect_capacity_jump__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_12'] = x_detect_capacity_jump__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_13'] = x_detect_capacity_jump__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_14'] = x_detect_capacity_jump__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_15'] = x_detect_capacity_jump__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_16'] = x_detect_capacity_jump__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_17'] = x_detect_capacity_jump__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_18'] = x_detect_capacity_jump__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_19'] = x_detect_capacity_jump__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_20'] = x_detect_capacity_jump__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_21'] = x_detect_capacity_jump__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_capacity_jump__mutmut['x_detect_capacity_jump__mutmut_22'] = x_detect_capacity_jump__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_growth_rate__mutmut)
def compute_growth_rate(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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


def x_compute_growth_rate__mutmut_orig(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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


def x_compute_growth_rate__mutmut_1(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = None
    if window_days_used < 2:  # noqa: PLR2004
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


def x_compute_growth_rate__mutmut_2(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used <= 2:  # noqa: PLR2004
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


def x_compute_growth_rate__mutmut_3(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 3:  # noqa: PLR2004
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


def x_compute_growth_rate__mutmut_4(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=None,
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


def x_compute_growth_rate__mutmut_5(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=None,
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


def x_compute_growth_rate__mutmut_6(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=None,
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


def x_compute_growth_rate__mutmut_7(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=None,
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


def x_compute_growth_rate__mutmut_8(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
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


def x_compute_growth_rate__mutmut_9(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
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


def x_compute_growth_rate__mutmut_10(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
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


def x_compute_growth_rate__mutmut_11(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
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


def x_compute_growth_rate__mutmut_12(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=1.0,
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


def x_compute_growth_rate__mutmut_13(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=True,
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


def x_compute_growth_rate__mutmut_14(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=True,
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


def x_compute_growth_rate__mutmut_15(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = None
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_16(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(None)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_17(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = None

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_18(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_19(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = None
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_20(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(None)
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_21(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = None

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_22(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = True if jump_index is not None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_23(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is None else _has_recent_spike(series, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_24(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(None, slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_25(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, None)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_26(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(slope)

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_27(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
        return GrowthRateResult(
            slope_per_day=0.0,
            window_days_used=window_days_used,
            capacity_jump_detected=False,
            spike_caveat=False,
        )

    jump_index = detect_capacity_jump(daily_values)
    series = daily_values[jump_index:] if jump_index is not None else daily_values

    slope = _least_squares_slope(series)
    spike_caveat = False if jump_index is not None else _has_recent_spike(series, )

    return GrowthRateResult(
        slope_per_day=slope,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_28(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        slope_per_day=None,
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_29(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        window_days_used=None,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_30(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        capacity_jump_detected=None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_31(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        spike_caveat=None,
    )


def x_compute_growth_rate__mutmut_32(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        window_days_used=window_days_used,
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_33(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        capacity_jump_detected=jump_index is not None,
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_34(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        spike_caveat=spike_caveat,
    )


def x_compute_growth_rate__mutmut_35(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        )


def x_compute_growth_rate__mutmut_36(daily_values: list[float]) -> GrowthRateResult:
    window_days_used = len(daily_values)
    if window_days_used < 2:  # noqa: PLR2004
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
        capacity_jump_detected=jump_index is None,
        spike_caveat=spike_caveat,
    )

mutants_x_compute_growth_rate__mutmut['_mutmut_orig'] = x_compute_growth_rate__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_1'] = x_compute_growth_rate__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_2'] = x_compute_growth_rate__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_3'] = x_compute_growth_rate__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_4'] = x_compute_growth_rate__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_5'] = x_compute_growth_rate__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_6'] = x_compute_growth_rate__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_7'] = x_compute_growth_rate__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_8'] = x_compute_growth_rate__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_9'] = x_compute_growth_rate__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_10'] = x_compute_growth_rate__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_11'] = x_compute_growth_rate__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_12'] = x_compute_growth_rate__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_13'] = x_compute_growth_rate__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_14'] = x_compute_growth_rate__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_15'] = x_compute_growth_rate__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_16'] = x_compute_growth_rate__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_17'] = x_compute_growth_rate__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_18'] = x_compute_growth_rate__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_19'] = x_compute_growth_rate__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_20'] = x_compute_growth_rate__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_21'] = x_compute_growth_rate__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_22'] = x_compute_growth_rate__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_23'] = x_compute_growth_rate__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_24'] = x_compute_growth_rate__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_25'] = x_compute_growth_rate__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_26'] = x_compute_growth_rate__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_27'] = x_compute_growth_rate__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_28'] = x_compute_growth_rate__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_29'] = x_compute_growth_rate__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_30'] = x_compute_growth_rate__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_31'] = x_compute_growth_rate__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_32'] = x_compute_growth_rate__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_33'] = x_compute_growth_rate__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_34'] = x_compute_growth_rate__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_35'] = x_compute_growth_rate__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_growth_rate__mutmut['x_compute_growth_rate__mutmut_36'] = x_compute_growth_rate__mutmut_36 # type: ignore # mutmut generated
mutants_x__is_outlier__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_outlier__mutmut)
def _is_outlier(delta: float, threshold: float, baseline: float) -> bool:
    return delta > threshold if baseline > 0 else delta > 0


def x__is_outlier__mutmut_orig(delta: float, threshold: float, baseline: float) -> bool:
    return delta > threshold if baseline > 0 else delta > 0


def x__is_outlier__mutmut_1(delta: float, threshold: float, baseline: float) -> bool:
    return delta >= threshold if baseline > 0 else delta > 0


def x__is_outlier__mutmut_2(delta: float, threshold: float, baseline: float) -> bool:
    return delta > threshold if baseline >= 0 else delta > 0


def x__is_outlier__mutmut_3(delta: float, threshold: float, baseline: float) -> bool:
    return delta > threshold if baseline > 1 else delta > 0


def x__is_outlier__mutmut_4(delta: float, threshold: float, baseline: float) -> bool:
    return delta > threshold if baseline > 0 else delta >= 0


def x__is_outlier__mutmut_5(delta: float, threshold: float, baseline: float) -> bool:
    return delta > threshold if baseline > 0 else delta > 1

mutants_x__is_outlier__mutmut['_mutmut_orig'] = x__is_outlier__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_outlier__mutmut['x__is_outlier__mutmut_1'] = x__is_outlier__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_outlier__mutmut['x__is_outlier__mutmut_2'] = x__is_outlier__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_outlier__mutmut['x__is_outlier__mutmut_3'] = x__is_outlier__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_outlier__mutmut['x__is_outlier__mutmut_4'] = x__is_outlier__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_outlier__mutmut['x__is_outlier__mutmut_5'] = x__is_outlier__mutmut_5 # type: ignore # mutmut generated
mutants_x__deltas__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__deltas__mutmut)
def _deltas(values: list[float]) -> list[float]:
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


def x__deltas__mutmut_orig(values: list[float]) -> list[float]:
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


def x__deltas__mutmut_1(values: list[float]) -> list[float]:
    return [values[i + 1] + values[i] for i in range(len(values) - 1)]


def x__deltas__mutmut_2(values: list[float]) -> list[float]:
    return [values[i - 1] - values[i] for i in range(len(values) - 1)]


def x__deltas__mutmut_3(values: list[float]) -> list[float]:
    return [values[i + 2] - values[i] for i in range(len(values) - 1)]


def x__deltas__mutmut_4(values: list[float]) -> list[float]:
    return [values[i + 1] - values[i] for i in range(None)]


def x__deltas__mutmut_5(values: list[float]) -> list[float]:
    return [values[i + 1] - values[i] for i in range(len(values) + 1)]


def x__deltas__mutmut_6(values: list[float]) -> list[float]:
    return [values[i + 1] - values[i] for i in range(len(values) - 2)]

mutants_x__deltas__mutmut['_mutmut_orig'] = x__deltas__mutmut_orig # type: ignore # mutmut generated
mutants_x__deltas__mutmut['x__deltas__mutmut_1'] = x__deltas__mutmut_1 # type: ignore # mutmut generated
mutants_x__deltas__mutmut['x__deltas__mutmut_2'] = x__deltas__mutmut_2 # type: ignore # mutmut generated
mutants_x__deltas__mutmut['x__deltas__mutmut_3'] = x__deltas__mutmut_3 # type: ignore # mutmut generated
mutants_x__deltas__mutmut['x__deltas__mutmut_4'] = x__deltas__mutmut_4 # type: ignore # mutmut generated
mutants_x__deltas__mutmut['x__deltas__mutmut_5'] = x__deltas__mutmut_5 # type: ignore # mutmut generated
mutants_x__deltas__mutmut['x__deltas__mutmut_6'] = x__deltas__mutmut_6 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__least_squares_slope__mutmut)
def _least_squares_slope(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_orig(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_1(series: list[float]) -> float:
    n = None
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_2(series: list[float]) -> float:
    n = len(series)
    if n <= 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_3(series: list[float]) -> float:
    n = len(series)
    if n < 3:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_4(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 1.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_5(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = None
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_6(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) * 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_7(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n + 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_8(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 2) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_9(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 3
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_10(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = None
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_11(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(None)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_12(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = None
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_13(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum(None)
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_14(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) / (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_15(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x + mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_16(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y + mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_17(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(None))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_18(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = None
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_19(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum(None)
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_20(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) * 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_21(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x + mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_22(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 3 for x in range(n))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_23(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(None))
    return numerator / denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_24(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator * denominator if denominator != 0 else 0.0


def x__least_squares_slope__mutmut_25(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator == 0 else 0.0


def x__least_squares_slope__mutmut_26(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 1 else 0.0


def x__least_squares_slope__mutmut_27(series: list[float]) -> float:
    n = len(series)
    if n < 2:  # noqa: PLR2004
        return 0.0

    mean_x = (n - 1) / 2
    mean_y = mean(series)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in enumerate(series))
    denominator = sum((x - mean_x) ** 2 for x in range(n))
    return numerator / denominator if denominator != 0 else 1.0

mutants_x__least_squares_slope__mutmut['_mutmut_orig'] = x__least_squares_slope__mutmut_orig # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_1'] = x__least_squares_slope__mutmut_1 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_2'] = x__least_squares_slope__mutmut_2 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_3'] = x__least_squares_slope__mutmut_3 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_4'] = x__least_squares_slope__mutmut_4 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_5'] = x__least_squares_slope__mutmut_5 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_6'] = x__least_squares_slope__mutmut_6 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_7'] = x__least_squares_slope__mutmut_7 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_8'] = x__least_squares_slope__mutmut_8 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_9'] = x__least_squares_slope__mutmut_9 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_10'] = x__least_squares_slope__mutmut_10 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_11'] = x__least_squares_slope__mutmut_11 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_12'] = x__least_squares_slope__mutmut_12 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_13'] = x__least_squares_slope__mutmut_13 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_14'] = x__least_squares_slope__mutmut_14 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_15'] = x__least_squares_slope__mutmut_15 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_16'] = x__least_squares_slope__mutmut_16 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_17'] = x__least_squares_slope__mutmut_17 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_18'] = x__least_squares_slope__mutmut_18 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_19'] = x__least_squares_slope__mutmut_19 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_20'] = x__least_squares_slope__mutmut_20 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_21'] = x__least_squares_slope__mutmut_21 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_22'] = x__least_squares_slope__mutmut_22 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_23'] = x__least_squares_slope__mutmut_23 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_24'] = x__least_squares_slope__mutmut_24 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_25'] = x__least_squares_slope__mutmut_25 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_26'] = x__least_squares_slope__mutmut_26 # type: ignore # mutmut generated
mutants_x__least_squares_slope__mutmut['x__least_squares_slope__mutmut_27'] = x__least_squares_slope__mutmut_27 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__has_recent_spike__mutmut)
def _has_recent_spike(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_orig(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_1(series: list[float], overall_slope: float) -> bool:
    if len(series) <= _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_2(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days - 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_3(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 2:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_4(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return True

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_5(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = None
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_6(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(None)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_7(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[+_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_8(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = None
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_9(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(None)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_10(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(None) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_11(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) <= 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_12(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1.000000001:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_13(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(None) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_14(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) >= 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_15(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1.000000001  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_16(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(None) > _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_17(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) >= _SPIKE_RATIO_THRESHOLD * abs(overall_slope)


def x__has_recent_spike__mutmut_18(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD / abs(overall_slope)


def x__has_recent_spike__mutmut_19(series: list[float], overall_slope: float) -> bool:
    if len(series) < _cfg.trend_window_days + 1:
        return False

    recent_deltas = _deltas(series)[-_cfg.trend_window_days :]
    recent_avg = mean(recent_deltas)
    if abs(overall_slope) < 1e-9:  # noqa: PLR2004
        return abs(recent_avg) > 1e-9  # noqa: PLR2004
    return abs(recent_avg) > _SPIKE_RATIO_THRESHOLD * abs(None)

mutants_x__has_recent_spike__mutmut['_mutmut_orig'] = x__has_recent_spike__mutmut_orig # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_1'] = x__has_recent_spike__mutmut_1 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_2'] = x__has_recent_spike__mutmut_2 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_3'] = x__has_recent_spike__mutmut_3 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_4'] = x__has_recent_spike__mutmut_4 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_5'] = x__has_recent_spike__mutmut_5 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_6'] = x__has_recent_spike__mutmut_6 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_7'] = x__has_recent_spike__mutmut_7 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_8'] = x__has_recent_spike__mutmut_8 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_9'] = x__has_recent_spike__mutmut_9 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_10'] = x__has_recent_spike__mutmut_10 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_11'] = x__has_recent_spike__mutmut_11 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_12'] = x__has_recent_spike__mutmut_12 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_13'] = x__has_recent_spike__mutmut_13 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_14'] = x__has_recent_spike__mutmut_14 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_15'] = x__has_recent_spike__mutmut_15 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_16'] = x__has_recent_spike__mutmut_16 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_17'] = x__has_recent_spike__mutmut_17 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_18'] = x__has_recent_spike__mutmut_18 # type: ignore # mutmut generated
mutants_x__has_recent_spike__mutmut['x__has_recent_spike__mutmut_19'] = x__has_recent_spike__mutmut_19 # type: ignore # mutmut generated

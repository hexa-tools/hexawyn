from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from statistics import mean

from hexawyn.domain.models.constants import HotNodeAnalysisConstants

_cfg = HotNodeAnalysisConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class HotStatus:
    is_hot: bool
    avg_percent: float
    hot_hours: int
    business_hours_pattern: bool
mutants_x_compute_hot_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_hot_status__mutmut)
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


def x_compute_hot_status__mutmut_orig(
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


def x_compute_hot_status__mutmut_1(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if series:
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


def x_compute_hot_status__mutmut_2(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=None, avg_percent=0.0, hot_hours=0, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_3(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=None, hot_hours=0, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_4(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=None, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_5(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=0, business_hours_pattern=None)

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


def x_compute_hot_status__mutmut_6(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(avg_percent=0.0, hot_hours=0, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_7(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, hot_hours=0, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_8(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_9(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=0, )

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


def x_compute_hot_status__mutmut_10(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=True, avg_percent=0.0, hot_hours=0, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_11(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=1.0, hot_hours=0, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_12(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=1, business_hours_pattern=False)

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


def x_compute_hot_status__mutmut_13(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=0, business_hours_pattern=True)

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


def x_compute_hot_status__mutmut_14(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=0, business_hours_pattern=False)

    values = None
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


def x_compute_hot_status__mutmut_15(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=0, business_hours_pattern=False)

    values = [value for _, value in series]
    hot_points = None
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


def x_compute_hot_status__mutmut_16(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=0, business_hours_pattern=False)

    values = [value for _, value in series]
    hot_points = [(timestamp, value) for timestamp, value in series if value >= threshold_pct]
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


def x_compute_hot_status__mutmut_17(
    series: list[tuple[str, float]], threshold_pct: float, duration_pct: float
) -> HotStatus:
    """A resource is "hot" when it exceeds `threshold_pct` for at least
    `duration_pct` of the observed window — computed independently per
    resource (CPU and memory are never collapsed into one flag)."""
    if not series:
        return HotStatus(is_hot=False, avg_percent=0.0, hot_hours=0, business_hours_pattern=False)

    values = [value for _, value in series]
    hot_points = [(timestamp, value) for timestamp, value in series if value > threshold_pct]
    hot_hours = None
    is_hot = (hot_hours / len(series) * 100) >= duration_pct

    return HotStatus(
        is_hot=is_hot,
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_18(
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
    is_hot = None

    return HotStatus(
        is_hot=is_hot,
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_19(
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
    is_hot = (hot_hours / len(series) / 100) >= duration_pct

    return HotStatus(
        is_hot=is_hot,
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_20(
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
    is_hot = (hot_hours * len(series) * 100) >= duration_pct

    return HotStatus(
        is_hot=is_hot,
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_21(
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
    is_hot = (hot_hours / len(series) * 101) >= duration_pct

    return HotStatus(
        is_hot=is_hot,
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_22(
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
    is_hot = (hot_hours / len(series) * 100) > duration_pct

    return HotStatus(
        is_hot=is_hot,
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_23(
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
        is_hot=None,
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_24(
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
        avg_percent=None,
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_25(
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
        hot_hours=None,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_26(
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
        business_hours_pattern=None,
    )


def x_compute_hot_status__mutmut_27(
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
        avg_percent=round(mean(values), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_28(
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
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_29(
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
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_30(
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
        )


def x_compute_hot_status__mutmut_31(
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
        avg_percent=round(None, 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_32(
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
        avg_percent=round(mean(values), None),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_33(
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
        avg_percent=round(2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_34(
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
        avg_percent=round(mean(values), ),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_35(
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
        avg_percent=round(mean(None), 2),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_36(
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
        avg_percent=round(mean(values), 3),
        hot_hours=hot_hours,
        business_hours_pattern=_is_business_hours_pattern(
            [timestamp for timestamp, _ in hot_points]
        ),
    )


def x_compute_hot_status__mutmut_37(
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
            None
        ),
    )

mutants_x_compute_hot_status__mutmut['_mutmut_orig'] = x_compute_hot_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_1'] = x_compute_hot_status__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_2'] = x_compute_hot_status__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_3'] = x_compute_hot_status__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_4'] = x_compute_hot_status__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_5'] = x_compute_hot_status__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_6'] = x_compute_hot_status__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_7'] = x_compute_hot_status__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_8'] = x_compute_hot_status__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_9'] = x_compute_hot_status__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_10'] = x_compute_hot_status__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_11'] = x_compute_hot_status__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_12'] = x_compute_hot_status__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_13'] = x_compute_hot_status__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_14'] = x_compute_hot_status__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_15'] = x_compute_hot_status__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_16'] = x_compute_hot_status__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_17'] = x_compute_hot_status__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_18'] = x_compute_hot_status__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_19'] = x_compute_hot_status__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_20'] = x_compute_hot_status__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_21'] = x_compute_hot_status__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_22'] = x_compute_hot_status__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_23'] = x_compute_hot_status__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_24'] = x_compute_hot_status__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_25'] = x_compute_hot_status__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_26'] = x_compute_hot_status__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_27'] = x_compute_hot_status__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_28'] = x_compute_hot_status__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_29'] = x_compute_hot_status__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_30'] = x_compute_hot_status__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_31'] = x_compute_hot_status__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_32'] = x_compute_hot_status__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_33'] = x_compute_hot_status__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_34'] = x_compute_hot_status__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_35'] = x_compute_hot_status__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_36'] = x_compute_hot_status__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_hot_status__mutmut['x_compute_hot_status__mutmut_37'] = x_compute_hot_status__mutmut_37 # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_business_hours_pattern__mutmut)
def _is_business_hours_pattern(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = sum(1 for timestamp in hot_timestamps if _is_business_hour(timestamp))
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_orig(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = sum(1 for timestamp in hot_timestamps if _is_business_hour(timestamp))
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_1(hot_timestamps: list[str]) -> bool:
    if hot_timestamps:
        return False
    in_business_hours = sum(1 for timestamp in hot_timestamps if _is_business_hour(timestamp))
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_2(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return True
    in_business_hours = sum(1 for timestamp in hot_timestamps if _is_business_hour(timestamp))
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_3(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = None
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_4(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = sum(None)
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_5(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = sum(2 for timestamp in hot_timestamps if _is_business_hour(timestamp))
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_6(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = sum(1 for timestamp in hot_timestamps if _is_business_hour(None))
    return (in_business_hours / len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_7(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = sum(1 for timestamp in hot_timestamps if _is_business_hour(timestamp))
    return (in_business_hours * len(hot_timestamps)) >= _cfg.business_hours_match_ratio


def x__is_business_hours_pattern__mutmut_8(hot_timestamps: list[str]) -> bool:
    if not hot_timestamps:
        return False
    in_business_hours = sum(1 for timestamp in hot_timestamps if _is_business_hour(timestamp))
    return (in_business_hours / len(hot_timestamps)) > _cfg.business_hours_match_ratio

mutants_x__is_business_hours_pattern__mutmut['_mutmut_orig'] = x__is_business_hours_pattern__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut['x__is_business_hours_pattern__mutmut_1'] = x__is_business_hours_pattern__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut['x__is_business_hours_pattern__mutmut_2'] = x__is_business_hours_pattern__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut['x__is_business_hours_pattern__mutmut_3'] = x__is_business_hours_pattern__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut['x__is_business_hours_pattern__mutmut_4'] = x__is_business_hours_pattern__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut['x__is_business_hours_pattern__mutmut_5'] = x__is_business_hours_pattern__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut['x__is_business_hours_pattern__mutmut_6'] = x__is_business_hours_pattern__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut['x__is_business_hours_pattern__mutmut_7'] = x__is_business_hours_pattern__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_business_hours_pattern__mutmut['x__is_business_hours_pattern__mutmut_8'] = x__is_business_hours_pattern__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_business_hour__mutmut)
def _is_business_hour(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_orig(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_1(timestamp: str) -> bool:
    hour = None
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_2(timestamp: str) -> bool:
    hour = datetime.fromisoformat(None).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_3(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace(None, "+00:00")).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_4(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("Z", None)).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_5(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("+00:00")).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_6(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("Z", )).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_7(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("XXZXX", "+00:00")).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_8(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("z", "+00:00")).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_9(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("Z", "XX+00:00XX")).hour
    return _cfg.business_hours_start <= hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_10(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).hour
    return _cfg.business_hours_start < hour < _cfg.business_hours_end


def x__is_business_hour__mutmut_11(timestamp: str) -> bool:
    hour = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).hour
    return _cfg.business_hours_start <= hour <= _cfg.business_hours_end

mutants_x__is_business_hour__mutmut['_mutmut_orig'] = x__is_business_hour__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_1'] = x__is_business_hour__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_2'] = x__is_business_hour__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_3'] = x__is_business_hour__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_4'] = x__is_business_hour__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_5'] = x__is_business_hour__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_6'] = x__is_business_hour__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_7'] = x__is_business_hour__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_8'] = x__is_business_hour__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_9'] = x__is_business_hour__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_10'] = x__is_business_hour__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_business_hour__mutmut['x__is_business_hour__mutmut_11'] = x__is_business_hour__mutmut_11 # type: ignore # mutmut generated

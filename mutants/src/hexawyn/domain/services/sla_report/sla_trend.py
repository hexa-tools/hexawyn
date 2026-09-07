from __future__ import annotations

_TREND_TOLERANCE_PCT = 0.1


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_trend__mutmut)
def classify_trend(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_orig(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_1(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is not None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_2(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "XXstableXX"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_3(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "STABLE"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_4(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = None
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_5(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current + previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_6(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta >= _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_7(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "XXimprovingXX"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_8(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "IMPROVING"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_9(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta <= -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_10(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < +_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"


def x_classify_trend__mutmut_11(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "XXdegradingXX"
    return "stable"


def x_classify_trend__mutmut_12(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "DEGRADING"
    return "stable"


def x_classify_trend__mutmut_13(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "XXstableXX"


def x_classify_trend__mutmut_14(current: float, previous: float | None) -> str:
    """Compare current vs previous quarter average uptime.

    A difference within +/- 0.1 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous quarter the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "STABLE"

mutants_x_classify_trend__mutmut['_mutmut_orig'] = x_classify_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_1'] = x_classify_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_2'] = x_classify_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_3'] = x_classify_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_4'] = x_classify_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_5'] = x_classify_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_6'] = x_classify_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_7'] = x_classify_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_8'] = x_classify_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_9'] = x_classify_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_10'] = x_classify_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_11'] = x_classify_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_12'] = x_classify_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_13'] = x_classify_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_trend__mutmut['x_classify_trend__mutmut_14'] = x_classify_trend__mutmut_14 # type: ignore # mutmut generated

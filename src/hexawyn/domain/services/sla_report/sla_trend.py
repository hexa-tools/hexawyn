from __future__ import annotations

_TREND_TOLERANCE_PCT = 0.1


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

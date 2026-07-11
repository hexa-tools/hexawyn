from __future__ import annotations

from hexawyn.domain.models.security_posture import PostureTrend

_TREND_TOLERANCE_PCT = 0.5


def classify_trend(current: float, previous: float | None) -> PostureTrend:
    """Compare the current overall score against the previous period.

    A difference within +/- 0.5 points is treated as stable to avoid noisy
    quarter-over-quarter flapping. With no previous score the trend is stable.
    """
    if previous is None:
        return "stable"
    delta = current - previous
    if delta > _TREND_TOLERANCE_PCT:
        return "improving"
    if delta < -_TREND_TOLERANCE_PCT:
        return "degrading"
    return "stable"

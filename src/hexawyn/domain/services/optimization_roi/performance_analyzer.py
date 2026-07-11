from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import PerformanceMetricRaw
from hexawyn.domain.models.optimization_roi import PerformanceImpact

_HIGHER_IS_BETTER_TOKENS = ("uptime", "availability", "success")


def analyze_performance(metrics: list[PerformanceMetricRaw]) -> list[PerformanceImpact]:
    """Compare before/after for each performance metric.

    For latency- and error-style metrics lower is better; for uptime/
    availability-style metrics higher is better. The direction determines
    whether a change counts as an improvement or a regression.
    """
    return [_to_impact(metric) for metric in metrics]


def has_regression(impacts: list[PerformanceImpact]) -> bool:
    """True when any analyzed metric regressed."""
    return any(impact.regressed for impact in impacts)


def _to_impact(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = False
    elif higher_is_better:
        improved = after > before
        regressed = after < before
    else:
        improved = after < before
        regressed = after > before

    return PerformanceImpact(
        metric=metric["metric"],
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def _higher_is_better(metric_name: str) -> bool:
    normalized = metric_name.lower()
    return any(token in normalized for token in _HIGHER_IS_BETTER_TOKENS)

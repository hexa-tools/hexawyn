from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import PerformanceMetricRaw
from hexawyn.domain.models.optimization_roi import PerformanceImpact

_HIGHER_IS_BETTER_TOKENS = ("uptime", "availability", "success")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analyze_performance__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_performance__mutmut)
def analyze_performance(metrics: list[PerformanceMetricRaw]) -> list[PerformanceImpact]:
    """Compare before/after for each performance metric.

    For latency- and error-style metrics lower is better; for uptime/
    availability-style metrics higher is better. The direction determines
    whether a change counts as an improvement or a regression.
    """
    return [_to_impact(metric) for metric in metrics]


def x_analyze_performance__mutmut_orig(metrics: list[PerformanceMetricRaw]) -> list[PerformanceImpact]:
    """Compare before/after for each performance metric.

    For latency- and error-style metrics lower is better; for uptime/
    availability-style metrics higher is better. The direction determines
    whether a change counts as an improvement or a regression.
    """
    return [_to_impact(metric) for metric in metrics]


def x_analyze_performance__mutmut_1(metrics: list[PerformanceMetricRaw]) -> list[PerformanceImpact]:
    """Compare before/after for each performance metric.

    For latency- and error-style metrics lower is better; for uptime/
    availability-style metrics higher is better. The direction determines
    whether a change counts as an improvement or a regression.
    """
    return [_to_impact(None) for metric in metrics]

mutants_x_analyze_performance__mutmut['_mutmut_orig'] = x_analyze_performance__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_performance__mutmut['x_analyze_performance__mutmut_1'] = x_analyze_performance__mutmut_1 # type: ignore # mutmut generated
mutants_x_has_regression__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_has_regression__mutmut)
def has_regression(impacts: list[PerformanceImpact]) -> bool:
    """True when any analyzed metric regressed."""
    return any(impact.regressed for impact in impacts)


def x_has_regression__mutmut_orig(impacts: list[PerformanceImpact]) -> bool:
    """True when any analyzed metric regressed."""
    return any(impact.regressed for impact in impacts)


def x_has_regression__mutmut_1(impacts: list[PerformanceImpact]) -> bool:
    """True when any analyzed metric regressed."""
    return any(None)

mutants_x_has_regression__mutmut['_mutmut_orig'] = x_has_regression__mutmut_orig # type: ignore # mutmut generated
mutants_x_has_regression__mutmut['x_has_regression__mutmut_1'] = x_has_regression__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_impact__mutmut)
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


def x__to_impact__mutmut_orig(metric: PerformanceMetricRaw) -> PerformanceImpact:
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


def x__to_impact__mutmut_1(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = None
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


def x__to_impact__mutmut_2(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["XXbeforeXX"]
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


def x__to_impact__mutmut_3(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["BEFORE"]
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


def x__to_impact__mutmut_4(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = None
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


def x__to_impact__mutmut_5(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["XXafterXX"]
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


def x__to_impact__mutmut_6(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["AFTER"]
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


def x__to_impact__mutmut_7(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = None

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


def x__to_impact__mutmut_8(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(None)

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


def x__to_impact__mutmut_9(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["XXmetricXX"])

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


def x__to_impact__mutmut_10(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["METRIC"])

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


def x__to_impact__mutmut_11(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after != before:
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


def x__to_impact__mutmut_12(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = None
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


def x__to_impact__mutmut_13(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = True
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


def x__to_impact__mutmut_14(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = False
    elif higher_is_better:
        improved = None
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


def x__to_impact__mutmut_15(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = False
    elif higher_is_better:
        improved = after >= before
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


def x__to_impact__mutmut_16(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = False
    elif higher_is_better:
        improved = after > before
        regressed = None
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


def x__to_impact__mutmut_17(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = False
    elif higher_is_better:
        improved = after > before
        regressed = after <= before
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


def x__to_impact__mutmut_18(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = False
    elif higher_is_better:
        improved = after > before
        regressed = after < before
    else:
        improved = None
        regressed = after > before

    return PerformanceImpact(
        metric=metric["metric"],
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_19(metric: PerformanceMetricRaw) -> PerformanceImpact:
    before = metric["before"]
    after = metric["after"]
    higher_is_better = _higher_is_better(metric["metric"])

    if after == before:
        improved = regressed = False
    elif higher_is_better:
        improved = after > before
        regressed = after < before
    else:
        improved = after <= before
        regressed = after > before

    return PerformanceImpact(
        metric=metric["metric"],
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_20(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        regressed = None

    return PerformanceImpact(
        metric=metric["metric"],
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_21(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        regressed = after >= before

    return PerformanceImpact(
        metric=metric["metric"],
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_22(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        metric=None,
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_23(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        before=None,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_24(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        after=None,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_25(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        improved=None,
        regressed=regressed,
    )


def x__to_impact__mutmut_26(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        regressed=None,
    )


def x__to_impact__mutmut_27(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_28(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_29(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_30(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        regressed=regressed,
    )


def x__to_impact__mutmut_31(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        )


def x__to_impact__mutmut_32(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        metric=metric["XXmetricXX"],
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )


def x__to_impact__mutmut_33(metric: PerformanceMetricRaw) -> PerformanceImpact:
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
        metric=metric["METRIC"],
        before=before,
        after=after,
        improved=improved,
        regressed=regressed,
    )

mutants_x__to_impact__mutmut['_mutmut_orig'] = x__to_impact__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_1'] = x__to_impact__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_2'] = x__to_impact__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_3'] = x__to_impact__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_4'] = x__to_impact__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_5'] = x__to_impact__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_6'] = x__to_impact__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_7'] = x__to_impact__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_8'] = x__to_impact__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_9'] = x__to_impact__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_10'] = x__to_impact__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_11'] = x__to_impact__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_12'] = x__to_impact__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_13'] = x__to_impact__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_14'] = x__to_impact__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_15'] = x__to_impact__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_16'] = x__to_impact__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_17'] = x__to_impact__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_18'] = x__to_impact__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_19'] = x__to_impact__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_20'] = x__to_impact__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_21'] = x__to_impact__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_22'] = x__to_impact__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_23'] = x__to_impact__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_24'] = x__to_impact__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_25'] = x__to_impact__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_26'] = x__to_impact__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_27'] = x__to_impact__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_28'] = x__to_impact__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_29'] = x__to_impact__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_30'] = x__to_impact__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_31'] = x__to_impact__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_32'] = x__to_impact__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_impact__mutmut['x__to_impact__mutmut_33'] = x__to_impact__mutmut_33 # type: ignore # mutmut generated
mutants_x__higher_is_better__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__higher_is_better__mutmut)
def _higher_is_better(metric_name: str) -> bool:
    normalized = metric_name.lower()
    return any(token in normalized for token in _HIGHER_IS_BETTER_TOKENS)


def x__higher_is_better__mutmut_orig(metric_name: str) -> bool:
    normalized = metric_name.lower()
    return any(token in normalized for token in _HIGHER_IS_BETTER_TOKENS)


def x__higher_is_better__mutmut_1(metric_name: str) -> bool:
    normalized = None
    return any(token in normalized for token in _HIGHER_IS_BETTER_TOKENS)


def x__higher_is_better__mutmut_2(metric_name: str) -> bool:
    normalized = metric_name.upper()
    return any(token in normalized for token in _HIGHER_IS_BETTER_TOKENS)


def x__higher_is_better__mutmut_3(metric_name: str) -> bool:
    normalized = metric_name.lower()
    return any(None)


def x__higher_is_better__mutmut_4(metric_name: str) -> bool:
    normalized = metric_name.lower()
    return any(token not in normalized for token in _HIGHER_IS_BETTER_TOKENS)

mutants_x__higher_is_better__mutmut['_mutmut_orig'] = x__higher_is_better__mutmut_orig # type: ignore # mutmut generated
mutants_x__higher_is_better__mutmut['x__higher_is_better__mutmut_1'] = x__higher_is_better__mutmut_1 # type: ignore # mutmut generated
mutants_x__higher_is_better__mutmut['x__higher_is_better__mutmut_2'] = x__higher_is_better__mutmut_2 # type: ignore # mutmut generated
mutants_x__higher_is_better__mutmut['x__higher_is_better__mutmut_3'] = x__higher_is_better__mutmut_3 # type: ignore # mutmut generated
mutants_x__higher_is_better__mutmut['x__higher_is_better__mutmut_4'] = x__higher_is_better__mutmut_4 # type: ignore # mutmut generated

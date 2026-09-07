from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.budget_projection_port import MonthlyCostRaw

_FLAT_TOLERANCE_PCT = 0.5
_EXPONENTIAL_ACCELERATION_PCT = 2.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class GrowthEstimate:
    current_monthly_usd: float
    monthly_rate_pct: float
    model: str
mutants_x_estimate_growth__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_estimate_growth__mutmut)
def estimate_growth(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_orig(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_1(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) <= 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_2(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 3:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_3(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = None
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_4(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[+1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_5(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-2]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_6(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["XXtotal_usdXX"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_7(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["TOTAL_USD"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_8(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 1.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_9(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=None, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_10(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=None, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_11(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model=None)

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_12(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_13(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_14(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, )

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_15(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=1.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_16(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="XXflatXX")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_17(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="FLAT")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_18(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = None
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_19(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(None)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_20(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_21(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = None
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_22(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[+1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_23(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-2]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_24(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["XXtotal_usdXX"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_25(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["TOTAL_USD"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_26(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=None, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_27(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=None, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_28(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model=None)
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_29(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_30(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_31(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, )
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_32(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=1.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_33(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="XXflatXX")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_34(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="FLAT")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_35(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = None
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_36(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(None, 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_37(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), None)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_38(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_39(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), )
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_40(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) * len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_41(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(None) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_42(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 3)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_43(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = None
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_44(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[+1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_45(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-2]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_46(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["XXtotal_usdXX"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_47(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["TOTAL_USD"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_48(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = None
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_49(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(None, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_50(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, None)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_51(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_52(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, )
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_53(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=None, monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_54(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=None, model=model)


def x_estimate_growth__mutmut_55(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=None)


def x_estimate_growth__mutmut_56(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(monthly_rate_pct=mean_rate, model=model)


def x_estimate_growth__mutmut_57(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, model=model)


def x_estimate_growth__mutmut_58(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, )

mutants_x_estimate_growth__mutmut['_mutmut_orig'] = x_estimate_growth__mutmut_orig # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_1'] = x_estimate_growth__mutmut_1 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_2'] = x_estimate_growth__mutmut_2 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_3'] = x_estimate_growth__mutmut_3 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_4'] = x_estimate_growth__mutmut_4 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_5'] = x_estimate_growth__mutmut_5 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_6'] = x_estimate_growth__mutmut_6 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_7'] = x_estimate_growth__mutmut_7 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_8'] = x_estimate_growth__mutmut_8 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_9'] = x_estimate_growth__mutmut_9 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_10'] = x_estimate_growth__mutmut_10 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_11'] = x_estimate_growth__mutmut_11 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_12'] = x_estimate_growth__mutmut_12 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_13'] = x_estimate_growth__mutmut_13 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_14'] = x_estimate_growth__mutmut_14 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_15'] = x_estimate_growth__mutmut_15 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_16'] = x_estimate_growth__mutmut_16 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_17'] = x_estimate_growth__mutmut_17 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_18'] = x_estimate_growth__mutmut_18 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_19'] = x_estimate_growth__mutmut_19 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_20'] = x_estimate_growth__mutmut_20 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_21'] = x_estimate_growth__mutmut_21 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_22'] = x_estimate_growth__mutmut_22 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_23'] = x_estimate_growth__mutmut_23 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_24'] = x_estimate_growth__mutmut_24 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_25'] = x_estimate_growth__mutmut_25 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_26'] = x_estimate_growth__mutmut_26 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_27'] = x_estimate_growth__mutmut_27 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_28'] = x_estimate_growth__mutmut_28 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_29'] = x_estimate_growth__mutmut_29 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_30'] = x_estimate_growth__mutmut_30 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_31'] = x_estimate_growth__mutmut_31 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_32'] = x_estimate_growth__mutmut_32 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_33'] = x_estimate_growth__mutmut_33 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_34'] = x_estimate_growth__mutmut_34 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_35'] = x_estimate_growth__mutmut_35 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_36'] = x_estimate_growth__mutmut_36 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_37'] = x_estimate_growth__mutmut_37 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_38'] = x_estimate_growth__mutmut_38 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_39'] = x_estimate_growth__mutmut_39 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_40'] = x_estimate_growth__mutmut_40 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_41'] = x_estimate_growth__mutmut_41 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_42'] = x_estimate_growth__mutmut_42 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_43'] = x_estimate_growth__mutmut_43 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_44'] = x_estimate_growth__mutmut_44 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_45'] = x_estimate_growth__mutmut_45 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_46'] = x_estimate_growth__mutmut_46 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_47'] = x_estimate_growth__mutmut_47 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_48'] = x_estimate_growth__mutmut_48 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_49'] = x_estimate_growth__mutmut_49 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_50'] = x_estimate_growth__mutmut_50 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_51'] = x_estimate_growth__mutmut_51 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_52'] = x_estimate_growth__mutmut_52 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_53'] = x_estimate_growth__mutmut_53 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_54'] = x_estimate_growth__mutmut_54 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_55'] = x_estimate_growth__mutmut_55 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_56'] = x_estimate_growth__mutmut_56 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_57'] = x_estimate_growth__mutmut_57 # type: ignore # mutmut generated
mutants_x_estimate_growth__mutmut['x_estimate_growth__mutmut_58'] = x_estimate_growth__mutmut_58 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__month_over_month_changes__mutmut)
def _month_over_month_changes(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_orig(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_1(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = None
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_2(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(None, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_3(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, None, strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_4(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=None):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_5(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_6(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_7(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], ):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_8(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[2:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_9(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=True):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_10(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = None
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_11(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["XXtotal_usdXX"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_12(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["TOTAL_USD"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_13(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total != 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_14(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 1:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_15(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            break
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_16(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append(None)
    return changes


def x__month_over_month_changes__mutmut_17(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total / 100)
    return changes


def x__month_over_month_changes__mutmut_18(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) * previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_19(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] + previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_20(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["XXtotal_usdXX"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_21(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["TOTAL_USD"] - previous_total) / previous_total * 100)
    return changes


def x__month_over_month_changes__mutmut_22(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 101)
    return changes

mutants_x__month_over_month_changes__mutmut['_mutmut_orig'] = x__month_over_month_changes__mutmut_orig # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_1'] = x__month_over_month_changes__mutmut_1 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_2'] = x__month_over_month_changes__mutmut_2 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_3'] = x__month_over_month_changes__mutmut_3 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_4'] = x__month_over_month_changes__mutmut_4 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_5'] = x__month_over_month_changes__mutmut_5 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_6'] = x__month_over_month_changes__mutmut_6 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_7'] = x__month_over_month_changes__mutmut_7 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_8'] = x__month_over_month_changes__mutmut_8 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_9'] = x__month_over_month_changes__mutmut_9 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_10'] = x__month_over_month_changes__mutmut_10 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_11'] = x__month_over_month_changes__mutmut_11 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_12'] = x__month_over_month_changes__mutmut_12 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_13'] = x__month_over_month_changes__mutmut_13 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_14'] = x__month_over_month_changes__mutmut_14 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_15'] = x__month_over_month_changes__mutmut_15 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_16'] = x__month_over_month_changes__mutmut_16 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_17'] = x__month_over_month_changes__mutmut_17 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_18'] = x__month_over_month_changes__mutmut_18 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_19'] = x__month_over_month_changes__mutmut_19 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_20'] = x__month_over_month_changes__mutmut_20 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_21'] = x__month_over_month_changes__mutmut_21 # type: ignore # mutmut generated
mutants_x__month_over_month_changes__mutmut['x__month_over_month_changes__mutmut_22'] = x__month_over_month_changes__mutmut_22 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify_model__mutmut)
def _classify_model(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_orig(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_1(mean_rate: float, changes: list[float]) -> str:
    if abs(None) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_2(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) < _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_3(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "XXflatXX"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_4(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "FLAT"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_5(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate <= 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_6(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 1:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_7(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "XXdecreasingXX"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_8(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "DECREASING"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_9(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(None):
        return "exponential"
    return "linear"


def x__classify_model__mutmut_10(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "XXexponentialXX"
    return "linear"


def x__classify_model__mutmut_11(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "EXPONENTIAL"
    return "linear"


def x__classify_model__mutmut_12(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "XXlinearXX"


def x__classify_model__mutmut_13(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "LINEAR"

mutants_x__classify_model__mutmut['_mutmut_orig'] = x__classify_model__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_1'] = x__classify_model__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_2'] = x__classify_model__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_3'] = x__classify_model__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_4'] = x__classify_model__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_5'] = x__classify_model__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_6'] = x__classify_model__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_7'] = x__classify_model__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_8'] = x__classify_model__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_9'] = x__classify_model__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_10'] = x__classify_model__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_11'] = x__classify_model__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_12'] = x__classify_model__mutmut_12 # type: ignore # mutmut generated
mutants_x__classify_model__mutmut['x__classify_model__mutmut_13'] = x__classify_model__mutmut_13 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_accelerating__mutmut)
def _is_accelerating(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_orig(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_1(changes: list[float]) -> bool:
    if len(changes) <= 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_2(changes: list[float]) -> bool:
    if len(changes) < 3:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_3(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return True
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_4(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        None
    )


def x__is_accelerating__mutmut_5(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later + earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_6(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier >= _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_7(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(None, changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_8(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, None, strict=False)
    )


def x__is_accelerating__mutmut_9(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=None)
    )


def x__is_accelerating__mutmut_10(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes[1:], strict=False)
    )


def x__is_accelerating__mutmut_11(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, strict=False)
    )


def x__is_accelerating__mutmut_12(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], )
    )


def x__is_accelerating__mutmut_13(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[2:], strict=False)
    )


def x__is_accelerating__mutmut_14(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=True)
    )

mutants_x__is_accelerating__mutmut['_mutmut_orig'] = x__is_accelerating__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_1'] = x__is_accelerating__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_2'] = x__is_accelerating__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_3'] = x__is_accelerating__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_4'] = x__is_accelerating__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_5'] = x__is_accelerating__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_6'] = x__is_accelerating__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_7'] = x__is_accelerating__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_8'] = x__is_accelerating__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_9'] = x__is_accelerating__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_10'] = x__is_accelerating__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_11'] = x__is_accelerating__mutmut_11 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_12'] = x__is_accelerating__mutmut_12 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_13'] = x__is_accelerating__mutmut_13 # type: ignore # mutmut generated
mutants_x__is_accelerating__mutmut['x__is_accelerating__mutmut_14'] = x__is_accelerating__mutmut_14 # type: ignore # mutmut generated

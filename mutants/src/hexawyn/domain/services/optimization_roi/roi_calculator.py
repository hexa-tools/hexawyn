from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRaw
from hexawyn.domain.models.optimization_roi import OptimizationItem

_MONTHS_PER_YEAR = 12


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class SavingsResult:
    monthly_saving_eur: float
    annual_saving_eur: float
    savings_pct: float
    normalized_current_eur: float
    traffic_normalized: bool
mutants_x_compute_savings__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_savings__mutmut)
def compute_savings(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_orig(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_1(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = None
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_2(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(None, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_3(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, None)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_4(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_5(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, )
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_6(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = None
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_7(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(None, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_8(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, None)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_9(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_10(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, )
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_11(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline + normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_12(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 3)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_13(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=None,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_14(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=None,
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_15(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=None,
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_16(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=None,
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_17(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=None,
    )


def x_compute_savings__mutmut_18(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_19(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_20(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_21(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_22(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        )


def x_compute_savings__mutmut_23(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(None, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_24(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, None),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_25(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_26(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, ),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_27(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving / _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_28(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 3),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_29(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(None, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_30(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, None),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_31(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_32(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, ),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_33(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(None, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_34(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, None),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_35(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_36(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, ),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_37(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 3),
        traffic_normalized=traffic_growth_pct > 0,
    )


def x_compute_savings__mutmut_38(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct >= 0,
    )


def x_compute_savings__mutmut_39(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 1,
    )

mutants_x_compute_savings__mutmut['_mutmut_orig'] = x_compute_savings__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_1'] = x_compute_savings__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_2'] = x_compute_savings__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_3'] = x_compute_savings__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_4'] = x_compute_savings__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_5'] = x_compute_savings__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_6'] = x_compute_savings__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_7'] = x_compute_savings__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_8'] = x_compute_savings__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_9'] = x_compute_savings__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_10'] = x_compute_savings__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_11'] = x_compute_savings__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_12'] = x_compute_savings__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_13'] = x_compute_savings__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_14'] = x_compute_savings__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_15'] = x_compute_savings__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_16'] = x_compute_savings__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_17'] = x_compute_savings__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_18'] = x_compute_savings__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_19'] = x_compute_savings__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_20'] = x_compute_savings__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_21'] = x_compute_savings__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_22'] = x_compute_savings__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_23'] = x_compute_savings__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_24'] = x_compute_savings__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_25'] = x_compute_savings__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_26'] = x_compute_savings__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_27'] = x_compute_savings__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_28'] = x_compute_savings__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_29'] = x_compute_savings__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_30'] = x_compute_savings__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_31'] = x_compute_savings__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_32'] = x_compute_savings__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_33'] = x_compute_savings__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_34'] = x_compute_savings__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_35'] = x_compute_savings__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_36'] = x_compute_savings__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_37'] = x_compute_savings__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_38'] = x_compute_savings__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_savings__mutmut['x_compute_savings__mutmut_39'] = x_compute_savings__mutmut_39 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_rank_optimizations__mutmut)
def rank_optimizations(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_orig(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_1(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = None
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_2(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=None,
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_3(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=None,
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_4(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=None,
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_5(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=None,
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_6(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_7(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_8(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_9(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_10(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["XXnameXX"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_11(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["NAME"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_12(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["XXcategoryXX"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_13(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["CATEGORY"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_14(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["XXmonthly_saving_eurXX"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_15(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["MONTHLY_SAVING_EUR"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_16(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get(None, ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_17(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", None),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_18(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get(""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_19(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_20(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("XXdescriptionXX", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_21(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("DESCRIPTION", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_22(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", "XXXX"),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_23(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(None, key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_24(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=None, reverse=True)


def x_rank_optimizations__mutmut_25(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=None)


def x_rank_optimizations__mutmut_26(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(key=lambda item: item.monthly_saving_eur, reverse=True)


def x_rank_optimizations__mutmut_27(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, reverse=True)


def x_rank_optimizations__mutmut_28(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, )


def x_rank_optimizations__mutmut_29(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: None, reverse=True)


def x_rank_optimizations__mutmut_30(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=False)

mutants_x_rank_optimizations__mutmut['_mutmut_orig'] = x_rank_optimizations__mutmut_orig # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_1'] = x_rank_optimizations__mutmut_1 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_2'] = x_rank_optimizations__mutmut_2 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_3'] = x_rank_optimizations__mutmut_3 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_4'] = x_rank_optimizations__mutmut_4 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_5'] = x_rank_optimizations__mutmut_5 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_6'] = x_rank_optimizations__mutmut_6 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_7'] = x_rank_optimizations__mutmut_7 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_8'] = x_rank_optimizations__mutmut_8 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_9'] = x_rank_optimizations__mutmut_9 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_10'] = x_rank_optimizations__mutmut_10 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_11'] = x_rank_optimizations__mutmut_11 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_12'] = x_rank_optimizations__mutmut_12 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_13'] = x_rank_optimizations__mutmut_13 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_14'] = x_rank_optimizations__mutmut_14 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_15'] = x_rank_optimizations__mutmut_15 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_16'] = x_rank_optimizations__mutmut_16 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_17'] = x_rank_optimizations__mutmut_17 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_18'] = x_rank_optimizations__mutmut_18 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_19'] = x_rank_optimizations__mutmut_19 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_20'] = x_rank_optimizations__mutmut_20 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_21'] = x_rank_optimizations__mutmut_21 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_22'] = x_rank_optimizations__mutmut_22 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_23'] = x_rank_optimizations__mutmut_23 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_24'] = x_rank_optimizations__mutmut_24 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_25'] = x_rank_optimizations__mutmut_25 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_26'] = x_rank_optimizations__mutmut_26 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_27'] = x_rank_optimizations__mutmut_27 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_28'] = x_rank_optimizations__mutmut_28 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_29'] = x_rank_optimizations__mutmut_29 # type: ignore # mutmut generated
mutants_x_rank_optimizations__mutmut['x_rank_optimizations__mutmut_30'] = x_rank_optimizations__mutmut_30 # type: ignore # mutmut generated
mutants_x__normalize__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__normalize__mutmut)
def _normalize(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 0:
        return current
    return current / (1 + traffic_growth_pct / 100)


def x__normalize__mutmut_orig(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 0:
        return current
    return current / (1 + traffic_growth_pct / 100)


def x__normalize__mutmut_1(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct < 0:
        return current
    return current / (1 + traffic_growth_pct / 100)


def x__normalize__mutmut_2(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 1:
        return current
    return current / (1 + traffic_growth_pct / 100)


def x__normalize__mutmut_3(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 0:
        return current
    return current * (1 + traffic_growth_pct / 100)


def x__normalize__mutmut_4(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 0:
        return current
    return current / (1 - traffic_growth_pct / 100)


def x__normalize__mutmut_5(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 0:
        return current
    return current / (2 + traffic_growth_pct / 100)


def x__normalize__mutmut_6(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 0:
        return current
    return current / (1 + traffic_growth_pct * 100)


def x__normalize__mutmut_7(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 0:
        return current
    return current / (1 + traffic_growth_pct / 101)

mutants_x__normalize__mutmut['_mutmut_orig'] = x__normalize__mutmut_orig # type: ignore # mutmut generated
mutants_x__normalize__mutmut['x__normalize__mutmut_1'] = x__normalize__mutmut_1 # type: ignore # mutmut generated
mutants_x__normalize__mutmut['x__normalize__mutmut_2'] = x__normalize__mutmut_2 # type: ignore # mutmut generated
mutants_x__normalize__mutmut['x__normalize__mutmut_3'] = x__normalize__mutmut_3 # type: ignore # mutmut generated
mutants_x__normalize__mutmut['x__normalize__mutmut_4'] = x__normalize__mutmut_4 # type: ignore # mutmut generated
mutants_x__normalize__mutmut['x__normalize__mutmut_5'] = x__normalize__mutmut_5 # type: ignore # mutmut generated
mutants_x__normalize__mutmut['x__normalize__mutmut_6'] = x__normalize__mutmut_6 # type: ignore # mutmut generated
mutants_x__normalize__mutmut['x__normalize__mutmut_7'] = x__normalize__mutmut_7 # type: ignore # mutmut generated
mutants_x__pct__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pct__mutmut)
def _pct(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving / baseline * 100, 1)


def x__pct__mutmut_orig(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving / baseline * 100, 1)


def x__pct__mutmut_1(monthly_saving: float, baseline: float) -> float:
    if baseline < 0:
        return 0.0
    return round(monthly_saving / baseline * 100, 1)


def x__pct__mutmut_2(monthly_saving: float, baseline: float) -> float:
    if baseline <= 1:
        return 0.0
    return round(monthly_saving / baseline * 100, 1)


def x__pct__mutmut_3(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 1.0
    return round(monthly_saving / baseline * 100, 1)


def x__pct__mutmut_4(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(None, 1)


def x__pct__mutmut_5(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving / baseline * 100, None)


def x__pct__mutmut_6(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(1)


def x__pct__mutmut_7(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving / baseline * 100, )


def x__pct__mutmut_8(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving / baseline / 100, 1)


def x__pct__mutmut_9(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving * baseline * 100, 1)


def x__pct__mutmut_10(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving / baseline * 101, 1)


def x__pct__mutmut_11(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving / baseline * 100, 2)

mutants_x__pct__mutmut['_mutmut_orig'] = x__pct__mutmut_orig # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_1'] = x__pct__mutmut_1 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_2'] = x__pct__mutmut_2 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_3'] = x__pct__mutmut_3 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_4'] = x__pct__mutmut_4 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_5'] = x__pct__mutmut_5 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_6'] = x__pct__mutmut_6 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_7'] = x__pct__mutmut_7 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_8'] = x__pct__mutmut_8 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_9'] = x__pct__mutmut_9 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_10'] = x__pct__mutmut_10 # type: ignore # mutmut generated
mutants_x__pct__mutmut['x__pct__mutmut_11'] = x__pct__mutmut_11 # type: ignore # mutmut generated

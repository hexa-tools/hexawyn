from __future__ import annotations

import math

from hexawyn.application.ports.driven.engineer_workload_port import MonthNightData
from hexawyn.domain.models.engineer_workload import NightInterventionReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_night_intervention_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_night_intervention_report__mutmut)
def compute_night_intervention_report(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_orig(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_1(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = None
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_2(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(None)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_3(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_4(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(None) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_5(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = None
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_6(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(None, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_7(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, None)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_8(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_9(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, )
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_10(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = None

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_11(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(None, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_12(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, None, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_13(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, None, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_14(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, None)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_15(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_16(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_17(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_18(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, )

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_19(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=None,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_20(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=None,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_21(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=None,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_22(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=None,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_23(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=None,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_24(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=None,
    )


def x_compute_night_intervention_report__mutmut_25(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_26(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_27(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        delta_pct=delta,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_28(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        trend=trend,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_29(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        summary=summary,
    )


def x_compute_night_intervention_report__mutmut_30(
    current_months: list[MonthNightData],
    previous_months: list[MonthNightData],
    period: str,
) -> NightInterventionReport:
    """Compute the average night-intervention load and its trend.

    The delta uses the exact formula the semantic layer verifies:
    ``(current_avg - previous_avg) / previous_avg × 100``.
    """
    current_avg = _average(current_months)
    previous_avg = _average(previous_months) if previous_months else None
    delta, trend = _compute_trend(current_avg, previous_avg)
    summary = _build_summary(current_avg, previous_avg, delta, trend)

    return NightInterventionReport(
        period_label=period,
        avg_interventions_per_night=current_avg,
        previous_avg_per_night=previous_avg,
        delta_pct=delta,
        trend=trend,
        )

mutants_x_compute_night_intervention_report__mutmut['_mutmut_orig'] = x_compute_night_intervention_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_1'] = x_compute_night_intervention_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_2'] = x_compute_night_intervention_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_3'] = x_compute_night_intervention_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_4'] = x_compute_night_intervention_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_5'] = x_compute_night_intervention_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_6'] = x_compute_night_intervention_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_7'] = x_compute_night_intervention_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_8'] = x_compute_night_intervention_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_9'] = x_compute_night_intervention_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_10'] = x_compute_night_intervention_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_11'] = x_compute_night_intervention_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_12'] = x_compute_night_intervention_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_13'] = x_compute_night_intervention_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_14'] = x_compute_night_intervention_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_15'] = x_compute_night_intervention_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_16'] = x_compute_night_intervention_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_17'] = x_compute_night_intervention_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_18'] = x_compute_night_intervention_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_19'] = x_compute_night_intervention_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_20'] = x_compute_night_intervention_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_21'] = x_compute_night_intervention_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_22'] = x_compute_night_intervention_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_23'] = x_compute_night_intervention_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_24'] = x_compute_night_intervention_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_25'] = x_compute_night_intervention_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_26'] = x_compute_night_intervention_report__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_27'] = x_compute_night_intervention_report__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_28'] = x_compute_night_intervention_report__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_29'] = x_compute_night_intervention_report__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_night_intervention_report__mutmut['x_compute_night_intervention_report__mutmut_30'] = x_compute_night_intervention_report__mutmut_30 # type: ignore # mutmut generated
mutants_x__average__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__average__mutmut)
def _average(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_orig(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_1(months: list[MonthNightData]) -> float:
    total_interventions = None
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_2(months: list[MonthNightData]) -> float:
    total_interventions = sum(None)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_3(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["XXnight_intervention_countXX"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_4(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["NIGHT_INTERVENTION_COUNT"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_5(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = None
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_6(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(None)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_7(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["XXtotal_nightsXX"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_8(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["TOTAL_NIGHTS"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_9(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights != 0:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_10(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 1:
        return 0.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_11(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 1.0
    return round(total_interventions / total_nights, 1)


def x__average__mutmut_12(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(None, 1)


def x__average__mutmut_13(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, None)


def x__average__mutmut_14(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(1)


def x__average__mutmut_15(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, )


def x__average__mutmut_16(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions * total_nights, 1)


def x__average__mutmut_17(months: list[MonthNightData]) -> float:
    total_interventions = sum(month["night_intervention_count"] for month in months)
    total_nights = sum(month["total_nights"] for month in months)
    if total_nights == 0:
        return 0.0
    return round(total_interventions / total_nights, 2)

mutants_x__average__mutmut['_mutmut_orig'] = x__average__mutmut_orig # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_1'] = x__average__mutmut_1 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_2'] = x__average__mutmut_2 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_3'] = x__average__mutmut_3 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_4'] = x__average__mutmut_4 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_5'] = x__average__mutmut_5 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_6'] = x__average__mutmut_6 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_7'] = x__average__mutmut_7 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_8'] = x__average__mutmut_8 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_9'] = x__average__mutmut_9 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_10'] = x__average__mutmut_10 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_11'] = x__average__mutmut_11 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_12'] = x__average__mutmut_12 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_13'] = x__average__mutmut_13 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_14'] = x__average__mutmut_14 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_15'] = x__average__mutmut_15 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_16'] = x__average__mutmut_16 # type: ignore # mutmut generated
mutants_x__average__mutmut['x__average__mutmut_17'] = x__average__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_trend__mutmut)
def _compute_trend(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_orig(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_1(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None and previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_2(current: float, previous: float | None) -> tuple[float, str]:
    if previous is not None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_3(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous != 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_4(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 1.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_5(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 1.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_6(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "XXstableXX"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_7(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "STABLE"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_8(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = None
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_9(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round(None, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_10(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, None)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_11(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round(1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_12(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, )
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_13(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous / 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_14(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) * previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_15(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current + previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_16(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 101, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_17(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 2)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_18(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta <= -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_19(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < +5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_20(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -6.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_21(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "XXimprovingXX"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_22(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "IMPROVING"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_23(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta >= 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_24(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 6.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "stable"


def x__compute_trend__mutmut_25(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "XXdegradingXX"
    return delta, "stable"


def x__compute_trend__mutmut_26(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "DEGRADING"
    return delta, "stable"


def x__compute_trend__mutmut_27(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "XXstableXX"


def x__compute_trend__mutmut_28(current: float, previous: float | None) -> tuple[float, str]:
    if previous is None or previous == 0.0:
        return 0.0, "stable"
    delta = round((current - previous) / previous * 100, 1)
    if delta < -5.0:  # noqa: PLR2004
        return delta, "improving"
    if delta > 5.0:  # noqa: PLR2004
        return delta, "degrading"
    return delta, "STABLE"

mutants_x__compute_trend__mutmut['_mutmut_orig'] = x__compute_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_1'] = x__compute_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_2'] = x__compute_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_3'] = x__compute_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_4'] = x__compute_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_5'] = x__compute_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_6'] = x__compute_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_7'] = x__compute_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_8'] = x__compute_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_9'] = x__compute_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_10'] = x__compute_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_11'] = x__compute_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_12'] = x__compute_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_13'] = x__compute_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_14'] = x__compute_trend__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_15'] = x__compute_trend__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_16'] = x__compute_trend__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_17'] = x__compute_trend__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_18'] = x__compute_trend__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_19'] = x__compute_trend__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_20'] = x__compute_trend__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_21'] = x__compute_trend__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_22'] = x__compute_trend__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_23'] = x__compute_trend__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_24'] = x__compute_trend__mutmut_24 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_25'] = x__compute_trend__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_26'] = x__compute_trend__mutmut_26 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_27'] = x__compute_trend__mutmut_27 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_28'] = x__compute_trend__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_orig(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_1(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = None
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_2(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(None, ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_3(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", None)
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_4(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_5(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", )
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_6(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(None).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_7(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace("XX.XX", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_8(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", "XX,XX")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_9(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is not None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_10(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = None
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_11(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "XXbaisseXX" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_12(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "BAISSE" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_13(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta <= 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_14(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 1 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_15(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "XXhausseXX"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_16(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "HAUSSE"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_17(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = None
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_18(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(None)
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_19(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(None))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_20(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(None)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_21(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace(None, ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_22(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', None)} le trimestre dernier)."
    )


def x__build_summary__mutmut_23(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace(',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_24(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', )} le trimestre dernier)."
    )


def x__build_summary__mutmut_25(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(None).replace('.', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_26(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('XX.XX', ',')} le trimestre dernier)."
    )


def x__build_summary__mutmut_27(current: float, previous: float | None, delta: float, trend: str) -> str:
    current_text = str(current).replace(".", ",")
    if previous is None:
        return f"Moyenne : {current_text} intervention/nuit ce mois."
    direction = "baisse" if delta < 0 else "hausse"
    delta_abs = int(abs(math.floor(delta)))
    return (
        f"Les interventions nocturnes ont {direction} de {delta_abs}% ce trimestre. "
        f"Moyenne : {current_text} intervention/nuit ce mois "
        f"(vs {str(previous).replace('.', 'XX,XX')} le trimestre dernier)."
    )

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_6'] = x__build_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_7'] = x__build_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_8'] = x__build_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_9'] = x__build_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_10'] = x__build_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_11'] = x__build_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_12'] = x__build_summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_13'] = x__build_summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_14'] = x__build_summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_15'] = x__build_summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_16'] = x__build_summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_17'] = x__build_summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_18'] = x__build_summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_19'] = x__build_summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_20'] = x__build_summary__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_21'] = x__build_summary__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_22'] = x__build_summary__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_23'] = x__build_summary__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_24'] = x__build_summary__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_25'] = x__build_summary__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_26'] = x__build_summary__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_27'] = x__build_summary__mutmut_27 # type: ignore # mutmut generated

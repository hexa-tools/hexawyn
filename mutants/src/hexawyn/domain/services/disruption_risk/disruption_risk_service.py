from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import RiskEventRaw
from hexawyn.domain.models.disruption_risk import DisruptionRiskReport, RiskEvent


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_disruption_risks__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_disruption_risks__mutmut)
def compute_disruption_risks(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_orig(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_1(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_2(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=None, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_3(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=None, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_4(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning=None
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_5(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_6(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_7(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_8(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=True, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_9(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="XXAucune donnee de prediction disponible.XX"
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_10(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_11(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="AUCUNE DONNEE DE PREDICTION DISPONIBLE."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_12(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = None  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_13(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["XXdays_from_nowXX"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_14(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["DAYS_FROM_NOW"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_15(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] < 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_16(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 8]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_17(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = None
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_18(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=None,
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_19(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=None,
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_20(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=None,
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_21(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=None,
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_22(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=None,
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_23(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_24(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_25(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_26(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_27(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_28(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["XXbusiness_service_nameXX"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_29(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["BUSINESS_SERVICE_NAME"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_30(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["XXrisk_typeXX"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_31(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["RISK_TYPE"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_32(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["XXpredicted_dateXX"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_33(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["PREDICTED_DATE"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_34(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["XXdays_from_nowXX"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_35(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["DAYS_FROM_NOW"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_36(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["XXdetailXX"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_37(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["DETAIL"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_38(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=None,
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_39(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=None,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_40(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=None,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_41(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=None,
    )


def x_compute_disruption_risks__mutmut_42(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        risks=events,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_43(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        has_risks=len(events) > 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_44(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_45(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        )


def x_compute_disruption_risks__mutmut_46(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) >= 0,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_47(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 1,
        has_data=True,
    )


def x_compute_disruption_risks__mutmut_48(
    risks: list[RiskEventRaw], period: str, has_data: bool
) -> DisruptionRiskReport:
    if not has_data:
        return DisruptionRiskReport(
            period_label=period, has_data=False, warning="Aucune donnee de prediction disponible."
        )

    filtered = [risk for risk in risks if risk["days_from_now"] <= 7]  # noqa: PLR2004
    events = [
        RiskEvent(
            business_service_name=risk["business_service_name"],
            risk_type=risk["risk_type"],
            predicted_date=risk["predicted_date"],
            days_from_now=risk["days_from_now"],
            detail=risk["detail"],
        )
        for risk in filtered
    ]
    return DisruptionRiskReport(
        period_label=period,
        risks=events,
        has_risks=len(events) > 0,
        has_data=False,
    )

mutants_x_compute_disruption_risks__mutmut['_mutmut_orig'] = x_compute_disruption_risks__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_1'] = x_compute_disruption_risks__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_2'] = x_compute_disruption_risks__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_3'] = x_compute_disruption_risks__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_4'] = x_compute_disruption_risks__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_5'] = x_compute_disruption_risks__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_6'] = x_compute_disruption_risks__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_7'] = x_compute_disruption_risks__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_8'] = x_compute_disruption_risks__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_9'] = x_compute_disruption_risks__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_10'] = x_compute_disruption_risks__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_11'] = x_compute_disruption_risks__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_12'] = x_compute_disruption_risks__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_13'] = x_compute_disruption_risks__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_14'] = x_compute_disruption_risks__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_15'] = x_compute_disruption_risks__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_16'] = x_compute_disruption_risks__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_17'] = x_compute_disruption_risks__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_18'] = x_compute_disruption_risks__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_19'] = x_compute_disruption_risks__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_20'] = x_compute_disruption_risks__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_21'] = x_compute_disruption_risks__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_22'] = x_compute_disruption_risks__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_23'] = x_compute_disruption_risks__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_24'] = x_compute_disruption_risks__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_25'] = x_compute_disruption_risks__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_26'] = x_compute_disruption_risks__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_27'] = x_compute_disruption_risks__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_28'] = x_compute_disruption_risks__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_29'] = x_compute_disruption_risks__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_30'] = x_compute_disruption_risks__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_31'] = x_compute_disruption_risks__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_32'] = x_compute_disruption_risks__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_33'] = x_compute_disruption_risks__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_34'] = x_compute_disruption_risks__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_35'] = x_compute_disruption_risks__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_36'] = x_compute_disruption_risks__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_37'] = x_compute_disruption_risks__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_38'] = x_compute_disruption_risks__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_39'] = x_compute_disruption_risks__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_40'] = x_compute_disruption_risks__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_41'] = x_compute_disruption_risks__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_42'] = x_compute_disruption_risks__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_43'] = x_compute_disruption_risks__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_44'] = x_compute_disruption_risks__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_45'] = x_compute_disruption_risks__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_46'] = x_compute_disruption_risks__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_47'] = x_compute_disruption_risks__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_disruption_risks__mutmut['x_compute_disruption_risks__mutmut_48'] = x_compute_disruption_risks__mutmut_48 # type: ignore # mutmut generated

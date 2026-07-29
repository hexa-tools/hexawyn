from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import RiskEventRaw
from hexawyn.domain.models.disruption_risk import DisruptionRiskReport, RiskEvent


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

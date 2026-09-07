from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import RiskEventRaw
from hexawyn.domain.models.disruption_risk import DisruptionRiskReport, RiskEvent
from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
    compute_disruption_risks,
)


def _risk(
    name: str,
    days: int,
    risk_type: str = "TLS cert expiry",
    date: str = "2026-07-20",
    detail: str = "some detail",
) -> RiskEventRaw:
    return {
        "business_service_name": name,
        "risk_type": risk_type,
        "predicted_date": date,
        "days_from_now": days,
        "detail": detail,
    }


class TestComputeDisruptionRisks:
    def test_no_data_returns_warning(self) -> None:
        result = compute_disruption_risks([], period="2026-07", has_data=False)
        assert result.has_data is False
        assert result.warning is not None

    def test_filters_risks_within_7_days(self) -> None:
        risk1: RiskEventRaw = {
            "business_service_name": "payments-api",
            "risk_type": "TLS cert expiry",
            "predicted_date": "2026-07-20",
            "days_from_now": 3,
            "detail": "cert will expire in 3 days",
        }
        risk2: RiskEventRaw = {
            "business_service_name": "auth-api",
            "risk_type": "Secret rotation",
            "predicted_date": "2026-08-15",
            "days_from_now": 30,
            "detail": "token rotation due",
        }
        result = compute_disruption_risks([risk1, risk2], period="2026-07", has_data=True)
        assert result.has_risks is True
        assert len(result.risks) == 1
        assert result.risks[0].business_service_name == "payments-api"


class TestExactPayloads:
    def test_no_data_full_payload(self) -> None:
        result = compute_disruption_risks([], period="2026-07", has_data=False)

        assert result == DisruptionRiskReport(
            period_label="2026-07",
            risks=[],
            has_risks=False,
            has_data=False,
            warning="Aucune donnee de prediction disponible.",
        )

    def test_with_data_full_payload(self) -> None:
        risks = [
            _risk("payments-api", 3),
            _risk("auth-api", 30),
            _risk("storage", 7),
        ]
        result = compute_disruption_risks(risks, period="2026-07", has_data=True)

        assert result == DisruptionRiskReport(
            period_label="2026-07",
            risks=[
                RiskEvent(
                    business_service_name="payments-api",
                    risk_type="TLS cert expiry",
                    predicted_date="2026-07-20",
                    days_from_now=3,
                    detail="some detail",
                ),
                RiskEvent(
                    business_service_name="storage",
                    risk_type="TLS cert expiry",
                    predicted_date="2026-07-20",
                    days_from_now=7,
                    detail="some detail",
                ),
            ],
            has_risks=True,
            has_data=True,
            warning="",
        )

    def test_all_risks_beyond_window_no_risks(self) -> None:
        risks = [_risk("auth-api", 8), _risk("payments-api", 30)]
        result = compute_disruption_risks(risks, period="2026-07", has_data=True)

        assert result == DisruptionRiskReport(
            period_label="2026-07",
            risks=[],
            has_risks=False,
            has_data=True,
            warning="",
        )

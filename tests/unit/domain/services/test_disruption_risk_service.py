from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import RiskEventRaw
from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
    compute_disruption_risks,
)


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

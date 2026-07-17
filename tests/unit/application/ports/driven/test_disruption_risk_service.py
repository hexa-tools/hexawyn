from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import RiskEventRaw


def _risk(
    business_service_name: str = "moteur de recommandation",
    risk_type: str = "memory_saturation",
    days: int = 3,
) -> RiskEventRaw:
    return RiskEventRaw(
        business_service_name=business_service_name,
        risk_type=risk_type,
        predicted_date="2026-09-20",
        days_from_now=days,
        detail="Saturation memoire prevue",
    )


class TestRiskFiltering:
    def test_risk_within_seven_days_included(self) -> None:
        from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
            compute_disruption_risks,
        )

        report = compute_disruption_risks([_risk(days=3)], period="Semaine 39", has_data=True)

        assert report.has_risks is True
        assert report.risks[0].days_from_now == 3

    def test_risk_beyond_seven_days_excluded(self) -> None:
        from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
            compute_disruption_risks,
        )

        report = compute_disruption_risks([_risk(days=14)], period="Semaine 39", has_data=True)

        assert report.has_risks is False

    def test_no_risks_stable(self) -> None:
        from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
            compute_disruption_risks,
        )

        report = compute_disruption_risks([], period="Semaine 39", has_data=True)

        assert report.has_risks is False


class TestNoData:
    def test_missing_data_warns(self) -> None:
        from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
            compute_disruption_risks,
        )

        report = compute_disruption_risks([], period="Semaine 39", has_data=False)

        assert report.has_data is False
        assert report.warning != ""


class TestBusinessLanguage:
    def test_business_service_name_preserved(self) -> None:
        from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
            compute_disruption_risks,
        )

        report = compute_disruption_risks(
            [_risk(business_service_name="moteur de recommandation", days=3)],
            period="Semaine 39",
            has_data=True,
        )

        assert report.risks[0].business_service_name == "moteur de recommandation"
        for term in ("pod", "worker", "deployment"):
            assert term not in report.risks[0].business_service_name.lower()

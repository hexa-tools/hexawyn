from __future__ import annotations

from hexawyn.domain.models.budget_intelligence import (
    BudgetAlertRecommendation,
    BudgetIntelligenceReport,
)
from hexawyn.domain.models.consolidation import ConsolidatedKnowledge, ConsolidationConfig
from hexawyn.domain.models.cost_audit import CostAudit
from hexawyn.domain.models.critical_cve import CriticalCveReport, CveSummary
from hexawyn.domain.models.disruption_risk import DisruptionRiskReport, RiskEvent
from hexawyn.domain.models.stale_credentials import StaleCredential, StaleCredentialsReport
from hexawyn.domain.models.unauthorized_access import UnauthorizedAccessReport


class TestConsolidation:
    def test_config(self) -> None:
        c = ConsolidationConfig()
        assert c.min_occurrences >= 1

    def test_knowledge(self) -> None:
        k = ConsolidatedKnowledge(pattern="OOM", tool_name="detect_zombies", occurrence_count=5)
        assert k.pattern == "OOM"
        assert k.occurrence_count == 5  # noqa: PLR2004


class TestCostAudit:
    def test_defaults(self) -> None:
        ca = CostAudit(
            namespace="ns",
            pod_count=10,
            total_cost=100.0,
            total_waste=50.0,
            waste_percent=50.0,
            savings_right_sizing=30.0,
            savings_spot=10.0,
            savings_total=40.0,
        )
        assert ca.namespace == "ns"
        assert ca.total_waste == 50.0  # noqa: PLR2004


class TestCriticalCve:
    def test_summary(self) -> None:
        c = CveSummary(
            business_service_name="api", severity="CRITICAL", count=3, oldest_unresolved_days=30
        )
        assert c.severity == "CRITICAL"
        assert c.count == 3  # noqa: PLR2004

    def test_report(self) -> None:
        r = CriticalCveReport(
            period_label="week",
            total_critical_cves=5,
            affected_service_count=3,
            oldest_unresolved_days=30,
            cves=[],
            total_images_scanned=100,
            has_data=True,
            warning=None,
        )
        assert r.total_critical_cves == 5  # noqa: PLR2004
        assert r.has_data is True


class TestDisruptionRisk:
    def test_event(self) -> None:
        e = RiskEvent(
            business_service_name="api",
            risk_type="cert_expiry",
            predicted_date="2026-08",
            days_from_now=7,
            detail="expires soon",
        )
        assert e.risk_type == "cert_expiry"
        assert e.days_from_now == 7  # noqa: PLR2004

    def test_report(self) -> None:
        r = DisruptionRiskReport(
            period_label="week", risks=[], has_risks=True, has_data=True, warning=None
        )
        assert r.has_risks is True


class TestStaleCredentials:
    def test_credential(self) -> None:
        c = StaleCredential(name="token-abc", risk_level="high", days_unrotated=120)
        assert c.name == "token-abc"
        assert c.risk_level == "high"

    def test_report(self) -> None:
        r = StaleCredentialsReport(
            period_label="month", total_stale=5, critical_count=2, credentials=[]
        )
        assert r.total_stale == 5  # noqa: PLR2004


class TestUnauthorizedAccess:
    def test_report(self) -> None:
        r = UnauthorizedAccessReport(
            period_label="week",
            attempt_count=10,
            window_minutes=60,
            source_type="external",
            alert_level="medium",
        )
        assert r.attempt_count == 10  # noqa: PLR2004
        assert r.alert_level == "medium"


class TestBudgetIntelligence:
    def test_recommendation(self) -> None:
        rec = BudgetAlertRecommendation(action="Optimiser", description="Desc")
        assert rec.action == "Optimiser"

    def test_report(self) -> None:
        r = BudgetIntelligenceReport(
            period_label="2026-07",
            current_spend_eur=500.0,
            projected_spend_eur=1200.0,
            budget_monthly_eur=1000.0,
            overshoot_pct=20.0,
            budget_exceeded=True,
            recommendations=[],
        )
        assert r.budget_exceeded is True

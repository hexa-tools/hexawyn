from dataclasses import fields


class TestCalculationBasis:
    def test_fields(self) -> None:
        from hexawyn.domain.models.incident_cost import CalculationBasis

        names = {f.name for f in fields(CalculationBasis)}
        assert names == {"formula", "config_values_used", "source_metrics"}

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.incident_cost import CalculationBasis

        basis = CalculationBasis(
            formula="downtime_minutes x revenue_per_minute + support_cost + sla_penalty",
            config_values_used={"revenue_per_minute": "500"},
            source_metrics={"downtime_minutes": "27"},
        )

        assert basis.config_values_used["revenue_per_minute"] == "500"
        assert basis.source_metrics["downtime_minutes"] == "27"


class TestIncidentCostReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.incident_cost import IncidentCostReport

        report = IncidentCostReport(business_service_name="Service Paiement", downtime_minutes=27)

        assert report.business_service_name == "Service Paiement"
        assert report.downtime_minutes == 27  # noqa: PLR2004
        assert report.revenue_impact_eur is None
        assert report.support_cost_eur is None
        assert report.sla_penalty_eur is None
        assert report.total_cost_eur is None
        assert report.impacted_service_count == 0
        assert report.resolved_at == ""
        assert report.config_available is False
        assert report.explanation == ""
        assert report.calculation_basis is None

    def test_holds_computed_costs(self) -> None:
        from hexawyn.domain.models.incident_cost import (
            CalculationBasis,
            IncidentCostReport,
        )

        basis = CalculationBasis(formula="f", config_values_used={}, source_metrics={})
        report = IncidentCostReport(
            business_service_name="Service Paiement",
            downtime_minutes=27,
            revenue_impact_eur=13500.0,
            support_cost_eur=0.0,
            sla_penalty_eur=0.0,
            total_cost_eur=13500.0,
            impacted_service_count=3,
            resolved_at="14h23",
            config_available=True,
            calculation_basis=basis,
        )

        assert report.total_cost_eur == 13500.0  # noqa: PLR2004
        assert report.impacted_service_count == 3  # noqa: PLR2004
        assert report.calculation_basis is basis

from __future__ import annotations

from hexawyn.application.ports.driven.incident_cost_port import (
    BusinessConfigRaw,
    IncidentCostData,
)


def _config(
    revenue: float | None = 500.0,
    support: float | None = None,
    sla: float | None = None,
) -> BusinessConfigRaw:
    return BusinessConfigRaw(
        revenue_per_minute=revenue,
        support_cost_per_hour=support,
        sla_penalty_per_hour=sla,
    )


def _data(
    downtime: int = 27,
    service: str = "Service Paiement",
    impacted: int = 3,
    resolved: str = "14h23",
    sla_breached: bool = False,
    config: BusinessConfigRaw | None = None,
) -> IncidentCostData:
    return IncidentCostData(
        business_service_name=service,
        downtime_minutes=downtime,
        impacted_service_count=impacted,
        resolved_at=resolved,
        sla_breached=sla_breached,
        business_config=config if config is not None else _config(),
    )


class TestRevenueImpact:
    def test_twenty_seven_min_at_500_is_13500(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        report = compute_incident_cost(_data(downtime=27, config=_config(revenue=500.0)))

        assert report.revenue_impact_eur == 13500.0
        assert report.total_cost_eur == 13500.0

    def test_config_available_true(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        report = compute_incident_cost(_data(config=_config(revenue=500.0)))

        assert report.config_available is True
        assert report.calculation_basis is not None


class TestMissingConfig:
    def test_no_revenue_yields_no_euro_amount(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        report = compute_incident_cost(_data(config=_config(revenue=None)))

        assert report.revenue_impact_eur is None
        assert report.total_cost_eur is None
        assert report.config_available is False

    def test_no_revenue_returns_explanation(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        report = compute_incident_cost(_data(downtime=27, config=_config(revenue=None)))

        assert "revenue_per_minute" in report.explanation
        assert "27" in report.explanation

    def test_no_revenue_keeps_duration_facts(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        report = compute_incident_cost(_data(downtime=27, config=_config(revenue=None)))

        assert report.downtime_minutes == 27
        assert report.business_service_name == "Service Paiement"


class TestSupportAndSla:
    def test_support_cost_added(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        # 60 min downtime = 1h support @ 180/h.
        report = compute_incident_cost(
            _data(downtime=60, config=_config(revenue=500.0, support=180.0))
        )

        assert report.support_cost_eur == 180.0
        assert report.total_cost_eur == 60 * 500.0 + 180.0

    def test_sla_penalty_only_when_breached(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        breached = compute_incident_cost(
            _data(downtime=60, sla_breached=True, config=_config(revenue=500.0, sla=1500.0))
        )
        not_breached = compute_incident_cost(
            _data(downtime=60, sla_breached=False, config=_config(revenue=500.0, sla=1500.0))
        )

        assert breached.sla_penalty_eur == 1500.0
        assert not_breached.sla_penalty_eur == 0.0


class TestCalculationBasis:
    def test_basis_records_formula_and_config(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        report = compute_incident_cost(_data(downtime=27, config=_config(revenue=500.0)))
        basis = report.calculation_basis

        assert basis is not None
        assert "revenue_per_minute" in basis.config_values_used
        assert basis.source_metrics["downtime_minutes"] == "27"
        assert "downtime" in basis.formula.lower()


class TestBusinessLanguage:
    def test_uses_business_service_name(self) -> None:
        from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
            compute_incident_cost,
        )

        report = compute_incident_cost(_data(service="Service Paiement"))

        assert report.business_service_name == "Service Paiement"
        for term in ("pod", "deployment", "replicaset"):
            assert term not in report.business_service_name.lower()

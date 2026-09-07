"""Tests for domain/services/incident_cost — incident financial impact."""

from __future__ import annotations

from hexawyn.application.ports.driven.incident_cost_port import (
    BusinessConfigRaw,
    IncidentCostData,
)
from hexawyn.domain.models.incident_cost import (
    CalculationBasis,
    IncidentCostReport,
)
from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
    _build_basis,
    _sla_penalty,
    _support_cost,
    _unconfigured_report,
    compute_incident_cost,
)


def _config(**overrides: object) -> BusinessConfigRaw:
    base: dict[str, object] = {
        "revenue_per_minute": 100.0,
        "support_cost_per_hour": 120.0,
        "sla_penalty_per_hour": 500.0,
    }
    base.update(overrides)
    return BusinessConfigRaw(**base)  # type: ignore[arg-type]


def _incident(**overrides: object) -> IncidentCostData:
    base: dict[str, object] = {
        "business_service_name": "payments",
        "downtime_minutes": 45,
        "impacted_service_count": 3,
        "resolved_at": "2026-01-01T10:00:00Z",
        "sla_breached": True,
        "business_config": _config(),
    }
    base.update(overrides)
    return IncidentCostData(**base)  # type: ignore[arg-type]


class TestComputeIncidentCost:
    def test_full_config_report_exact(self) -> None:
        report = compute_incident_cost(_incident())
        assert report == IncidentCostReport(
            business_service_name="payments",
            downtime_minutes=45,
            revenue_impact_eur=4500.0,
            support_cost_eur=90.0,
            sla_penalty_eur=500.0,
            total_cost_eur=5090.0,
            impacted_service_count=3,
            resolved_at="2026-01-01T10:00:00Z",
            config_available=True,
            calculation_basis=CalculationBasis(
                formula=("downtime_minutes x revenue_per_minute + support_cost + sla_penalty"),
                config_values_used={
                    "revenue_per_minute": "100.0",
                    "support_cost_per_hour": "120.0",
                    "sla_penalty_per_hour": "500.0",
                },
                source_metrics={
                    "downtime_minutes": "45",
                    "sla_breached": "True",
                },
            ),
        )

    def test_fractional_revenue_rounded_to_two_decimals(self) -> None:
        report = compute_incident_cost(_incident(downtime_minutes=7))
        assert report.revenue_impact_eur == 700.0  # noqa: PLR2004
        assert report.support_cost_eur == 14.0  # noqa: PLR2004

    def test_partial_minute_support_rounding(self) -> None:
        report = compute_incident_cost(
            _incident(downtime_minutes=1, business_config=_config(support_cost_per_hour=10.0))
        )
        assert report.support_cost_eur == 0.17  # noqa: PLR2004

    def test_no_sla_breach_excludes_penalty(self) -> None:
        report = compute_incident_cost(_incident(sla_breached=False))
        assert report.sla_penalty_eur == 0.0
        assert report.total_cost_eur == 4590.0  # noqa: PLR2004
        assert report.calculation_basis is not None
        assert report.calculation_basis.config_values_used == {
            "revenue_per_minute": "100.0",
            "support_cost_per_hour": "120.0",
        }

    def test_unconfigured_extras_excluded(self) -> None:
        report = compute_incident_cost(
            _incident(
                business_config=_config(support_cost_per_hour=None, sla_penalty_per_hour=None)
            )
        )
        assert report.support_cost_eur == 0.0
        assert report.sla_penalty_eur == 0.0
        assert report.total_cost_eur == 4500.0  # noqa: PLR2004
        assert report.calculation_basis is not None
        assert report.calculation_basis.config_values_used == {
            "revenue_per_minute": "100.0",
        }

    def test_missing_revenue_returns_explanation(self) -> None:
        report = compute_incident_cost(
            _incident(
                business_config=_config(
                    revenue_per_minute=None,
                    support_cost_per_hour=None,
                    sla_penalty_per_hour=None,
                )
            )
        )
        assert report.config_available is False
        assert report.business_service_name == "payments"
        assert report.downtime_minutes == 45  # noqa: PLR2004
        assert report.revenue_impact_eur is None
        assert report.support_cost_eur is None
        assert report.total_cost_eur is None
        assert report.calculation_basis is None
        assert report.explanation == (
            "Le service payments est reste indisponible pendant 45 minutes. "
            "Configurez 'revenue_per_minute' dans la section business pour obtenir "
            "l'estimation du chiffre d'affaires affecte."
        )

    def test_zero_downtime_revenue_zero(self) -> None:
        report = compute_incident_cost(_incident(downtime_minutes=0))
        assert report.revenue_impact_eur == 0.0
        assert report.support_cost_eur == 0.0
        assert report.total_cost_eur == 500.0  # noqa: PLR2004 (sla only)

    def test_rounding_carries_into_total(self) -> None:
        report = compute_incident_cost(
            _incident(
                downtime_minutes=13,
                business_config=_config(
                    revenue_per_minute=33.33,
                    support_cost_per_hour=77.77,
                    sla_penalty_per_hour=199.99,
                ),
            )
        )
        assert report.revenue_impact_eur == 433.29  # noqa: PLR2004
        assert report.support_cost_eur == 16.85  # noqa: PLR2004
        assert report.sla_penalty_eur == 199.99  # noqa: PLR2004
        assert report.total_cost_eur == 650.13  # noqa: PLR2004

    def test_revenue_three_decimals_rounded_to_two(self) -> None:
        report = compute_incident_cost(
            _incident(
                downtime_minutes=1,
                sla_breached=False,
                business_config=_config(
                    revenue_per_minute=1.235,
                    support_cost_per_hour=None,
                    sla_penalty_per_hour=None,
                ),
            )
        )
        assert report.revenue_impact_eur == 1.24  # noqa: PLR2004
        assert report.total_cost_eur == 1.24  # noqa: PLR2004

    def test_sla_three_decimals_rounded_to_two(self) -> None:
        report = compute_incident_cost(
            _incident(
                downtime_minutes=1,
                sla_breached=True,
                business_config=_config(
                    revenue_per_minute=0.0,
                    support_cost_per_hour=None,
                    sla_penalty_per_hour=1.235,
                ),
            )
        )
        assert report.sla_penalty_eur == 1.24  # noqa: PLR2004
        assert report.total_cost_eur == 1.24  # noqa: PLR2004


class TestSupportCostDirect:
    def test_none_returns_zero(self) -> None:
        assert _support_cost(60, _config(support_cost_per_hour=None)) == 0.0

    def test_exact_hour(self) -> None:
        assert _support_cost(60, _config(support_cost_per_hour=120.0)) == 120.0  # noqa: PLR2004

    def test_half_hour(self) -> None:
        assert _support_cost(30, _config(support_cost_per_hour=120.0)) == 60.0  # noqa: PLR2004

    def test_partial_rounding(self) -> None:
        assert _support_cost(1, _config(support_cost_per_hour=10.0)) == 0.17  # noqa: PLR2004


class TestSlaPenaltyDirect:
    def test_not_breached_returns_zero(self) -> None:
        assert _sla_penalty(False, _config()) == 0.0

    def test_breached_no_config_returns_zero(self) -> None:
        assert _sla_penalty(True, _config(sla_penalty_per_hour=None)) == 0.0

    def test_breached_configured_returns_penalty(self) -> None:
        assert _sla_penalty(True, _config(sla_penalty_per_hour=500.0)) == 500.0  # noqa: PLR2004


class TestUnconfiguredReportDirect:
    def test_defaults_filled(self) -> None:
        report = _unconfigured_report(_incident(downtime_minutes=30))
        assert report.config_available is False
        assert report.downtime_minutes == 30  # noqa: PLR2004
        assert report.impacted_service_count == 3  # noqa: PLR2004
        assert report.resolved_at == "2026-01-01T10:00:00Z"
        assert report.explanation != ""


class TestBuildBasisDirect:
    def test_all_config_values_recorded_when_breached(self) -> None:
        incident = _incident()
        config = _config()
        basis = _build_basis(incident, config)
        assert basis.formula == (
            "downtime_minutes x revenue_per_minute + support_cost + sla_penalty"
        )
        assert basis.source_metrics == {"downtime_minutes": "45", "sla_breached": "True"}

    def test_sla_config_omitted_when_not_breached(self) -> None:
        incident = _incident(sla_breached=False)
        config = _config()
        basis = _build_basis(incident, config)
        assert basis.config_values_used == {
            "revenue_per_minute": "100.0",
            "support_cost_per_hour": "120.0",
        }

    def test_support_config_omitted_when_none(self) -> None:
        incident = _incident()
        config = _config(support_cost_per_hour=None)
        basis = _build_basis(incident, config)
        assert basis.config_values_used == {
            "revenue_per_minute": "100.0",
            "sla_penalty_per_hour": "500.0",
        }

"""RED → GREEN — Executive summary builder (exact French business language)."""

from __future__ import annotations

from hexawyn.domain.models.platform_reliability import IncidentSummary
from hexawyn.domain.services.platform_reliability import executive_summary_builder as builder


def _incident(
    severity: str,
    downtime: int,
    date: str = "2026-06-14",
    root_cause: str = "",
    resolved: bool = True,
) -> IncidentSummary:
    return IncidentSummary(
        date=date,
        severity=severity,
        downtime_minutes=downtime,
        root_cause=root_cause,
        resolved=resolved,
    )


class TestEmptyMonth:
    def test_no_incidents_returns_stable_sentence(self) -> None:
        summary = builder.build_summary(
            uptime_pct=100.0,
            incidents=[],
            avg_resolution_minutes=0,
            resolution_delta_pct=0.0,
            resolution_trend="stable",
            financial_impact_eur=None,
            pricing_configured=False,
        )

        assert summary == "Plateforme stable. Aucun incident ce mois."


class TestAvailabilitySentence:
    def test_single_minor(self) -> None:
        incidents = [_incident("minor", 30)]

        assert builder._availability_sentence(99.95, incidents) == (
            "99,95% de disponibilite, avec 1 incident mineur resolu."
        )

    def test_two_minors_plural(self) -> None:
        incidents = [_incident("minor", 30), _incident("minor", 45)]

        assert builder._availability_sentence(100.0, incidents) == (
            "100,00% de disponibilite, avec 2 incidents mineurs resolus."
        )

    def test_single_major_singular_label(self) -> None:
        incidents = [_incident("major", 120)]

        assert builder._availability_sentence(99.5, incidents) == (
            "99,50% de disponibilite, avec 1 incident majeur resolu."
        )

    def test_mixed_major_and_minor_plural_label(self) -> None:
        incidents = [_incident("major", 120), _incident("minor", 30)]

        assert builder._availability_sentence(98.21, incidents) == (
            "98,21% de disponibilite, avec 2 incidents majeurs resolus."
        )


class TestMajorSentence:
    def test_with_root_cause_and_fractional_hours(self) -> None:
        incident = _incident("major", 90, root_cause="Panne base de donnees")

        assert builder._major_sentence(incident) == (
            "Incident critique le 2026-06-14 : 1,5h d'indisponibilite. "
            "Cause racine : Panne base de donnees. Corrige."
        )

    def test_without_root_cause_uses_default(self) -> None:
        incident = _incident("major", 120)

        assert builder._major_sentence(incident) == (
            "Incident critique le 2026-06-14 : 2,0h d'indisponibilite. "
            "Cause racine : cause en cours d'analyse. Corrige."
        )


class TestResolutionSentence:
    def test_stable_trend(self) -> None:
        assert builder._resolution_sentence(12, 0.0, "stable") == (
            "Temps de resolution moyen : 12 min."
        )

    def test_improving_trend_prefixes_minus(self) -> None:
        assert builder._resolution_sentence(45, -15.3, "improving") == (
            "Temps de resolution moyen : 45 min (-15% vs mois dernier)."
        )

    def test_degrading_trend_prefixes_plus(self) -> None:
        assert builder._resolution_sentence(68, 12.6, "degrading") == (
            "Temps de resolution moyen : 68 min (+13% vs mois dernier)."
        )


class TestFinancialSentence:
    def test_amount_without_decimals(self) -> None:
        assert builder._financial_sentence(2500.0) == (
            "Cout estime des interventions : 2500\u20ac."
        )


class TestSeverityLabel:
    def test_major_only_singular(self) -> None:
        assert builder._severity_label([_incident("major", 30)]) == "majeur"

    def test_major_mixed_plural(self) -> None:
        label = builder._severity_label([_incident("major", 30), _incident("minor", 30)])
        assert label == "majeurs"

    def test_minor_only_singular(self) -> None:
        assert builder._severity_label([_incident("minor", 30)]) == "mineur"

    def test_minor_only_plural(self) -> None:
        label = builder._severity_label([_incident("minor", 30), _incident("minor", 45)])
        assert label == "mineurs"


class TestFirstMajor:
    def test_returns_first_major_when_present(self) -> None:
        minor = _incident("minor", 30, date="2026-06-01")
        major = _incident("major", 90, date="2026-06-10")
        incidents = [minor, major]

        assert builder._first_major(incidents) == major

    def test_returns_none_when_no_major(self) -> None:
        assert builder._first_major([_incident("minor", 30)]) is None


class TestFullSummary:
    def test_minor_only_without_financial(self) -> None:
        incidents = [_incident("minor", 30, date="2026-06-10", root_cause="deploiement")]

        summary = builder.build_summary(
            uptime_pct=99.95,
            incidents=incidents,
            avg_resolution_minutes=12,
            resolution_delta_pct=-15.0,
            resolution_trend="improving",
            financial_impact_eur=None,
            pricing_configured=False,
        )

        assert summary == (
            "99,95% de disponibilite, avec 1 incident mineur resolu. "
            "Temps de resolution moyen : 12 min (-15% vs mois dernier)."
        )

    def test_major_with_financial_and_stable_resolution(self) -> None:
        incidents = [_incident("major", 90, date="2026-06-14", root_cause="Panne DB")]

        summary = builder.build_summary(
            uptime_pct=99.5,
            incidents=incidents,
            avg_resolution_minutes=45,
            resolution_delta_pct=0.0,
            resolution_trend="stable",
            financial_impact_eur=2500.0,
            pricing_configured=True,
        )

        assert summary == (
            "99,50% de disponibilite, avec 1 incident majeur resolu. "
            "Incident critique le 2026-06-14 : 1,5h d'indisponibilite. "
            "Cause racine : Panne DB. Corrige. "
            "Temps de resolution moyen : 45 min. "
            "Cout estime des interventions : 2500\u20ac."
        )

    def test_major_after_minor_not_mentioned_in_major_sentence(self) -> None:
        incidents = [
            _incident("minor", 30, date="2026-06-01"),
            _incident("major", 120, date="2026-06-14", root_cause="reseau"),
        ]

        summary = builder.build_summary(
            uptime_pct=99.0,
            incidents=incidents,
            avg_resolution_minutes=60,
            resolution_delta_pct=0.0,
            resolution_trend="stable",
            financial_impact_eur=None,
            pricing_configured=False,
        )

        assert "2026-06-01" not in summary
        assert "Incident critique le 2026-06-14" in summary
        assert summary.startswith("99,00% de disponibilite, avec 2 incidents majeurs resolus.")


class TestDiscriminantBoundaries:
    def test_major_hours_rounded_to_one_decimal(self) -> None:
        incident = _incident("major", 100, root_cause="reseau")

        assert builder._major_sentence(incident) == (
            "Incident critique le 2026-06-14 : 1,7h d'indisponibilite. "
            "Cause racine : reseau. Corrige."
        )

    def test_resolution_delta_exactly_zero_uses_plus_when_not_stable(self) -> None:
        assert builder._resolution_sentence(30, 0.0, "improving") == (
            "Temps de resolution moyen : 30 min (+0% vs mois dernier)."
        )

    def test_resolution_delta_positive_fraction_uses_plus(self) -> None:
        assert builder._resolution_sentence(30, 0.5, "degrading") == (
            "Temps de resolution moyen : 30 min (+0% vs mois dernier)."
        )

    def test_pricing_configured_without_amount_skips_financial_sentence(self) -> None:
        incidents = [_incident("minor", 30)]

        summary = builder.build_summary(
            uptime_pct=99.95,
            incidents=incidents,
            avg_resolution_minutes=12,
            resolution_delta_pct=0.0,
            resolution_trend="stable",
            financial_impact_eur=None,
            pricing_configured=True,
        )

        assert "\u20ac" not in summary
        assert "Cout estime" not in summary

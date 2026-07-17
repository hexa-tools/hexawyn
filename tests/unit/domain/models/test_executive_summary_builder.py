from __future__ import annotations

from hexawyn.domain.models.platform_reliability import IncidentSummary

_FORBIDDEN_JARGON = ["pod", "kubectl", "namespace", "crashloop", "node", "container"]


def _incident(
    severity: str, downtime: int, date: str = "2026-06-14", rc: str = ""
) -> IncidentSummary:
    return IncidentSummary(
        date=date, severity=severity, downtime_minutes=downtime, root_cause=rc, resolved=True
    )


class TestHealthyMonth:
    def test_zero_incidents_says_stable(self) -> None:
        from hexawyn.domain.services.platform_reliability.executive_summary_builder import (
            build_summary,
        )

        summary = build_summary(
            uptime_pct=100.0,
            incidents=[],
            avg_resolution_minutes=0,
            resolution_delta_pct=0.0,
            resolution_trend="stable",
            financial_impact_eur=None,
            pricing_configured=False,
        )

        assert "stable" in summary.lower() or "aucun incident" in summary.lower()


class TestMinorIncidents:
    def test_mentions_uptime_and_incident_count(self) -> None:
        from hexawyn.domain.services.platform_reliability.executive_summary_builder import (
            build_summary,
        )

        summary = build_summary(
            uptime_pct=99.95,
            incidents=[_incident("minor", 12), _incident("minor", 12)],
            avg_resolution_minutes=12,
            resolution_delta_pct=-15.0,
            resolution_trend="improving",
            financial_impact_eur=0.0,
            pricing_configured=True,
        )

        assert "99,95" in summary or "99.95" in summary
        assert "2" in summary
        assert "12" in summary


class TestMajorIncident:
    def test_highlights_major_with_date_and_cause(self) -> None:
        from hexawyn.domain.services.platform_reliability.executive_summary_builder import (
            build_summary,
        )

        summary = build_summary(
            uptime_pct=99.72,
            incidents=[_incident("major", 120, date="2026-06-14", rc="Panne base de donnees")],
            avg_resolution_minutes=120,
            resolution_delta_pct=0.0,
            resolution_trend="stable",
            financial_impact_eur=None,
            pricing_configured=False,
        )

        assert "2026-06-14" in summary
        assert "base de donnees" in summary.lower()


class TestFinancial:
    def test_financial_shown_when_configured(self) -> None:
        from hexawyn.domain.services.platform_reliability.executive_summary_builder import (
            build_summary,
        )

        summary = build_summary(
            uptime_pct=99.95,
            incidents=[_incident("minor", 12)],
            avg_resolution_minutes=12,
            resolution_delta_pct=0.0,
            resolution_trend="stable",
            financial_impact_eur=0.0,
            pricing_configured=True,
        )

        assert "€" in summary or "eur" in summary.lower() or "co\u00fbt" in summary.lower()

    def test_no_financial_figure_when_pricing_absent(self) -> None:
        from hexawyn.domain.services.platform_reliability.executive_summary_builder import (
            build_summary,
        )

        summary = build_summary(
            uptime_pct=99.95,
            incidents=[_incident("minor", 12)],
            avg_resolution_minutes=12,
            resolution_delta_pct=0.0,
            resolution_trend="stable",
            financial_impact_eur=None,
            pricing_configured=False,
        )

        assert "€" not in summary


class TestNoJargon:
    def test_summary_contains_no_kubernetes_jargon(self) -> None:
        from hexawyn.domain.services.platform_reliability.executive_summary_builder import (
            build_summary,
        )

        summary = build_summary(
            uptime_pct=99.72,
            incidents=[_incident("major", 120, rc="Panne base de donnees")],
            avg_resolution_minutes=120,
            resolution_delta_pct=-15.0,
            resolution_trend="improving",
            financial_impact_eur=0.0,
            pricing_configured=True,
        )

        lowered = summary.lower()
        for term in _FORBIDDEN_JARGON:
            assert term not in lowered


class TestConciseness:
    def test_summary_at_most_five_sentences(self) -> None:
        from hexawyn.domain.services.platform_reliability.executive_summary_builder import (
            build_summary,
        )

        summary = build_summary(
            uptime_pct=99.95,
            incidents=[_incident("minor", 12), _incident("minor", 12)],
            avg_resolution_minutes=12,
            resolution_delta_pct=-15.0,
            resolution_trend="improving",
            financial_impact_eur=0.0,
            pricing_configured=True,
        )

        sentence_count = summary.count(".") + summary.count("!")
        assert sentence_count <= 5

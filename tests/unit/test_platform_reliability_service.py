from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityData,
    ReliabilityIncidentRaw,
)


def _incident(
    severity: str = "minor",
    downtime: int = 12,
    resolution: int = 12,
    date: str = "2026-06-14",
    rc: str = "",
    planned: bool = False,
) -> ReliabilityIncidentRaw:
    return ReliabilityIncidentRaw(
        date=date,
        severity=severity,
        downtime_minutes=downtime,
        resolution_minutes=resolution,
        root_cause=rc,
        resolved=True,
        planned_maintenance=planned,
    )


def _data(
    incidents: list[ReliabilityIncidentRaw] | None = None,
    period_minutes: int = 43200,
    previous_avg: int | None = None,
    cost_per_minute: float | None = None,
) -> ReliabilityData:
    return ReliabilityData(
        period_minutes=period_minutes,
        incidents=incidents if incidents is not None else [],
        previous_avg_resolution_minutes=previous_avg,
        cost_per_downtime_minute_eur=cost_per_minute,
    )


class TestHealthyMonth:
    def test_zero_incidents(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        report = PlatformReliabilityService().generate(_data(), period="2026-06")

        assert report.uptime_pct == 100.0
        assert report.total_incidents == 0
        assert "Aucun incident" in report.executive_summary


class TestMinorIncidents:
    def test_two_minor_incidents(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        data = _data(
            incidents=[_incident(downtime=15, resolution=10), _incident(downtime=45, resolution=14)]
        )

        report = PlatformReliabilityService().generate(data, period="2026-06")

        assert report.minor_count == 2
        assert report.major_count == 0
        assert report.has_major_incident is False
        assert report.avg_resolution_minutes == 12


class TestMajorIncident:
    def test_major_incident_flagged(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        data = _data(
            incidents=[_incident(severity="major", downtime=120, resolution=120, rc="Panne base")]
        )

        report = PlatformReliabilityService().generate(data, period="2026-06")

        assert report.has_major_incident is True
        assert report.major_count == 1
        assert report.uptime_pct == 99.72


class TestFinancial:
    def test_impact_none_when_no_pricing(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        report = PlatformReliabilityService().generate(
            _data(incidents=[_incident(downtime=120)], cost_per_minute=None), period="2026-06"
        )

        assert report.pricing_configured is False
        assert report.financial_impact_eur is None

    def test_impact_computed_when_pricing(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        report = PlatformReliabilityService().generate(
            _data(incidents=[_incident(downtime=120)], cost_per_minute=10.0), period="2026-06"
        )

        assert report.pricing_configured is True
        assert report.financial_impact_eur == 1200.0


class TestTrend:
    def test_resolution_trend_improving(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        report = PlatformReliabilityService().generate(
            _data(incidents=[_incident(resolution=12)], previous_avg=14), period="2026-06"
        )

        assert report.resolution_trend == "improving"
        assert report.previous_avg_resolution_minutes == 14


class TestExecutiveSummary:
    def test_summary_present_and_jargon_free(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        data = _data(
            incidents=[_incident(downtime=12), _incident(downtime=12)],
            previous_avg=14,
            cost_per_minute=0.0,
        )

        report = PlatformReliabilityService().generate(data, period="2026-06")

        assert report.executive_summary != ""
        for term in ("pod", "kubectl", "namespace"):
            assert term not in report.executive_summary.lower()

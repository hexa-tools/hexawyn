from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityData,
    ReliabilityIncidentRaw,
)


def _incident(  # noqa: PLR0913
    date: str = "2026-06-10",
    severity: str = "minor",
    downtime_minutes: int = 30,
    resolution_minutes: int = 60,
    root_cause: str = "test",
    resolved: bool = True,
    planned_maintenance: bool = False,
) -> ReliabilityIncidentRaw:
    return ReliabilityIncidentRaw(
        date=date,
        severity=severity,
        downtime_minutes=downtime_minutes,
        resolution_minutes=resolution_minutes,
        root_cause=root_cause,
        resolved=resolved,
        planned_maintenance=planned_maintenance,
    )


def _data(
    incidents: list[ReliabilityIncidentRaw] | None = None,
    period_minutes: int = 43200,
    previous_avg_resolution_minutes: int | None = 30,
    cost_per_downtime_minute_eur: float | None = 10.0,
) -> ReliabilityData:
    return ReliabilityData(
        period_minutes=period_minutes,
        incidents=incidents or [],
        previous_avg_resolution_minutes=previous_avg_resolution_minutes,
        cost_per_downtime_minute_eur=cost_per_downtime_minute_eur,
    )


class TestPlatformReliabilityService:
    def test_generate_no_incidents(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(incidents=[], period_minutes=43200)
        report = service.generate(data=data, period="2026-06")
        assert report.uptime_pct == 100.0  # noqa: PLR2004
        assert report.total_incidents == 0
        assert report.major_count == 0
        assert report.minor_count == 0
        assert report.has_major_incident is False

    def test_generate_with_minor_incidents(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[_incident(), _incident()],
            period_minutes=43200,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.total_incidents == 2  # noqa: PLR2004
        assert report.major_count == 0
        assert report.minor_count == 2  # noqa: PLR2004
        assert report.has_major_incident is False
        assert report.uptime_pct < 100.0  # noqa: PLR2004

    def test_generate_with_major_incident(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[
                _incident(severity="major", downtime_minutes=120, resolution_minutes=300),
            ],
            period_minutes=43200,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.total_incidents == 1
        assert report.major_count == 1
        assert report.minor_count == 0
        assert report.has_major_incident is True

    def test_generate_planned_maintenance_excluded_from_count(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[
                _incident(planned_maintenance=True),
                _incident(),
            ],
            period_minutes=43200,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.total_incidents == 1

    def test_generate_planned_maintenance_included_in_uptime(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[
                _incident(downtime_minutes=1440, planned_maintenance=True),
            ],
            period_minutes=1440,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.uptime_pct == 100.0  # noqa: PLR2004

    def test_generate_financial_impact_with_pricing(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[_incident(downtime_minutes=60)],
            period_minutes=43200,
            cost_per_downtime_minute_eur=10.0,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.pricing_configured is True
        assert report.financial_impact_eur is not None
        assert report.financial_impact_eur == 600.0  # noqa: PLR2004

    def test_generate_financial_impact_without_pricing(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[_incident(downtime_minutes=60)],
            period_minutes=43200,
            cost_per_downtime_minute_eur=None,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.pricing_configured is False
        assert report.financial_impact_eur is None

    def test_generate_incidents_summaries(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[
                _incident(
                    date="2026-06-10", severity="major", downtime_minutes=120, root_cause="OOM"
                ),
                _incident(
                    date="2026-06-15", severity="minor", downtime_minutes=30, root_cause="DNS"
                ),
            ],
            period_minutes=43200,
        )
        report = service.generate(data=data, period="2026-06")
        assert len(report.incidents) == 2  # noqa: PLR2004
        assert report.incidents[0].severity == "major"

    def test_generate_period_label_set(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(incidents=[], period_minutes=43200)
        report = service.generate(data=data, period="2026-Q2")
        assert report.period_label == "2026-Q2"

    def test_generate_executive_summary_not_empty(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(incidents=[_incident()], period_minutes=43200)
        report = service.generate(data=data, period="2026-06")
        assert len(report.executive_summary) > 0

    def test_generate_resolution_trend(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[_incident(resolution_minutes=60)],
            period_minutes=43200,
            previous_avg_resolution_minutes=30,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.avg_resolution_minutes == 60  # noqa: PLR2004
        assert report.resolution_trend in ("improving", "degrading", "stable")
        assert report.resolution_delta_pct != 0.0

    def test_generate_previous_avg_none(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[_incident(resolution_minutes=45)],
            period_minutes=43200,
            previous_avg_resolution_minutes=None,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.previous_avg_resolution_minutes is None
        assert report.resolution_trend == "stable"

    def test_generate_zero_period(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[_incident(downtime_minutes=60)],
            period_minutes=0,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.uptime_pct == 100.0  # noqa: PLR2004

    def test_generate_mixed_major_and_minor(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[
                _incident(severity="major", downtime_minutes=120, resolution_minutes=300),
                _incident(severity="minor", downtime_minutes=30, resolution_minutes=45),
                _incident(severity="minor", downtime_minutes=15, resolution_minutes=20),
            ],
            period_minutes=43200,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.total_incidents == 3  # noqa: PLR2004
        assert report.major_count == 1
        assert report.minor_count == 2  # noqa: PLR2004

    def test_generate_multiple_major(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(
            incidents=[
                _incident(severity="major", downtime_minutes=60, resolution_minutes=120),
                _incident(severity="major", downtime_minutes=90, resolution_minutes=180),
            ],
            period_minutes=43200,
        )
        report = service.generate(data=data, period="2026-06")
        assert report.total_incidents == 2  # noqa: PLR2004
        assert report.major_count == 2  # noqa: PLR2004
        assert report.minor_count == 0

    def test_generate_return_type(self) -> None:
        from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
            PlatformReliabilityService,
        )

        service = PlatformReliabilityService()
        data = _data(incidents=[], period_minutes=43200)
        report = service.generate(data=data, period="2026-06")
        assert hasattr(report, "period_label")
        assert hasattr(report, "uptime_pct")
        assert hasattr(report, "total_incidents")
        assert hasattr(report, "executive_summary")

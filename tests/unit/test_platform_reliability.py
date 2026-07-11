from dataclasses import fields


class TestIncidentSummary:
    def test_fields(self) -> None:
        from hexawyn.domain.models.platform_reliability import IncidentSummary

        names = {f.name for f in fields(IncidentSummary)}
        assert names == {"date", "severity", "downtime_minutes", "root_cause", "resolved"}

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.platform_reliability import IncidentSummary

        incident = IncidentSummary(
            date="2026-06-14",
            severity="major",
            downtime_minutes=120,
            root_cause="Database outage",
            resolved=True,
        )

        assert incident.severity == "major"
        assert incident.downtime_minutes == 120


class TestPlatformReliabilityReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.platform_reliability import PlatformReliabilityReport

        report = PlatformReliabilityReport(period_label="2026-06", uptime_pct=100.0)

        assert report.period_label == "2026-06"
        assert report.uptime_pct == 100.0
        assert report.total_incidents == 0
        assert report.major_count == 0
        assert report.minor_count == 0
        assert report.avg_resolution_minutes == 0
        assert report.resolution_trend == "stable"
        assert report.resolution_delta_pct == 0.0
        assert report.previous_avg_resolution_minutes is None
        assert report.financial_impact_eur is None
        assert report.pricing_configured is False
        assert report.incidents == []
        assert report.has_major_incident is False
        assert report.executive_summary == ""

    def test_holds_summary(self) -> None:
        from hexawyn.domain.models.platform_reliability import PlatformReliabilityReport

        report = PlatformReliabilityReport(
            period_label="2026-06",
            uptime_pct=99.95,
            total_incidents=2,
            minor_count=2,
            avg_resolution_minutes=12,
            resolution_trend="improving",
            resolution_delta_pct=-15.0,
            financial_impact_eur=0.0,
            pricing_configured=True,
            executive_summary="99,95% de disponibilite...",
        )

        assert report.uptime_pct == 99.95
        assert report.resolution_delta_pct == -15.0
        assert report.financial_impact_eur == 0.0

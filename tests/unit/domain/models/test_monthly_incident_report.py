"""RED → GREEN — Layer 1: Monthly Incident Report domain models."""

from hexawyn.domain.models.monthly_incident_report import (
    ImpactedService,
    MonthlyIncidentReport,
    SeverityBreakdown,
)


class TestSeverityBreakdown:
    def test_is_frozen(self) -> None:
        import pytest

        b = SeverityBreakdown(severity="P1", count=3, downtime_minutes=180)
        with pytest.raises(Exception):
            b.count = 5  # type: ignore[misc]


class TestImpactedService:
    def test_is_frozen(self) -> None:
        import pytest

        s = ImpactedService(service_name="payment-service", total_downtime=165, incident_count=2)
        with pytest.raises(Exception):
            s.total_downtime = 0  # type: ignore[misc]


class TestMonthlyIncidentReport:
    def test_defaults(self) -> None:
        report = MonthlyIncidentReport()
        assert report.total_count == 0
        assert report.total_downtime_minutes == 0

    def test_can_populate(self) -> None:
        report = MonthlyIncidentReport(
            total_count=8,
            total_downtime_minutes=220,
            incidents_decreasing=True,
        )
        assert report.total_count == 8
        assert report.incidents_decreasing is True

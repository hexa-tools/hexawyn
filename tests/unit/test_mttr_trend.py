"""RED → GREEN — Layer 1: MTTR Trend domain models."""

from hexawyn.domain.models.mttr_trend import (
    MTTRPerSeverity,
    MTTRTrendReport,
    SlowestIncident,
)


class TestMTTRPerSeverity:
    def test_is_frozen(self) -> None:
        import pytest

        m = MTTRPerSeverity(
            severity="P1", mttr_minutes=45.0, incident_count=3, meets_benchmark=False
        )
        with pytest.raises(Exception):
            m.mttr_minutes = 30.0  # type: ignore[misc]


class TestSlowestIncident:
    def test_is_frozen(self) -> None:
        import pytest

        s = SlowestIncident(
            incident_id="INC-001",
            service_name="svc",
            severity="P1",
            resolution_minutes=120,
            root_cause="OOM",
            month="2026-07",
        )
        with pytest.raises(Exception):
            s.resolution_minutes = 60  # type: ignore[misc]


class TestMTTRTrendReport:
    def test_defaults(self) -> None:
        report = MTTRTrendReport()
        assert report.trend == "stable"
        assert report.slowest_incidents == []

    def test_can_populate(self) -> None:
        report = MTTRTrendReport(
            trend="improving",
            recommendation="Response processes are effective",
        )
        assert report.trend == "improving"

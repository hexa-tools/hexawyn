"""RED → GREEN — Layer 1: Weekly Reliability Report domain models."""

from hexawyn.domain.models.weekly_reliability_report import (
    ServiceReliability,
    TopIncident,
    WeeklyReliabilityReport,
)


class TestServiceReliability:
    def test_is_frozen(self) -> None:
        import pytest

        svc = ServiceReliability(
            service_name="test",
            uptime_pct=99.9,
            error_rate=0.1,
            p99_latency_ms=100.0,
            slo_target=99.9,
            slo_status="pass",
            downtime_minutes=0,
            data_gap_minutes=0,
            created_mid_week=False,
        )
        with pytest.raises(Exception):
            svc.slo_status = "fail"  # type: ignore[misc]

    def test_all_fields_accessible(self) -> None:
        svc = ServiceReliability(
            service_name="payment-service",
            uptime_pct=99.92,
            error_rate=0.08,
            p99_latency_ms=245.0,
            slo_target=99.9,
            slo_status="pass",
            downtime_minutes=0,
            data_gap_minutes=0,
            created_mid_week=False,
        )
        assert svc.service_name == "payment-service"
        assert svc.slo_status == "pass"


class TestTopIncident:
    def test_is_frozen(self) -> None:
        import pytest

        inc = TopIncident(
            service_name="svc",
            timestamp="2026-01-01",
            duration_minutes=10,
            error_rate=2.0,
            impact_score=20.0,
            description="test",
        )
        with pytest.raises(Exception):
            inc.impact_score = 0.0  # type: ignore[misc]


class TestWeeklyReliabilityReport:
    def test_default_values(self) -> None:
        report = WeeklyReliabilityReport()
        assert report.services == []
        assert report.health_score == 0.0
        assert report.total_services == 0

    def test_can_populate_services_and_incidents(self) -> None:
        report = WeeklyReliabilityReport(
            health_score=75.0,
            slo_pass_count=3,
            slo_fail_count=1,
            total_services=4,
        )
        assert report.health_score == 75.0
        assert report.slo_pass_count == 3
        assert report.slo_fail_count == 1

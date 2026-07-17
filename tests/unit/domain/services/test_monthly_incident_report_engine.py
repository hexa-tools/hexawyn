"""RED → GREEN — Monthly Incident Report domain logic."""

from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
    MonthlyIncidentReportEngine,
    _as_bool,
    _as_int,
)


def _incident(
    incident_id: str = "INC-001",
    service_name: str = "payment-service",
    severity: str = "P1",
    downtime_minutes: int = 45,
    timestamp: str = "2026-07-15T10:00:00Z",
    resolved_at: str = "2026-07-15T10:45:00Z",
    is_planned_maintenance: bool = False,
    reopened: bool = False,
) -> dict[str, object]:
    return {
        "incident_id": incident_id,
        "service_name": service_name,
        "severity": severity,
        "downtime_minutes": downtime_minutes,
        "timestamp": timestamp,
        "resolved_at": resolved_at,
        "is_planned_maintenance": is_planned_maintenance,
        "reopened": reopened,
    }


class TestIncidentCount:
    def test_three_p1_five_p2_zero_p3(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(severity="P1", downtime_minutes=45),
            _incident(incident_id="INC-002", severity="P1", downtime_minutes=120),
            _incident(incident_id="INC-003", severity="P1", downtime_minutes=15),
            _incident(incident_id="INC-004", severity="P2", downtime_minutes=8),
            _incident(incident_id="INC-005", severity="P2", downtime_minutes=8),
            _incident(
                incident_id="INC-006", severity="P2", service_name="auth", downtime_minutes=8
            ),
            _incident(
                incident_id="INC-007", severity="P2", service_name="cart", downtime_minutes=8
            ),
            _incident(
                incident_id="INC-008", severity="P2", service_name="infra", downtime_minutes=8
            ),
        ]

        result = engine.compute(incidents)

        assert result.per_severity["P1"].count == 3
        assert result.per_severity["P2"].count == 5
        assert result.per_severity["P3"].count == 0
        assert result.total_count == 8

    def test_no_incidents_clean_report(self) -> None:
        engine = MonthlyIncidentReportEngine()

        result = engine.compute([])

        assert result.total_count == 0
        assert result.total_downtime_minutes == 0
        assert result.incidents_decreasing is False


class TestDowntimeCalculation:
    def test_total_downtime_per_severity(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(severity="P1", downtime_minutes=45),
            _incident(incident_id="INC-002", severity="P1", downtime_minutes=120),
            _incident(incident_id="INC-003", severity="P1", downtime_minutes=15),
            _incident(incident_id="INC-004", severity="P2", downtime_minutes=8),
            _incident(incident_id="INC-005", severity="P2", downtime_minutes=8),
        ]

        result = engine.compute(incidents)

        assert result.per_severity["P1"].downtime_minutes == 180
        assert result.per_severity["P2"].downtime_minutes == 16

    def test_under_one_minute_shown_as_less_than_one(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [_incident(downtime_minutes=0)]

        result = engine.compute(incidents)

        assert result.per_severity["P1"].downtime_minutes == 0

    def test_incident_spanning_midnight(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(
                timestamp="2026-07-15T23:30:00Z",
                resolved_at="2026-07-16T00:30:00Z",
                downtime_minutes=60,
            ),
        ]

        result = engine.compute(incidents)

        assert result.total_downtime_minutes == 60


class TestMostImpactedServices:
    def test_services_ranked_by_downtime(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(service_name="payment-service", downtime_minutes=120),
            _incident(incident_id="INC-002", service_name="auth-service", downtime_minutes=30),
            _incident(incident_id="INC-003", service_name="payment-service", downtime_minutes=45),
        ]

        result = engine.compute(incidents)

        assert result.most_impacted_services[0].service_name == "payment-service"
        assert result.most_impacted_services[0].total_downtime == 165
        assert result.most_impacted_services[1].service_name == "auth-service"


class TestEdgeCases:
    def test_overlapping_incidents_not_double_counted(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(service_name="payment-service", downtime_minutes=30),
            _incident(
                incident_id="INC-002",
                service_name="payment-service",
                downtime_minutes=30,
            ),
        ]

        result = engine.compute(incidents)

        assert result.total_downtime_minutes == 60
        assert result.most_impacted_services[0].total_downtime == 60

    def test_planned_maintenance_excluded(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(downtime_minutes=45),
            _incident(
                incident_id="INC-002",
                downtime_minutes=120,
                is_planned_maintenance=True,
            ),
        ]

        result = engine.compute(incidents)

        assert result.total_count == 1
        assert result.total_downtime_minutes == 45

    def test_reopened_incident_duration_includes_reopen(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(downtime_minutes=10),  # resolved
            _incident(incident_id="INC-001", downtime_minutes=15, reopened=True),
        ]

        result = engine.compute(incidents)

        assert result.total_downtime_minutes == 25

    def test_month_over_month_comparison(self) -> None:
        engine = MonthlyIncidentReportEngine()
        current = [_incident(downtime_minutes=45)]
        previous = [
            _incident(downtime_minutes=45),
            _incident(incident_id="INC-002", downtime_minutes=15),
        ]

        result = engine.compute(current, previous_incidents=previous)

        assert result.previous_month_total_count == 2
        assert result.incidents_decreasing is True

    def test_sub_minute_downtime_counted_as_one(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [_incident(downtime_minutes=1)]

        result = engine.compute(incidents)

        assert result.total_downtime_minutes == 1
        assert result.total_count == 1

    def test_unknown_severity_falls_back_to_p3(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [_incident(severity="P4", downtime_minutes=10)]

        result = engine.compute(incidents)

        assert result.per_severity["P3"].count == 1
        assert result.per_severity["P3"].downtime_minutes == 10


class TestHelperFunctions:
    def test_as_int_none_returns_zero(self) -> None:
        assert _as_int(None) == 0

    def test_as_int_list_returns_zero(self) -> None:
        assert _as_int([1, 2]) == 0

    def test_as_bool_none_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_non_empty_string_true(self) -> None:
        assert _as_bool("yes") is True

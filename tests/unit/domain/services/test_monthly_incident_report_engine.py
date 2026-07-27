"""RED → GREEN — Monthly Incident Report domain logic."""

from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
    MonthlyIncidentReportEngine,
    _as_bool,
    _as_int,
)


def _incident(  # noqa: PLR0913
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
                incident_id="INC-006",
                severity="P2",
                service_name="auth",
                downtime_minutes=8,
            ),
            _incident(
                incident_id="INC-007",
                severity="P2",
                service_name="cart",
                downtime_minutes=8,
            ),
            _incident(
                incident_id="INC-008",
                severity="P2",
                service_name="infra",
                downtime_minutes=8,
            ),
        ]

        result = engine.compute(incidents)

        assert result.per_severity["P1"].count == 3  # noqa: PLR2004
        assert result.per_severity["P2"].count == 5  # noqa: PLR2004
        assert result.per_severity["P3"].count == 0
        assert result.total_count == 8  # noqa: PLR2004

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

        assert result.per_severity["P1"].downtime_minutes == 180  # noqa: PLR2004
        assert result.per_severity["P2"].downtime_minutes == 16  # noqa: PLR2004

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

        assert result.total_downtime_minutes == 60  # noqa: PLR2004


class TestMostImpactedServices:
    def test_services_ranked_by_downtime(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(service_name="payment-service", downtime_minutes=120),
            _incident(incident_id="INC-002", service_name="auth-service", downtime_minutes=30),
            _incident(
                incident_id="INC-003",
                service_name="payment-service",
                downtime_minutes=45,
            ),
        ]

        result = engine.compute(incidents)

        assert result.most_impacted_services[0].service_name == "payment-service"
        assert result.most_impacted_services[0].total_downtime == 165  # noqa: PLR2004
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

        assert result.total_downtime_minutes == 60  # noqa: PLR2004
        assert result.most_impacted_services[0].total_downtime == 60  # noqa: PLR2004

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
        assert result.total_downtime_minutes == 45  # noqa: PLR2004

    def test_reopened_incident_duration_includes_reopen(self) -> None:
        engine = MonthlyIncidentReportEngine()
        incidents = [
            _incident(downtime_minutes=10),  # resolved
            _incident(incident_id="INC-001", downtime_minutes=15, reopened=True),
        ]

        result = engine.compute(incidents)

        assert result.total_downtime_minutes == 25  # noqa: PLR2004

    def test_month_over_month_comparison(self) -> None:
        engine = MonthlyIncidentReportEngine()
        current = [_incident(downtime_minutes=45)]
        previous = [
            _incident(downtime_minutes=45),
            _incident(incident_id="INC-002", downtime_minutes=15),
        ]

        result = engine.compute(current, previous_incidents=previous)

        assert result.previous_month_total_count == 2  # noqa: PLR2004
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
        assert result.per_severity["P3"].downtime_minutes == 10  # noqa: PLR2004


class TestHelperFunctions:
    def test_as_int_none_returns_zero(self) -> None:
        assert _as_int(None) == 0

    def test_as_int_list_returns_zero(self) -> None:
        assert _as_int([1, 2]) == 0

    def test_as_bool_none_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_non_empty_string_true(self) -> None:
        assert _as_bool("yes") is True


class TestAggregateIncidents:
    def test_aggregate_incidents_empty(self) -> None:
        from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
            aggregate_incidents,
        )

        result = aggregate_incidents([])
        assert result["total_count"] == 0

    def test_aggregate_incidents_skips_planned_maintenance(self) -> None:
        from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
            aggregate_incidents,
        )

        incidents: list[dict[str, object]] = [
            _incident(severity="P1", downtime_minutes=45, is_planned_maintenance=True),
            _incident(incident_id="INC-002", severity="P1", downtime_minutes=30),
        ]
        result = aggregate_incidents(incidents)
        assert result["total_downtime_minutes"] == 30  # noqa: PLR2004

    def test_aggregate_incidents_skips_reopened(self) -> None:
        from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
            aggregate_incidents,
        )

        incidents: list[dict[str, object]] = [
            _incident(severity="P1", downtime_minutes=45, reopened=True),
            _incident(incident_id="INC-002", severity="P2", downtime_minutes=15),
        ]
        result = aggregate_incidents(incidents)
        assert result["total_downtime_minutes"] == 15  # noqa: PLR2004

    def test_aggregate_incidents_unknown_severity_fallback(self) -> None:
        from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
            aggregate_incidents,
        )

        incidents: list[dict[str, object]] = [
            _incident(severity="P5", downtime_minutes=10),
        ]
        result = aggregate_incidents(incidents)
        assert result["per_severity"]["P3"]["count"] == 1

    def test_aggregate_incidents_month_extracted(self) -> None:
        from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
            aggregate_incidents,
        )

        incidents: list[dict[str, object]] = [
            _incident(timestamp="2026-07-15T10:00:00Z", downtime_minutes=20),
        ]
        result = aggregate_incidents(incidents)
        assert result["month"] == "2026-07"


class TestPreviousMonthName:
    def test_previous_month_name_january(self) -> None:
        from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
            previous_month_name,
        )

        assert previous_month_name("2026-01") == "2025-12"

    def test_previous_month_name_july(self) -> None:
        from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
            previous_month_name,
        )

        assert previous_month_name("2026-07") == "2026-06"

    def test_default_month_str(self) -> None:
        from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
            default_month_str,
        )

        result = default_month_str()
        assert "-" in result
        assert len(result) == 7  # noqa: PLR2004

"""RED → GREEN — Monthly Incident Report domain logic."""

from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
    MonthlyIncidentReportEngine,
    _as_bool,
    _as_int,
    _process_incidents,
    _rank_impacted_services,
    aggregate_incidents,
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
        assert result.previous_month_downtime_minutes == 60  # noqa: PLR2004
        assert result.incidents_decreasing is True

    def test_compute_report_field_values(self) -> None:
        # asserte severity + counts retournes (kills severity=None / field=None)
        engine = MonthlyIncidentReportEngine()
        current = [
            _incident(downtime_minutes=45),
            _incident(
                incident_id="INC-002", service_name="api", severity="P2", downtime_minutes=15
            ),
        ]
        result = engine.compute(current, previous_incidents=[_incident(downtime_minutes=60)])
        assert result.per_severity["P1"].severity == "P1"
        assert result.per_severity["P1"].count == 1  # noqa: PLR2004
        assert result.per_severity["P2"].severity == "P2"
        assert result.per_severity["P2"].downtime_minutes == 15  # noqa: PLR2004
        assert result.total_count == 2  # noqa: PLR2004
        assert result.total_downtime_minutes == 60  # noqa: PLR2004
        assert result.previous_month_total_count == 1  # noqa: PLR2004
        assert result.previous_month_downtime_minutes == 60  # noqa: PLR2004
        assert result.incidents_decreasing is False

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


class TestAggregateExact:
    def test_aggregate_full_fields(self) -> None:
        # 2 P1 svc-a, 1 P2 svc-b, 1 P3 svc-c ; maintenance et reopened exclus du downtime
        incidents = [
            {
                "severity": "P1",
                "service_name": "svc-a",
                "downtime_minutes": 30,
                "timestamp": "2026-07-15T10:00:00Z",
            },
            {
                "severity": "P1",
                "service_name": "svc-a",
                "downtime_minutes": 10,
                "timestamp": "2026-07-16T10:00:00Z",
            },
            {
                "severity": "P2",
                "service_name": "svc-b",
                "downtime_minutes": 5,
                "timestamp": "2026-07-17T10:00:00Z",
            },
            {
                "severity": "P3",
                "service_name": "svc-c",
                "downtime_minutes": 1,
                "timestamp": "2026-07-18T10:00:00Z",
            },
            {
                "severity": "P1",
                "service_name": "maint",
                "downtime_minutes": 999,
                "timestamp": "2026-07-19T10:00:00Z",
                "is_planned_maintenance": True,
            },
            {
                "severity": "P1",
                "service_name": "reop",
                "downtime_minutes": 999,
                "timestamp": "2026-07-20T10:00:00Z",
                "reopened": True,
            },
        ]
        result = aggregate_incidents(incidents)
        assert result["month"] == "2026-07"
        assert result["total_count"] == 6  # noqa: PLR2004
        assert result["total_downtime_minutes"] == 46  # noqa: PLR2004
        assert result["per_severity"]["P1"] == {"count": 2, "downtime_minutes": 40}  # noqa: PLR2004
        assert result["per_severity"]["P2"] == {"count": 1, "downtime_minutes": 5}  # noqa: PLR2004
        assert result["per_severity"]["P3"] == {"count": 1, "downtime_minutes": 1}  # noqa: PLR2004
        impacted = result["most_impacted_services"]
        assert [(s.service_name, s.total_downtime, s.incident_count) for s in impacted] == [
            ("svc-a", 40, 2),
            ("svc-b", 5, 1),
            ("svc-c", 1, 1),
        ]

    def test_aggregate_empty_no_month(self) -> None:
        result = aggregate_incidents([])
        assert result["month"] == ""
        assert result["total_count"] == 0  # noqa: PLR2004
        assert result["total_downtime_minutes"] == 0  # noqa: PLR2004
        assert result["most_impacted_services"] == []


class TestRankImpactedServicesDirect:
    def test_multi_incident_same_service_counts(self) -> None:
        # 2 incidents svc-a -> count 2 ; mutant +=1 -> =1/ +=2 detectes
        incidents = [
            {"service_name": "svc-a", "downtime_minutes": 30},
            {"service_name": "svc-a", "downtime_minutes": 10},
            {"service_name": "svc-b", "downtime_minutes": 5},
        ]
        result = _rank_impacted_services(incidents)
        by_name = {s.service_name: s for s in result}
        assert by_name["svc-a"].incident_count == 2  # noqa: PLR2004
        assert by_name["svc-a"].total_downtime == 40  # noqa: PLR2004
        assert by_name["svc-b"].incident_count == 1  # noqa: PLR2004
        assert [s.service_name for s in result] == ["svc-a", "svc-b"]

    def test_planned_maintenance_skipped_then_normal(self) -> None:
        # maintenance en 1er puis normal : si break, le normal serait perdu
        incidents = [
            {"service_name": "maint", "downtime_minutes": 999, "is_planned_maintenance": True},
            {"service_name": "svc-a", "downtime_minutes": 10},
        ]
        result = _rank_impacted_services(incidents)
        assert [s.service_name for s in result] == ["svc-a"]
        assert result[0].incident_count == 1  # noqa: PLR2004

    def test_missing_service_name_default_empty(self) -> None:
        # incidents sans cle service_name -> "" (kills get(...,None)/XXXX)
        incidents = [{"downtime_minutes": 10}, {"downtime_minutes": 5}]
        result = _rank_impacted_services(incidents)
        assert result[0].service_name == ""
        assert result[0].total_downtime == 15  # noqa: PLR2004


class TestProcessIncidentsDirect:
    def test_planned_maintenance_then_normal_continue(self) -> None:
        # maintenance exclue puis normal : si break, le normal serait perdu
        incidents = [
            {"severity": "P1", "downtime_minutes": 999, "is_planned_maintenance": True},
            {"severity": "P2", "downtime_minutes": 5},
        ]
        total, downtime, sev_map = _process_incidents(incidents)
        assert total == 1
        assert downtime == 5  # noqa: PLR2004
        assert sev_map["P2"]["count"] == 1  # noqa: PLR2004

    def test_missing_severity_defaults_p3(self) -> None:
        # incident sans severity -> P3 (kills get(...,None)/XX)
        incidents = [{"downtime_minutes": 10}]
        total, downtime, sev_map = _process_incidents(incidents)
        assert total == 1
        assert sev_map["P3"]["count"] == 1  # noqa: PLR2004
        assert sev_map["P3"]["downtime"] == 10  # noqa: PLR2004


class TestAggregateDefaults:
    def test_aggregate_missing_keys_defaults(self) -> None:
        # incident sans severity/service_name/timestamp -> defauts P3/unknown/''
        # (kills get(...,None)/XX/p3 pour severity et service_name)
        result = aggregate_incidents([{"downtime_minutes": 10}])
        assert result["month"] == ""
        assert result["total_count"] == 1  # noqa: PLR2004
        assert result["per_severity"]["P3"] == {"count": 1, "downtime_minutes": 10}  # noqa: PLR2004
        impacted = result["most_impacted_services"]
        assert impacted[0].service_name == "unknown"
        assert impacted[0].total_downtime == 10  # noqa: PLR2004

    def test_aggregate_short_timestamp_kept(self) -> None:
        # timestamp '2026-07' -> [:7] garde tel quel
        result = aggregate_incidents(
            [{"severity": "P1", "service_name": "a", "downtime_minutes": 5, "timestamp": "2026-07"}]
        )
        assert result["month"] == "2026-07"

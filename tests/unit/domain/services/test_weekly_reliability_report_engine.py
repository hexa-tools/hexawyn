"""RED → GREEN — Weekly Reliability Report domain logic."""

from hexawyn.domain.models.weekly_reliability_report import (
    ServiceReliability,
    TopIncident,
)
from hexawyn.domain.services.reliability_report.weekly_reliability_report_engine import (
    WeeklyReliabilityReportEngine,
    _as_bool,
    _as_float,
    _as_int,
)


def _service(  # noqa: PLR0913
    name: str = "payment-service",
    uptime_pct: float = 99.92,
    error_rate: float = 0.08,
    p99_latency_ms: float = 245.0,
    slo_target: float = 99.9,
    downtime_minutes: int = 0,
    data_gap_minutes: int = 0,
    created_mid_week: bool = False,
) -> dict[str, object]:
    return {
        "service_name": name,
        "uptime_pct": uptime_pct,
        "error_rate": error_rate,
        "p99_latency_ms": p99_latency_ms,
        "slo_target": slo_target,
        "downtime_minutes": downtime_minutes,
        "data_gap_minutes": data_gap_minutes,
        "created_mid_week": created_mid_week,
    }


def _incident(
    service_name: str = "auth-service",
    timestamp: str = "2026-06-13T14:30:00Z",
    duration_minutes: int = 18,
    error_rate: float = 2.0,
    description: str = "503 errors",
) -> dict[str, object]:
    return {
        "service_name": service_name,
        "timestamp": timestamp,
        "duration_minutes": duration_minutes,
        "error_rate": error_rate,
        "description": description,
    }


class TestSLOEvaluation:
    def test_slo_pass_when_uptime_above_target(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [_service(uptime_pct=99.92, slo_target=99.9)]

        result = engine.compute(services, [])

        assert result.services[0].slo_status == "pass"
        assert result.slo_pass_count == 1
        assert result.slo_fail_count == 0

    def test_slo_fail_when_uptime_below_target(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [_service(uptime_pct=99.72, slo_target=99.9)]

        result = engine.compute(services, [])

        assert result.services[0].slo_status == "fail"
        assert result.slo_pass_count == 0
        assert result.slo_fail_count == 1

    def test_two_services_one_fails(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [
            _service(name="payment-service", uptime_pct=99.92, slo_target=99.9),
            _service(name="auth-service", uptime_pct=99.72, slo_target=99.9),
        ]

        result = engine.compute(services, [])

        assert result.slo_pass_count == 1
        assert result.slo_fail_count == 1
        assert result.total_services == 2  # noqa: PLR2004
        assert result.services[0].slo_status == "pass"
        assert result.services[1].slo_status == "fail"


class TestIncidentRanking:
    def test_top_three_incidents_by_impact(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        incidents = [
            _incident(duration_minutes=18, error_rate=2.0),  # impact = 36
            _incident(
                service_name="payment",
                duration_minutes=5,
                error_rate=8.0,
                description="spike",
            ),  # impact = 40
            _incident(
                service_name="cart",
                duration_minutes=10,
                error_rate=1.0,
                description="slow",
            ),  # impact = 10
        ]

        result = engine.compute([], incidents)

        assert len(result.top_incidents) == 3  # noqa: PLR2004
        assert result.top_incidents[0].service_name == "payment"
        assert result.top_incidents[0].impact_score == 40.0  # noqa: PLR2004
        assert result.top_incidents[1].service_name == "auth-service"
        assert result.top_incidents[1].impact_score == 36.0  # noqa: PLR2004
        assert result.top_incidents[2].service_name == "cart"

    def test_worst_error_spike_selected_as_incident(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        incidents = [
            _incident(error_rate=2.0, duration_minutes=10, description="spike-1"),
            _incident(error_rate=8.0, duration_minutes=2, description="spike-2"),
            _incident(error_rate=1.0, duration_minutes=30, description="spike-3"),
        ]

        result = engine.compute([], incidents)

        assert result.top_incidents[0].impact_score == 30.0  # noqa: PLR2004
        assert result.top_incidents[0].description == "spike-3"

    def test_more_than_three_incidents_keeps_total_count(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        incidents = [
            _incident(duration_minutes=i + 1, error_rate=1.0, service_name=f"svc-{i}")
            for i in range(7)
        ]

        result = engine.compute([], incidents)

        assert len(result.top_incidents) == 3  # noqa: PLR2004
        assert result.total_incident_count == 7  # noqa: PLR2004

    def test_no_incidents_empty_list(self) -> None:
        engine = WeeklyReliabilityReportEngine()

        result = engine.compute([], [])

        assert result.top_incidents == []
        assert result.total_incident_count == 0


class TestHealthScore:
    def test_all_slo_pass_health_100(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [
            _service(name="a", uptime_pct=99.95, slo_target=99.9),
            _service(name="b", uptime_pct=99.99, slo_target=99.9),
        ]

        result = engine.compute(services, [])

        assert result.health_score == 100.0  # noqa: PLR2004
        assert result.slo_pass_count == 2  # noqa: PLR2004

    def test_half_fail_health_50(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [
            _service(name="a", uptime_pct=99.95, slo_target=99.9),
            _service(name="b", uptime_pct=99.72, slo_target=99.9),
        ]

        result = engine.compute(services, [])

        assert result.health_score == 50.0  # noqa: PLR2004

    def test_empty_services_health_zero(self) -> None:
        engine = WeeklyReliabilityReportEngine()

        result = engine.compute([], [])

        assert result.health_score == 0.0
        assert result.total_services == 0


class TestEdgeCases:
    def test_service_created_mid_week_noted(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [_service(created_mid_week=True)]

        result = engine.compute(services, [])

        assert result.services[0].created_mid_week is True

    def test_data_gap_marked_as_unavailable(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [_service(data_gap_minutes=30)]

        result = engine.compute(services, [])

        assert result.services[0].data_gap_minutes == 30  # noqa: PLR2004

    def test_service_with_p99_regression_slo_still_evaluated(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [_service(uptime_pct=99.95, slo_target=99.9, p99_latency_ms=950.0)]

        result = engine.compute(services, [])

        assert result.services[0].slo_status == "pass"
        assert result.services[0].p99_latency_ms == 950.0  # noqa: PLR2004

    def test_mixed_slo_targets_evaluated_individually(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [
            _service(name="a", uptime_pct=99.95, slo_target=99.99),
            _service(name="b", uptime_pct=99.5, slo_target=99.0),
        ]

        result = engine.compute(services, [])

        assert result.services[0].slo_status == "fail"
        assert result.services[1].slo_status == "pass"


class TestHelperFunctions:
    def test_as_float_none_returns_zero(self) -> None:
        assert _as_float(None) == 0.0

    def test_as_float_list_returns_zero(self) -> None:
        assert _as_float([1, 2]) == 0.0

    def test_as_int_none_returns_zero(self) -> None:
        assert _as_int(None) == 0

    def test_as_int_list_returns_zero(self) -> None:
        assert _as_int([1, 2]) == 0

    def test_as_bool_none_returns_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_non_empty_string_true(self) -> None:
        assert _as_bool("yes") is True


def _exact_service() -> ServiceReliability:
    return ServiceReliability(
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


def _exact_incident() -> TopIncident:
    return TopIncident(
        service_name="auth-service",
        timestamp="2026-06-13T14:30:00Z",
        duration_minutes=18,
        error_rate=2.0,
        impact_score=36.0,
        description="503 errors",
    )


class TestServiceReliabilityEquality:
    def test_service_equality_full_dataclass(self) -> None:
        engine = WeeklyReliabilityReportEngine()

        result = engine.compute([_service()], [])

        assert result.services == [_exact_service()]

    def test_missing_keys_use_defaults(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        raw: dict[str, object] = {}

        result = engine.compute([raw], [])

        assert result.services == [
            ServiceReliability(
                service_name="",
                uptime_pct=0.0,
                error_rate=0.0,
                p99_latency_ms=0.0,
                slo_target=0.0,
                slo_status="pass",
                downtime_minutes=0,
                data_gap_minutes=0,
                created_mid_week=False,
            )
        ]

    def test_uptime_equal_to_target_is_pass(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [_service(uptime_pct=99.9, slo_target=99.9)]

        result = engine.compute(services, [])

        assert result.services[0].slo_status == "pass"


class TestIncidentEquality:
    def test_ranked_incident_full_equality(self) -> None:
        engine = WeeklyReliabilityReportEngine()

        result = engine.compute([], [_incident()])

        assert result.top_incidents == [_exact_incident()]

    def test_incident_missing_keys_use_defaults(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        raw: dict[str, object] = {"service_name": "svc"}

        result = engine.compute([], [raw])

        assert result.top_incidents == [
            TopIncident(
                service_name="svc",
                timestamp="",
                duration_minutes=0,
                error_rate=0.0,
                impact_score=0.0,
                description="",
            )
        ]

    def test_impact_rounded_to_two_decimals(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        incidents = [_incident(duration_minutes=3, error_rate=0.123, description="tiny")]

        result = engine.compute([], incidents)

        assert result.top_incidents[0].impact_score == 0.37  # noqa: PLR2004


class TestHealthScoreFraction:
    def test_one_of_three_pass_health_rounded_to_one_decimal(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [
            _service(name="a", uptime_pct=99.95, slo_target=99.9),
            _service(name="b", uptime_pct=99.72, slo_target=99.9),
            _service(name="c", uptime_pct=99.72, slo_target=99.9),
        ]

        result = engine.compute(services, [])

        assert result.health_score == 33.3  # noqa: PLR2004
        assert result.slo_pass_count == 1
        assert result.slo_fail_count == 2  # noqa: PLR2004

    def test_single_service_health_uses_length_guard(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [_service(uptime_pct=99.95, slo_target=99.9)]

        result = engine.compute(services, [])

        assert result.health_score == 100.0  # noqa: PLR2004


class TestReportPeriodFields:
    def test_period_fields_empty_by_default(self) -> None:
        engine = WeeklyReliabilityReportEngine()

        result = engine.compute([], [])

        assert result.report_period_start == ""
        assert result.report_period_end == ""


class TestRankedOrdering:
    def test_full_ranked_order_equality(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        incidents = [
            _incident(service_name="low", duration_minutes=10, error_rate=1.0, description="d-low"),
            _incident(
                service_name="high", duration_minutes=20, error_rate=3.0, description="d-high"
            ),
            _incident(service_name="mid", duration_minutes=15, error_rate=2.0, description="d-mid"),
        ]

        result = engine.compute([], incidents)

        assert result.top_incidents == [
            TopIncident("high", "2026-06-13T14:30:00Z", 20, 3.0, 60.0, "d-high"),
            TopIncident("mid", "2026-06-13T14:30:00Z", 15, 2.0, 30.0, "d-mid"),
            TopIncident("low", "2026-06-13T14:30:00Z", 10, 1.0, 10.0, "d-low"),
        ]


class TestServiceDowntimeValue:
    def test_non_zero_downtime_forwarded_exactly(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        services = [_service(downtime_minutes=35, data_gap_minutes=20)]

        result = engine.compute(services, [])

        assert result.services == [
            ServiceReliability(
                service_name="payment-service",
                uptime_pct=99.92,
                error_rate=0.08,
                p99_latency_ms=245.0,
                slo_target=99.9,
                slo_status="pass",
                downtime_minutes=35,
                data_gap_minutes=20,
                created_mid_week=False,
            )
        ]


class TestIncidentMissingServiceName:
    def test_missing_service_name_defaults_to_empty(self) -> None:
        engine = WeeklyReliabilityReportEngine()
        raw: dict[str, object] = {
            "duration_minutes": 10,
            "error_rate": 2.0,
            "description": "orphan incident",
        }

        result = engine.compute([], [raw])

        assert result.top_incidents == [
            TopIncident(
                service_name="",
                timestamp="",
                duration_minutes=10,
                error_rate=2.0,
                impact_score=20.0,
                description="orphan incident",
            )
        ]

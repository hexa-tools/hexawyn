"""RED → GREEN — Weekly Reliability Report domain logic."""

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

"""RED → GREEN — MTTR Trend domain logic."""

from hexawyn.domain.services.mttr_trend.mttr_trend_engine import (
    MTTRTrendEngine,
    _as_bool,
    _as_int,
)


def _incident(  # noqa: PLR0913
    incident_id: str = "INC-001",
    service_name: str = "payment-service",
    severity: str = "P1",
    resolution_minutes: int = 45,
    resolved: bool = True,
    root_cause: str = "OOMKilled",
) -> dict[str, object]:
    return {
        "incident_id": incident_id,
        "service_name": service_name,
        "severity": severity,
        "resolution_minutes": resolution_minutes,
        "resolved": resolved,
        "root_cause": root_cause,
    }


class TestMTTRCalculation:
    def test_mttr_per_month_per_severity(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                _incident(severity="P1", resolution_minutes=45),
                _incident(incident_id="INC-002", severity="P1", resolution_minutes=60),
                _incident(incident_id="INC-003", severity="P1", resolution_minutes=30),
                _incident(incident_id="INC-004", severity="P2", resolution_minutes=120),
            ],
            "2026-06": [
                _incident(severity="P1", resolution_minutes=32),
                _incident(incident_id="INC-005", severity="P1", resolution_minutes=32),
                _incident(incident_id="INC-006", severity="P2", resolution_minutes=110),
            ],
            "2026-07": [
                _incident(severity="P1", resolution_minutes=18),
            ],
        }

        result = engine.compute(months)

        assert result.per_month["2026-05"]["P1"].mttr_minutes == 45.0  # noqa: PLR2004
        assert result.per_month["2026-06"]["P1"].mttr_minutes == 32.0  # noqa: PLR2004
        assert result.per_month["2026-07"]["P1"].mttr_minutes == 18.0  # noqa: PLR2004

    def test_mttr_improving_trend(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [_incident(resolution_minutes=45)],
            "2026-06": [_incident(incident_id="INC-002", resolution_minutes=32)],
            "2026-07": [_incident(incident_id="INC-003", resolution_minutes=18)],
        }

        result = engine.compute(months)

        assert result.trend == "improving"

    def test_mttr_degrading_trend(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [_incident(resolution_minutes=20)],
            "2026-06": [_incident(incident_id="INC-002", resolution_minutes=45)],
            "2026-07": [_incident(incident_id="INC-003", resolution_minutes=90)],
        }

        result = engine.compute(months)

        assert result.trend == "degrading"

    def test_stable_trend(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [_incident(resolution_minutes=30)],
            "2026-06": [_incident(incident_id="INC-002", resolution_minutes=30)],
            "2026-07": [_incident(incident_id="INC-003", resolution_minutes=30)],
        }

        result = engine.compute(months)

        assert result.trend == "stable"

    def test_no_p1_incidents_mttr_na(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P1"].mttr_minutes is None

    def test_single_incident_mttr_equals_resolution(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [_incident(resolution_minutes=72)],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P1"].mttr_minutes == 72.0  # noqa: PLR2004


class TestSlowestIncidents:
    def test_top_three_slowest_ranked(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                _incident(resolution_minutes=120, root_cause="db-deadlock", service_name="payment"),
                _incident(
                    incident_id="INC-002",
                    resolution_minutes=90,
                    root_cause="mem-leak",
                    service_name="auth",
                ),
                _incident(
                    incident_id="INC-003",
                    resolution_minutes=60,
                    root_cause="dns-timeout",
                    service_name="cart",
                ),
                _incident(
                    incident_id="INC-004",
                    resolution_minutes=30,
                    root_cause="quick-fix",
                    service_name="infra",
                ),
            ],
        }

        result = engine.compute(months)

        assert len(result.slowest_incidents) == 3  # noqa: PLR2004
        assert result.slowest_incidents[0].resolution_minutes == 120  # noqa: PLR2004
        assert result.slowest_incidents[2].resolution_minutes == 60  # noqa: PLR2004


class TestEdgeCases:
    def test_unresolved_incident_excluded(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [
                _incident(resolution_minutes=30),
                _incident(incident_id="INC-002", resolved=False, resolution_minutes=0),
            ],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P1"].mttr_minutes == 30.0  # noqa: PLR2004

    def test_benchmark_p1_under_30min_pass(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [_incident(resolution_minutes=25)],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P1"].mttr_minutes == 25.0  # noqa: PLR2004
        assert result.per_month["2026-07"]["P1"].meets_benchmark is True

    def test_benchmark_p2_under_120min_fail(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [_incident(severity="P2", resolution_minutes=150)],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P2"].meets_benchmark is False


class TestHelperFunctions:
    def test_as_int_none_returns_zero(self) -> None:
        assert _as_int(None) == 0

    def test_as_int_list_returns_zero(self) -> None:
        assert _as_int([1, 2]) == 0

    def test_as_bool_none_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_non_empty_string_true(self) -> None:
        assert _as_bool("yes") is True

    def test_first_month_zero_mttr_returns_stable(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [_incident(resolution_minutes=0)],
            "2026-06": [_incident(incident_id="INC-002", resolution_minutes=10)],
        }

        result = engine.compute(months)

        assert result.trend == "stable"

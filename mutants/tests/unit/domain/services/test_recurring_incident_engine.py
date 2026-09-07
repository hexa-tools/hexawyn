"""RED → GREEN — Recurring Incident Pattern domain logic."""

from hexawyn.domain.services.recurring_incident.recurring_incident_engine import (
    RecurringIncidentEngine,
    _as_float,
)


def _incident(
    incident_id: str = "INC-001",
    service_name: str = "payment-service",
    root_cause: str = "DB connection pool exhausted",
    duration_minutes: int = 20,
    timestamp: str = "2026-07-01T10:00:00Z",
) -> dict[str, object]:
    return {
        "incident_id": incident_id,
        "service_name": service_name,
        "root_cause": root_cause,
        "duration_minutes": duration_minutes,
        "timestamp": timestamp,
    }


class TestIncidentRanking:
    def test_services_ranked_by_incident_count(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(service_name="payment-service"),
            _incident(incident_id="INC-002", service_name="payment-service"),
            _incident(incident_id="INC-003", service_name="payment-service"),
            _incident(incident_id="INC-004", service_name="auth-service"),
            _incident(incident_id="INC-005", service_name="auth-service"),
            _incident(incident_id="INC-006", service_name="checkout-service", duration_minutes=240),
        ]

        result = engine.compute(incidents)

        assert result.services[0].service_name == "payment-service"
        assert result.services[0].incident_count == 3  # noqa: PLR2004
        assert result.services[1].service_name == "auth-service"
        assert result.services[1].incident_count == 2  # noqa: PLR2004

    def test_top_10_limit(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [_incident(service_name=f"svc-{i}", incident_id=f"INC-{i}") for i in range(15)]

        result = engine.compute(incidents)

        assert len(result.services) == 10  # noqa: PLR2004

    def test_average_duration_computed(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(duration_minutes=20),
            _incident(incident_id="INC-002", duration_minutes=30),
            _incident(incident_id="INC-003", duration_minutes=10),
        ]

        result = engine.compute(incidents)

        assert result.services[0].avg_duration_minutes == 20.0  # noqa: PLR2004

    def test_service_with_one_long_incident_high_avg(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(service_name="checkout-service", duration_minutes=240),
        ]

        result = engine.compute(incidents)

        assert result.services[0].avg_duration_minutes == 240.0  # noqa: PLR2004
        assert result.services[0].incident_count == 1


class TestRecurringPattern:
    def test_same_root_cause_more_than_3_times_flagged(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(root_cause="DB connection pool exhausted"),
            _incident(incident_id="INC-002", root_cause="DB connection pool exhausted"),
            _incident(incident_id="INC-003", root_cause="DB connection pool exhausted"),
            _incident(incident_id="INC-004", root_cause="DB connection pool exhausted"),
        ]

        result = engine.compute(incidents)

        assert result.services[0].is_recurring is True
        assert result.services[0].most_common_cause == "DB connection pool exhausted"
        assert result.services[0].recurrence_count == 4  # noqa: PLR2004

    def test_same_cause_but_only_twice_not_flagged(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(root_cause="DB connection pool exhausted"),
            _incident(incident_id="INC-002", root_cause="DB connection pool exhausted"),
        ]

        result = engine.compute(incidents)

        assert result.services[0].is_recurring is False

    def test_multiple_services_same_incident_counted_individually(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(service_name="payment"),
            _incident(incident_id="INC-002", service_name="auth"),
            _incident(incident_id="INC-003", service_name="cart"),
        ]

        result = engine.compute(incidents)

        assert len(result.services) == 3  # noqa: PLR2004
        assert result.services[0].incident_count == 1


class TestInvestmentRecommendation:
    def test_recurring_same_cause_suggests_code_quality(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(root_cause="null pointer exception"),
            _incident(incident_id="INC-002", root_cause="null pointer exception"),
            _incident(incident_id="INC-003", root_cause="null pointer exception"),
            _incident(incident_id="INC-004", root_cause="null pointer exception"),
        ]

        result = engine.compute(incidents)

        assert "code quality" in result.services[0].recommendation.lower()

    def test_high_incident_count_suggests_reliability(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(root_cause="oom"),
            _incident(incident_id="INC-002", root_cause="db-deadlock"),
            _incident(incident_id="INC-003", root_cause="network-timeout"),
            _incident(incident_id="INC-004", root_cause="disk-full"),
            _incident(incident_id="INC-005", root_cause="config-error"),
        ]

        result = engine.compute(incidents)

        assert "reliability" in result.services[0].recommendation.lower()

    def test_decommissioned_service_still_counted(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(service_name="old-service"),
        ]

        result = engine.compute(incidents)

        assert result.services[0].service_name == "old-service"
        assert result.services[0].incident_count == 1


class TestEdgeCases:
    def test_empty_incidents_returns_empty(self) -> None:
        engine = RecurringIncidentEngine()

        result = engine.compute([])

        assert result.services == []

    def test_uncategorized_root_cause_shown(self) -> None:
        engine = RecurringIncidentEngine()
        incidents = [
            _incident(root_cause=""),
        ]

        result = engine.compute(incidents)

        assert result.services[0].most_common_cause == "uncategorized"


class TestHelperFunctions:
    def test_as_float_none_returns_zero(self) -> None:
        assert _as_float(None) == 0.0

    def test_as_float_list_returns_zero(self) -> None:
        assert _as_float([1, 2, 3]) == 0.0

    def test_as_float_string_returns_zero(self) -> None:
        assert _as_float("not-a-number") == 0.0

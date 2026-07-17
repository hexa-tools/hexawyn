"""RED → GREEN — Layer 1: Recurring Incident domain models."""

from hexawyn.domain.models.recurring_incident import (
    RecurringIncidentReport,
    ServiceIncidentSummary,
)


class TestServiceIncidentSummary:
    def test_is_frozen(self) -> None:
        import pytest

        s = ServiceIncidentSummary(
            service_name="svc",
            incident_count=5,
            avg_duration_minutes=20.0,
            most_common_cause="OOM",
            recurrence_count=4,
            is_recurring=True,
            recommendation="Fix it",
        )
        with pytest.raises(Exception):
            s.incident_count = 3  # type: ignore[misc]


class TestRecurringIncidentReport:
    def test_defaults(self) -> None:
        report = RecurringIncidentReport()
        assert report.services == []

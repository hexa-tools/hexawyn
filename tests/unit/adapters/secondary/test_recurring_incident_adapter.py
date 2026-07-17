"""RED → GREEN — RecurringIncidentAdapter unit tests."""

from hexawyn.adapters.secondary.gitops.recurring_incident_adapter import (
    RecurringIncidentAdapter,
)
from hexawyn.application.ports.driven.recurring_incident_port import (
    RecurringIncidentPort,
)


class TestRecurringIncidentAdapter:
    def test_implements_port(self) -> None:
        adapter = RecurringIncidentAdapter()
        assert isinstance(adapter, RecurringIncidentPort)

    def test_fetch_incidents_returns_empty(self) -> None:
        adapter = RecurringIncidentAdapter()
        result = adapter.fetch_incidents(30)
        assert result == []

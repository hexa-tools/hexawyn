"""RED → GREEN — MonthlyIncidentAdapter unit tests."""

from hexawyn.adapters.secondary.gitops.monthly_incident_adapter import (
    MonthlyIncidentAdapter,
)
from hexawyn.application.ports.driven.monthly_incident_port import MonthlyIncidentPort


class TestMonthlyIncidentAdapter:
    def test_implements_port(self) -> None:
        adapter = MonthlyIncidentAdapter()
        assert isinstance(adapter, MonthlyIncidentPort)

    def test_fetch_incidents_returns_empty(self) -> None:
        adapter = MonthlyIncidentAdapter()
        result = adapter.fetch_incidents("2026-07")
        assert result == []

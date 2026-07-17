from __future__ import annotations

from hexawyn.application.ports.driven.incident_cost_port import (
    IncidentCostData,
    IncidentCostPort,
)


class _FakeSource:
    def __init__(self, data: IncidentCostData) -> None:
        self._data = data

    def fetch_incident_cost_data(self, incident_ref: str) -> IncidentCostData:
        return self._data


def _data() -> IncidentCostData:
    return IncidentCostData(
        business_service_name="Service Paiement",
        downtime_minutes=27,
        impacted_service_count=3,
        resolved_at="14h23",
        sla_breached=False,
        business_config={
            "revenue_per_minute": 500.0,
            "support_cost_per_hour": None,
            "sla_penalty_per_hour": None,
        },
    )


class TestPortImplementation:
    def test_is_an_incident_cost_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.incident_cost_adapter import (
            IncidentCostAdapter,
        )

        assert isinstance(IncidentCostAdapter(source=_FakeSource(_data())), IncidentCostPort)


class TestDelegation:
    def test_get_incident_cost_data_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.incident_cost_adapter import (
            IncidentCostAdapter,
        )

        adapter = IncidentCostAdapter(source=_FakeSource(_data()))

        result = adapter.get_incident_cost_data("yesterday")

        assert result["business_service_name"] == "Service Paiement"
        assert result["business_config"]["revenue_per_minute"] == 500.0

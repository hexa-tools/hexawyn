from hexawyn.application.ports.driven.engineer_workload_port import (
    EngineerWorkloadPort,
    MonthNightData,
)


class _FakeSource:
    def fetch_night_intervention_data(self, history_months: int) -> list[MonthNightData]:
        return [MonthNightData(month="2026-06", night_intervention_count=5, total_nights=30)]


class TestPortImplementation:
    def test_is_engineer_workload_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.night_intervention_adapter import (
            NightInterventionAdapter,
        )

        assert isinstance(NightInterventionAdapter(source=_FakeSource()), EngineerWorkloadPort)

    def test_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.night_intervention_adapter import (
            NightInterventionAdapter,
        )

        adapter = NightInterventionAdapter(source=_FakeSource())
        result = adapter.get_night_intervention_data(6)
        assert result[0]["night_intervention_count"] == 5

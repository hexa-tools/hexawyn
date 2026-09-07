from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.engineer_workload_port import (
    EngineerWorkloadPort,
    MonthNightData,
)


class NightInterventionSource(Protocol):
    def fetch_night_intervention_data(self, history_months: int) -> list[MonthNightData]: ...


class NightInterventionAdapter(EngineerWorkloadPort):
    def __init__(self, source: NightInterventionSource) -> None:
        self._source = source

    def get_night_intervention_data(self, history_months: int) -> list[MonthNightData]:
        return self._source.fetch_night_intervention_data(history_months)

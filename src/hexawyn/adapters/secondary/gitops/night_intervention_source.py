from __future__ import annotations

from hexawyn.application.ports.driven.engineer_workload_port import MonthNightData

_MONTHS_IN_QUARTER = 3


class EmptyNightInterventionSource:
    def fetch_night_intervention_data(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=0, total_nights=30)
            for _ in range(history_months)
        ]

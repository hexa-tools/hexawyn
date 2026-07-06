from __future__ import annotations

from hexawyn.application.ports.driven.recurring_incident_port import (
    IncidentFrequencyData,
    RecurringIncidentPort,
)


class RecurringIncidentAdapter(RecurringIncidentPort):
    def fetch_incidents(self, window_days: int) -> list[IncidentFrequencyData]:
        return []

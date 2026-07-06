from __future__ import annotations

from hexawyn.application.ports.driven.monthly_incident_port import (
    IncidentSnapshotData,
    MonthlyIncidentPort,
)


class MonthlyIncidentAdapter(MonthlyIncidentPort):
    def fetch_incidents(self, month: str) -> list[IncidentSnapshotData]:
        return []

from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.recurring_incident import RecurringIncidentReport


@dataclass
class DetectRecurringIncidentsResponse:
    result: RecurringIncidentReport

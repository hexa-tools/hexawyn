from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.monthly_incident_report import MonthlyIncidentReport


@dataclass
class ComputeMonthlyIncidentReportResponse:
    result: MonthlyIncidentReport

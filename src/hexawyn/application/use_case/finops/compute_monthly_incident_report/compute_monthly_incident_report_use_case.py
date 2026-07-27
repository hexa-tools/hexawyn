from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.monthly_incident_port import MonthlyIncidentPort
from hexawyn.application.use_case.finops.compute_monthly_incident_report.command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.use_case.finops.compute_monthly_incident_report.response import (
    ComputeMonthlyIncidentReportResponse,
)
from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
    MonthlyIncidentReportEngine,
)


class ComputeMonthlyIncidentReportUseCase:
    def __init__(self, incident_port: MonthlyIncidentPort) -> None:
        self._port = incident_port
        self._engine = MonthlyIncidentReportEngine()

    def execute(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore


def _previous_month(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"

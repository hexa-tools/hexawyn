from __future__ import annotations

from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_response import (
    ComputeMonthlyIncidentReportResponse,
)
from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_service_port import (
    ComputeMonthlyIncidentReportServicePort,
)


class ComputeMonthlyIncidentReportUseCase:
    def __init__(self, service: ComputeMonthlyIncidentReportServicePort) -> None:
        self._service = service

    def execute(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        return self._service.compute(command)

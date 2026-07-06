from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_response import (
    ComputeMonthlyIncidentReportResponse,
)


class ComputeMonthlyIncidentReportServicePort(ABC):
    @abstractmethod
    def compute(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse: ...

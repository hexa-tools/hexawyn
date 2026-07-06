from __future__ import annotations

from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_response import (
    GenerateWeeklyReliabilityReportResponse,
)
from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_service_port import (
    GenerateWeeklyReliabilityReportServicePort,
)


class GenerateWeeklyReliabilityReportUseCase:
    def __init__(self, service: GenerateWeeklyReliabilityReportServicePort) -> None:
        self._service = service

    def execute(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        return self._service.generate_report(command)

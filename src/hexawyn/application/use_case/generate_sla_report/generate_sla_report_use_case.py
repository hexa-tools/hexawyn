from __future__ import annotations

from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_command import (
    GenerateSlaReportCommand,
)
from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_response import (
    GenerateSlaReportResponse,
)
from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_service_port import (
    GenerateSlaReportServicePort,
)


class GenerateSlaReportUseCase:
    def __init__(self, service: GenerateSlaReportServicePort) -> None:
        self._service = service

    def execute(self, command: GenerateSlaReportCommand) -> GenerateSlaReportResponse:
        return self._service.generate(command)

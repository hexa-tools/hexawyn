from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import SlaReportPort
from hexawyn.application.use_case.generate_sla_report.command import (
    GenerateSlaReportCommand,
)
from hexawyn.application.use_case.generate_sla_report.response import (
    GenerateSlaReportResponse,
)
from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_service_port import (
    GenerateSlaReportServicePort,
)
from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService


class GenerateSlaReportService(GenerateSlaReportServicePort):
    def __init__(self, sla_port: SlaReportPort) -> None:
        self._port = sla_port
        self._engine = SlaReportService()

    def generate(self, command: GenerateSlaReportCommand) -> GenerateSlaReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSlaReportResponse(result=result)

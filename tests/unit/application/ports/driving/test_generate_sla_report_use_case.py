from unittest.mock import MagicMock

from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_command import (
    GenerateSlaReportCommand,
)
from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_response import (
    GenerateSlaReportResponse,
)
from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_service_port import (
    GenerateSlaReportServicePort,
)
from hexawyn.domain.models.sla_report import SlaReport


class TestGenerateSlaReportUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.generate_sla_report.generate_sla_report_use_case import (
            GenerateSlaReportUseCase,
        )

        service = MagicMock(spec=GenerateSlaReportServicePort)
        expected = GenerateSlaReportResponse(result=SlaReport(quarter_label="2026-Q1"))
        service.generate.return_value = expected
        use_case = GenerateSlaReportUseCase(service=service)
        command = GenerateSlaReportCommand(quarter="2026-Q1")

        response = use_case.execute(command)

        service.generate.assert_called_once_with(command)
        assert response is expected

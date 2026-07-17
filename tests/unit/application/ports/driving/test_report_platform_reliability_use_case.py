from unittest.mock import MagicMock

from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_response import (  # noqa: E501
    ReportPlatformReliabilityResponse,
)
from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_service_port import (  # noqa: E501
    ReportPlatformReliabilityServicePort,
)
from hexawyn.domain.models.platform_reliability import PlatformReliabilityReport


class TestReportPlatformReliabilityUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.report_platform_reliability.report_platform_reliability_use_case import (  # noqa: E501
            ReportPlatformReliabilityUseCase,
        )

        service = MagicMock(spec=ReportPlatformReliabilityServicePort)
        expected = ReportPlatformReliabilityResponse(
            result=PlatformReliabilityReport(period_label="2026-06", uptime_pct=99.95)
        )
        service.report.return_value = expected
        use_case = ReportPlatformReliabilityUseCase(service=service)
        command = ReportPlatformReliabilityCommand(period="2026-06")

        response = use_case.execute(command)

        service.report.assert_called_once_with(command)
        assert response is expected

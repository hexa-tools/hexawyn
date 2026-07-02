from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_response import (
    AnalyzePodLogsResponse,
)
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_service_port import (
    AnalyzePodLogsServicePort,
)
from hexawyn.application.use_case.analyze_pod_logs.analyze_pod_logs_use_case import (
    AnalyzePodLogsUseCase,
)


class TestAnalyzePodLogsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=AnalyzePodLogsServicePort)
        expected = AnalyzePodLogsResponse(pod_name="api-gateway-7f9b")
        service.analyze.return_value = expected
        use_case = AnalyzePodLogsUseCase(service=service)
        command = AnalyzePodLogsCommand(pod_name="api-gateway-7f9b", namespace="prod")

        result = use_case.execute(command)

        service.analyze.assert_called_once_with(command)
        assert result is expected

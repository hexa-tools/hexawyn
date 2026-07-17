from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_response import (
    DetectLogAnomaliesResponse,
)
from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_service_port import (
    DetectLogAnomaliesServicePort,
)
from hexawyn.application.use_case.detect_log_anomalies.detect_log_anomalies_use_case import (
    DetectLogAnomaliesUseCase,
)


class TestDetectLogAnomaliesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectLogAnomaliesServicePort)
        expected = DetectLogAnomaliesResponse(pod_name="inventory-service")
        service.detect.return_value = expected
        use_case = DetectLogAnomaliesUseCase(service=service)
        command = DetectLogAnomaliesCommand(pod_name="inventory-service", namespace="prod")

        result = use_case.execute(command)

        service.detect.assert_called_once_with(command)
        assert result is expected

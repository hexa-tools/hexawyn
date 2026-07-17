from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_response import (
    DetectPodAnomaliesResponse,
)
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_service_port import (
    DetectPodAnomaliesServicePort,
)
from hexawyn.application.use_case.detect_pod_anomalies.detect_pod_anomalies_use_case import (
    DetectPodAnomaliesUseCase,
)


class TestDetectPodAnomaliesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectPodAnomaliesServicePort)
        expected = DetectPodAnomaliesResponse(namespace="production")
        service.detect.return_value = expected
        use_case = DetectPodAnomaliesUseCase(service=service)
        command = DetectPodAnomaliesCommand(namespace="production")

        result = use_case.execute(command)

        service.detect.assert_called_once_with(command)
        assert result is expected

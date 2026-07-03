from __future__ import annotations

from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_response import (
    DetectLogAnomaliesResponse,
)
from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_service_port import (
    DetectLogAnomaliesServicePort,
)


class DetectLogAnomaliesUseCase:
    def __init__(self, service: DetectLogAnomaliesServicePort) -> None:
        self._svc = service

    def execute(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        return self._svc.detect(command)

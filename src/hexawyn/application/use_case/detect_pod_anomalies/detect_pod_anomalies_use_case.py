from __future__ import annotations

from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_response import (
    DetectPodAnomaliesResponse,
)
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_service_port import (
    DetectPodAnomaliesServicePort,
)


class DetectPodAnomaliesUseCase:
    def __init__(self, service: DetectPodAnomaliesServicePort) -> None:
        self._svc = service

    def execute(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        return self._svc.detect(command)

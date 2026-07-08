from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_response import (
    DetectPodAnomaliesResponse,
)


class DetectPodAnomaliesServicePort(ABC):
    @abstractmethod
    def detect(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse: ...

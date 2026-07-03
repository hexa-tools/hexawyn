from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_response import (
    DetectLogAnomaliesResponse,
)


class DetectLogAnomaliesServicePort(ABC):
    @abstractmethod
    def detect(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse: ...

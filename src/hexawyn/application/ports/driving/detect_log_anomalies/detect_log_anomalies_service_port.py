from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.response import (
    DetectLogAnomaliesResponse,
)


class DetectLogAnomaliesServicePort(ABC):
    @abstractmethod
    def detect(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse: ...

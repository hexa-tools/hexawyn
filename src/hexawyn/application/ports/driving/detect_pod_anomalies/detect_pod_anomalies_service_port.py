from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.response import (
    DetectPodAnomaliesResponse,
)


class DetectPodAnomaliesServicePort(ABC):
    @abstractmethod
    def detect(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse: ...

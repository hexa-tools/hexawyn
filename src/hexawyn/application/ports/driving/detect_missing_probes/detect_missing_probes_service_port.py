from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_response import (
    DetectMissingProbesResponse,
)


class DetectMissingProbesServicePort(ABC):
    @abstractmethod
    def detect_missing_probes(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse: ...

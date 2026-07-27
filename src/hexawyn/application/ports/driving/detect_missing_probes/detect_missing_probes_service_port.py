from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.detect_missing_probes.command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.use_case.security.detect_missing_probes.response import (
    DetectMissingProbesResponse,
)


class DetectMissingProbesServicePort(ABC):
    @abstractmethod
    def detect_missing_probes(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse: ...

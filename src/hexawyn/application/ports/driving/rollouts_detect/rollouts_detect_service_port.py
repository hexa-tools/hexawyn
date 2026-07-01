from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.rollouts_detect.rollouts_detect_command import (
    RolloutsDetectCommand,
)
from hexawyn.application.ports.driving.rollouts_detect.rollouts_detect_response import (
    RolloutsDetectResponse,
)


class RolloutsDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        """Detect if Argo Rollouts is installed."""

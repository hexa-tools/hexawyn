from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.policy_detect.policy_detect_command import (
    PolicyDetectCommand,
)
from hexawyn.application.ports.driving.policy_detect.policy_detect_response import (
    PolicyDetectResponse,
)


class PolicyDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        """Detect the policy engine."""

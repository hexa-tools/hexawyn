from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_detect.command import (
    PolicyDetectCommand,
)
from hexawyn.application.use_case.governance.policy_detect.response import (
    PolicyDetectResponse,
)


class PolicyDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: PolicyDetectCommand) -> PolicyDetectResponse: ...

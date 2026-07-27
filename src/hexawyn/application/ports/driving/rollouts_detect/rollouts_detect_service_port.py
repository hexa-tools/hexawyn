from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.rollouts_detect.command import (
    RolloutsDetectCommand,
)
from hexawyn.application.use_case.workloads.rollouts_detect.response import (
    RolloutsDetectResponse,
)


class RolloutsDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse: ...

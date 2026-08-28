from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_detect.command import (
    CiliumDetectCommand,
)
from hexawyn.application.use_case.cilium.cilium_detect.response import (
    CiliumDetectResponse,
)


class CiliumDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: CiliumDetectCommand) -> CiliumDetectResponse: ...

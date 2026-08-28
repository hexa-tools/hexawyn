from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_service_graph.command import (
    CiliumServiceGraphCommand,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.response import (
    CiliumServiceGraphResponse,
)


class CiliumServiceGraphServicePort(ABC):
    @abstractmethod
    def build(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse: ...

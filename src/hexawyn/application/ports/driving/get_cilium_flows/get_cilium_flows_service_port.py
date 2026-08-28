from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.get_cilium_flows.command import (
    GetCiliumFlowsCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_flows.response import (
    GetCiliumFlowsResponse,
)


class GetCiliumFlowsServicePort(ABC):
    @abstractmethod
    def get(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse: ...

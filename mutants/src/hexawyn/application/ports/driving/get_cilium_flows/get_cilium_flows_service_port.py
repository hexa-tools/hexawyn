from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.get_cilium_flows.command import (
    GetCiliumFlowsCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_flows.response import (
    GetCiliumFlowsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GetCiliumFlowsServicePort(ABC):
    @abstractmethod
    def get(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse: ...

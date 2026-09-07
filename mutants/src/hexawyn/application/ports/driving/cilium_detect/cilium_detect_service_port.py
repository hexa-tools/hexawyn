from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_detect.command import (
    CiliumDetectCommand,
)
from hexawyn.application.use_case.cilium.cilium_detect.response import (
    CiliumDetectResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CiliumDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: CiliumDetectCommand) -> CiliumDetectResponse: ...

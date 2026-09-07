from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.detect_cilium_denials.command import (
    DetectCiliumDenialsCommand,
)
from hexawyn.application.use_case.cilium.detect_cilium_denials.response import (
    DetectCiliumDenialsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectCiliumDenialsServicePort(ABC):
    @abstractmethod
    def detect(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse: ...

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_detect.command import CalicoDetectCommand
from hexawyn.application.use_case.calico.calico_detect.response import CalicoDetectResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CalicoDetectServicePort(ABC):
    """Inbound port for Calico detection."""

    @abstractmethod
    def detect(self, command: CalicoDetectCommand) -> CalicoDetectResponse: ...

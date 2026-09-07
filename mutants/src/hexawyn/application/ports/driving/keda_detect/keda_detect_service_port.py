from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_detect.command import (
    KedaDetectCommand,
)
from hexawyn.application.use_case.keda.keda_detect.response import (
    KedaDetectResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KedaDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: KedaDetectCommand) -> KedaDetectResponse: ...

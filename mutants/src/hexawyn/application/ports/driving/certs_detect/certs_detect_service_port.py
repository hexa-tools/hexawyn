from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_detect.command import (
    CertsDetectCommand,
)
from hexawyn.application.use_case.cert_manager.certs_detect.response import (
    CertsDetectResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CertsDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: CertsDetectCommand) -> CertsDetectResponse: ...

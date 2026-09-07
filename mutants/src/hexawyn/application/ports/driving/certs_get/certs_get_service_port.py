from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_get.command import (
    CertsGetCommand,
)
from hexawyn.application.use_case.cert_manager.certs_get.response import (
    CertsGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CertsGetServicePort(ABC):
    @abstractmethod
    def get_cert(self, command: CertsGetCommand) -> CertsGetResponse: ...

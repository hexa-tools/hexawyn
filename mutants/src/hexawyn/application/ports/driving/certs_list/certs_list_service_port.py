from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_list.command import (
    CertsListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_list.response import (
    CertsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CertsListServicePort(ABC):
    @abstractmethod
    def list_certs(self, command: CertsListCommand) -> CertsListResponse: ...

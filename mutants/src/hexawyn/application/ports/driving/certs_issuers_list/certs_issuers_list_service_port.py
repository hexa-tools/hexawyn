from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_issuers_list.command import (
    CertsIssuersListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_issuers_list.response import (
    CertsIssuersListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CertsIssuersListServicePort(ABC):
    @abstractmethod
    def list_issuers(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse: ...

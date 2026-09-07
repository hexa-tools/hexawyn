from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.list_cilium_identities.command import (
    ListCiliumIdentitiesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_identities.response import (
    ListCiliumIdentitiesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ListCiliumIdentitiesServicePort(ABC):
    @abstractmethod
    def list(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse: ...

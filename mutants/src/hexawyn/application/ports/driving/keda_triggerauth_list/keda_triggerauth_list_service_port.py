from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_triggerauth_list.command import (  # type: ignore
    KedaTriggerAuthListCommand,
)
from hexawyn.application.use_case.keda.keda_triggerauth_list.response import (  # type: ignore
    KedaTriggerAuthListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KedaTriggerAuthListServicePort(ABC):
    @abstractmethod
    def list_auths(self, command: KedaTriggerAuthListCommand) -> KedaTriggerAuthListResponse: ...

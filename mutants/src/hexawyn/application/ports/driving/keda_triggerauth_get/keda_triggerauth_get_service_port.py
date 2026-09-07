from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_triggerauth_get.command import (  # type: ignore
    KedaTriggerAuthGetCommand,
)
from hexawyn.application.use_case.keda.keda_triggerauth_get.response import (  # type: ignore
    KedaTriggerAuthGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KedaTriggerAuthGetServicePort(ABC):
    @abstractmethod
    def get_auth(self, command: KedaTriggerAuthGetCommand) -> KedaTriggerAuthGetResponse: ...

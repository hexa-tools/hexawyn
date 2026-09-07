from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledjob_get.command import (  # type: ignore
    KedaScaledJobGetCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjob_get.response import (  # type: ignore
    KedaScaledJobGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KedaScaledJobGetServicePort(ABC):
    @abstractmethod
    def get_job(self, command: KedaScaledJobGetCommand) -> KedaScaledJobGetResponse: ...

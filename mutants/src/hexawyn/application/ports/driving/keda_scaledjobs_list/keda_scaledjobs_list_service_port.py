from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledjobs_list.command import (  # type: ignore
    KedaScaledJobsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjobs_list.response import (  # type: ignore
    KedaScaledJobsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KedaScaledJobsListServicePort(ABC):
    @abstractmethod
    def list_jobs(self, command: KedaScaledJobsListCommand) -> KedaScaledJobsListResponse: ...

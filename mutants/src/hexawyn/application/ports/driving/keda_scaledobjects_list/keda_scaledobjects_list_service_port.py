from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledobjects_list.command import (  # type: ignore
    KedaScaledObjectsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobjects_list.response import (  # type: ignore
    KedaScaledObjectsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KedaScaledObjectsListServicePort(ABC):
    @abstractmethod
    def list_objects(
        self, command: KedaScaledObjectsListCommand
    ) -> KedaScaledObjectsListResponse: ...

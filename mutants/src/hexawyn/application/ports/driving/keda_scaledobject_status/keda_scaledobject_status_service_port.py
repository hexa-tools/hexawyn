from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledobject_status.command import (  # type: ignore
    KedaScaledObjectStatusCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_status.response import (  # type: ignore
    KedaScaledObjectStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KedaScaledObjectStatusServicePort(ABC):
    @abstractmethod
    def get_status(
        self, command: KedaScaledObjectStatusCommand
    ) -> KedaScaledObjectStatusResponse: ...

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.error_attribution.command import (
    ErrorAttributionCommand,
)
from hexawyn.application.use_case.observability.error_attribution.response import (
    ErrorAttributionResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ErrorAttributionServicePort(ABC):
    @abstractmethod
    def attribute(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse: ...

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.semantic_log_search.command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.use_case.observability.semantic_log_search.response import (
    SemanticLogSearchResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SemanticLogSearchServicePort(ABC):
    @abstractmethod
    def search(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse: ...

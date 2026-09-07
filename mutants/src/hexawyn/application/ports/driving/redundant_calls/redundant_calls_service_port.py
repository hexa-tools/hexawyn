from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.redundant_calls.command import (
    RedundantCallsCommand,
)
from hexawyn.application.use_case.observability.redundant_calls.response import (
    RedundantCallsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class RedundantCallsServicePort(ABC):
    @abstractmethod
    def detect(self, command: RedundantCallsCommand) -> RedundantCallsResponse: ...

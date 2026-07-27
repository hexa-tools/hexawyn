from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.redundant_calls.command import (
    RedundantCallsCommand,
)
from hexawyn.application.use_case.observability.redundant_calls.response import (
    RedundantCallsResponse,
)


class RedundantCallsServicePort(ABC):
    @abstractmethod
    def detect(self, command: RedundantCallsCommand) -> RedundantCallsResponse: ...

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.redundant_calls.redundant_calls_command import (
    RedundantCallsCommand,
)
from hexawyn.application.ports.driving.redundant_calls.redundant_calls_response import (
    RedundantCallsResponse,
)


class RedundantCallsServicePort(ABC):
    @abstractmethod
    def detect(self, command: RedundantCallsCommand) -> RedundantCallsResponse: ...

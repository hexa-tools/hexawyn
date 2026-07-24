from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.error_attribution.command import (
    ErrorAttributionCommand,
)
from hexawyn.application.use_case.error_attribution.response import (
    ErrorAttributionResponse,
)


class ErrorAttributionServicePort(ABC):
    @abstractmethod
    def attribute(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse: ...

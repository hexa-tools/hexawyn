from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.error_attribution.error_attribution_command import (
    ErrorAttributionCommand,
)
from hexawyn.application.ports.driving.error_attribution.error_attribution_response import (
    ErrorAttributionResponse,
)


class ErrorAttributionServicePort(ABC):
    @abstractmethod
    def attribute(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse: ...

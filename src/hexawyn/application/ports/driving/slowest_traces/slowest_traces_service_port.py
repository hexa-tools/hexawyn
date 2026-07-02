from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.slowest_traces.slowest_traces_command import (
    SlowestTracesCommand,
)
from hexawyn.application.ports.driving.slowest_traces.slowest_traces_response import (
    SlowestTracesResponse,
)


class SlowestTracesServicePort(ABC):
    @abstractmethod
    def find_slowest(self, command: SlowestTracesCommand) -> SlowestTracesResponse: ...

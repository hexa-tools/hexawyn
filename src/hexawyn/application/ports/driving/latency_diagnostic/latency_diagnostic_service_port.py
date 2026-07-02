from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.latency_diagnostic.latency_diagnostic_command import (
    LatencyDiagnosticCommand,
)
from hexawyn.application.ports.driving.latency_diagnostic.latency_diagnostic_response import (
    LatencyDiagnosticResponse,
)


class LatencyDiagnosticServicePort(ABC):
    @abstractmethod
    def diagnose(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse: ...

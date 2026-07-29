from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.latency_diagnostic.command import (
    LatencyDiagnosticCommand,
)
from hexawyn.application.use_case.observability.latency_diagnostic.response import (
    LatencyDiagnosticResponse,
)


class LatencyDiagnosticServicePort(ABC):
    @abstractmethod
    def diagnose(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse: ...

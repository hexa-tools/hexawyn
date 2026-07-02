from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_response import (
    AnalyzePodLogsResponse,
)


class AnalyzePodLogsServicePort(ABC):
    @abstractmethod
    def analyze(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse: ...

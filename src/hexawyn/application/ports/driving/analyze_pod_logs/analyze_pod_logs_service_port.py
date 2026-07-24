from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.analyze_pod_logs.command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.use_case.analyze_pod_logs.response import (
    AnalyzePodLogsResponse,
)


class AnalyzePodLogsServicePort(ABC):
    @abstractmethod
    def analyze(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse: ...

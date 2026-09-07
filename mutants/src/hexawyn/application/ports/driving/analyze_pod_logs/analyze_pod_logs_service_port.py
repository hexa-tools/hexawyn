from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.analyze_pod_logs.command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.use_case.observability.analyze_pod_logs.response import (
    AnalyzePodLogsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AnalyzePodLogsServicePort(ABC):
    @abstractmethod
    def analyze(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse: ...

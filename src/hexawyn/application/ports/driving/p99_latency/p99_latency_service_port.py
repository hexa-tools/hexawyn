from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.p99_latency.command import P99LatencyCommand
from hexawyn.application.use_case.p99_latency.response import P99LatencyResponse


class P99LatencyServicePort(ABC):
    @abstractmethod
    def compute_p99(self, command: P99LatencyCommand) -> P99LatencyResponse: ...

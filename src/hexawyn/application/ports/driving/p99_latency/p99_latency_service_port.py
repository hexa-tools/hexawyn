from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.p99_latency.p99_latency_command import P99LatencyCommand
from hexawyn.application.ports.driving.p99_latency.p99_latency_response import P99LatencyResponse


class P99LatencyServicePort(ABC):
    @abstractmethod
    def compute_p99(self, command: P99LatencyCommand) -> P99LatencyResponse: ...

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.trace_k8s_events.command import (
    TraceK8sEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.response import (
    TraceK8sEventsResponse,
)


class TraceK8sEventsServicePort(ABC):
    @abstractmethod
    def correlate(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse: ...

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.trace_k8s_events.trace_k8s_events_command import (
    TraceK8sEventsCommand,
)
from hexawyn.application.ports.driving.trace_k8s_events.trace_k8s_events_response import (
    TraceK8sEventsResponse,
)


class TraceK8sEventsServicePort(ABC):
    @abstractmethod
    def correlate(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse: ...

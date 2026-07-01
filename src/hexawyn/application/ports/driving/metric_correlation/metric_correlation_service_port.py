from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.metric_correlation.metric_correlation_command import (
    MetricCorrelationCommand,
)
from hexawyn.application.ports.driving.metric_correlation.metric_correlation_response import (
    MetricCorrelationResponse,
)


class MetricCorrelationServicePort(ABC):
    @abstractmethod
    def correlate(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse: ...

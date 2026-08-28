from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_felix_metrics.command import (
    CalicoFelixMetricsCommand,
)
from hexawyn.application.use_case.calico.calico_felix_metrics.response import (
    CalicoFelixMetricsResponse,
)


class CalicoFelixMetricsServicePort(ABC):
    """Inbound port for Felix per-policy metrics."""

    @abstractmethod
    def metrics(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse: ...

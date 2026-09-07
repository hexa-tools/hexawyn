from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_felix_metrics.command import (
    CalicoFelixMetricsCommand,
)
from hexawyn.application.use_case.calico.calico_felix_metrics.response import (
    CalicoFelixMetricsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CalicoFelixMetricsServicePort(ABC):
    """Inbound port for Felix per-policy metrics."""

    @abstractmethod
    def metrics(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse: ...

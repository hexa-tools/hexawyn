from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.slo_breach_prediction.command import (
    SLOBreachPredictionCommand,
)
from hexawyn.application.use_case.workloads.slo_breach_prediction.response import (
    SLOBreachPredictionResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SLOBreachPredictionServicePort(ABC):
    @abstractmethod
    def predict(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse: ...

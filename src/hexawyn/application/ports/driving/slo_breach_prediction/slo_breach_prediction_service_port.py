from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.slo_breach_prediction.command import (
    SLOBreachPredictionCommand,
)
from hexawyn.application.use_case.slo_breach_prediction.response import (
    SLOBreachPredictionResponse,
)


class SLOBreachPredictionServicePort(ABC):
    @abstractmethod
    def predict(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse: ...

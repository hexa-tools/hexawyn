from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_command import (
    SLOBreachPredictionCommand,
)
from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_response import (
    SLOBreachPredictionResponse,
)


class SLOBreachPredictionServicePort(ABC):
    @abstractmethod
    def predict(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse: ...

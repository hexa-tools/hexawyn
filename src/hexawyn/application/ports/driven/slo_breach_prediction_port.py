from abc import ABC, abstractmethod

from hexawyn.domain.models.slo_breach_prediction import SLOBreachPredictionRequest


class SLOBreachPredictionPort(ABC):
    @abstractmethod
    def fetch_trend_metrics(
        self, request: SLOBreachPredictionRequest
    ) -> list[dict[str, object]]: ...

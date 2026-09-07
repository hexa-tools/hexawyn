from abc import ABC, abstractmethod

from hexawyn.domain.models.slo_breach_prediction import SLOBreachPredictionRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SLOBreachPredictionPort(ABC):
    @abstractmethod
    def fetch_trend_metrics(
        self, request: SLOBreachPredictionRequest
    ) -> list[dict[str, object]]: ...

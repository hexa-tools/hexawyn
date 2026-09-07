from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class MonthNightData(TypedDict):
    month: str
    night_intervention_count: int
    total_nights: int


class EngineerWorkloadPort(ABC):
    @abstractmethod
    def get_night_intervention_data(self, history_months: int) -> list[MonthNightData]: ...

from abc import ABC, abstractmethod
from typing import TypedDict


class MonthNightData(TypedDict):
    month: str
    night_intervention_count: int
    total_nights: int


class EngineerWorkloadPort(ABC):
    @abstractmethod
    def get_night_intervention_data(self, history_months: int) -> list[MonthNightData]: ...

from abc import ABC, abstractmethod
from typing import TypedDict


class RiskEventRaw(TypedDict):
    business_service_name: str
    risk_type: str
    predicted_date: str
    days_from_now: int
    detail: str


class DisruptionRiskPort(ABC):
    @abstractmethod
    def get_disruption_risks(self, warning_days: int) -> list[RiskEventRaw]: ...

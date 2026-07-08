from abc import ABC, abstractmethod
from typing import TypedDict


class ServiceSuccessRateRawData(TypedDict):
    service_name: str
    total_requests: int
    successful_requests: int
    failed_requests: int
    success_rate: float
    error_rate: float
    has_data: bool
    observation_days: int


class ErrorBudgetPort(ABC):
    @abstractmethod
    def fetch_success_rate(
        self, service_name: str, window_days: int
    ) -> ServiceSuccessRateRawData: ...

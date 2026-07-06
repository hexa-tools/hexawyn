from abc import ABC, abstractmethod
from typing import TypedDict


class ServiceReliabilityRawData(TypedDict):
    service_name: str
    uptime_pct: float
    error_rate: float
    p99_latency_ms: float
    slo_target: float
    downtime_minutes: int
    data_gap_minutes: int
    created_mid_week: bool


class IncidentRawData(TypedDict):
    service_name: str
    timestamp: str
    duration_minutes: int
    error_rate: float
    description: str


class WeeklyReliabilityReportPort(ABC):
    @abstractmethod
    def fetch_service_reliability(self, window_days: int) -> list[ServiceReliabilityRawData]: ...

    @abstractmethod
    def fetch_incidents(self, window_days: int) -> list[IncidentRawData]: ...

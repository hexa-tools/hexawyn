from abc import ABC, abstractmethod
from typing import TypedDict


class ZombiePodData(TypedDict):
    pod_name: str
    namespace: str
    traffic_rps: float
    cpu_cores: float
    memory_gb: float
    age_days: int
    has_service: bool
    is_cronjob: bool
    is_terminating: bool
    has_sidecar: bool
    sidecar_traffic_rps: float
    seven_day_traffic_rps: float


class ZombieDetectionPort(ABC):
    @abstractmethod
    def get_zombie_workloads(self, window_hours: int) -> list[ZombiePodData]: ...

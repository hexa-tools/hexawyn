from abc import ABC, abstractmethod
from typing import TypedDict


class DependentServiceData(TypedDict):
    name: str
    calls_per_second: float


class PDBData(TypedDict, total=False):
    min_available: int | None
    max_unavailable: int | None


class HPAData(TypedDict, total=False):
    min_replicas: int
    max_replicas: int
    current_replicas: int


class WhatIfSimulationPort(ABC):
    @abstractmethod
    def get_service_topology(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        """Return a mapping of service_name → list of dependent services."""

    @abstractmethod
    def get_pdb_info(self, namespace: str, service_name: str) -> PDBData | None:
        """Return PodDisruptionBudget info for the service, or None."""

    @abstractmethod
    def get_hpa_info(self, namespace: str, service_name: str) -> HPAData | None:
        """Return HPA info for the service, or None."""

    @abstractmethod
    def get_current_cpu_utilization(self, namespace: str, service_name: str) -> float:
        """Return current CPU utilization percent (0–100)."""

    @abstractmethod
    def get_current_replicas(self, namespace: str, service_name: str) -> int:
        """Return the current number of ready replicas."""

    @abstractmethod
    def get_dependency_graph(self, namespace: str) -> dict[str, list[str]]:
        """Return a directed graph of service dependencies (name → list of downstream names)."""

from abc import ABC, abstractmethod
from typing import TypedDict


class ReliabilityIncidentRaw(TypedDict):
    date: str
    severity: str
    downtime_minutes: int
    resolution_minutes: int
    root_cause: str
    resolved: bool
    planned_maintenance: bool


class ReliabilityData(TypedDict):
    period_minutes: int
    incidents: list[ReliabilityIncidentRaw]
    previous_avg_resolution_minutes: int | None
    cost_per_downtime_minute_eur: float | None


class PlatformReliabilityPort(ABC):
    """Driven port — provides raw reliability inputs for a period: incidents
    (severity, downtime, resolution, root cause), the total period length, the
    previous period's average resolution time, and the per-minute downtime cost
    (None when pricing is not configured).

    A secondary adapter aggregates the incident/MTTR sources; the domain never
    touches them directly and never invents a financial figure.
    """

    @abstractmethod
    def get_reliability_data(self, period: str) -> ReliabilityData:
        """Return the reliability inputs for *period* (e.g. ``"2026-06"``).

        Raises ClusterUnreachableError on data-source failures.
        """

from abc import ABC, abstractmethod
from typing import TypedDict


class ServiceSlaRaw(TypedDict):
    service_name: str
    sla_target_pct: float
    uptime_pct: float
    coverage_days: int
    quarter_days: int
    maintenance_minutes: int


class SlaBreachRaw(TypedDict):
    service_name: str
    date: str
    duration_minutes: int
    impacted_users: int
    root_cause_ref: str
    planned_maintenance: bool


class QuarterSlaData(TypedDict):
    has_data: bool
    services: list[ServiceSlaRaw]
    breaches: list[SlaBreachRaw]


class SlaReportPort(ABC):
    """Driven port — provides per-service SLA data for a quarter, plus the
    previous quarter's average uptime for trend comparison.

    A secondary adapter aggregates the weekly reliability / SLO sources into
    quarter-level records; the domain never touches those sources directly.
    """

    @abstractmethod
    def get_quarter_sla_data(self, quarter: str) -> QuarterSlaData:
        """Return per-service uptime/target/coverage and breaches for *quarter*.

        ``has_data`` is False when no incident/reliability data is available, so
        the domain warns instead of reporting a misleading 100% uptime.

        Raises ClusterUnreachableError on data-source failures.
        """

    @abstractmethod
    def get_previous_quarter_avg_uptime(self, quarter: str) -> float | None:
        """Return the previous quarter's average uptime %, or None when there is
        no prior quarter to compare against."""

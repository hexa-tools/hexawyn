from abc import ABC, abstractmethod
from typing import TypedDict


class BusinessConfigRaw(TypedDict):
    revenue_per_minute: float | None
    support_cost_per_hour: float | None
    sla_penalty_per_hour: float | None


class IncidentCostData(TypedDict):
    business_service_name: str
    downtime_minutes: int
    impacted_service_count: int
    resolved_at: str
    sla_breached: bool
    business_config: BusinessConfigRaw


class IncidentCostPort(ABC):
    """Driven port — provides an incident's business-facing facts (service
    name, downtime, impacted services, resolution time, SLA breach) together
    with the configured business financial parameters.

    The business config carries None for any unconfigured parameter, so the
    domain never fabricates a euro amount.
    """

    @abstractmethod
    def get_incident_cost_data(self, incident_ref: str) -> IncidentCostData:
        """Return the cost inputs for *incident_ref* (e.g. ``"yesterday"``).

        Raises ClusterUnreachableError on data-source failures.
        """

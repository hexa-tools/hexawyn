from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.incident_cost_port import (
    IncidentCostData,
    IncidentCostPort,
)


class IncidentCostSource(Protocol):
    """Assembles an incident's business facts and the configured financial
    parameters into the uniform IncidentCostData contract."""

    def fetch_incident_cost_data(self, incident_ref: str) -> IncidentCostData: ...


class IncidentCostAdapter(IncidentCostPort):
    """Facade over the incident source and the business financial config.

    Delegates to an injected source, keeping the domain free of any knowledge
    of where the incident data or the business parameters come from.
    """

    def __init__(self, source: IncidentCostSource) -> None:
        self._source = source

    def get_incident_cost_data(self, incident_ref: str) -> IncidentCostData:
        return self._source.fetch_incident_cost_data(incident_ref)

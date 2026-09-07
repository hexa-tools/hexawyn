from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.incident_cost_port import (
    IncidentCostData,
    IncidentCostPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class IncidentCostSource(Protocol):
    """Assembles an incident's business facts and the configured financial
    parameters into the uniform IncidentCostData contract."""

    def fetch_incident_cost_data(self, incident_ref: str) -> IncidentCostData: ...
mutants_xǁIncidentCostAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁIncidentCostAdapterǁget_incident_cost_data__mutmut: MutantDict = {}  # type: ignore


class IncidentCostAdapter(IncidentCostPort):
    """Facade over the incident source and the business financial config.

    Delegates to an injected source, keeping the domain free of any knowledge
    of where the incident data or the business parameters come from.
    """

    @_mutmut_mutated(mutants_xǁIncidentCostAdapterǁ__init____mutmut)
    def __init__(self, source: IncidentCostSource) -> None:
        self._source = source

    def xǁIncidentCostAdapterǁ__init____mutmut_orig(self, source: IncidentCostSource) -> None:
        self._source = source

    def xǁIncidentCostAdapterǁ__init____mutmut_1(self, source: IncidentCostSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁIncidentCostAdapterǁget_incident_cost_data__mutmut)
    def get_incident_cost_data(self, incident_ref: str) -> IncidentCostData:
        return self._source.fetch_incident_cost_data(incident_ref)

    def xǁIncidentCostAdapterǁget_incident_cost_data__mutmut_orig(self, incident_ref: str) -> IncidentCostData:
        return self._source.fetch_incident_cost_data(incident_ref)

    def xǁIncidentCostAdapterǁget_incident_cost_data__mutmut_1(self, incident_ref: str) -> IncidentCostData:
        return self._source.fetch_incident_cost_data(None)

mutants_xǁIncidentCostAdapterǁ__init____mutmut['_mutmut_orig'] = IncidentCostAdapter.xǁIncidentCostAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁIncidentCostAdapterǁ__init____mutmut['xǁIncidentCostAdapterǁ__init____mutmut_1'] = IncidentCostAdapter.xǁIncidentCostAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁIncidentCostAdapterǁget_incident_cost_data__mutmut['_mutmut_orig'] = IncidentCostAdapter.xǁIncidentCostAdapterǁget_incident_cost_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIncidentCostAdapterǁget_incident_cost_data__mutmut['xǁIncidentCostAdapterǁget_incident_cost_data__mutmut_1'] = IncidentCostAdapter.xǁIncidentCostAdapterǁget_incident_cost_data__mutmut_1 # type: ignore # mutmut generated

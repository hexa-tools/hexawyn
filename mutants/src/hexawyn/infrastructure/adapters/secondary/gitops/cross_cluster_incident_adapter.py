from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    ClusterFailureSignature,
    CrossClusterIncidentPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class FailureSignatureSource(Protocol):
    def fetch_all_cluster_failures(self) -> list[ClusterFailureSignature]: ...
mutants_xǁCrossClusterIncidentAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore


class CrossClusterIncidentAdapter(CrossClusterIncidentPort):
    @_mutmut_mutated(mutants_xǁCrossClusterIncidentAdapterǁ__init____mutmut)
    def __init__(self, source: FailureSignatureSource) -> None:
        self._source = source
    def xǁCrossClusterIncidentAdapterǁ__init____mutmut_orig(self, source: FailureSignatureSource) -> None:
        self._source = source
    def xǁCrossClusterIncidentAdapterǁ__init____mutmut_1(self, source: FailureSignatureSource) -> None:
        self._source = None

    def list_all_cluster_failures(self) -> list[ClusterFailureSignature]:
        return self._source.fetch_all_cluster_failures()

mutants_xǁCrossClusterIncidentAdapterǁ__init____mutmut['_mutmut_orig'] = CrossClusterIncidentAdapter.xǁCrossClusterIncidentAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCrossClusterIncidentAdapterǁ__init____mutmut['xǁCrossClusterIncidentAdapterǁ__init____mutmut_1'] = CrossClusterIncidentAdapter.xǁCrossClusterIncidentAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

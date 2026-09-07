from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterDiffPort,
    ClusterInventoryData,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ClusterInventorySource(Protocol):
    def fetch_resource_inventory(self, cluster_context: str) -> ClusterInventoryData: ...
mutants_xǁClusterDiffAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁClusterDiffAdapterǁget_resource_inventory__mutmut: MutantDict = {}  # type: ignore


class ClusterDiffAdapter(ClusterDiffPort):
    @_mutmut_mutated(mutants_xǁClusterDiffAdapterǁ__init____mutmut)
    def __init__(self, source: ClusterInventorySource) -> None:
        self._source = source
    def xǁClusterDiffAdapterǁ__init____mutmut_orig(self, source: ClusterInventorySource) -> None:
        self._source = source
    def xǁClusterDiffAdapterǁ__init____mutmut_1(self, source: ClusterInventorySource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁClusterDiffAdapterǁget_resource_inventory__mutmut)
    def get_resource_inventory(self, cluster_context: str) -> ClusterInventoryData:
        return self._source.fetch_resource_inventory(cluster_context)

    def xǁClusterDiffAdapterǁget_resource_inventory__mutmut_orig(self, cluster_context: str) -> ClusterInventoryData:
        return self._source.fetch_resource_inventory(cluster_context)

    def xǁClusterDiffAdapterǁget_resource_inventory__mutmut_1(self, cluster_context: str) -> ClusterInventoryData:
        return self._source.fetch_resource_inventory(None)

mutants_xǁClusterDiffAdapterǁ__init____mutmut['_mutmut_orig'] = ClusterDiffAdapter.xǁClusterDiffAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterDiffAdapterǁ__init____mutmut['xǁClusterDiffAdapterǁ__init____mutmut_1'] = ClusterDiffAdapter.xǁClusterDiffAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁClusterDiffAdapterǁget_resource_inventory__mutmut['_mutmut_orig'] = ClusterDiffAdapter.xǁClusterDiffAdapterǁget_resource_inventory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterDiffAdapterǁget_resource_inventory__mutmut['xǁClusterDiffAdapterǁget_resource_inventory__mutmut_1'] = ClusterDiffAdapter.xǁClusterDiffAdapterǁget_resource_inventory__mutmut_1 # type: ignore # mutmut generated

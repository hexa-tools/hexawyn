from __future__ import annotations

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterInventoryData,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut: MutantDict = {}  # type: ignore


class EmptyClusterInventorySource:
    @_mutmut_mutated(mutants_xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut)
    def fetch_resource_inventory(self, cluster_context: str) -> ClusterInventoryData:
        return ClusterInventoryData(cluster_name=cluster_context, resources=[])
    def xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_orig(self, cluster_context: str) -> ClusterInventoryData:
        return ClusterInventoryData(cluster_name=cluster_context, resources=[])
    def xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_1(self, cluster_context: str) -> ClusterInventoryData:
        return ClusterInventoryData(cluster_name=None, resources=[])
    def xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_2(self, cluster_context: str) -> ClusterInventoryData:
        return ClusterInventoryData(cluster_name=cluster_context, resources=None)
    def xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_3(self, cluster_context: str) -> ClusterInventoryData:
        return ClusterInventoryData(resources=[])
    def xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_4(self, cluster_context: str) -> ClusterInventoryData:
        return ClusterInventoryData(cluster_name=cluster_context, )

mutants_xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut['_mutmut_orig'] = EmptyClusterInventorySource.xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut['xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_1'] = EmptyClusterInventorySource.xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut['xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_2'] = EmptyClusterInventorySource.xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut['xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_3'] = EmptyClusterInventorySource.xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut['xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_4'] = EmptyClusterInventorySource.xǁEmptyClusterInventorySourceǁfetch_resource_inventory__mutmut_4 # type: ignore # mutmut generated

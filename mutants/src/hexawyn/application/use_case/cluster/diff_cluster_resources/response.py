from dataclasses import dataclass

from hexawyn.domain.models.cluster_diff import ClusterDiffReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class DiffClusterResourcesResponse:
    result: ClusterDiffReport

from dataclasses import dataclass

from hexawyn.domain.models.cluster_health_comparison import HealthComparisonResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CompareClusterHealthResponse:
    result: HealthComparisonResult

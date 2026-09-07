from dataclasses import dataclass

from hexawyn.domain.models.cluster_operator_health import ClusterOperatorHealthReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CheckClusterOperatorHealthResponse:
    result: ClusterOperatorHealthReport

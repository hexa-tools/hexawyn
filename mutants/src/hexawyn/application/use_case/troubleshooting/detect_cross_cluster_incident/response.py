from dataclasses import dataclass

from hexawyn.domain.models.cross_cluster_correlation import CrossClusterCorrelationReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class DetectCrossClusterIncidentResponse:
    result: CrossClusterCorrelationReport

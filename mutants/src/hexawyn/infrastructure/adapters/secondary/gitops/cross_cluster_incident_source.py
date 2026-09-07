from __future__ import annotations

from hexawyn.application.ports.driven.cross_cluster_incident_port import ClusterFailureSignature


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class EmptyFailureSignatureSource:
    def fetch_all_cluster_failures(self) -> list[ClusterFailureSignature]:
        return []

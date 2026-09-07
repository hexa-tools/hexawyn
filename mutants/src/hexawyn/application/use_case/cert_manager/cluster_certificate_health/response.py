from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.certificate import ClusterCertificateReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ClusterCertificateHealthResponse:
    report: ClusterCertificateReport | None = None
    error: str | None = None

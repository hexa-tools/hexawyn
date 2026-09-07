from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.cluster_certificate_health.command import (
    ClusterCertificateHealthCommand,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.response import (
    ClusterCertificateHealthResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CheckClusterCertificateHealthServicePort(ABC):
    @abstractmethod
    def check_cluster_certificate_health(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse: ...

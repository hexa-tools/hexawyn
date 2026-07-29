from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.cluster_certificate_health.command import (
    ClusterCertificateHealthCommand,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.response import (
    ClusterCertificateHealthResponse,
)


class CheckClusterCertificateHealthServicePort(ABC):
    @abstractmethod
    def check_cluster_certificate_health(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse: ...

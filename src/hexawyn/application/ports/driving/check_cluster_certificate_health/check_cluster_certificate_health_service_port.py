from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_command import (
    CheckClusterCertificateHealthCommand,
)
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_response import (
    CheckClusterCertificateHealthResponse,
)


class CheckClusterCertificateHealthServicePort(ABC):
    @abstractmethod
    def check_cluster_certificate_health(
        self, command: CheckClusterCertificateHealthCommand
    ) -> CheckClusterCertificateHealthResponse: ...

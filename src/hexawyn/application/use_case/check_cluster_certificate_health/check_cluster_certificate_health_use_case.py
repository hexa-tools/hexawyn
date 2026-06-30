from __future__ import annotations

from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_command import (
    CheckClusterCertificateHealthCommand,
)
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_response import (
    CheckClusterCertificateHealthResponse,
)
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_service_port import (
    CheckClusterCertificateHealthServicePort,
)


class CheckClusterCertificateHealthUseCase:
    def __init__(self, service: CheckClusterCertificateHealthServicePort) -> None:
        self._service = service

    def execute(
        self, command: CheckClusterCertificateHealthCommand
    ) -> CheckClusterCertificateHealthResponse:
        return self._service.check_cluster_certificate_health(command)

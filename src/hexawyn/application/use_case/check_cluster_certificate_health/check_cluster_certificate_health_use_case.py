from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
)
from hexawyn.application.use_case.check_cluster_certificate_health.command import (
    CheckClusterCertificateHealthCommand,
)
from hexawyn.application.use_case.check_cluster_certificate_health.response import (
    CheckClusterCertificateHealthResponse,
)


class CheckClusterCertificateHealthUseCase:
    def __init__(self, port: ClusterCertificateHealthPort) -> None:
        self._port = port

    def execute(
        self, command: CheckClusterCertificateHealthCommand
    ) -> CheckClusterCertificateHealthResponse:
        return CheckClusterCertificateHealthResponse()

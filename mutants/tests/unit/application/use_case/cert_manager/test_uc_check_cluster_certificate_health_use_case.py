from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cert_manager.cluster_certificate_health.cluster_certificate_health_use_case import (  # noqa: E501
    ClusterCertificateHealthUseCase,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.command import (
    ClusterCertificateHealthCommand,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.response import (
    ClusterCertificateHealthResponse,
)


class TestCheckClusterCertificateHealthUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = []
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(ClusterCertificateHealthCommand())

        assert isinstance(result, ClusterCertificateHealthResponse)

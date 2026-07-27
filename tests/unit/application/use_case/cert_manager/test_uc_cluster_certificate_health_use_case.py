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
from hexawyn.domain.models.certificate import ClusterCertificateReport


class TestClusterCertificateHealthUseCase:
    def test_execute_returns_cluster_certificate_health_response(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = []
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert isinstance(result, ClusterCertificateHealthResponse)
        assert isinstance(result.report, ClusterCertificateReport)
        assert result.error is None

    def test_execute_with_no_tls_secrets_returns_empty_report(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = []
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 0

    def test_execute_skips_namespace_on_permission_error(self) -> None:
        from hexawyn.domain.errors import InsufficientPermissionsError

        port = MagicMock()
        port.list_namespaces.return_value = ["default", "restricted"]
        port.list_tls_secrets.side_effect = [
            [],
            InsufficientPermissionsError(
                "Forbidden", context={"resource": "secrets", "namespace": "restricted"}
            ),
        ]
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert "restricted" in result.report.skipped_namespaces

from __future__ import annotations

from hexawyn.application.use_case.cert_manager.cluster_certificate_health.response import (
    ClusterCertificateHealthResponse,
)
from hexawyn.domain.models.certificate import ClusterCertificateReport


class TestClusterCertificateHealthResponse:
    def test_default_construction_report_is_none(self) -> None:
        response = ClusterCertificateHealthResponse()
        assert response.report is None
        assert response.error is None

    def test_can_set_report(self) -> None:
        report = ClusterCertificateReport(cluster_name="test-cluster")
        response = ClusterCertificateHealthResponse(report=report)
        assert response.report is report
        assert response.report.cluster_name == "test-cluster"

    def test_can_set_error(self) -> None:
        response = ClusterCertificateHealthResponse(error="connection refused")
        assert response.error == "connection refused"
        assert response.report is None

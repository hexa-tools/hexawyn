from __future__ import annotations

from abc import ABC
from unittest.mock import MagicMock

from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_service_port import (  # noqa: E501
    CheckClusterCertificateHealthServicePort,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.command import (
    ClusterCertificateHealthCommand,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.response import (
    ClusterCertificateHealthResponse,
)


def test_service_port_is_abc() -> None:
    assert issubclass(CheckClusterCertificateHealthServicePort, ABC)


def test_service_port_has_abstract_method() -> None:
    method = getattr(
        CheckClusterCertificateHealthServicePort, "check_cluster_certificate_health", None
    )
    assert method is not None
    assert hasattr(method, "__isabstractmethod__")


def test_can_mock_service_port() -> None:
    mock = MagicMock(spec=CheckClusterCertificateHealthServicePort)
    assert mock is not None


def test_method_accepts_cluster_certificate_health_command() -> None:
    port = MagicMock(spec=CheckClusterCertificateHealthServicePort)
    port.check_cluster_certificate_health(
        ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
    )
    assert True


def test_method_returns_cluster_certificate_health_response_type() -> None:
    mock_port = MagicMock(spec=CheckClusterCertificateHealthServicePort)
    mock_port.check_cluster_certificate_health.return_value = ClusterCertificateHealthResponse()
    result = mock_port.check_cluster_certificate_health(ClusterCertificateHealthCommand())
    assert isinstance(result, ClusterCertificateHealthResponse)

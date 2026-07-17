"""Unit tests for CheckClusterCertificateHealthUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_service_port import (
    CheckClusterCertificateHealthServicePort,
)
from hexawyn.application.use_case.check_cluster_certificate_health.check_cluster_certificate_health_use_case import (
    CheckClusterCertificateHealthUseCase,
)


class TestCheckClusterCertificateHealthUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CheckClusterCertificateHealthServicePort)
        use_case = CheckClusterCertificateHealthUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.check_cluster_certificate_health.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CheckClusterCertificateHealthServicePort)
        mock_service.check_cluster_certificate_health.side_effect = RuntimeError("test error")
        use_case = CheckClusterCertificateHealthUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())

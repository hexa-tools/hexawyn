"""Unit tests for ScanContainerVulnerabilitiesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_service_port import (
    ScanContainerVulnerabilitiesServicePort,
)
from hexawyn.application.use_case.scan_container_vulnerabilities.scan_container_vulnerabilities_use_case import (
    ScanContainerVulnerabilitiesUseCase,
)


class TestScanContainerVulnerabilitiesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ScanContainerVulnerabilitiesServicePort)
        use_case = ScanContainerVulnerabilitiesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.scan_vulnerabilities.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ScanContainerVulnerabilitiesServicePort)
        mock_service.scan_vulnerabilities.side_effect = RuntimeError("test error")
        use_case = ScanContainerVulnerabilitiesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())

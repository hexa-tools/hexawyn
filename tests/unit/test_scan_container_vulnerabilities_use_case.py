from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_response import (
    ScanContainerVulnerabilitiesResponse,
)
from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_service_port import (
    ScanContainerVulnerabilitiesServicePort,
)
from hexawyn.application.use_case.scan_container_vulnerabilities.scan_container_vulnerabilities_use_case import (
    ScanContainerVulnerabilitiesUseCase,
)


class TestScanContainerVulnerabilitiesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=ScanContainerVulnerabilitiesServicePort)
        expected = ScanContainerVulnerabilitiesResponse()
        service.scan_vulnerabilities.return_value = expected
        use_case = ScanContainerVulnerabilitiesUseCase(service=service)
        command = ScanContainerVulnerabilitiesCommand()

        result = use_case.execute(command)

        service.scan_vulnerabilities.assert_called_once_with(command)
        assert result is expected

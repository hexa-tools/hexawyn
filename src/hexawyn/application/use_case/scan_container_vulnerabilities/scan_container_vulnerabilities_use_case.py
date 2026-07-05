from __future__ import annotations

from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_response import (
    ScanContainerVulnerabilitiesResponse,
)
from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_service_port import (
    ScanContainerVulnerabilitiesServicePort,
)


class ScanContainerVulnerabilitiesUseCase:
    def __init__(self, service: ScanContainerVulnerabilitiesServicePort) -> None:
        self._svc = service

    def execute(
        self, command: ScanContainerVulnerabilitiesCommand
    ) -> ScanContainerVulnerabilitiesResponse:
        return self._svc.scan_vulnerabilities(command)

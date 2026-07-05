from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_response import (
    ScanContainerVulnerabilitiesResponse,
)


class ScanContainerVulnerabilitiesServicePort(ABC):
    @abstractmethod
    def scan_vulnerabilities(
        self, command: ScanContainerVulnerabilitiesCommand
    ) -> ScanContainerVulnerabilitiesResponse: ...

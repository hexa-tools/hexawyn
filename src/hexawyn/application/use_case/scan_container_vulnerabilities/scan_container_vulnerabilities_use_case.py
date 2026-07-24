from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
    ImageVulnerabilityScanPort,
)
from hexawyn.application.use_case.scan_container_vulnerabilities.command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.use_case.scan_container_vulnerabilities.response import (
    ScanContainerVulnerabilitiesResponse,
)


class ScanContainerVulnerabilitiesUseCase:
    def __init__(self, port: ImageVulnerabilityScanPort) -> None:
        self._port = port

    def execute(
        self, command: ScanContainerVulnerabilitiesCommand
    ) -> ScanContainerVulnerabilitiesResponse:
        return ScanContainerVulnerabilitiesResponse()

from __future__ import annotations


class TestScanContainerVulnerabilitiesCommand:
    def test_defaults_namespaces_to_none(self) -> None:
        from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_command import (
            ScanContainerVulnerabilitiesCommand,
        )

        command = ScanContainerVulnerabilitiesCommand()

        assert command.namespaces is None

    def test_accepts_custom_namespaces(self) -> None:
        from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_command import (
            ScanContainerVulnerabilitiesCommand,
        )

        command = ScanContainerVulnerabilitiesCommand(namespaces=["production"])

        assert command.namespaces == ["production"]

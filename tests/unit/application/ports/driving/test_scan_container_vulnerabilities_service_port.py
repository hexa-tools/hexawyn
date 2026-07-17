from __future__ import annotations

from abc import ABC

import pytest


class TestScanContainerVulnerabilitiesServicePort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_service_port import (
            ScanContainerVulnerabilitiesServicePort,
        )

        assert issubclass(ScanContainerVulnerabilitiesServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_service_port import (
            ScanContainerVulnerabilitiesServicePort,
        )

        with pytest.raises(TypeError):
            ScanContainerVulnerabilitiesServicePort()  # type: ignore[abstract]

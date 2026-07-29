from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.scan_container_vulnerabilities.command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.scan_container_vulnerabilities.response import (  # noqa: E501
    ScanContainerVulnerabilitiesResponse,
)
from hexawyn.application.use_case.security.scan_container_vulnerabilities.scan_container_vulnerabilities_use_case import (  # noqa: E501
    ScanContainerVulnerabilitiesUseCase,
)


class TestScanContainerVulnerabilitiesUseCase:
    def test_execute_returns_response(self) -> None:
        inventory = MagicMock()
        inventory.list_running_images.return_value = []
        scan = MagicMock()

        use_case = ScanContainerVulnerabilitiesUseCase(
            inventory_port=inventory,
            scan_port=scan,
        )
        result = use_case.execute(ScanContainerVulnerabilitiesCommand())

        assert isinstance(result, ScanContainerVulnerabilitiesResponse)
        assert result.total_images_scanned == 0

    def test_execute_scans_unique_images(self) -> None:
        inventory = MagicMock()
        inventory.list_running_images.return_value = [
            {"image": "nginx:1.25", "namespace": "default", "pod_name": "web"},
            {"image": "nginx:1.25", "namespace": "default", "pod_name": "web2"},
        ]
        scan = MagicMock()
        scan.scan_image.return_value = {
            "scan_status": "scanned",
            "cves": [],
            "detected_base_image": "debian:12",
            "scanned_at": "2025-01-15T10:00:00Z",
        }

        use_case = ScanContainerVulnerabilitiesUseCase(
            inventory_port=inventory,
            scan_port=scan,
        )
        result = use_case.execute(ScanContainerVulnerabilitiesCommand())

        assert result.total_images_scanned == 1
        assert scan.scan_image.call_count == 1
        assert result.findings[0]["image"] == "nginx:1.25"

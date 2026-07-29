from __future__ import annotations

from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
    ImageVulnerabilityScanPort,
)
from hexawyn.application.use_case.security.scan_container_vulnerabilities.command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.scan_container_vulnerabilities.response import (
    ScanContainerVulnerabilitiesResponse,
)


class ScanContainerVulnerabilitiesUseCase:
    def __init__(
        self,
        inventory_port: ImageInventoryPort,
        scan_port: ImageVulnerabilityScanPort,
    ) -> None:
        self._inventory = inventory_port
        self._scan = scan_port

    def execute(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

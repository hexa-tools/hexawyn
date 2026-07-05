"""MCP tool: scan_container_vulnerabilities — lists every unique container
image currently running in the cluster, scans each for known CVEs, flags
deprecated/EOL base images, and prioritizes Critical CVEs running in
production."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.scan_container_vulnerabilities.scan_container_vulnerabilities_command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.use_case.scan_container_vulnerabilities.scan_container_vulnerabilities_use_case import (
    ScanContainerVulnerabilitiesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def scan_container_vulnerabilities(namespaces: list[str] | None = None) -> dict[str, object]:
    from hexawyn.application.service.container_image_vulnerability_service import (
        ContainerImageVulnerabilityService,
    )
    from hexawyn.mcp.server import (
        build_image_inventory_adapter,
        build_image_vulnerability_scan_adapter,
    )

    try:
        service = ContainerImageVulnerabilityService(
            image_inventory_port=build_image_inventory_adapter(),
            vulnerability_scan_port=build_image_vulnerability_scan_adapter(),
        )
        r = ScanContainerVulnerabilitiesUseCase(service=service).execute(
            ScanContainerVulnerabilitiesCommand(namespaces=namespaces)
        )
        return {
            "findings": r.findings,
            "total_images_scanned": r.total_images_scanned,
            "images_with_critical_cves": r.images_with_critical_cves,
            "eol_image_count": r.eol_image_count,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(scan_container_vulnerabilities)

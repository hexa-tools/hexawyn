"""MCP tool: scan_container_vulnerabilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.scan_container_vulnerabilities.command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.use_case.scan_container_vulnerabilities.scan_container_vulnerabilities_use_case import (
    ScanContainerVulnerabilitiesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def scan_container_vulnerabilities() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(scan_container_vulnerabilities)

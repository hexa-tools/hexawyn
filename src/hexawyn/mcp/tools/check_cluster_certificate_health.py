"""MCP tool: check_cluster_certificate_health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.check_cluster_certificate_health.check_cluster_certificate_health_use_case import (
    CheckClusterCertificateHealthUseCase,
)
from hexawyn.application.use_case.check_cluster_certificate_health.command import (
    CheckClusterCertificateHealthCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def check_cluster_certificate_health() -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CheckClusterCertificateHealthUseCase(port=build_fleet_health_adapter())
        use_case.execute(CheckClusterCertificateHealthCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_cluster_certificate_health)

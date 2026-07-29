"""MCP tool: check_cluster_certificate_health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.cluster_certificate_health.cluster_certificate_health_use_case import (  # noqa: E501
    ClusterCertificateHealthUseCase,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.command import (
    ClusterCertificateHealthCommand,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from fastmcp import FastMCP


def check_cluster_certificate_health() -> dict[str, object]:
    from hexawyn.mcp.server import build_cluster_certificate_health_adapter

    try:
        use_case = ClusterCertificateHealthUseCase(port=build_cluster_certificate_health_adapter())
        response = use_case.check_cluster_certificate_health(ClusterCertificateHealthCommand())

        report = response.report
        if report is None:
            return {"error": "No report generated"}

        def _serialize_entries(
            entries: Sequence[object],
        ) -> list[dict[str, object]]:
            result: list[dict[str, object]] = []
            for e in entries:
                result.append(
                    {
                        "secret_name": getattr(e, "secret_name", ""),
                        "namespace": getattr(e, "namespace", ""),
                        "common_name": getattr(e, "common_name", ""),
                        "expiry_date": str(getattr(e, "expiry_date", "")),
                        "days_remaining": getattr(e, "days_remaining", 0),
                        "issuer": getattr(e, "issuer", ""),
                        "severity": getattr(e, "severity", ""),
                        "is_orphan": getattr(e, "is_orphan", False),
                        "error_message": getattr(e, "error_message", ""),
                    }
                )
            return result

        return {
            "cluster_name": report.cluster_name,
            "total_scanned": report.total_scanned,
            "expired": _serialize_entries(report.expired),
            "critical": _serialize_entries(report.critical),
            "warning": _serialize_entries(report.warning),
            "healthy": _serialize_entries(report.healthy),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_cluster_certificate_health)

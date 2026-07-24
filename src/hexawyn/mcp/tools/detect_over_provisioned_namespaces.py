"""MCP tool: detect_over_provisioned_namespaces — FinOps waste analysis across namespaces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.detect_over_provisioned_namespaces.command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_use_case import (
    DetectOverProvisionedNamespacesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_over_provisioned_namespaces(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    """Register detect_over_provisioned_namespaces as an MCP tool."""
    mcp.tool()(detect_over_provisioned_namespaces)

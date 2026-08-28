"""MCP tool: calico_felix_metrics — per-policy Felix allow/deny counters."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_felix_metrics.calico_felix_metrics_use_case import (
    CalicoFelixMetricsUseCase,
)
from hexawyn.application.use_case.calico.calico_felix_metrics.command import (
    CalicoFelixMetricsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _policy_dict(counter: object) -> dict[str, object]:
    """Project a CalicoFelixPolicyCounter into a plain, serialisable dict."""
    return {
        "policy": getattr(counter, "policy", None),
        "allow_packets": getattr(counter, "allow_packets", 0),
        "deny_packets": getattr(counter, "deny_packets", 0),
        "allow_bytes": getattr(counter, "allow_bytes", 0),
        "deny_bytes": getattr(counter, "deny_bytes", 0),
    }


def calico_felix_metrics() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoFelixMetricsUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoFelixMetricsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "metrics_available": result.metrics_available,
            "metrics_message": result.metrics_message,
            "total_denies": result.total_denies,
            "total_allows": result.total_allows,
            "deny_policy_count": result.deny_policy_count,
            "policies": [_policy_dict(counter) for counter in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "metrics_available": False,
            "metrics_message": None,
            "total_denies": 0,
            "total_allows": 0,
            "deny_policy_count": 0,
            "policies": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_felix_metrics)

"""MCP tool: get_calico_host_endpoints — list Calico HostEndpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.get_calico_host_endpoints.command import (
    GetCalicoHostEndpointsCommand,
)
from hexawyn.application.use_case.calico.get_calico_host_endpoints.get_calico_host_endpoints_use_case import (  # noqa: E501
    GetCalicoHostEndpointsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _endpoint_dict(endpoint: object) -> dict[str, object]:
    """Project a CalicoHostEndpoint into a plain, serialisable dict."""
    return {
        "name": getattr(endpoint, "name", None),
        "node": getattr(endpoint, "node", None),
        "interface_name": getattr(endpoint, "interface_name", None),
        "expected_ip": getattr(endpoint, "expected_ip", None),
        "expected_ips": list(getattr(endpoint, "expected_ips", ())),
        "labels": [list(label) for label in getattr(endpoint, "labels", ())],
        "applied_policies": list(getattr(endpoint, "applied_policies", ())),
    }


def get_calico_host_endpoints() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoHostEndpointsUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoHostEndpointsCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "endpoints": [_endpoint_dict(endpoint) for endpoint in result.endpoints],
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "total": 0,
            "endpoints": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_calico_host_endpoints)

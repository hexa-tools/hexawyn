"""MCP tool: certs_detect — Detect if Cert-Manager is installed."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.certs_detect.certs_detect_use_case import CertsDetectUseCase
from hexawyn.application.use_case.certs_detect.command import CertsDetectCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsDetectUseCase(cert_manager_port=adapter)
        r = uc.execute(CertsDetectCommand())
        return {
            "installed": r.installed,
            "version": r.version,
            "namespace": r.namespace,
            "total_certs": r.total_certs,
            "ready_certs": r.ready_certs,
            "expiring_soon": r.expiring_soon,
            "failed_certs": r.failed_certs,
            "active_challenges": r.active_challenges,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "version": None,
            "namespace": None,
            "total_certs": 0,
            "ready_certs": 0,
            "expiring_soon": 0,
            "failed_certs": 0,
            "active_challenges": 0,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_detect)

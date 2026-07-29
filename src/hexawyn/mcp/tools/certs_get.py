"""MCP tool: certs_get — Get detailed status of a specific certificate."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.certs_get.certs_get_use_case import CertsGetUseCase
from hexawyn.application.use_case.cert_manager.certs_get.command import CertsGetCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_get)

"""MCP tool: certs_issuer_get — Get detail of a specific Issuer."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.certs_issuer_get.certs_issuer_get_command import (
    CertsIssuerGetCommand,
)
from hexawyn.application.use_case.certs_issuer_get.certs_issuer_get_use_case import (
    CertsIssuerGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_issuer_get(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.certs_issuer_get_service import CertsIssuerGetService
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        svc = CertsIssuerGetService(port=adapter)
        uc = CertsIssuerGetUseCase(service=svc)
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_issuer_get)

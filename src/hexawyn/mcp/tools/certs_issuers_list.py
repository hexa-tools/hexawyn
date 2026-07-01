"""MCP tool: certs_issuers_list — List all Issuers and ClusterIssuers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.certs_issuers_list.certs_issuers_list_command import (
    CertsIssuersListCommand,
)
from hexawyn.application.use_case.certs_issuers_list.certs_issuers_list_use_case import (
    CertsIssuersListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_issuers_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.certs_issuers_list_service import CertsIssuersListService
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        svc = CertsIssuersListService(port=adapter)
        uc = CertsIssuersListUseCase(service=svc)
        r = uc.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": r.issuers, "error": r.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_issuers_list)

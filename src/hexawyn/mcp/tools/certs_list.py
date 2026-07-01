"""MCP tool: certs_list — List all certificates with expiration status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.certs_list.certs_list_command import CertsListCommand
from hexawyn.application.use_case.certs_list.certs_list_use_case import CertsListUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.certs_list_service import CertsListService
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        svc = CertsListService(port=adapter)
        uc = CertsListUseCase(service=svc)
        r = uc.execute(CertsListCommand(namespace=namespace))
        return {"certificates": r.certificates, "error": r.error}
    except Exception as exc:
        return {"certificates": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_list)

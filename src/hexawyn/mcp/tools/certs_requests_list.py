"""MCP tool: certs_requests_list — List recent CertificateRequests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_command import (
    CertsRequestsListCommand,
)
from hexawyn.application.use_case.certs_requests_list.certs_requests_list_use_case import (
    CertsRequestsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_requests_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.certs_requests_list_service import CertsRequestsListService
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        svc = CertsRequestsListService(port=adapter)
        uc = CertsRequestsListUseCase(service=svc)
        r = uc.execute(CertsRequestsListCommand(namespace=namespace))
        return {"requests": r.requests, "error": r.error}
    except Exception as exc:
        return {"requests": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_requests_list)

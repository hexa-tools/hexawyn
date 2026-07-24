"""MCP tool: certs_list — List all certificates."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.certs_list.certs_list_use_case import CertsListUseCase
from hexawyn.application.use_case.certs_list.command import CertsListCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsListUseCase(cert_manager_port=adapter)
        response = use_case.execute(CertsListCommand(namespace=namespace))
        return {"certificates": response.certificates, "error": response.error}
    except Exception as exc:
        return {"certificates": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_list)

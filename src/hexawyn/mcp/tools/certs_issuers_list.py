"""MCP tool: certs_issuers_list — List all Issuers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.certs_issuers_list.certs_issuers_list_use_case import (  # noqa: E501
    CertsIssuersListUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_issuers_list.command import (
    CertsIssuersListCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_issuers_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_issuers_list)

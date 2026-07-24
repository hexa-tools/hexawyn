"""MCP tool: certs_challenges_list — List ACME challenges."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.certs_challenges_list.certs_challenges_list_use_case import (
    CertsChallengesListUseCase,
)
from hexawyn.application.use_case.certs_challenges_list.command import CertsChallengesListCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_challenges_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsChallengesListUseCase(cert_manager_port=adapter)
        response = use_case.execute(CertsChallengesListCommand(namespace=namespace))
        return {"challenges": response.challenges, "error": response.error}
    except Exception as exc:
        return {"challenges": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_challenges_list)

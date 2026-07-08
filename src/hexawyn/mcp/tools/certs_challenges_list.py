"""MCP tool: certs_challenges_list — List ACME challenges."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_command import (
    CertsChallengesListCommand,
)
from hexawyn.application.use_case.certs_challenges_list.certs_challenges_list_use_case import (
    CertsChallengesListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_challenges_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.certs_challenges_list_service import CertsChallengesListService
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        svc = CertsChallengesListService(port=adapter)
        uc = CertsChallengesListUseCase(service=svc)
        r = uc.execute(CertsChallengesListCommand(namespace=namespace))
        return {"challenges": r.challenges, "error": r.error}
    except Exception as exc:
        return {"challenges": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_challenges_list)

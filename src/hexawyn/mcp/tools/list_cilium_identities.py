"""MCP tool: list_cilium_identities — Cilium security identity list."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.list_cilium_identities.command import (
    ListCiliumIdentitiesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_identities.list_cilium_identities_use_case import (  # noqa: E501
    ListCiliumIdentitiesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_cilium_identities() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumIdentitiesUseCase(port=adapter)
        result = use_case.execute(ListCiliumIdentitiesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_identities": result.total_identities,
            "identities": result.identities,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_identities": 0,
            "identities": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_cilium_identities)

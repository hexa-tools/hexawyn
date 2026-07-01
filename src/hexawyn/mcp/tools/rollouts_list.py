"""MCP tool: rollouts_list — List all Argo Rollouts with strategy and phase."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.rollouts_list.rollouts_list_command import (
    RolloutsListCommand,
)
from hexawyn.application.use_case.rollouts_list.rollouts_list_use_case import (
    RolloutsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def rollouts_list(namespace: str | None = None) -> dict[str, object]:
    """List all Argo Rollouts with their strategy and current phase.

    Args:
        namespace: Optional namespace filter.
    """
    from hexawyn.application.service.rollouts_list_service import RolloutsListService
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        service = RolloutsListService(rollouts_port=adapter)
        use_case = RolloutsListUseCase(service=service)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(rollouts_list)

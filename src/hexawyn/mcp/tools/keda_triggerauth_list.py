"""MCP tool: keda_triggerauth_list — List KEDA TriggerAuthentications."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda_triggerauth_list.command import KedaTriggerauthListCommand
from hexawyn.application.use_case.keda_triggerauth_list.keda_triggerauth_list_use_case import (
    KedaTriggerAuthListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_triggerauth_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaTriggerAuthListUseCase(keda_port=adapter)
        response = use_case.execute(KedaTriggerauthListCommand(namespace=namespace))
        return {"trigger_auths": response.trigger_auths, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_triggerauth_list)

"""keda_triggerauth_list.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.keda_triggerauth_list.keda_triggerauth_list_command import (
    KedaTriggerAuthListCommand,
)
from hexawyn.application.use_case.keda_triggerauth_list.keda_triggerauth_list_use_case import (
    KedaTriggerAuthListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_triggerauth_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.keda_triggerauth_list_service import KedaTriggerAuthListService
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        svc = KedaTriggerAuthListService(port=a)
        uc = KedaTriggerAuthListUseCase(service=svc)
        r = uc.execute(KedaTriggerAuthListCommand(namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_triggerauth_list)

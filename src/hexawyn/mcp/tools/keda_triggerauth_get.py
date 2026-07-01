"""keda_triggerauth_get.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_command import (
    KedaTriggerAuthGetCommand,
)
from hexawyn.application.use_case.keda_triggerauth_get.keda_triggerauth_get_use_case import (
    KedaTriggerAuthGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_triggerauth_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.application.service.keda_triggerauth_get_service import KedaTriggerAuthGetService
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        svc = KedaTriggerAuthGetService(port=a)
        uc = KedaTriggerAuthGetUseCase(service=svc)
        r = uc.execute(KedaTriggerAuthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_triggerauth_get)

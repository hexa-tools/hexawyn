"""keda_triggerauth_get.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda.keda_triggerauth_get.command import KedaTriggerauthGetCommand
from hexawyn.application.use_case.keda.keda_triggerauth_get.keda_triggerauth_get_use_case import (
    KedaTriggerauthGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_triggerauth_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_triggerauth_get)

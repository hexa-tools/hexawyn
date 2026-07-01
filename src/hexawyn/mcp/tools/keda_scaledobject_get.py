"""keda_scaledobject_get.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.keda_scaledobject_get.keda_scaledobject_get_command import (
    KedaScaledObjectGetCommand,
)
from hexawyn.application.use_case.keda_scaledobject_get.keda_scaledobject_get_use_case import (
    KedaScaledObjectGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobject_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.application.service.keda_scaledobject_get_service import KedaScaledObjectGetService
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        svc = KedaScaledObjectGetService(port=a)
        uc = KedaScaledObjectGetUseCase(service=svc)
        r = uc.execute(KedaScaledObjectGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledobject_get)

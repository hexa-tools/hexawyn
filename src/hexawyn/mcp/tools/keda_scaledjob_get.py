"""keda_scaledjob_get.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_command import (
    KedaScaledJobGetCommand,
)
from hexawyn.application.use_case.keda_scaledjob_get.keda_scaledjob_get_use_case import (
    KedaScaledJobGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledjob_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.application.service.keda_scaledjob_get_service import KedaScaledJobGetService
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        svc = KedaScaledJobGetService(port=a)
        uc = KedaScaledJobGetUseCase(service=svc)
        r = uc.execute(KedaScaledJobGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledjob_get)

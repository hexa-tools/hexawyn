"""keda_scaledjob_get.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda.keda_scaledjob_get.command import KedaScaledjobGetCommand
from hexawyn.application.use_case.keda.keda_scaledjob_get.keda_scaledjob_get_use_case import (
    KedaScaledjobGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledjob_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaScaledjobGetUseCase(port=a)
        r = uc.execute(KedaScaledjobGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledjob_get)

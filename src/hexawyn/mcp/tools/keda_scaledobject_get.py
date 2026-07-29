"""keda_scaledobject_get.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda.keda_scaledobject_get.command import (
    KedaScaledobjectGetCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_get.keda_scaledobject_get_use_case import (
    KedaScaledobjectGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobject_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaScaledobjectGetUseCase(port=a)
        r = uc.execute(KedaScaledobjectGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledobject_get)

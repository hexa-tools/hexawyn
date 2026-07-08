"""keda_scaledobjects_list.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_command import (
    KedaScaledObjectsListCommand,
)
from hexawyn.application.use_case.keda_scaledobjects_list.keda_scaledobjects_list_use_case import (
    KedaScaledObjectsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobjects_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.keda_scaledobjects_list_service import (
        KedaScaledObjectsListService,
    )
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        svc = KedaScaledObjectsListService(port=a)
        uc = KedaScaledObjectsListUseCase(service=svc)
        r = uc.execute(KedaScaledObjectsListCommand(namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledobjects_list)

"""keda_scaledobject_status.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_command import (
    KedaScaledObjectStatusCommand,
)
from hexawyn.application.use_case.keda_scaledobject_status.keda_scaledobject_status_use_case import (
    KedaScaledObjectStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobject_status(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.application.service.keda_scaledobject_status_service import (
        KedaScaledObjectStatusService,
    )
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        svc = KedaScaledObjectStatusService(port=a)
        uc = KedaScaledObjectStatusUseCase(service=svc)
        r = uc.execute(KedaScaledObjectStatusCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledobject_status)

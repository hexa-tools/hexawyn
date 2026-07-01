"""keda_scaledobject_triggers.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.keda_scaledobject_triggers.keda_scaledobject_triggers_command import (
    KedaScaledObjectTriggersCommand,
)
from hexawyn.application.use_case.keda_scaledobject_triggers.keda_scaledobject_triggers_use_case import (
    KedaScaledObjectTriggersUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobject_triggers(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.application.service.keda_scaledobject_triggers_service import (
        KedaScaledObjectTriggersService,
    )
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        svc = KedaScaledObjectTriggersService(port=a)
        uc = KedaScaledObjectTriggersUseCase(service=svc)
        r = uc.execute(KedaScaledObjectTriggersCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledobject_triggers)

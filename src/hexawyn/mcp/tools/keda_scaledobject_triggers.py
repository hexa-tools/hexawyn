"""MCP tool: keda_scaledobject_triggers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda_scaledobject_triggers.command import (
    KedaScaledobjectTriggersCommand,
)
from hexawyn.application.use_case.keda_scaledobject_triggers.keda_scaledobject_triggers_use_case import (
    KedaScaledObjectTriggersUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobject_triggers(name="test-name", namespace="test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        use_case = KedaScaledObjectTriggersUseCase(keda_port=build_keda_adapter())
        _ = use_case.execute(KedaScaledobjectTriggersCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledobject_triggers)

"""MCP tool: keda_scaledobjects_list — List KEDA ScaledObjects."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda_scaledobjects_list.command import (
    KedaScaledobjectsListCommand,
)
from hexawyn.application.use_case.keda_scaledobjects_list.keda_scaledobjects_list_use_case import (
    KedaScaledObjectsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobjects_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledObjectsListUseCase(keda_port=adapter)
        response = use_case.execute(KedaScaledobjectsListCommand(namespace=namespace))
        return {"scaled_objects": response.scaled_objects, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledobjects_list)

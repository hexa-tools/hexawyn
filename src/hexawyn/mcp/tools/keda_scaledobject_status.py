"""MCP tool: keda_scaledobject_status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda_scaledobject_status.command import (
    KedaScaledobjectStatusCommand,
)
from hexawyn.application.use_case.keda_scaledobject_status.keda_scaledobject_status_use_case import (
    KedaScaledObjectStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobject_status(name="test-name", namespace="test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        use_case = KedaScaledObjectStatusUseCase(keda_port=build_keda_adapter())
        _ = use_case.execute(KedaScaledobjectStatusCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledobject_status)

# mypy: ignore-errors
"""MCP tool: keda_scaledobject_triggers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda.keda_scaledobject_triggers.command import (
    KedaScaledobjectTriggersCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_triggers.keda_scaledobject_triggers_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    KedaScaledObjectTriggersUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledobject_triggers(
    name: str = "test-name", namespace: str = "test-ns"
) -> dict[str, object]:  # type: ignore[no-untyped-def]  # noqa: E501
    from hexawyn.mcp.server import build_keda_adapter

    try:
        use_case = KedaScaledObjectTriggersUseCase(keda_port=build_keda_adapter())
        _ = use_case.execute(KedaScaledobjectTriggersCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(keda_scaledobject_triggers)

"""MCP tool: get_namespace_events."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.get_namespace_events.command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_namespace_events.get_namespace_events_use_case import (  # noqa: E501
    GetNamespaceEventsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_namespace_events(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetNamespaceEventsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetNamespaceEventsCommand(namespace=namespace))  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_namespace_events)

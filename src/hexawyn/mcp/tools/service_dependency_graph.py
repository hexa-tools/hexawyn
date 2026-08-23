# mypy: ignore-errors
"""MCP tool: service_dependency_graph."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.service_dependency_graph.command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.use_case.observability.service_dependency_graph.service_dependency_graph_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    UseCaseDependencyGraphUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def service_dependency_graph() -> dict[str, object]:
    from hexawyn.mcp.server import build_service_dependency_graph_adapter

    try:
        use_case = UseCaseDependencyGraphUseCase(port=build_service_dependency_graph_adapter())
        _ = use_case.execute(ServiceDependencyGraphCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(service_dependency_graph)

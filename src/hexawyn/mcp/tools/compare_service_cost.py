"""MCP tool: compare_service_cost."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.compare_service_cost.command import CompareServiceCostCommand
from hexawyn.application.use_case.compare_service_cost.compare_service_cost_use_case import (
    CompareServiceCostUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compare_service_cost(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareServiceCostUseCase(port=build_service_cost_adapter())
        _ = use_case.execute(CompareServiceCostCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(compare_service_cost)

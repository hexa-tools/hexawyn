"""MCP tool: compute_slo_error_budget."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.compute_slo_error_budget.command import (
    ComputeSloErrorBudgetCommand,
)
from hexawyn.application.use_case.compute_slo_error_budget.compute_slo_error_budget_use_case import (
    ComputeSLOErrorBudgetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_slo_error_budget(service_name="test-service_name") -> dict[str, object]:
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSloErrorBudgetCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_slo_error_budget)

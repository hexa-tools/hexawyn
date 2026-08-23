# mypy: ignore-errors
"""MCP tool: compute_slo_error_budget."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.compute_slo_error_budget.command import (  # type: ignore
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.use_case.workloads.compute_slo_error_budget.compute_slo_error_budget_use_case import (  # noqa: E501
    ComputeSLOErrorBudgetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_slo_error_budget(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(compute_slo_error_budget)

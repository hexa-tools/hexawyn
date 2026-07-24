"""MCP tool: project_budget."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.project_budget.command import ProjectBudgetCommand
from hexawyn.application.use_case.project_budget.project_budget_use_case import ProjectBudgetUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def project_budget() -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_projection_adapter

    try:
        use_case = ProjectBudgetUseCase(port=build_budget_projection_adapter())
        _ = use_case.execute(ProjectBudgetCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(project_budget)

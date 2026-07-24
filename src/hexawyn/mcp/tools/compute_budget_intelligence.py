"""MCP tool: compute_budget_intelligence — Compute budget intelligence."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.compute_budget_intelligence.command import (
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.use_case.compute_budget_intelligence.compute_budget_intelligence_use_case import (
    ComputeBudgetIntelligenceUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_budget_intelligence(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        use_case = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_budget_intelligence)

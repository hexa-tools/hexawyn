"""MCP tool: conservative_namespace_overview — compact, token-budgeted namespace health overview."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.conservative_namespace_overview.command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.conservative_namespace_overview.conservative_namespace_overview_use_case import (
    ConservativeNamespaceOverviewUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def conservative_namespace_overview(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(conservative_namespace_overview)

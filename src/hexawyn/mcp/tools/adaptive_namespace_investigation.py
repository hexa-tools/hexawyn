"""MCP tool: adaptive_namespace_investigation — namespace investigation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.adaptive_namespace_investigation.adaptive_namespace_investigation_use_case import (
    AdaptiveNamespaceInvestigationUseCase,
)
from hexawyn.application.use_case.adaptive_namespace_investigation.command import (
    AdaptiveNamespaceInvestigationCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def adaptive_namespace_investigation(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "overview_summary": r.overview_summary,
            "investigated_resources": r.investigated_resources,
            "root_cause_candidates": r.root_cause_candidates,
            "recommended_actions": r.recommended_actions,
            "skipped_resources": r.skipped_resources,
            "node_pressure_context": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(adaptive_namespace_investigation)

"""MCP tool: adaptive_namespace_investigation — starts with a conservative
namespace overview, then automatically drills into the most critical failing
resources."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.use_case.adaptive_namespace_investigation.adaptive_namespace_investigation_use_case import (
    AdaptiveNamespaceInvestigationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def adaptive_namespace_investigation(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_service_port import (
        ConservativeNamespaceOverviewServicePort,
    )
    from hexawyn.application.service.adaptive_namespace_investigation_service import (
        AdaptiveNamespaceInvestigationService,
    )
    from hexawyn.application.service.conservative_namespace_overview_service import (
        ConservativeNamespaceOverviewService,
    )
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        overview_service: ConservativeNamespaceOverviewServicePort = (
            ConservativeNamespaceOverviewService(
                port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
            )
        )
        service = AdaptiveNamespaceInvestigationService(
            overview_service=overview_service,
            k8s_port=build_k8s_adapter(),
            investigation_port=build_adaptive_investigation_adapter(),
        )
        r = AdaptiveNamespaceInvestigationUseCase(service=service).execute(
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

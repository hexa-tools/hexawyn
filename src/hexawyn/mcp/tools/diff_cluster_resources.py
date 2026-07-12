"""MCP tool: diff_cluster_resources — diff resources between two clusters
(staging vs production), showing missing, unpromoted, and version mismatches."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_command import (  # noqa: E501
    DiffClusterResourcesCommand,
)
from hexawyn.application.use_case.diff_cluster_resources.diff_cluster_resources_use_case import (  # noqa: E501
    DiffClusterResourcesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.cluster_diff import ResourceDiff


def diff_cluster_resources(source_context: str, target_context: str) -> dict[str, object]:
    from hexawyn.application.service.diff_cluster_resources_service import (
        DiffClusterResourcesService,
    )
    from hexawyn.mcp.server import build_cluster_diff_adapter

    try:
        adapter = build_cluster_diff_adapter()
        service = DiffClusterResourcesService(cluster_diff_port=adapter)
        use_case = DiffClusterResourcesUseCase(service=service)
        response = use_case.execute(
            DiffClusterResourcesCommand(
                source_context=source_context, target_context=target_context
            )
        )
        r = response.result
        return {
            "source_cluster": r.source_cluster,
            "target_cluster": r.target_cluster,
            "sync_status": r.sync_status,
            "total_differences": r.total_differences,
            "in_staging_not_prod": [_serialize(d) for d in r.in_staging_not_prod],
            "version_mismatches": [_serialize(d) for d in r.version_mismatches],
            "prod_only": [_serialize(d) for d in r.prod_only],
            "promotion_checklist": {
                "ready_to_promote": r.promotion_checklist.ready_to_promote
                if r.promotion_checklist
                else [],
                "requires_review": r.promotion_checklist.requires_review
                if r.promotion_checklist
                else [],
            },
            "has_data": r.has_data,
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "source_cluster": source_context,
            "target_cluster": target_context,
            "sync_status": "in_sync",
            "total_differences": 0,
            "in_staging_not_prod": [],
            "version_mismatches": [],
            "prod_only": [],
            "promotion_checklist": {"ready_to_promote": [], "requires_review": []},
            "has_data": False,
            "warning": "",
            "error": str(exc),
        }


def _serialize(d: ResourceDiff) -> dict[str, object]:
    return {
        "resource": d.resource,
        "namespace": d.namespace,
        "reason": d.reason,
        "priority": d.priority,
        "staging_value": d.staging_value,
        "prod_value": d.prod_value,
        "detail": d.detail,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(diff_cluster_resources)

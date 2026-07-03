"""MCP tool: search_resources_by_labels — find K8s resources by label selector."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.use_case.search_resources_by_labels.search_resources_by_labels_use_case import (
    SearchResourcesByLabelsUseCase,
)
from hexawyn.domain.models.label_search import ResourceType

if TYPE_CHECKING:
    from fastmcp import FastMCP

_ALL_RESOURCE_TYPES: list[ResourceType] = ["pods", "deployments", "services", "configmaps"]


def search_resources_by_labels(
    label_selector: str,
    resource_types: list[ResourceType] | None = None,
    namespace: str | None = None,
) -> dict[str, object]:
    from hexawyn.application.service.search_resources_by_labels_service import (
        SearchResourcesByLabelsService,
    )
    from hexawyn.mcp.server import build_k8s_adapter, build_resource_search_adapter

    try:
        service = SearchResourcesByLabelsService(
            port=build_resource_search_adapter(), k8s_port=build_k8s_adapter()
        )
        r = SearchResourcesByLabelsUseCase(service=service).execute(
            SearchResourcesByLabelsCommand(
                label_selector=label_selector,
                resource_types=resource_types or list(_ALL_RESOURCE_TYPES),
                namespace=namespace,
            )
        )
        return {
            "label_selector": r.label_selector,
            "total_matched": r.total_matched,
            "groups": r.groups,
            "has_more": r.has_more,
            "remaining_count": r.remaining_count,
            "no_matches": r.no_matches,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"label_selector": label_selector, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(search_resources_by_labels)

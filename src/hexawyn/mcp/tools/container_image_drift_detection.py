"""MCP tool: detect_container_image_drift — flags running Deployment
container images that differ (tag or digest) from what's declared in the
Helm-release or Kustomize-rendered manifest."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.container_image_drift.container_image_drift_command import (
    ContainerImageDriftCommand,
)
from hexawyn.application.use_case.container_image_drift.container_image_drift_use_case import (
    ContainerImageDriftUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_container_image_drift(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.application.service.container_image_drift_service import (
        ContainerImageDriftService,
    )
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_image_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ContainerImageDriftService(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
            image_drift_port=build_image_drift_adapter(),
        )
        r = ContainerImageDriftUseCase(service=service).execute(
            ContainerImageDriftCommand(namespace=namespace, kustomize_paths=kustomize_paths or [])
        )
        return {
            "out_of_sync": r.out_of_sync,
            "in_sync_count": r.in_sync_count,
            "excluded_count": r.excluded_count,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_container_image_drift)

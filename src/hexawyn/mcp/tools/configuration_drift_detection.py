"""MCP tool: configuration_drift_detection — compares live Kubernetes
resources against their rendered Helm/Kustomize desired state, flagging
drifted fields and orphaned resources."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.configuration_drift_detection.command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.use_case.configuration_drift_detection.configuration_drift_detection_use_case import (
    ConfigurationDriftDetectionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def configuration_drift_detection(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        use_case = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_drift_port=build_helm_drift_adapter(),
            kustomize_drift_port=build_kustomize_drift_adapter(),
        )
        r = use_case.execute(
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(configuration_drift_detection)

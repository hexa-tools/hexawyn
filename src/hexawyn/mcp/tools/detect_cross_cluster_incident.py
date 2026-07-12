"""MCP tool: detect_cross_cluster_incident — detects whether the same failure
pattern is affecting multiple clusters simultaneously (global vs isolated)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.use_case.detect_cross_cluster_incident.detect_cross_cluster_incident_use_case import (  # noqa: E501
    DetectCrossClusterIncidentUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.cross_cluster_correlation import AffectedCluster


def detect_cross_cluster_incident(window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.application.service.detect_cross_cluster_incident_service import (
        DetectCrossClusterIncidentService,
    )
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        adapter = build_cross_cluster_incident_adapter()
        service = DetectCrossClusterIncidentService(incident_port=adapter)
        use_case = DetectCrossClusterIncidentUseCase(service=service)
        response = use_case.execute(
            DetectCrossClusterIncidentCommand(window_minutes=window_minutes)
        )
        r = response.result
        return {
            "scope": r.scope,
            "common_failure_type": r.common_failure_type,
            "common_factor": r.common_factor,
            "suggestion": r.suggestion,
            "cascading": r.cascading,
            "affected_clusters": [_serialize(c) for c in r.affected_clusters],
            "has_data": r.has_data,
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "scope": "none",
            "common_failure_type": "",
            "common_factor": "",
            "suggestion": "",
            "cascading": False,
            "affected_clusters": [],
            "has_data": False,
            "warning": "",
            "error": str(exc),
        }


def _serialize(c: AffectedCluster) -> dict[str, object]:
    return {
        "cluster_name": c.cluster_name,
        "onset_utc": c.onset_utc,
        "pod_count": c.pod_count,
        "failure_type": c.failure_type,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_cross_cluster_incident)

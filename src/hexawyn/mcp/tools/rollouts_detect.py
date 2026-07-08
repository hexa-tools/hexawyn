"""MCP tool: rollouts_detect — Detect if Argo Rollouts is installed."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.rollouts_detect.rollouts_detect_command import (
    RolloutsDetectCommand,
)
from hexawyn.application.use_case.rollouts_detect.rollouts_detect_use_case import (
    RolloutsDetectUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def rollouts_detect() -> dict[str, object]:
    """Detect if Argo Rollouts is installed in the cluster and return summary counts."""
    from hexawyn.application.service.rollouts_detect_service import (
        RolloutsDetectService,
    )
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        service = RolloutsDetectService(rollouts_port=adapter)
        use_case = RolloutsDetectUseCase(service=service)
        response = use_case.execute(RolloutsDetectCommand())
        return {
            "installed": response.installed,
            "version": response.version,
            "namespace": response.namespace,
            "total_rollouts": response.total_rollouts,
            "healthy": response.healthy,
            "progressing": response.progressing,
            "degraded": response.degraded,
            "paused": response.paused,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "version": None,
            "namespace": None,
            "total_rollouts": 0,
            "healthy": 0,
            "progressing": 0,
            "degraded": 0,
            "paused": 0,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(rollouts_detect)

"""MCP tool: rollout_status — Real-time status with canary weight and step info."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.rollout_status.rollout_status_command import (
    RolloutStatusCommand,
)
from hexawyn.application.use_case.rollout_status.rollout_status_use_case import (
    RolloutStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def rollout_status(name: str, namespace: str) -> dict[str, object]:
    """Get real-time status of a Rollout: phase, step, canary weight.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.application.service.rollout_status_service import (
        RolloutStatusService,
    )
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        service = RolloutStatusService(rollouts_port=adapter)
        use_case = RolloutStatusUseCase(service=service)
        response = use_case.execute(RolloutStatusCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "phase": response.phase,
            "strategy": response.strategy,
            "canary_weight": response.canary_weight,
            "step_index": response.step_index,
            "total_steps": response.total_steps,
            "current_step_type": response.current_step_type,
            "paused_at": response.paused_at,
            "pause_reason": response.pause_reason,
            "message": response.message,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(rollout_status)

"""MCP tool: rollout_get — Get detailed status of a specific Rollout."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.rollout_get.command import RolloutGetCommand
from hexawyn.application.use_case.rollout_get.rollout_get_use_case import RolloutGetUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def rollout_get(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "desired_replicas": response.desired_replicas,
            "ready_replicas": response.ready_replicas,
            "canary_replicas": response.canary_replicas,
            "stable_replicas": response.stable_replicas,
            "current_image": response.current_image,
            "stable_image": response.stable_image,
            "step_index": response.step_index,
            "total_steps": response.total_steps,
            "current_step_type": response.current_step_type,
            "canary_weight": response.canary_weight,
            "paused_at": response.paused_at,
            "pause_reason": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(rollout_get)

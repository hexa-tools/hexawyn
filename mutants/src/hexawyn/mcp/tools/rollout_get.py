"""MCP tool: rollout_get — Get detailed status of a specific Rollout."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.rollout_get.command import RolloutGetCommand
from hexawyn.application.use_case.workloads.rollout_get.rollout_get_use_case import (
    RolloutGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_rollout_get__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_rollout_get__mutmut)
def rollout_get(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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


def x_rollout_get__mutmut_orig(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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


def x_rollout_get__mutmut_1(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = None
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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


def x_rollout_get__mutmut_2(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = None  # type: ignore
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


def x_rollout_get__mutmut_3(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=None)  # type: ignore
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


def x_rollout_get__mutmut_4(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = None
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


def x_rollout_get__mutmut_5(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(None)
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


def x_rollout_get__mutmut_6(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=None, namespace=namespace))
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


def x_rollout_get__mutmut_7(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=None))
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


def x_rollout_get__mutmut_8(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(namespace=namespace))
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


def x_rollout_get__mutmut_9(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, ))
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


def x_rollout_get__mutmut_10(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "XXnameXX": response.name,
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


def x_rollout_get__mutmut_11(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "NAME": response.name,
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


def x_rollout_get__mutmut_12(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "XXnamespaceXX": response.namespace,
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


def x_rollout_get__mutmut_13(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "NAMESPACE": response.namespace,
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


def x_rollout_get__mutmut_14(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "XXstrategyXX": response.strategy,
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


def x_rollout_get__mutmut_15(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "STRATEGY": response.strategy,
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


def x_rollout_get__mutmut_16(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "XXphaseXX": response.phase,
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


def x_rollout_get__mutmut_17(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "PHASE": response.phase,
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


def x_rollout_get__mutmut_18(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "XXdesired_replicasXX": response.desired_replicas,
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


def x_rollout_get__mutmut_19(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "DESIRED_REPLICAS": response.desired_replicas,
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


def x_rollout_get__mutmut_20(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "desired_replicas": response.desired_replicas,
            "XXready_replicasXX": response.ready_replicas,
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


def x_rollout_get__mutmut_21(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "desired_replicas": response.desired_replicas,
            "READY_REPLICAS": response.ready_replicas,
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


def x_rollout_get__mutmut_22(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "desired_replicas": response.desired_replicas,
            "ready_replicas": response.ready_replicas,
            "XXcanary_replicasXX": response.canary_replicas,
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


def x_rollout_get__mutmut_23(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "desired_replicas": response.desired_replicas,
            "ready_replicas": response.ready_replicas,
            "CANARY_REPLICAS": response.canary_replicas,
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


def x_rollout_get__mutmut_24(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "desired_replicas": response.desired_replicas,
            "ready_replicas": response.ready_replicas,
            "canary_replicas": response.canary_replicas,
            "XXstable_replicasXX": response.stable_replicas,
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


def x_rollout_get__mutmut_25(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
        response = use_case.execute(RolloutGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "strategy": response.strategy,
            "phase": response.phase,
            "desired_replicas": response.desired_replicas,
            "ready_replicas": response.ready_replicas,
            "canary_replicas": response.canary_replicas,
            "STABLE_REPLICAS": response.stable_replicas,
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


def x_rollout_get__mutmut_26(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXcurrent_imageXX": response.current_image,
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


def x_rollout_get__mutmut_27(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "CURRENT_IMAGE": response.current_image,
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


def x_rollout_get__mutmut_28(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXstable_imageXX": response.stable_image,
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


def x_rollout_get__mutmut_29(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "STABLE_IMAGE": response.stable_image,
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


def x_rollout_get__mutmut_30(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXstep_indexXX": response.step_index,
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


def x_rollout_get__mutmut_31(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "STEP_INDEX": response.step_index,
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


def x_rollout_get__mutmut_32(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXtotal_stepsXX": response.total_steps,
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


def x_rollout_get__mutmut_33(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "TOTAL_STEPS": response.total_steps,
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


def x_rollout_get__mutmut_34(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXcurrent_step_typeXX": response.current_step_type,
            "canary_weight": response.canary_weight,
            "paused_at": response.paused_at,
            "pause_reason": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_35(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "CURRENT_STEP_TYPE": response.current_step_type,
            "canary_weight": response.canary_weight,
            "paused_at": response.paused_at,
            "pause_reason": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_36(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXcanary_weightXX": response.canary_weight,
            "paused_at": response.paused_at,
            "pause_reason": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_37(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "CANARY_WEIGHT": response.canary_weight,
            "paused_at": response.paused_at,
            "pause_reason": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_38(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXpaused_atXX": response.paused_at,
            "pause_reason": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_39(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "PAUSED_AT": response.paused_at,
            "pause_reason": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_40(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXpause_reasonXX": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_41(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "PAUSE_REASON": response.pause_reason,
            "message": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_42(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXmessageXX": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_43(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "MESSAGE": response.message,
            "analysis_run_name": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_44(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXanalysis_run_nameXX": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_45(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "ANALYSIS_RUN_NAME": response.analysis_run_name,
            "error": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_46(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "XXerrorXX": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_47(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
            "ERROR": response.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_48(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"XXnameXX": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_49(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"NAME": "", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_50(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"name": "XXXX", "namespace": "", "error": str(exc)}


def x_rollout_get__mutmut_51(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"name": "", "XXnamespaceXX": "", "error": str(exc)}


def x_rollout_get__mutmut_52(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"name": "", "NAMESPACE": "", "error": str(exc)}


def x_rollout_get__mutmut_53(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"name": "", "namespace": "XXXX", "error": str(exc)}


def x_rollout_get__mutmut_54(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"name": "", "namespace": "", "XXerrorXX": str(exc)}


def x_rollout_get__mutmut_55(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"name": "", "namespace": "", "ERROR": str(exc)}


def x_rollout_get__mutmut_56(name: str, namespace: str) -> dict[str, object]:
    """Get detailed status of a specific Argo Rollout with step information.

    Args:
        name: Rollout name.
        namespace: Rollout namespace.
    """
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutGetUseCase(port=adapter)  # type: ignore
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
        return {"name": "", "namespace": "", "error": str(None)}

mutants_x_rollout_get__mutmut['_mutmut_orig'] = x_rollout_get__mutmut_orig # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_1'] = x_rollout_get__mutmut_1 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_2'] = x_rollout_get__mutmut_2 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_3'] = x_rollout_get__mutmut_3 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_4'] = x_rollout_get__mutmut_4 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_5'] = x_rollout_get__mutmut_5 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_6'] = x_rollout_get__mutmut_6 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_7'] = x_rollout_get__mutmut_7 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_8'] = x_rollout_get__mutmut_8 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_9'] = x_rollout_get__mutmut_9 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_10'] = x_rollout_get__mutmut_10 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_11'] = x_rollout_get__mutmut_11 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_12'] = x_rollout_get__mutmut_12 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_13'] = x_rollout_get__mutmut_13 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_14'] = x_rollout_get__mutmut_14 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_15'] = x_rollout_get__mutmut_15 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_16'] = x_rollout_get__mutmut_16 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_17'] = x_rollout_get__mutmut_17 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_18'] = x_rollout_get__mutmut_18 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_19'] = x_rollout_get__mutmut_19 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_20'] = x_rollout_get__mutmut_20 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_21'] = x_rollout_get__mutmut_21 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_22'] = x_rollout_get__mutmut_22 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_23'] = x_rollout_get__mutmut_23 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_24'] = x_rollout_get__mutmut_24 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_25'] = x_rollout_get__mutmut_25 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_26'] = x_rollout_get__mutmut_26 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_27'] = x_rollout_get__mutmut_27 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_28'] = x_rollout_get__mutmut_28 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_29'] = x_rollout_get__mutmut_29 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_30'] = x_rollout_get__mutmut_30 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_31'] = x_rollout_get__mutmut_31 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_32'] = x_rollout_get__mutmut_32 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_33'] = x_rollout_get__mutmut_33 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_34'] = x_rollout_get__mutmut_34 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_35'] = x_rollout_get__mutmut_35 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_36'] = x_rollout_get__mutmut_36 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_37'] = x_rollout_get__mutmut_37 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_38'] = x_rollout_get__mutmut_38 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_39'] = x_rollout_get__mutmut_39 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_40'] = x_rollout_get__mutmut_40 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_41'] = x_rollout_get__mutmut_41 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_42'] = x_rollout_get__mutmut_42 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_43'] = x_rollout_get__mutmut_43 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_44'] = x_rollout_get__mutmut_44 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_45'] = x_rollout_get__mutmut_45 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_46'] = x_rollout_get__mutmut_46 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_47'] = x_rollout_get__mutmut_47 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_48'] = x_rollout_get__mutmut_48 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_49'] = x_rollout_get__mutmut_49 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_50'] = x_rollout_get__mutmut_50 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_51'] = x_rollout_get__mutmut_51 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_52'] = x_rollout_get__mutmut_52 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_53'] = x_rollout_get__mutmut_53 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_54'] = x_rollout_get__mutmut_54 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_55'] = x_rollout_get__mutmut_55 # type: ignore # mutmut generated
mutants_x_rollout_get__mutmut['x_rollout_get__mutmut_56'] = x_rollout_get__mutmut_56 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(rollout_get)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(rollout_get)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated

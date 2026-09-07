"""MCP tool: adaptive_namespace_investigation — namespace investigation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.adaptive_namespace_investigation_use_case import (  # noqa: E501
    AdaptiveNamespaceInvestigationUseCase,
)
from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.command import (
    AdaptiveNamespaceInvestigationCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_adaptive_namespace_investigation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_adaptive_namespace_investigation__mutmut)
def adaptive_namespace_investigation(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_orig(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_1(namespace: str, depth: int = 4) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_2(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = None
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_3(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=None,
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_4(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=None,
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_5(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=None,
        )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_6(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_7(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_8(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            )
        r = use_case.execute(  # type: ignore
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


def x_adaptive_namespace_investigation__mutmut_9(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = None
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


def x_adaptive_namespace_investigation__mutmut_10(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            None
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


def x_adaptive_namespace_investigation__mutmut_11(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=None, depth=depth)
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


def x_adaptive_namespace_investigation__mutmut_12(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=None)
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


def x_adaptive_namespace_investigation__mutmut_13(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(depth=depth)
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


def x_adaptive_namespace_investigation__mutmut_14(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, )
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


def x_adaptive_namespace_investigation__mutmut_15(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "XXnamespaceXX": r.namespace,
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


def x_adaptive_namespace_investigation__mutmut_16(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "NAMESPACE": r.namespace,
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


def x_adaptive_namespace_investigation__mutmut_17(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "XXnamespace_statusXX": r.namespace_status,
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


def x_adaptive_namespace_investigation__mutmut_18(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "NAMESPACE_STATUS": r.namespace_status,
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


def x_adaptive_namespace_investigation__mutmut_19(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "XXhealth_statusXX": r.health_status,
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


def x_adaptive_namespace_investigation__mutmut_20(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "HEALTH_STATUS": r.health_status,
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


def x_adaptive_namespace_investigation__mutmut_21(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "XXoverview_summaryXX": r.overview_summary,
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


def x_adaptive_namespace_investigation__mutmut_22(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "OVERVIEW_SUMMARY": r.overview_summary,
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


def x_adaptive_namespace_investigation__mutmut_23(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "overview_summary": r.overview_summary,
            "XXinvestigated_resourcesXX": r.investigated_resources,
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


def x_adaptive_namespace_investigation__mutmut_24(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "overview_summary": r.overview_summary,
            "INVESTIGATED_RESOURCES": r.investigated_resources,
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


def x_adaptive_namespace_investigation__mutmut_25(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "overview_summary": r.overview_summary,
            "investigated_resources": r.investigated_resources,
            "XXroot_cause_candidatesXX": r.root_cause_candidates,
            "recommended_actions": r.recommended_actions,
            "skipped_resources": r.skipped_resources,
            "node_pressure_context": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_26(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "overview_summary": r.overview_summary,
            "investigated_resources": r.investigated_resources,
            "ROOT_CAUSE_CANDIDATES": r.root_cause_candidates,
            "recommended_actions": r.recommended_actions,
            "skipped_resources": r.skipped_resources,
            "node_pressure_context": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_27(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "overview_summary": r.overview_summary,
            "investigated_resources": r.investigated_resources,
            "root_cause_candidates": r.root_cause_candidates,
            "XXrecommended_actionsXX": r.recommended_actions,
            "skipped_resources": r.skipped_resources,
            "node_pressure_context": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_28(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
            AdaptiveNamespaceInvestigationCommand(namespace=namespace, depth=depth)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "health_status": r.health_status,
            "overview_summary": r.overview_summary,
            "investigated_resources": r.investigated_resources,
            "root_cause_candidates": r.root_cause_candidates,
            "RECOMMENDED_ACTIONS": r.recommended_actions,
            "skipped_resources": r.skipped_resources,
            "node_pressure_context": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_29(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "XXskipped_resourcesXX": r.skipped_resources,
            "node_pressure_context": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_30(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "SKIPPED_RESOURCES": r.skipped_resources,
            "node_pressure_context": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_31(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "XXnode_pressure_contextXX": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_32(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "NODE_PRESSURE_CONTEXT": r.node_pressure_context,
            "has_more_failing": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_33(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "XXhas_more_failingXX": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_34(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "HAS_MORE_FAILING": r.has_more_failing,
            "remaining_failing_count": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_35(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "XXremaining_failing_countXX": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_36(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "REMAINING_FAILING_COUNT": r.remaining_failing_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_37(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_38(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_39(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
        return {"XXnamespaceXX": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_40(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
        return {"NAMESPACE": namespace, "error": str(exc)}


def x_adaptive_namespace_investigation__mutmut_41(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
        return {"namespace": namespace, "XXerrorXX": str(exc)}


def x_adaptive_namespace_investigation__mutmut_42(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
        return {"namespace": namespace, "ERROR": str(exc)}


def x_adaptive_namespace_investigation__mutmut_43(namespace: str, depth: int = 3) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_adaptive_investigation_adapter,
        build_k8s_adapter,
        build_namespace_overview_adapter,
    )

    try:
        use_case = AdaptiveNamespaceInvestigationUseCase(  # type: ignore
            investigation_port=build_adaptive_investigation_adapter(),
            k8s_port=build_k8s_adapter(),
            overview_port=build_namespace_overview_adapter(),
        )
        r = use_case.execute(  # type: ignore
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
        return {"namespace": namespace, "error": str(None)}

mutants_x_adaptive_namespace_investigation__mutmut['_mutmut_orig'] = x_adaptive_namespace_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_1'] = x_adaptive_namespace_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_2'] = x_adaptive_namespace_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_3'] = x_adaptive_namespace_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_4'] = x_adaptive_namespace_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_5'] = x_adaptive_namespace_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_6'] = x_adaptive_namespace_investigation__mutmut_6 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_7'] = x_adaptive_namespace_investigation__mutmut_7 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_8'] = x_adaptive_namespace_investigation__mutmut_8 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_9'] = x_adaptive_namespace_investigation__mutmut_9 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_10'] = x_adaptive_namespace_investigation__mutmut_10 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_11'] = x_adaptive_namespace_investigation__mutmut_11 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_12'] = x_adaptive_namespace_investigation__mutmut_12 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_13'] = x_adaptive_namespace_investigation__mutmut_13 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_14'] = x_adaptive_namespace_investigation__mutmut_14 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_15'] = x_adaptive_namespace_investigation__mutmut_15 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_16'] = x_adaptive_namespace_investigation__mutmut_16 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_17'] = x_adaptive_namespace_investigation__mutmut_17 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_18'] = x_adaptive_namespace_investigation__mutmut_18 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_19'] = x_adaptive_namespace_investigation__mutmut_19 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_20'] = x_adaptive_namespace_investigation__mutmut_20 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_21'] = x_adaptive_namespace_investigation__mutmut_21 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_22'] = x_adaptive_namespace_investigation__mutmut_22 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_23'] = x_adaptive_namespace_investigation__mutmut_23 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_24'] = x_adaptive_namespace_investigation__mutmut_24 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_25'] = x_adaptive_namespace_investigation__mutmut_25 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_26'] = x_adaptive_namespace_investigation__mutmut_26 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_27'] = x_adaptive_namespace_investigation__mutmut_27 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_28'] = x_adaptive_namespace_investigation__mutmut_28 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_29'] = x_adaptive_namespace_investigation__mutmut_29 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_30'] = x_adaptive_namespace_investigation__mutmut_30 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_31'] = x_adaptive_namespace_investigation__mutmut_31 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_32'] = x_adaptive_namespace_investigation__mutmut_32 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_33'] = x_adaptive_namespace_investigation__mutmut_33 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_34'] = x_adaptive_namespace_investigation__mutmut_34 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_35'] = x_adaptive_namespace_investigation__mutmut_35 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_36'] = x_adaptive_namespace_investigation__mutmut_36 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_37'] = x_adaptive_namespace_investigation__mutmut_37 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_38'] = x_adaptive_namespace_investigation__mutmut_38 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_39'] = x_adaptive_namespace_investigation__mutmut_39 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_40'] = x_adaptive_namespace_investigation__mutmut_40 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_41'] = x_adaptive_namespace_investigation__mutmut_41 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_42'] = x_adaptive_namespace_investigation__mutmut_42 # type: ignore # mutmut generated
mutants_x_adaptive_namespace_investigation__mutmut['x_adaptive_namespace_investigation__mutmut_43'] = x_adaptive_namespace_investigation__mutmut_43 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(adaptive_namespace_investigation)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(adaptive_namespace_investigation)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated

"""MCP tool: conservative_namespace_overview — compact, token-budgeted namespace health overview."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.conservative_namespace_overview_use_case import (  # noqa: E501
    ConservativeNamespaceOverviewUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_conservative_namespace_overview__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_conservative_namespace_overview__mutmut)
def conservative_namespace_overview(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_orig(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_1(namespace: str, max_tokens: int = 2001) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_2(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = None
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_3(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=None, k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_4(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=None
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_5(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_6(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_7(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = None
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_8(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            None
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_9(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=None, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_10(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=None)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_11(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_12(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, )
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_13(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "XXnamespaceXX": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_14(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "NAMESPACE": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_15(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "XXnamespace_statusXX": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_16(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "NAMESPACE_STATUS": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_17(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "XXcountsXX": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_18(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "COUNTS": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_19(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "XXhealth_statusXX": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_20(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "HEALTH_STATUS": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_21(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "XXroot_causeXX": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_22(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "ROOT_CAUSE": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_23(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "XXrecommendationsXX": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_24(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "RECOMMENDATIONS": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_25(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "XXcost_impactXX": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_26(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "COST_IMPACT": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_27(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_28(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_29(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXnamespaceXX": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_30(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"NAMESPACE": namespace, "error": str(exc)}


def x_conservative_namespace_overview__mutmut_31(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "XXerrorXX": str(exc)}


def x_conservative_namespace_overview__mutmut_32(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "ERROR": str(exc)}


def x_conservative_namespace_overview__mutmut_33(namespace: str, max_tokens: int = 2000) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_overview_adapter

    try:
        use_case = ConservativeNamespaceOverviewUseCase(
            port=build_namespace_overview_adapter(), k8s_port=build_k8s_adapter()
        )
        r = use_case.execute(  # type: ignore
            ConservativeNamespaceOverviewCommand(namespace=namespace, max_tokens=max_tokens)
        )
        return {
            "namespace": r.namespace,
            "namespace_status": r.namespace_status,
            "counts": r.counts,
            "health_status": r.health_status,
            "root_cause": r.root_cause,
            "recommendations": r.recommendations,
            "cost_impact": r.cost_impact,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(None)}

mutants_x_conservative_namespace_overview__mutmut['_mutmut_orig'] = x_conservative_namespace_overview__mutmut_orig # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_1'] = x_conservative_namespace_overview__mutmut_1 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_2'] = x_conservative_namespace_overview__mutmut_2 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_3'] = x_conservative_namespace_overview__mutmut_3 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_4'] = x_conservative_namespace_overview__mutmut_4 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_5'] = x_conservative_namespace_overview__mutmut_5 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_6'] = x_conservative_namespace_overview__mutmut_6 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_7'] = x_conservative_namespace_overview__mutmut_7 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_8'] = x_conservative_namespace_overview__mutmut_8 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_9'] = x_conservative_namespace_overview__mutmut_9 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_10'] = x_conservative_namespace_overview__mutmut_10 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_11'] = x_conservative_namespace_overview__mutmut_11 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_12'] = x_conservative_namespace_overview__mutmut_12 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_13'] = x_conservative_namespace_overview__mutmut_13 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_14'] = x_conservative_namespace_overview__mutmut_14 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_15'] = x_conservative_namespace_overview__mutmut_15 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_16'] = x_conservative_namespace_overview__mutmut_16 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_17'] = x_conservative_namespace_overview__mutmut_17 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_18'] = x_conservative_namespace_overview__mutmut_18 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_19'] = x_conservative_namespace_overview__mutmut_19 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_20'] = x_conservative_namespace_overview__mutmut_20 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_21'] = x_conservative_namespace_overview__mutmut_21 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_22'] = x_conservative_namespace_overview__mutmut_22 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_23'] = x_conservative_namespace_overview__mutmut_23 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_24'] = x_conservative_namespace_overview__mutmut_24 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_25'] = x_conservative_namespace_overview__mutmut_25 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_26'] = x_conservative_namespace_overview__mutmut_26 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_27'] = x_conservative_namespace_overview__mutmut_27 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_28'] = x_conservative_namespace_overview__mutmut_28 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_29'] = x_conservative_namespace_overview__mutmut_29 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_30'] = x_conservative_namespace_overview__mutmut_30 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_31'] = x_conservative_namespace_overview__mutmut_31 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_32'] = x_conservative_namespace_overview__mutmut_32 # type: ignore # mutmut generated
mutants_x_conservative_namespace_overview__mutmut['x_conservative_namespace_overview__mutmut_33'] = x_conservative_namespace_overview__mutmut_33 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(conservative_namespace_overview)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(conservative_namespace_overview)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated

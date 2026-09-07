"""MCP tool: estimate_rightsizing_savings — FinOps rightsizing recommendations."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.use_case.finops.estimate_rightsizing_savings.estimate_rightsizing_savings_use_case import (  # noqa: E501
    EstimateRightsizingSavingsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_estimate_rightsizing_savings__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_estimate_rightsizing_savings__mutmut)
def estimate_rightsizing_savings(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_orig(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_1(top_n: int = 6) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_2(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = None
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_3(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = None  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_4(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=None)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_5(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = None  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_6(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(None)  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_7(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=None))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_8(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = None
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_9(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "XXrecommendationsXX": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_10(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "RECOMMENDATIONS": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_11(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "XXresource_nameXX": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_12(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "RESOURCE_NAME": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_13(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "XXnamespaceXX": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_14(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "NAMESPACE": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_15(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "XXkindXX": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_16(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "KIND": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_17(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "XXrightsizing_typeXX": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_18(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "RIGHTSIZING_TYPE": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_19(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "XXcurrent_cpu_coresXX": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_20(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "CURRENT_CPU_CORES": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_21(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "XXrecommended_cpu_coresXX": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_22(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "RECOMMENDED_CPU_CORES": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_23(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(None, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_24(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, None),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_25(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_26(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, ),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_27(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 3),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_28(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "XXcurrent_memory_miXX": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_29(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "CURRENT_MEMORY_MI": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_30(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "XXrecommended_memory_miXX": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_31(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "RECOMMENDED_MEMORY_MI": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_32(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(None, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_33(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, None),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_34(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_35(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, ),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_36(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 2),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_37(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "XXmonthly_savings_usdXX": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_38(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "MONTHLY_SAVINGS_USD": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_39(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(None, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_40(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, None),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_41(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_42(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, ),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_43(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 3),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_44(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "XXwaste_percentageXX": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_45(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "WASTE_PERCENTAGE": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_46(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(None, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_47(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, None),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_48(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_49(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, ),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_50(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 2),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_51(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "XXreasonXX": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_52(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "REASON": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_53(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "XXpriorityXX": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_54(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "PRIORITY": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_55(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "XXtotal_monthly_savings_usdXX": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_56(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "TOTAL_MONTHLY_SAVINGS_USD": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_57(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(None, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_58(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, None),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_59(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_60(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, ),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_61(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 3),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_62(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "XXskipped_countXX": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_63(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "SKIPPED_COUNT": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_64(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "XXmetrics_server_availableXX": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_65(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "METRICS_SERVER_AVAILABLE": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_66(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_67(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_68(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXrecommendationsXX": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_69(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "RECOMMENDATIONS": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_70(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "XXtotal_monthly_savings_usdXX": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_71(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "TOTAL_MONTHLY_SAVINGS_USD": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_72(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 1.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_73(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "XXskipped_countXX": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_74(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "SKIPPED_COUNT": 0,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_75(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 1,
            "metrics_server_available": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_76(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "XXmetrics_server_availableXX": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_77(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "METRICS_SERVER_AVAILABLE": False,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_78(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": True,
            "error": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_79(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "XXerrorXX": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_80(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "ERROR": str(exc),
        }


def x_estimate_rightsizing_savings__mutmut_81(top_n: int = 5) -> dict[str, object]:
    """Compare K8s resource requests vs actual usage and recommend rightsizing with $ savings.

    Args:
        top_n: Maximum recommendations to return, ranked by savings (default: 5).
    """
    from hexawyn.mcp.server import build_rightsizing_adapter

    try:
        adapter = build_rightsizing_adapter()
        use_case = EstimateRightsizingSavingsUseCase(port=adapter)  # type: ignore
        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=top_n))  # type: ignore
        report = response.report
        return {
            "recommendations": [
                {
                    "resource_name": r.resource_name,
                    "namespace": r.namespace,
                    "kind": r.kind,
                    "rightsizing_type": r.rightsizing_type.value,
                    "current_cpu_cores": r.current_cpu_cores,
                    "recommended_cpu_cores": round(r.recommended_cpu_cores, 2),
                    "current_memory_mi": r.current_memory_mi,
                    "recommended_memory_mi": round(r.recommended_memory_mi, 1),
                    "monthly_savings_usd": round(r.monthly_savings_usd, 2),
                    "waste_percentage": round(r.waste_percentage, 1),
                    "reason": r.reason,
                    "priority": r.priority,
                }
                for r in report.recommendations
            ],
            "total_monthly_savings_usd": round(report.total_monthly_savings_usd, 2),
            "skipped_count": report.skipped_count,
            "metrics_server_available": response.metrics_server_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "recommendations": [],
            "total_monthly_savings_usd": 0.0,
            "skipped_count": 0,
            "metrics_server_available": False,
            "error": str(None),
        }

mutants_x_estimate_rightsizing_savings__mutmut['_mutmut_orig'] = x_estimate_rightsizing_savings__mutmut_orig # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_1'] = x_estimate_rightsizing_savings__mutmut_1 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_2'] = x_estimate_rightsizing_savings__mutmut_2 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_3'] = x_estimate_rightsizing_savings__mutmut_3 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_4'] = x_estimate_rightsizing_savings__mutmut_4 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_5'] = x_estimate_rightsizing_savings__mutmut_5 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_6'] = x_estimate_rightsizing_savings__mutmut_6 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_7'] = x_estimate_rightsizing_savings__mutmut_7 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_8'] = x_estimate_rightsizing_savings__mutmut_8 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_9'] = x_estimate_rightsizing_savings__mutmut_9 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_10'] = x_estimate_rightsizing_savings__mutmut_10 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_11'] = x_estimate_rightsizing_savings__mutmut_11 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_12'] = x_estimate_rightsizing_savings__mutmut_12 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_13'] = x_estimate_rightsizing_savings__mutmut_13 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_14'] = x_estimate_rightsizing_savings__mutmut_14 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_15'] = x_estimate_rightsizing_savings__mutmut_15 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_16'] = x_estimate_rightsizing_savings__mutmut_16 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_17'] = x_estimate_rightsizing_savings__mutmut_17 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_18'] = x_estimate_rightsizing_savings__mutmut_18 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_19'] = x_estimate_rightsizing_savings__mutmut_19 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_20'] = x_estimate_rightsizing_savings__mutmut_20 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_21'] = x_estimate_rightsizing_savings__mutmut_21 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_22'] = x_estimate_rightsizing_savings__mutmut_22 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_23'] = x_estimate_rightsizing_savings__mutmut_23 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_24'] = x_estimate_rightsizing_savings__mutmut_24 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_25'] = x_estimate_rightsizing_savings__mutmut_25 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_26'] = x_estimate_rightsizing_savings__mutmut_26 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_27'] = x_estimate_rightsizing_savings__mutmut_27 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_28'] = x_estimate_rightsizing_savings__mutmut_28 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_29'] = x_estimate_rightsizing_savings__mutmut_29 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_30'] = x_estimate_rightsizing_savings__mutmut_30 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_31'] = x_estimate_rightsizing_savings__mutmut_31 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_32'] = x_estimate_rightsizing_savings__mutmut_32 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_33'] = x_estimate_rightsizing_savings__mutmut_33 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_34'] = x_estimate_rightsizing_savings__mutmut_34 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_35'] = x_estimate_rightsizing_savings__mutmut_35 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_36'] = x_estimate_rightsizing_savings__mutmut_36 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_37'] = x_estimate_rightsizing_savings__mutmut_37 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_38'] = x_estimate_rightsizing_savings__mutmut_38 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_39'] = x_estimate_rightsizing_savings__mutmut_39 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_40'] = x_estimate_rightsizing_savings__mutmut_40 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_41'] = x_estimate_rightsizing_savings__mutmut_41 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_42'] = x_estimate_rightsizing_savings__mutmut_42 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_43'] = x_estimate_rightsizing_savings__mutmut_43 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_44'] = x_estimate_rightsizing_savings__mutmut_44 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_45'] = x_estimate_rightsizing_savings__mutmut_45 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_46'] = x_estimate_rightsizing_savings__mutmut_46 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_47'] = x_estimate_rightsizing_savings__mutmut_47 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_48'] = x_estimate_rightsizing_savings__mutmut_48 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_49'] = x_estimate_rightsizing_savings__mutmut_49 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_50'] = x_estimate_rightsizing_savings__mutmut_50 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_51'] = x_estimate_rightsizing_savings__mutmut_51 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_52'] = x_estimate_rightsizing_savings__mutmut_52 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_53'] = x_estimate_rightsizing_savings__mutmut_53 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_54'] = x_estimate_rightsizing_savings__mutmut_54 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_55'] = x_estimate_rightsizing_savings__mutmut_55 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_56'] = x_estimate_rightsizing_savings__mutmut_56 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_57'] = x_estimate_rightsizing_savings__mutmut_57 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_58'] = x_estimate_rightsizing_savings__mutmut_58 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_59'] = x_estimate_rightsizing_savings__mutmut_59 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_60'] = x_estimate_rightsizing_savings__mutmut_60 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_61'] = x_estimate_rightsizing_savings__mutmut_61 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_62'] = x_estimate_rightsizing_savings__mutmut_62 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_63'] = x_estimate_rightsizing_savings__mutmut_63 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_64'] = x_estimate_rightsizing_savings__mutmut_64 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_65'] = x_estimate_rightsizing_savings__mutmut_65 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_66'] = x_estimate_rightsizing_savings__mutmut_66 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_67'] = x_estimate_rightsizing_savings__mutmut_67 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_68'] = x_estimate_rightsizing_savings__mutmut_68 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_69'] = x_estimate_rightsizing_savings__mutmut_69 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_70'] = x_estimate_rightsizing_savings__mutmut_70 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_71'] = x_estimate_rightsizing_savings__mutmut_71 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_72'] = x_estimate_rightsizing_savings__mutmut_72 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_73'] = x_estimate_rightsizing_savings__mutmut_73 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_74'] = x_estimate_rightsizing_savings__mutmut_74 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_75'] = x_estimate_rightsizing_savings__mutmut_75 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_76'] = x_estimate_rightsizing_savings__mutmut_76 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_77'] = x_estimate_rightsizing_savings__mutmut_77 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_78'] = x_estimate_rightsizing_savings__mutmut_78 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_79'] = x_estimate_rightsizing_savings__mutmut_79 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_80'] = x_estimate_rightsizing_savings__mutmut_80 # type: ignore # mutmut generated
mutants_x_estimate_rightsizing_savings__mutmut['x_estimate_rightsizing_savings__mutmut_81'] = x_estimate_rightsizing_savings__mutmut_81 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(estimate_rightsizing_savings)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(estimate_rightsizing_savings)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated

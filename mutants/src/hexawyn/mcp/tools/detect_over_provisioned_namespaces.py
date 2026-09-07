"""MCP tool: detect_over_provisioned_namespaces — FinOps waste analysis across namespaces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_use_case import (  # noqa: E501
    DetectOverProvisionedNamespacesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_over_provisioned_namespaces__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_over_provisioned_namespaces__mutmut)
def detect_over_provisioned_namespaces(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_orig(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_1(
    analysis_window_days: int = 8, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_2(
    analysis_window_days: int = 7, top_n: int = 6
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_3(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = None
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_4(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = None
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_5(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=None)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_6(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = None
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_7(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            None
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_8(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=None, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_9(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=None
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_10(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_11(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_12(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = None
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_13(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "XXnamespacesXX": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_14(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "NAMESPACES": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_15(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "XXnamespaceXX": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_16(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "NAMESPACE": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_17(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "XXcpu_requested_coresXX": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_18(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "CPU_REQUESTED_CORES": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_19(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "XXcpu_actual_avg_coresXX": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_20(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "CPU_ACTUAL_AVG_CORES": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_21(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "XXcpu_waste_pctXX": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_22(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "CPU_WASTE_PCT": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_23(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(None, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_24(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, None),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_25(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_26(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, ),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_27(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 2),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_28(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "XXcpu_wasted_coresXX": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_29(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "CPU_WASTED_CORES": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_30(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(None, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_31(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, None),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_32(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_33(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, ),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_34(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 3),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_35(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "XXmemory_requested_gbXX": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_36(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "MEMORY_REQUESTED_GB": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_37(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "XXmemory_actual_avg_gbXX": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_38(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "MEMORY_ACTUAL_AVG_GB": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_39(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "XXmemory_waste_pctXX": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_40(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "MEMORY_WASTE_PCT": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_41(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(None, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_42(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, None),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_43(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_44(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, ),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_45(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 2),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_46(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "XXmemory_wasted_gbXX": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_47(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "MEMORY_WASTED_GB": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_48(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(None, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_49(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, None),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_50(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_51(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, ),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_52(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 3),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_53(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "XXis_over_provisionedXX": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_54(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "IS_OVER_PROVISIONED": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_55(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "XXexcludedXX": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_56(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "EXCLUDED": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_57(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"XXnamespaceXX": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_58(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"NAMESPACE": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_59(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "XXreasonXX": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_60(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "REASON": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_61(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "XXtotal_wasted_cpu_coresXX": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_62(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "TOTAL_WASTED_CPU_CORES": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_63(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(None, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_64(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, None),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_65(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_66(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, ),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_67(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 3),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_68(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "XXtotal_wasted_memory_gbXX": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_69(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "TOTAL_WASTED_MEMORY_GB": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_70(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(None, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_71(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, None),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_72(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_73(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, ),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_74(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 3),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_75(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "XXanalysis_window_daysXX": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_76(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "ANALYSIS_WINDOW_DAYS": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_77(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "XXprometheus_availableXX": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_78(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "PROMETHEUS_AVAILABLE": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_79(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_80(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_81(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXnamespacesXX": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_82(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "NAMESPACES": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_83(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "XXexcludedXX": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_84(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "EXCLUDED": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_85(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "XXtotal_wasted_cpu_coresXX": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_86(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "TOTAL_WASTED_CPU_CORES": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_87(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 1.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_88(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "XXtotal_wasted_memory_gbXX": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_89(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "TOTAL_WASTED_MEMORY_GB": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_90(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 1.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_91(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "XXanalysis_window_daysXX": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_92(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "ANALYSIS_WINDOW_DAYS": analysis_window_days,
            "prometheus_available": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_93(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "XXprometheus_availableXX": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_94(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "PROMETHEUS_AVAILABLE": False,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_95(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": True,
            "error": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_96(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "XXerrorXX": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_97(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "ERROR": str(exc),
        }


def x_detect_over_provisioned_namespaces__mutmut_98(
    analysis_window_days: int = 7, top_n: int = 5
) -> dict[str, object]:
    """Identify over-provisioned namespaces by comparing K8s resource requests vs actual usage.

    Args:
        analysis_window_days: Prometheus lookback window in days (default: 7).
        top_n: Maximum number of namespaces to return, ranked by waste% (default: 5).
    """
    from hexawyn.mcp.server import build_waste_adapter

    try:
        adapter = build_waste_adapter()
        use_case = DetectOverProvisionedNamespacesUseCase(waste_port=adapter)
        response = use_case.execute(  # type: ignore
            DetectOverProvisionedNamespacesCommand(
                analysis_window_days=analysis_window_days, top_n=top_n
            )
        )
        report = response.report
        return {
            "namespaces": [
                {
                    "namespace": ns.namespace,
                    "cpu_requested_cores": ns.cpu_requested_cores,
                    "cpu_actual_avg_cores": ns.cpu_actual_avg_cores,
                    "cpu_waste_pct": round(ns.cpu_waste_pct, 1),
                    "cpu_wasted_cores": round(ns.cpu_wasted_cores, 2),
                    "memory_requested_gb": ns.memory_requested_gb,
                    "memory_actual_avg_gb": ns.memory_actual_avg_gb,
                    "memory_waste_pct": round(ns.memory_waste_pct, 1),
                    "memory_wasted_gb": round(ns.memory_wasted_gb, 2),
                    "is_over_provisioned": ns.is_over_provisioned,
                }
                for ns in report.namespaces
            ],
            "excluded": [{"namespace": e.namespace, "reason": e.reason} for e in report.excluded],
            "total_wasted_cpu_cores": round(report.total_wasted_cpu_cores, 2),
            "total_wasted_memory_gb": round(report.total_wasted_memory_gb, 2),
            "analysis_window_days": report.analysis_window_days,
            "prometheus_available": response.prometheus_available,
            "error": None,
        }
    except Exception as exc:
        return {
            "namespaces": [],
            "excluded": [],
            "total_wasted_cpu_cores": 0.0,
            "total_wasted_memory_gb": 0.0,
            "analysis_window_days": analysis_window_days,
            "prometheus_available": False,
            "error": str(None),
        }

mutants_x_detect_over_provisioned_namespaces__mutmut['_mutmut_orig'] = x_detect_over_provisioned_namespaces__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_1'] = x_detect_over_provisioned_namespaces__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_2'] = x_detect_over_provisioned_namespaces__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_3'] = x_detect_over_provisioned_namespaces__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_4'] = x_detect_over_provisioned_namespaces__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_5'] = x_detect_over_provisioned_namespaces__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_6'] = x_detect_over_provisioned_namespaces__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_7'] = x_detect_over_provisioned_namespaces__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_8'] = x_detect_over_provisioned_namespaces__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_9'] = x_detect_over_provisioned_namespaces__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_10'] = x_detect_over_provisioned_namespaces__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_11'] = x_detect_over_provisioned_namespaces__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_12'] = x_detect_over_provisioned_namespaces__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_13'] = x_detect_over_provisioned_namespaces__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_14'] = x_detect_over_provisioned_namespaces__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_15'] = x_detect_over_provisioned_namespaces__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_16'] = x_detect_over_provisioned_namespaces__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_17'] = x_detect_over_provisioned_namespaces__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_18'] = x_detect_over_provisioned_namespaces__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_19'] = x_detect_over_provisioned_namespaces__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_20'] = x_detect_over_provisioned_namespaces__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_21'] = x_detect_over_provisioned_namespaces__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_22'] = x_detect_over_provisioned_namespaces__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_23'] = x_detect_over_provisioned_namespaces__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_24'] = x_detect_over_provisioned_namespaces__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_25'] = x_detect_over_provisioned_namespaces__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_26'] = x_detect_over_provisioned_namespaces__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_27'] = x_detect_over_provisioned_namespaces__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_28'] = x_detect_over_provisioned_namespaces__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_29'] = x_detect_over_provisioned_namespaces__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_30'] = x_detect_over_provisioned_namespaces__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_31'] = x_detect_over_provisioned_namespaces__mutmut_31 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_32'] = x_detect_over_provisioned_namespaces__mutmut_32 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_33'] = x_detect_over_provisioned_namespaces__mutmut_33 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_34'] = x_detect_over_provisioned_namespaces__mutmut_34 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_35'] = x_detect_over_provisioned_namespaces__mutmut_35 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_36'] = x_detect_over_provisioned_namespaces__mutmut_36 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_37'] = x_detect_over_provisioned_namespaces__mutmut_37 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_38'] = x_detect_over_provisioned_namespaces__mutmut_38 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_39'] = x_detect_over_provisioned_namespaces__mutmut_39 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_40'] = x_detect_over_provisioned_namespaces__mutmut_40 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_41'] = x_detect_over_provisioned_namespaces__mutmut_41 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_42'] = x_detect_over_provisioned_namespaces__mutmut_42 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_43'] = x_detect_over_provisioned_namespaces__mutmut_43 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_44'] = x_detect_over_provisioned_namespaces__mutmut_44 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_45'] = x_detect_over_provisioned_namespaces__mutmut_45 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_46'] = x_detect_over_provisioned_namespaces__mutmut_46 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_47'] = x_detect_over_provisioned_namespaces__mutmut_47 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_48'] = x_detect_over_provisioned_namespaces__mutmut_48 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_49'] = x_detect_over_provisioned_namespaces__mutmut_49 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_50'] = x_detect_over_provisioned_namespaces__mutmut_50 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_51'] = x_detect_over_provisioned_namespaces__mutmut_51 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_52'] = x_detect_over_provisioned_namespaces__mutmut_52 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_53'] = x_detect_over_provisioned_namespaces__mutmut_53 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_54'] = x_detect_over_provisioned_namespaces__mutmut_54 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_55'] = x_detect_over_provisioned_namespaces__mutmut_55 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_56'] = x_detect_over_provisioned_namespaces__mutmut_56 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_57'] = x_detect_over_provisioned_namespaces__mutmut_57 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_58'] = x_detect_over_provisioned_namespaces__mutmut_58 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_59'] = x_detect_over_provisioned_namespaces__mutmut_59 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_60'] = x_detect_over_provisioned_namespaces__mutmut_60 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_61'] = x_detect_over_provisioned_namespaces__mutmut_61 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_62'] = x_detect_over_provisioned_namespaces__mutmut_62 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_63'] = x_detect_over_provisioned_namespaces__mutmut_63 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_64'] = x_detect_over_provisioned_namespaces__mutmut_64 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_65'] = x_detect_over_provisioned_namespaces__mutmut_65 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_66'] = x_detect_over_provisioned_namespaces__mutmut_66 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_67'] = x_detect_over_provisioned_namespaces__mutmut_67 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_68'] = x_detect_over_provisioned_namespaces__mutmut_68 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_69'] = x_detect_over_provisioned_namespaces__mutmut_69 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_70'] = x_detect_over_provisioned_namespaces__mutmut_70 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_71'] = x_detect_over_provisioned_namespaces__mutmut_71 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_72'] = x_detect_over_provisioned_namespaces__mutmut_72 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_73'] = x_detect_over_provisioned_namespaces__mutmut_73 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_74'] = x_detect_over_provisioned_namespaces__mutmut_74 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_75'] = x_detect_over_provisioned_namespaces__mutmut_75 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_76'] = x_detect_over_provisioned_namespaces__mutmut_76 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_77'] = x_detect_over_provisioned_namespaces__mutmut_77 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_78'] = x_detect_over_provisioned_namespaces__mutmut_78 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_79'] = x_detect_over_provisioned_namespaces__mutmut_79 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_80'] = x_detect_over_provisioned_namespaces__mutmut_80 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_81'] = x_detect_over_provisioned_namespaces__mutmut_81 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_82'] = x_detect_over_provisioned_namespaces__mutmut_82 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_83'] = x_detect_over_provisioned_namespaces__mutmut_83 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_84'] = x_detect_over_provisioned_namespaces__mutmut_84 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_85'] = x_detect_over_provisioned_namespaces__mutmut_85 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_86'] = x_detect_over_provisioned_namespaces__mutmut_86 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_87'] = x_detect_over_provisioned_namespaces__mutmut_87 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_88'] = x_detect_over_provisioned_namespaces__mutmut_88 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_89'] = x_detect_over_provisioned_namespaces__mutmut_89 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_90'] = x_detect_over_provisioned_namespaces__mutmut_90 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_91'] = x_detect_over_provisioned_namespaces__mutmut_91 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_92'] = x_detect_over_provisioned_namespaces__mutmut_92 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_93'] = x_detect_over_provisioned_namespaces__mutmut_93 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_94'] = x_detect_over_provisioned_namespaces__mutmut_94 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_95'] = x_detect_over_provisioned_namespaces__mutmut_95 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_96'] = x_detect_over_provisioned_namespaces__mutmut_96 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_97'] = x_detect_over_provisioned_namespaces__mutmut_97 # type: ignore # mutmut generated
mutants_x_detect_over_provisioned_namespaces__mutmut['x_detect_over_provisioned_namespaces__mutmut_98'] = x_detect_over_provisioned_namespaces__mutmut_98 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    """Register detect_over_provisioned_namespaces as an MCP tool."""
    mcp.tool()(detect_over_provisioned_namespaces)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    """Register detect_over_provisioned_namespaces as an MCP tool."""
    mcp.tool()(detect_over_provisioned_namespaces)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    """Register detect_over_provisioned_namespaces as an MCP tool."""
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated

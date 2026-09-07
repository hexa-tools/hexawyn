"""MCP tool: detect_pod_anomalies — CPU/memory/error-rate anomaly detection vs 7-day baseline."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.detect_pod_anomalies_use_case import (  # noqa: E501
    DetectPodAnomaliesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_pod_anomalies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_pod_anomalies__mutmut)
def detect_pod_anomalies(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_orig(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_1(namespace: str, baseline_window_days: int = 8) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_2(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = None
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_3(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=None, k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_4(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=None
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_5(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_6(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_7(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = None  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_8(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=None)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_9(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = None
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_10(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            None
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_11(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=None, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_12(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=None
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_13(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_14(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_15(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "XXnamespaceXX": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_16(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "NAMESPACE": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_17(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "XXtotal_podsXX": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_18(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "TOTAL_PODS": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_19(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "XXanomaliesXX": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_20(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "ANOMALIES": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_21(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "XXexcluded_podsXX": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_22(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "EXCLUDED_PODS": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_23(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "XXsummaryXX": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_24(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "SUMMARY": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_25(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_26(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_27(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXnamespaceXX": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_28(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"NAMESPACE": namespace, "error": str(exc)}


def x_detect_pod_anomalies__mutmut_29(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "XXerrorXX": str(exc)}


def x_detect_pod_anomalies__mutmut_30(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "ERROR": str(exc)}


def x_detect_pod_anomalies__mutmut_31(namespace: str, baseline_window_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_baseline_adapter

    try:
        service = DetectPodAnomaliesUseCase(
            port=build_pod_metrics_baseline_adapter(), k8s_port=build_k8s_adapter()
        )
        use_case = DetectPodAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectPodAnomaliesCommand(
                namespace=namespace, baseline_window_days=baseline_window_days
            )
        )
        return {
            "namespace": r.namespace,
            "total_pods": r.total_pods,
            "anomalies": r.anomalies,
            "excluded_pods": r.excluded_pods,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(None)}

mutants_x_detect_pod_anomalies__mutmut['_mutmut_orig'] = x_detect_pod_anomalies__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_1'] = x_detect_pod_anomalies__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_2'] = x_detect_pod_anomalies__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_3'] = x_detect_pod_anomalies__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_4'] = x_detect_pod_anomalies__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_5'] = x_detect_pod_anomalies__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_6'] = x_detect_pod_anomalies__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_7'] = x_detect_pod_anomalies__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_8'] = x_detect_pod_anomalies__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_9'] = x_detect_pod_anomalies__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_10'] = x_detect_pod_anomalies__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_11'] = x_detect_pod_anomalies__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_12'] = x_detect_pod_anomalies__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_13'] = x_detect_pod_anomalies__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_14'] = x_detect_pod_anomalies__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_15'] = x_detect_pod_anomalies__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_16'] = x_detect_pod_anomalies__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_17'] = x_detect_pod_anomalies__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_18'] = x_detect_pod_anomalies__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_19'] = x_detect_pod_anomalies__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_20'] = x_detect_pod_anomalies__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_21'] = x_detect_pod_anomalies__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_22'] = x_detect_pod_anomalies__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_23'] = x_detect_pod_anomalies__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_24'] = x_detect_pod_anomalies__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_25'] = x_detect_pod_anomalies__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_26'] = x_detect_pod_anomalies__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_27'] = x_detect_pod_anomalies__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_28'] = x_detect_pod_anomalies__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_29'] = x_detect_pod_anomalies__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_30'] = x_detect_pod_anomalies__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_31'] = x_detect_pod_anomalies__mutmut_31 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_pod_anomalies)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_pod_anomalies)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated

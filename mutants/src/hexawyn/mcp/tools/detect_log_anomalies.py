"""MCP tool: detect_log_anomalies — Z-score volume spikes + Isolation Forest semantic outliers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.detect_log_anomalies_use_case import (  # noqa: E501
    DetectLogAnomaliesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_log_anomalies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_log_anomalies__mutmut)
def detect_log_anomalies(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_orig(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_1(
    pod_name: str, namespace: str, time_window_minutes: int = 241, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_2(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 4.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_3(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = None
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_4(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=None)
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_5(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = None  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_6(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=None)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_7(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = None
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_8(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            None
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_9(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=None,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_10(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=None,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_11(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=None,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_12(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=None,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_13(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_14(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_15(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_16(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_17(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "XXpod_nameXX": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_18(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "POD_NAME": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_19(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "XXnamespaceXX": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_20(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "NAMESPACE": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_21(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "XXtime_window_minutesXX": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_22(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "TIME_WINDOW_MINUTES": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_23(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "XXtotal_linesXX": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_24(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "TOTAL_LINES": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_25(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "XXbaseline_mean_lines_per_minuteXX": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_26(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "BASELINE_MEAN_LINES_PER_MINUTE": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_27(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "XXbaseline_std_devXX": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_28(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "BASELINE_STD_DEV": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_29(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "XXsummaryXX": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_30(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "SUMMARY": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_31(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "XXinsufficient_dataXX": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_32(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "INSUFFICIENT_DATA": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_33(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "XXformats_analyzed_separatelyXX": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_34(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "FORMATS_ANALYZED_SEPARATELY": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_35(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "XXanomaliesXX": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_36(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "ANOMALIES": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_37(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "XXerrorXX": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_38(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "ERROR": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_39(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"XXpod_nameXX": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_40(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"POD_NAME": pod_name, "namespace": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_41(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "XXnamespaceXX": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_42(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "NAMESPACE": namespace, "error": str(exc)}


def x_detect_log_anomalies__mutmut_43(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "XXerrorXX": str(exc)}


def x_detect_log_anomalies__mutmut_44(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "ERROR": str(exc)}


def x_detect_log_anomalies__mutmut_45(
    pod_name: str, namespace: str, time_window_minutes: int = 240, zscore_threshold: float = 3.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_logs_adapter

    try:
        service = DetectLogAnomaliesUseCase(port=build_pod_logs_adapter())
        use_case = DetectLogAnomaliesUseCase(service=service)  # type: ignore
        r = use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name=pod_name,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                zscore_threshold=zscore_threshold,
            )
        )
        return {
            "pod_name": r.pod_name,
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_lines": r.total_lines,
            "baseline_mean_lines_per_minute": r.baseline_mean_lines_per_minute,
            "baseline_std_dev": r.baseline_std_dev,
            "summary": r.summary,
            "insufficient_data": r.insufficient_data,
            "formats_analyzed_separately": r.formats_analyzed_separately,
            "anomalies": r.anomalies,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pod_name": pod_name, "namespace": namespace, "error": str(None)}

mutants_x_detect_log_anomalies__mutmut['_mutmut_orig'] = x_detect_log_anomalies__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_1'] = x_detect_log_anomalies__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_2'] = x_detect_log_anomalies__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_3'] = x_detect_log_anomalies__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_4'] = x_detect_log_anomalies__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_5'] = x_detect_log_anomalies__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_6'] = x_detect_log_anomalies__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_7'] = x_detect_log_anomalies__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_8'] = x_detect_log_anomalies__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_9'] = x_detect_log_anomalies__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_10'] = x_detect_log_anomalies__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_11'] = x_detect_log_anomalies__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_12'] = x_detect_log_anomalies__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_13'] = x_detect_log_anomalies__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_14'] = x_detect_log_anomalies__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_15'] = x_detect_log_anomalies__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_16'] = x_detect_log_anomalies__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_17'] = x_detect_log_anomalies__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_18'] = x_detect_log_anomalies__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_19'] = x_detect_log_anomalies__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_20'] = x_detect_log_anomalies__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_21'] = x_detect_log_anomalies__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_22'] = x_detect_log_anomalies__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_23'] = x_detect_log_anomalies__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_24'] = x_detect_log_anomalies__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_25'] = x_detect_log_anomalies__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_26'] = x_detect_log_anomalies__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_27'] = x_detect_log_anomalies__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_28'] = x_detect_log_anomalies__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_29'] = x_detect_log_anomalies__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_30'] = x_detect_log_anomalies__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_31'] = x_detect_log_anomalies__mutmut_31 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_32'] = x_detect_log_anomalies__mutmut_32 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_33'] = x_detect_log_anomalies__mutmut_33 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_34'] = x_detect_log_anomalies__mutmut_34 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_35'] = x_detect_log_anomalies__mutmut_35 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_36'] = x_detect_log_anomalies__mutmut_36 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_37'] = x_detect_log_anomalies__mutmut_37 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_38'] = x_detect_log_anomalies__mutmut_38 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_39'] = x_detect_log_anomalies__mutmut_39 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_40'] = x_detect_log_anomalies__mutmut_40 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_41'] = x_detect_log_anomalies__mutmut_41 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_42'] = x_detect_log_anomalies__mutmut_42 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_43'] = x_detect_log_anomalies__mutmut_43 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_44'] = x_detect_log_anomalies__mutmut_44 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_45'] = x_detect_log_anomalies__mutmut_45 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_log_anomalies)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_log_anomalies)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated

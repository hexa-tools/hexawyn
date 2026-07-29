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


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_log_anomalies)

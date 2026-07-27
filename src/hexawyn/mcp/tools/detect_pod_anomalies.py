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


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_pod_anomalies)

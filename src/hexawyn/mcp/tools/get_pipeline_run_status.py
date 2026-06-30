"""MCP tool: get_pipeline_run_status — Tekton PipelineRun health report for a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    TektonPipelineStatusPort,
)
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.get_pipeline_run_status.get_pipeline_run_status_use_case import (
    GetPipelineRunStatusUseCase,
)
from hexawyn.domain.models.pipeline import PipelineRunSummary

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _build_adapter() -> TektonPipelineStatusPort:
    from hexawyn.adapters.secondary.kubernetes_tekton_adapter import KubernetesTektonAdapter

    return KubernetesTektonAdapter()


def _serialize_summary(summary: PipelineRunSummary | None) -> dict[str, object] | None:
    if summary is None:
        return None
    return {
        "name": summary.name,
        "status": summary.status,
        "start_time": summary.start_time,
        "duration_seconds": summary.duration_seconds,
        "failure_reason": summary.failure_reason,
        "pipeline_ref": summary.pipeline_ref,
    }


def get_pipeline_run_status(
    namespace: str = "ci",
    hours_window: int = 24,
    limit: int = 500,
) -> dict[str, object]:
    """Return a status report for all Tekton PipelineRuns in a namespace.

    Aggregates counts by status (Running / Succeeded / Failed / Cancelled),
    surfaces the most recent failed run with its failure reason, and identifies
    the slowest completed run.

    Args:
        namespace: Kubernetes namespace to scan (default: "ci").
        hours_window: Time window in hours — only runs started within this window
            are included (default: 24).
        limit: Maximum number of PipelineRuns to fetch from the API (default: 500).
    """
    from hexawyn.application.service.pipeline_run_status_service import PipelineRunStatusService

    try:
        adapter = _build_adapter()
        service = PipelineRunStatusService(port=adapter)
        use_case = GetPipelineRunStatusUseCase(service=service)
        response = use_case.execute(
            GetPipelineRunStatusCommand(
                namespace=namespace,
                hours_window=hours_window,
                limit=limit,
            )
        )
        report = response.report
        return {
            "namespace": report.namespace,
            "window_hours": report.window_hours,
            "total": report.total,
            "running": report.running,
            "succeeded": report.succeeded,
            "failed": report.failed,
            "cancelled": report.cancelled,
            "not_started": report.not_started,
            "most_recent_failed": _serialize_summary(report.most_recent_failed),
            "slowest_run": _serialize_summary(report.slowest_run),
            "generated_at": report.generated_at.isoformat(),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "window_hours": hours_window,
            "total": 0,
            "running": 0,
            "succeeded": 0,
            "failed": 0,
            "cancelled": 0,
            "not_started": 0,
            "most_recent_failed": None,
            "slowest_run": None,
            "generated_at": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_pipeline_run_status)

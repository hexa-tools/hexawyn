"""MCP tool: trace_pipeline_run_dag — DAG visualization for a PipelineRun."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.pipeline_tracer_port import PipelineTracerPort
from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_command import (
    TracePipelineRunDAGCommand,
)
from hexawyn.application.use_case.trace_pipeline_run_dag.trace_pipeline_run_dag_use_case import (
    TracePipelineRunDAGUseCase,
)
from hexawyn.domain.models.pipeline_dag import TaskRunNodeDict

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _build_adapter() -> PipelineTracerPort:
    from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
        TektonPipelineTracerAdapter,
    )

    return TektonPipelineTracerAdapter()


def _serialize_node(node: TaskRunNodeDict) -> dict[str, str | float | bool | list[str] | None]:
    return {
        "name": node["name"],
        "start_time": node["start_time"],
        "duration_seconds": node["duration_seconds"],
        "status": node["status"],
        "dependencies": node["dependencies"],
        "is_on_critical_path": node["is_on_critical_path"],
        "failure_reason": node["failure_reason"],
    }


def trace_pipeline_run_dag(
    pipeline_run_name: str,
    namespace: str = "ci",
) -> dict[str, object]:
    """Trace the full execution DAG of a Tekton PipelineRun.

    Returns the PipelineRun status, all child TaskRuns with start times,
    durations, dependencies, the critical path (longest sequential chain),
    and any failed or skipped tasks.

    Args:
        pipeline_run_name: Name of the PipelineRun to trace.
        namespace: Kubernetes namespace (default: "ci").
    """
    from hexawyn.application.service.trace_pipeline_run_dag_service import (
        TracePipelineRunDAGService,
    )

    try:
        adapter = _build_adapter()
        service = TracePipelineRunDAGService(port=adapter)
        use_case = TracePipelineRunDAGUseCase(service=service)
        response = use_case.execute(
            TracePipelineRunDAGCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        dag = response.dag
        nodes_dict: list[dict[str, str | float | bool | list[str] | None]] = [
            _serialize_node(
                {
                    "name": n.name,
                    "start_time": n.start_time.isoformat() if n.start_time else None,
                    "duration_seconds": n.duration_seconds,
                    "status": n.status,
                    "dependencies": n.dependencies,
                    "is_on_critical_path": n.is_on_critical_path,
                    "failure_reason": n.failure_reason,
                }
            )
            for n in dag.task_runs
        ]
        return {
            "pipeline_run_name": dag.pipeline_run_name,
            "namespace": dag.namespace,
            "pipeline_status": dag.pipeline_status,
            "pipeline_ref": dag.pipeline_ref,
            "total_task_runs": len(dag.task_runs),
            "task_runs": nodes_dict,
            "critical_path": dag.critical_path,
            "failed_tasks": dag.failed_tasks,
            "skipped_tasks": dag.skipped_tasks,
            "cancelled_at_tasks": dag.cancelled_at_tasks,
            "error": None,
        }
    except Exception as exc:
        return {
            "pipeline_run_name": pipeline_run_name,
            "namespace": namespace,
            "pipeline_status": "",
            "pipeline_ref": "",
            "total_task_runs": 0,
            "task_runs": [],
            "critical_path": [],
            "failed_tasks": [],
            "skipped_tasks": [],
            "cancelled_at_tasks": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(trace_pipeline_run_dag)

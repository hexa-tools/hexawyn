from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.pipeline_baseline_port import (
    PipelineBaselinePort,
    PipelineRunRecord,
    TaskRunRecord,
)

if TYPE_CHECKING:
    pass


class TektonPipelineBaselineAdapter(PipelineBaselinePort):
    def list_pipeline_runs(
        self, pipeline_name: str, namespace: str, limit: int
    ) -> list[PipelineRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = get_connection()
        rows = conn.execute(
            """
            SELECT p.name, p.status, p.duration_seconds,
                   p.start_time, p.completion_time
            FROM tekton_pipeline_runs p
            WHERE p.pipeline_name = ? AND p.namespace = ?
            ORDER BY p.start_time DESC
            LIMIT ?
            """,
            [pipeline_name, namespace, limit],
        ).fetchall()
        return [
            {
                "name": r[0],
                "status": r[1] or "unknown",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]

    def list_task_runs_for_pipeline(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = get_connection()
        rows = conn.execute(
            """
            SELECT t.name, t.task_name, t.pipeline_run_name, t.duration_seconds
            FROM tekton_task_runs t
            WHERE t.pipeline_run_name = ? AND t.namespace = ?
            """,
            [pipeline_run_name, namespace],
        ).fetchall()
        return [
            {
                "name": r[0],
                "task_name": r[1] or "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

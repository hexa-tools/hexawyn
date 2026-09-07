from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.pipeline_baseline_port import (
    PipelineBaselinePort,
    PipelineRunRecord,
    TaskRunRecord,
)

if TYPE_CHECKING:
    pass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut: MutantDict = {}  # type: ignore


class TektonPipelineBaselineAdapter(PipelineBaselinePort):
    @_mutmut_mutated(mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut)
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
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_orig(
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
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_1(
        self, pipeline_name: str, namespace: str, limit: int
    ) -> list[PipelineRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = None
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
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_2(
        self, pipeline_name: str, namespace: str, limit: int
    ) -> list[PipelineRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = get_connection()
        rows = None
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
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_3(
        self, pipeline_name: str, namespace: str, limit: int
    ) -> list[PipelineRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = get_connection()
        rows = conn.execute(
            None,
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
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_4(
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
            None,
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
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_5(
        self, pipeline_name: str, namespace: str, limit: int
    ) -> list[PipelineRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = get_connection()
        rows = conn.execute(
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
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_6(
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
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_7(
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
                "XXnameXX": r[0],
                "status": r[1] or "unknown",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_8(
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
                "NAME": r[0],
                "status": r[1] or "unknown",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_9(
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
                "name": r[1],
                "status": r[1] or "unknown",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_10(
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
                "XXstatusXX": r[1] or "unknown",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_11(
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
                "STATUS": r[1] or "unknown",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_12(
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
                "status": r[1] and "unknown",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_13(
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
                "status": r[2] or "unknown",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_14(
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
                "status": r[1] or "XXunknownXX",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_15(
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
                "status": r[1] or "UNKNOWN",
                "duration_seconds": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_16(
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
                "XXduration_secondsXX": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_17(
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
                "DURATION_SECONDS": r[2],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_18(
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
                "duration_seconds": r[3],
                "start_time": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_19(
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
                "XXstart_timeXX": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_20(
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
                "START_TIME": r[3],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_21(
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
                "start_time": r[4],
                "completion_time": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_22(
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
                "XXcompletion_timeXX": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_23(
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
                "COMPLETION_TIME": r[4],
            }
            for r in rows
        ]
    def xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_24(
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
                "completion_time": r[5],
            }
            for r in rows
        ]

    @_mutmut_mutated(mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut)
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

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_orig(
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

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_1(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = None
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

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_2(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = get_connection()
        rows = None
        return [
            {
                "name": r[0],
                "task_name": r[1] or "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_3(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = get_connection()
        rows = conn.execute(
            None,
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

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_4(
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
            None,
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

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_5(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from hexawyn.mcp.server import get_connection  # type: ignore

        conn = get_connection()
        rows = conn.execute(
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

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_6(
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

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_7(
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
                "XXnameXX": r[0],
                "task_name": r[1] or "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_8(
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
                "NAME": r[0],
                "task_name": r[1] or "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_9(
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
                "name": r[1],
                "task_name": r[1] or "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_10(
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
                "XXtask_nameXX": r[1] or "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_11(
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
                "TASK_NAME": r[1] or "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_12(
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
                "task_name": r[1] and "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_13(
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
                "task_name": r[2] or "unknown",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_14(
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
                "task_name": r[1] or "XXunknownXX",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_15(
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
                "task_name": r[1] or "UNKNOWN",
                "pipeline_run_name": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_16(
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
                "XXpipeline_run_nameXX": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_17(
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
                "PIPELINE_RUN_NAME": r[2] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_18(
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
                "pipeline_run_name": r[2] and pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_19(
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
                "pipeline_run_name": r[3] or pipeline_run_name,
                "duration_seconds": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_20(
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
                "XXduration_secondsXX": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_21(
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
                "DURATION_SECONDS": r[3],
            }
            for r in rows
        ]

    def xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_22(
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
                "duration_seconds": r[4],
            }
            for r in rows
        ]

mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['_mutmut_orig'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_1'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_2'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_3'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_4'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_5'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_6'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_7'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_8'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_9'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_10'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_11'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_12'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_13'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_14'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_15'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_16'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_17'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_18'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_19'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_20'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_21'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_22'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_23'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut['xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_24'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_pipeline_runs__mutmut_24 # type: ignore # mutmut generated

mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['_mutmut_orig'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_1'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_2'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_3'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_4'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_5'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_6'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_7'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_8'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_9'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_10'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_11'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_12'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_13'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_14'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_15'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_16'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_17'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_18'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_19'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_20'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_21'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_22'] = TektonPipelineBaselineAdapter.xǁTektonPipelineBaselineAdapterǁlist_task_runs_for_pipeline__mutmut_22 # type: ignore # mutmut generated

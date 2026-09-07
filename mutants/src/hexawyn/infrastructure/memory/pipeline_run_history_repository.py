from __future__ import annotations

from pathlib import Path

import duckdb

from hexawyn.application.ports.driven.pipeline_run_history_port import (
    PipelineRunHistoryPort,
    PipelineRunSnapshot,
    TaskRunSnapshot,
)

SQL_DIR = Path(__file__).parent / "sql"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__load_sql__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__load_sql__mutmut)
def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_orig(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_1(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding=None)


def x__load_sql__mutmut_2(filename: str) -> str:
    return (SQL_DIR * filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_3(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="XXutf-8XX")


def x__load_sql__mutmut_4(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="UTF-8")

mutants_x__load_sql__mutmut['_mutmut_orig'] = x__load_sql__mutmut_orig # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_1'] = x__load_sql__mutmut_1 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_2'] = x__load_sql__mutmut_2 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_3'] = x__load_sql__mutmut_3 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_4'] = x__load_sql__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut: MutantDict = {}  # type: ignore


class PipelineRunHistoryRepository(PipelineRunHistoryPort):
    """Persists Tekton PipelineRun/TaskRun snapshots to DuckDB.

    Best-effort: storage failures are swallowed — history persistence must
    never block the caller's pipeline response. Records are upserted by name
    so repeated listing does not duplicate history.
    """

    @_mutmut_mutated(mutants_xǁPipelineRunHistoryRepositoryǁ__init____mutmut)
    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def xǁPipelineRunHistoryRepositoryǁ__init____mutmut_orig(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def xǁPipelineRunHistoryRepositoryǁ__init____mutmut_1(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = None

    @_mutmut_mutated(mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut)
    def save_pipeline_runs(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_orig(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_1(self, runs: list[PipelineRunSnapshot]) -> None:
        if runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_2(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    None,
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_3(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    None,
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_4(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_5(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_6(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql(None),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_7(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("XXinsert_tekton_pipeline_run.sqlXX"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_8(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("INSERT_TEKTON_PIPELINE_RUN.SQL"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_9(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["XXnameXX"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_10(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["NAME"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_11(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["XXnamespaceXX"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_12(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["NAMESPACE"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_13(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["XXpipeline_nameXX"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_14(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["PIPELINE_NAME"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_15(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["XXstatusXX"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_16(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["STATUS"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_17(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["XXduration_secondsXX"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_18(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["DURATION_SECONDS"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_19(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["XXstart_timeXX"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_20(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["START_TIME"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_21(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["XXcompletion_timeXX"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_22(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["COMPLETION_TIME"],
                    ],
                )
        except Exception:
            pass

    @_mutmut_mutated(mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut)
    def save_task_runs(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_orig(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_1(self, task_runs: list[TaskRunSnapshot]) -> None:
        if task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_2(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    None,
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_3(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    None,
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_4(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_5(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_6(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql(None),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_7(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("XXinsert_tekton_task_run.sqlXX"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_8(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("INSERT_TEKTON_TASK_RUN.SQL"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_9(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["XXnameXX"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_10(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["NAME"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_11(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["XXnamespaceXX"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_12(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["NAMESPACE"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_13(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["XXtask_nameXX"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_14(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["TASK_NAME"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_15(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["XXpipeline_run_nameXX"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_16(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["PIPELINE_RUN_NAME"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_17(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["XXduration_secondsXX"],
                    ],
                )
        except Exception:
            pass

    def xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_18(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["DURATION_SECONDS"],
                    ],
                )
        except Exception:
            pass

mutants_xǁPipelineRunHistoryRepositoryǁ__init____mutmut['_mutmut_orig'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁ__init____mutmut['xǁPipelineRunHistoryRepositoryǁ__init____mutmut_1'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['_mutmut_orig'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_1'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_2'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_3'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_4'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_5'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_6'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_7'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_8'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_9'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_10'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_11'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_12'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_13'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_14'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_15'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_16'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_17'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_18'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_19'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_20'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_21'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_22'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_pipeline_runs__mutmut_22 # type: ignore # mutmut generated

mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['_mutmut_orig'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_1'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_2'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_3'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_4'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_5'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_6'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_7'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_8'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_9'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_10'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_11'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_12'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_13'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_14'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_15'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_16'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_17'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut['xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_18'] = PipelineRunHistoryRepository.xǁPipelineRunHistoryRepositoryǁsave_task_runs__mutmut_18 # type: ignore # mutmut generated

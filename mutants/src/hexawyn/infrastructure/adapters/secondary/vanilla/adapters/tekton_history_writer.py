from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_history_port import (
    PipelineRunHistoryPort,
    PipelineRunSnapshot,
    TaskRunSnapshot,
)
from hexawyn.application.ports.driven.tekton_port import (
    NamespacedPipelineRunInfo,
    PipelineRunInfo,
    TaskRunInfo,
    TektonPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTektonHistoryWriterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut: MutantDict = {}  # type: ignore


class TektonHistoryWriter(TektonPort):
    """Reads Tekton CRDs from the cluster and persists snapshots to DuckDB.

    Best-effort: a DuckDB write failure must never break the pipeline listing
    returned to the caller. The Tekton error semantics are preserved — empty
    lists are returned on ServiceNotFound / PipelineNotFound so callers see the
    same behaviour as the plain TektonPort.
    """

    @_mutmut_mutated(mutants_xǁTektonHistoryWriterǁ__init____mutmut)
    def __init__(
        self,
        tekton_port: TektonPort,
        history_port: PipelineRunHistoryPort,
    ) -> None:
        self._tekton = tekton_port
        self._history = history_port

    def xǁTektonHistoryWriterǁ__init____mutmut_orig(
        self,
        tekton_port: TektonPort,
        history_port: PipelineRunHistoryPort,
    ) -> None:
        self._tekton = tekton_port
        self._history = history_port

    def xǁTektonHistoryWriterǁ__init____mutmut_1(
        self,
        tekton_port: TektonPort,
        history_port: PipelineRunHistoryPort,
    ) -> None:
        self._tekton = None
        self._history = history_port

    def xǁTektonHistoryWriterǁ__init____mutmut_2(
        self,
        tekton_port: TektonPort,
        history_port: PipelineRunHistoryPort,
    ) -> None:
        self._tekton = tekton_port
        self._history = None

    @_mutmut_mutated(mutants_xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut)
    def list_pipeline_runs_in_namespace(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._tekton.list_pipeline_runs_in_namespace(namespace, limit)

    def xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_orig(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._tekton.list_pipeline_runs_in_namespace(namespace, limit)

    def xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_1(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._tekton.list_pipeline_runs_in_namespace(None, limit)

    def xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_2(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._tekton.list_pipeline_runs_in_namespace(namespace, None)

    def xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_3(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._tekton.list_pipeline_runs_in_namespace(limit)

    def xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_4(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._tekton.list_pipeline_runs_in_namespace(namespace, )

    @_mutmut_mutated(mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut)
    def list_pipeline_runs(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_orig(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_1(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = None
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_2(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(None, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_3(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, None)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_4(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_5(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, )
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_6(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = None
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_7(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "XXnameXX": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_8(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "NAME": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_9(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["XXnameXX"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_10(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["NAME"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_11(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "XXnamespaceXX": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_12(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "NAMESPACE": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_13(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "XXpipeline_nameXX": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_14(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "PIPELINE_NAME": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_15(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "XXstatusXX": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_16(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "STATUS": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_17(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["XXstatusXX"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_18(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["STATUS"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_19(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "XXduration_secondsXX": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_20(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "DURATION_SECONDS": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_21(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["XXduration_secondsXX"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_22(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["DURATION_SECONDS"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_23(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "XXstart_timeXX": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_24(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "START_TIME": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_25(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["XXstart_timeXX"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_26(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["START_TIME"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_27(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "XXcompletion_timeXX": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_28(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "COMPLETION_TIME": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_29(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(None)
        except Exception:
            pass
        return runs

    @_mutmut_mutated(mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut)
    def list_task_runs(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_orig(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_1(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = None
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_2(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(None, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_3(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, None)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_4(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_5(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, )
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_6(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = None
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_7(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "XXnameXX": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_8(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "NAME": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_9(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["XXnameXX"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_10(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["NAME"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_11(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "XXnamespaceXX": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_12(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "NAMESPACE": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_13(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "XXtask_nameXX": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_14(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "TASK_NAME": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_15(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["XXtask_refXX"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_16(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["TASK_REF"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_17(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "XXpipeline_run_nameXX": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_18(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "PIPELINE_RUN_NAME": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_19(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "XXduration_secondsXX": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_20(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "DURATION_SECONDS": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs

    def xǁTektonHistoryWriterǁlist_task_runs__mutmut_21(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(None)
        except Exception:
            pass
        return task_runs

mutants_xǁTektonHistoryWriterǁ__init____mutmut['_mutmut_orig'] = TektonHistoryWriter.xǁTektonHistoryWriterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁ__init____mutmut['xǁTektonHistoryWriterǁ__init____mutmut_1'] = TektonHistoryWriter.xǁTektonHistoryWriterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁ__init____mutmut['xǁTektonHistoryWriterǁ__init____mutmut_2'] = TektonHistoryWriter.xǁTektonHistoryWriterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut['_mutmut_orig'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_1'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_2'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_3'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_4'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs_in_namespace__mutmut_4 # type: ignore # mutmut generated

mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['_mutmut_orig'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_1'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_2'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_3'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_4'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_5'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_6'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_7'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_8'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_9'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_10'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_11'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_12'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_13'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_14'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_15'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_16'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_17'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_18'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_19'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_20'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_21'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_22'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_23'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_24'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_25'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_26'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_27'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_28'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut['xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_29'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_pipeline_runs__mutmut_29 # type: ignore # mutmut generated

mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['_mutmut_orig'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_1'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_2'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_3'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_4'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_5'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_6'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_7'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_8'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_9'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_10'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_11'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_12'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_13'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_14'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_15'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_16'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_17'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_18'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_19'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_20'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTektonHistoryWriterǁlist_task_runs__mutmut['xǁTektonHistoryWriterǁlist_task_runs__mutmut_21'] = TektonHistoryWriter.xǁTektonHistoryWriterǁlist_task_runs__mutmut_21 # type: ignore # mutmut generated

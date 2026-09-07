from __future__ import annotations

from datetime import datetime

from hexawyn.application.ports.driven.pipeline_tracer_port import TaskRunRecord
from hexawyn.domain.models.pipeline_dag import PipelineDAG, TaskRunNode


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut: MutantDict = {}  # type: ignore


class PipelineDAGTracerService:
    @staticmethod
    @_mutmut_mutated(mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut)
    def build_dag(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_orig(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_1(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "XXXX",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_2(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = None

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_3(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=None,
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_4(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=None,
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_5(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=None,
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_6(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=None,
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_7(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=None,
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_8(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_9(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_10(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_11(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_12(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_13(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["XXnameXX"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_14(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["NAME"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_15(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(None, r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_16(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), None),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_17(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_18(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), ),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_19(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get(None), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_20(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("XXstart_timeXX"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_21(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("START_TIME"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_22(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get(None)),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_23(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("XXcompletion_timeXX")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_24(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("COMPLETION_TIME")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_25(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["XXstatusXX"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_26(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["STATUS"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_27(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(None),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_28(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get(None, [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_29(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", None)),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_30(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get([])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_31(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", )),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_32(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("XXrun_afterXX", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_33(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("RUN_AFTER", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_34(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get(None, ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_35(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", None),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_36(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get(""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_37(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_38(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("XXfailure_reasonXX", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_39(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("FAILURE_REASON", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_40(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", "XXXX"),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_41(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = None
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_42(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status != "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_43(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "XXFailedXX"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_44(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_45(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "FAILED"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_46(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = None
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_47(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(None, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_48(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, None, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_49(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, None)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_50(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_51(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_52(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, )

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_53(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = None

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_54(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(None)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_55(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = None

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_56(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(None)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_57(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name not in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_58(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = None

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_59(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = False

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_60(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = None
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_61(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(None)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_62(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=None,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_63(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=None,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_64(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=None,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_65(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=None,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_66(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=None,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_67(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=None,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_68(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=None,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_69(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=None,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_70(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_71(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_72(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_73(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_74(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_75(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            skipped_tasks=skipped_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_76(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            cancelled_at_tasks=cancelled_at_tasks,
        )
    @staticmethod
    def xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_77(
        pipeline_run_name: str,
        namespace: str,
        pipeline_status: str,
        task_runs: list[TaskRunRecord],
        cancelled_by: str = "",
    ) -> PipelineDAG:
        nodes = [
            TaskRunNode(
                name=r["name"],
                duration_seconds=_compute_duration(r.get("start_time"), r.get("completion_time")),
                status=r["status"],
                dependencies=list(r.get("run_after", [])),
                failure_reason=r.get("failure_reason", ""),
            )
            for r in task_runs
        ]

        failed_tasks = [n.name for n in nodes if n.status == "Failed"]
        downstream_skipped: set[str] = set()
        for failed_name in failed_tasks:
            _collect_downstream(failed_name, nodes, downstream_skipped)

        skipped_tasks = sorted(downstream_skipped)

        critical_path = PipelineDAGTracerService._compute_critical_path(nodes)

        for node in nodes:
            if node.name in critical_path:
                node.is_on_critical_path = True

        cancelled_at_tasks: list[str] = []
        if cancelled_by:
            cancelled_at_tasks.append(cancelled_by)

        return PipelineDAG(
            pipeline_run_name=pipeline_run_name,
            namespace=namespace,
            pipeline_status=pipeline_status,
            task_runs=nodes,
            critical_path=critical_path,
            failed_tasks=failed_tasks,
            skipped_tasks=skipped_tasks,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut)
    def compute_parallel_groups(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_orig(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_1(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = None
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_2(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = None
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_3(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(None, dag.task_runs)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_4(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, None)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_5(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(dag.task_runs)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_6(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, )
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_7(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, []).append(None)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_8(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(None, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_9(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, None).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_10(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault([]).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_11(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, ).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_12(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) >= 1]

    @staticmethod
    def xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_13(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 2]

    @staticmethod
    @_mutmut_mutated(mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut)
    def _compute_critical_path(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_orig(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_1(nodes: list[TaskRunNode]) -> list[str]:
        if nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_2(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = None
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_3(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = None

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_4(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name not in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_5(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = None
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_6(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(None)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_7(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is not None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_8(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_9(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = None
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_10(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = None
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_11(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = None
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_12(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 1.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_13(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = None
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_14(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) - [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_15(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(None) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_16(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = None
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_17(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    None
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_18(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n not in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_19(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost >= best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_20(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = None
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_21(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = None
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_22(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = None
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_23(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = None
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_24(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(None) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_25(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = None
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_26(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            None,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_27(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=None,
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_28(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n in name_to_node),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_29(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_30(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: None,
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_31(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(None),
        )
        return best_chain

    @staticmethod
    def xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_32(nodes: list[TaskRunNode]) -> list[str]:
        if not nodes:
            return []
        name_to_node = {n.name: n for n in nodes}
        memo: dict[str, list[str]] = {}

        def longest_from(name: str) -> list[str]:
            if name in memo:
                return memo[name]
            node = name_to_node.get(name)
            if node is None:
                return [name]
            if not node.dependencies:
                memo[name] = [name]
                return [name]
            best: list[str] = []
            best_cost: float = 0.0
            for dep in node.dependencies:
                candidate = longest_from(dep) + [name]
                candidate_cost = sum(
                    name_to_node[n].duration_seconds for n in candidate if n in name_to_node
                )
                if candidate_cost > best_cost:
                    best = candidate
                    best_cost = candidate_cost
            memo[name] = best
            return best

        all_chains = [longest_from(n.name) for n in nodes]
        best_chain = max(
            all_chains,
            key=lambda c: sum(name_to_node[n].duration_seconds for n in c if n not in name_to_node),
        )
        return best_chain

mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['_mutmut_orig'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_1'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_2'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_3'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_4'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_5'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_6'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_7'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_8'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_9'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_10'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_11'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_12'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_13'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_14'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_15'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_16'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_17'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_18'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_19'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_20'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_21'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_22'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_23'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_24'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_25'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_26'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_27'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_28'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_29'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_30'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_31'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_32'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_33'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_34'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_35'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_36'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_37'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_38'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_39'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_40'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_41'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_42'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_43'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_44'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_45'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_46'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_47'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_48'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_49'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_50'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_51'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_52'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_52 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_53'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_53 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_54'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_54 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_55'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_55 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_56'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_56 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_57'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_57 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_58'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_58 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_59'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_59 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_60'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_60 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_61'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_61 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_62'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_62 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_63'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_63 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_64'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_64 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_65'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_65 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_66'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_66 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_67'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_67 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_68'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_68 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_69'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_69 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_70'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_70 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_71'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_71 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_72'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_72 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_73'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_73 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_74'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_74 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_75'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_75 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_76'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_76 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁbuild_dag__mutmut['xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_77'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁbuild_dag__mutmut_77 # type: ignore # mutmut generated

mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['_mutmut_orig'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_1'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_2'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_3'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_4'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_5'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_6'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_7'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_8'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_9'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_10'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_11'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_12'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut['xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_13'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁcompute_parallel_groups__mutmut_13 # type: ignore # mutmut generated

mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['_mutmut_orig'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_1'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_2'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_3'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_4'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_5'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_6'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_7'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_8'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_9'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_10'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_11'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_12'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_13'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_14'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_15'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_16'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_17'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_18'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_19'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_20'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_21'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_22'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_23'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_24'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_25'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_26'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_27'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_28'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_29'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_30'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_31'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut['xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_32'] = PipelineDAGTracerService.xǁPipelineDAGTracerServiceǁ_compute_critical_path__mutmut_32 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_duration__mutmut)
def _compute_duration(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_orig(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_1(start: str | None, end: str | None) -> float:
    if not start and not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_2(start: str | None, end: str | None) -> float:
    if start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_3(start: str | None, end: str | None) -> float:
    if not start or end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_4(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 1.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_5(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = None
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_6(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(None)
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_7(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace(None, "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_8(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", None))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_9(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_10(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", ))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_11(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("XXZXX", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_12(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_13(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "XX+00:00XX"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_14(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = None
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_15(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(None)
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_16(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace(None, "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_17(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", None))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_18(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_19(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", ))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_20(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("XXZXX", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_21(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_22(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "XX+00:00XX"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_23(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e + s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def x__compute_duration__mutmut_24(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 1.0

mutants_x__compute_duration__mutmut['_mutmut_orig'] = x__compute_duration__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_1'] = x__compute_duration__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_2'] = x__compute_duration__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_3'] = x__compute_duration__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_4'] = x__compute_duration__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_5'] = x__compute_duration__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_6'] = x__compute_duration__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_7'] = x__compute_duration__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_8'] = x__compute_duration__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_9'] = x__compute_duration__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_10'] = x__compute_duration__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_11'] = x__compute_duration__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_12'] = x__compute_duration__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_13'] = x__compute_duration__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_14'] = x__compute_duration__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_15'] = x__compute_duration__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_16'] = x__compute_duration__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_17'] = x__compute_duration__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_18'] = x__compute_duration__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_19'] = x__compute_duration__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_20'] = x__compute_duration__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_21'] = x__compute_duration__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_22'] = x__compute_duration__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_23'] = x__compute_duration__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_duration__mutmut['x__compute_duration__mutmut_24'] = x__compute_duration__mutmut_24 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__collect_downstream__mutmut)
def _collect_downstream(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, nodes, result)


def x__collect_downstream__mutmut_orig(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, nodes, result)


def x__collect_downstream__mutmut_1(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result or failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, nodes, result)


def x__collect_downstream__mutmut_2(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, nodes, result)


def x__collect_downstream__mutmut_3(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name not in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, nodes, result)


def x__collect_downstream__mutmut_4(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(None)
            _collect_downstream(node.name, nodes, result)


def x__collect_downstream__mutmut_5(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(None, nodes, result)


def x__collect_downstream__mutmut_6(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, None, result)


def x__collect_downstream__mutmut_7(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, nodes, None)


def x__collect_downstream__mutmut_8(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(nodes, result)


def x__collect_downstream__mutmut_9(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, result)


def x__collect_downstream__mutmut_10(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, nodes, )

mutants_x__collect_downstream__mutmut['_mutmut_orig'] = x__collect_downstream__mutmut_orig # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_1'] = x__collect_downstream__mutmut_1 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_2'] = x__collect_downstream__mutmut_2 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_3'] = x__collect_downstream__mutmut_3 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_4'] = x__collect_downstream__mutmut_4 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_5'] = x__collect_downstream__mutmut_5 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_6'] = x__collect_downstream__mutmut_6 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_7'] = x__collect_downstream__mutmut_7 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_8'] = x__collect_downstream__mutmut_8 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_9'] = x__collect_downstream__mutmut_9 # type: ignore # mutmut generated
mutants_x__collect_downstream__mutmut['x__collect_downstream__mutmut_10'] = x__collect_downstream__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_depth__mutmut)
def _compute_depth(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_orig(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_1(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = None
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_2(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = None
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_3(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(None)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_4(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is not None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_5(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 1
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_6(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_7(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 1
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_8(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 - max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_9(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 2 + max(_compute_depth(d, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_10(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(None)


def x__compute_depth__mutmut_11(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(None, nodes) for d in node.dependencies)


def x__compute_depth__mutmut_12(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, None) for d in node.dependencies)


def x__compute_depth__mutmut_13(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(nodes) for d in node.dependencies)


def x__compute_depth__mutmut_14(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, ) for d in node.dependencies)

mutants_x__compute_depth__mutmut['_mutmut_orig'] = x__compute_depth__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_1'] = x__compute_depth__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_2'] = x__compute_depth__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_3'] = x__compute_depth__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_4'] = x__compute_depth__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_5'] = x__compute_depth__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_6'] = x__compute_depth__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_7'] = x__compute_depth__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_8'] = x__compute_depth__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_9'] = x__compute_depth__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_10'] = x__compute_depth__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_11'] = x__compute_depth__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_12'] = x__compute_depth__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_13'] = x__compute_depth__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_depth__mutmut['x__compute_depth__mutmut_14'] = x__compute_depth__mutmut_14 # type: ignore # mutmut generated

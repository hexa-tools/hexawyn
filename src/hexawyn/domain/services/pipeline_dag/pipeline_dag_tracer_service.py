from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_tracer_port import TaskRunRecord
from hexawyn.domain.models.pipeline_dag import PipelineDAG, TaskRunNode


class PipelineDAGTracerService:
    @staticmethod
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
    def compute_parallel_groups(dag: PipelineDAG) -> list[list[str]]:
        by_level: dict[int, list[str]] = {}
        for node in dag.task_runs:
            depth = _compute_depth(node.name, dag.task_runs)
            by_level.setdefault(depth, []).append(node.name)
        return [names for names in by_level.values() if len(names) > 1]

    @staticmethod
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


def _compute_duration(start: str | None, end: str | None) -> float:
    if not start or not end:
        return 0.0
    try:
        from datetime import datetime

        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (e - s).total_seconds()
    except (ValueError, TypeError):
        return 0.0


def _collect_downstream(
    failed_name: str,
    nodes: list[TaskRunNode],
    result: set[str],
) -> None:
    for node in nodes:
        if node.name not in result and failed_name in node.dependencies:
            result.add(node.name)
            _collect_downstream(node.name, nodes, result)


def _compute_depth(name: str, nodes: list[TaskRunNode]) -> int:
    name_to_node = {n.name: n for n in nodes}
    node = name_to_node.get(name)
    if node is None:
        return 0
    if not node.dependencies:
        return 0
    return 1 + max(_compute_depth(d, nodes) for d in node.dependencies)

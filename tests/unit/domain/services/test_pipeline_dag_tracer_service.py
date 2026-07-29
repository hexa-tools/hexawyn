from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_tracer_port import TaskRunRecord
from hexawyn.domain.models.pipeline_dag import TaskRunNode
from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
    PipelineDAGTracerService,
    _collect_downstream,
    _compute_depth,
    _compute_duration,
)


def _make_task(  # noqa: PLR0913
    name: str,
    status: str = "Succeeded",
    start_time: str | None = "2026-01-01T00:00:00Z",
    completion_time: str | None = "2026-01-01T00:05:00Z",
    dependencies: list[str] | None = None,
    failure_reason: str = "",
) -> TaskRunRecord:
    return TaskRunRecord(
        name=name,
        namespace="default",
        pipeline_run_name="test-run",
        start_time=start_time,
        completion_time=completion_time,
        status=status,
        run_after=dependencies or [],
        failure_reason=failure_reason,
    )


class TestComputeDuration:
    def test_iso_duration_computed(self) -> None:
        result = _compute_duration("2026-01-01T00:00:00Z", "2026-01-01T00:05:00Z")
        assert result == 300.0  # noqa: PLR2004

    def test_missing_start_returns_zero(self) -> None:
        assert _compute_duration(None, "2026-01-01T00:05:00Z") == 0.0

    def test_missing_end_returns_zero(self) -> None:
        assert _compute_duration("2026-01-01T00:00:00Z", None) == 0.0

    def test_invalid_format_returns_zero(self) -> None:
        assert _compute_duration("BAD", "2026-01-01T00:05:00Z") == 0.0

    def test_both_none_returns_zero(self) -> None:
        assert _compute_duration(None, None) == 0.0

    def test_with_timezone_offset(self) -> None:
        result = _compute_duration("2026-01-01T00:00:00+01:00", "2026-01-01T01:00:00+01:00")
        assert result == 3600.0  # noqa: PLR2004

    def test_with_microsecond_precision(self) -> None:
        result = _compute_duration("2026-01-01T00:00:00Z", "2026-01-01T00:01:30.500000Z")
        assert result == 90.5  # noqa: PLR2004


class TestCollectDownstream:
    def test_no_downstream_when_name_has_no_consumers(self) -> None:
        nodes = [
            TaskRunNode(name="build", status="Failed", dependencies=[]),
            TaskRunNode(name="test", status="Succeeded", dependencies=["other"]),
        ]
        result: set[str] = set()
        _collect_downstream("build", nodes, result)
        assert result == set()

    def test_collects_direct_downstream(self) -> None:
        nodes = [
            TaskRunNode(name="build", status="Failed", dependencies=[]),
            TaskRunNode(name="test", status="Succeeded", dependencies=["build"]),
        ]
        result: set[str] = set()
        _collect_downstream("build", nodes, result)
        assert result == {"test"}

    def test_collects_transitive_downstream(self) -> None:
        nodes = [
            TaskRunNode(name="a", status="Failed", dependencies=[]),
            TaskRunNode(name="b", status="Succeeded", dependencies=["a"]),
            TaskRunNode(name="c", status="Succeeded", dependencies=["b"]),
        ]
        result: set[str] = set()
        _collect_downstream("a", nodes, result)
        assert result == {"b", "c"}

    def test_does_not_add_already_collected(self) -> None:
        nodes = [
            TaskRunNode(name="a", status="Failed", dependencies=[]),
            TaskRunNode(name="b", status="Succeeded", dependencies=["a"]),
        ]
        result: set[str] = {"b"}
        _collect_downstream("a", nodes, result)
        assert result == {"b"}

    def test_diamond_dependency(self) -> None:
        nodes = [
            TaskRunNode(name="root", status="Failed", dependencies=[]),
            TaskRunNode(name="left", status="Succeeded", dependencies=["root"]),
            TaskRunNode(name="right", status="Succeeded", dependencies=["root"]),
            TaskRunNode(name="merge", status="Succeeded", dependencies=["left", "right"]),
        ]
        result: set[str] = set()
        _collect_downstream("root", nodes, result)
        assert result == {"left", "right", "merge"}


class TestComputeDepth:
    def test_no_deps_has_zero_depth(self) -> None:
        nodes = [TaskRunNode(name="build", dependencies=[])]
        assert _compute_depth("build", nodes) == 0

    def test_depth_one(self) -> None:
        nodes = [
            TaskRunNode(name="build", dependencies=[]),
            TaskRunNode(name="test", dependencies=["build"]),
        ]
        assert _compute_depth("test", nodes) == 1

    def test_depth_two(self) -> None:
        nodes = [
            TaskRunNode(name="a", dependencies=[]),
            TaskRunNode(name="b", dependencies=["a"]),
            TaskRunNode(name="c", dependencies=["b"]),
        ]
        assert _compute_depth("c", nodes) == 2  # noqa: PLR2004

    def test_unknown_name_returns_zero(self) -> None:
        nodes = [TaskRunNode(name="a", dependencies=[])]
        assert _compute_depth("unknown", nodes) == 0

    def test_deepest_branch_in_diamond(self) -> None:
        nodes = [
            TaskRunNode(name="root", dependencies=[]),
            TaskRunNode(name="left", dependencies=["root"]),
            TaskRunNode(name="right", dependencies=["root"]),
            TaskRunNode(name="merge", dependencies=["left", "right"]),
        ]
        assert _compute_depth("merge", nodes) == 2  # noqa: PLR2004


class TestBuildDAG:
    def test_builds_dag_with_simple_pipeline(self) -> None:
        tasks = [
            _make_task("build", status="Succeeded"),
            _make_task("test", status="Succeeded", dependencies=["build"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-1", "default", "Succeeded", tasks)
        assert dag.pipeline_run_name == "run-1"
        assert dag.namespace == "default"
        assert dag.pipeline_status == "Succeeded"
        assert len(dag.task_runs) == 2  # noqa: PLR2004
        assert dag.critical_path == ["build", "test"]
        assert dag.failed_tasks == []
        assert dag.skipped_tasks == []

    def test_failed_task_marks_downstream_as_skipped(self) -> None:
        tasks = [
            _make_task("build", status="Failed"),
            _make_task("test", status="Succeeded", dependencies=["build"]),
            _make_task("deploy", status="Succeeded", dependencies=["test"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-2", "ci", "Failed", tasks)
        assert dag.failed_tasks == ["build"]
        assert "test" in dag.skipped_tasks
        assert "deploy" in dag.skipped_tasks

    def test_critical_path_marked_on_nodes(self) -> None:
        tasks = [
            _make_task("build", status="Succeeded", completion_time="2026-01-01T00:05:00Z"),
            _make_task(
                "test",
                status="Succeeded",
                completion_time="2026-01-01T00:15:00Z",
                dependencies=["build"],
            ),
        ]
        dag = PipelineDAGTracerService.build_dag("run-3", "default", "Succeeded", tasks)
        for node in dag.task_runs:
            assert node.is_on_critical_path

    def test_cancelled_by_appended(self) -> None:
        tasks: list[TaskRunRecord] = [_make_task("build", status="Succeeded")]
        dag = PipelineDAGTracerService.build_dag(
            "run-4", "default", "Cancelled", tasks, cancelled_by="user-ops"
        )
        assert dag.cancelled_at_tasks == ["user-ops"]

    def test_cancelled_by_omitted_when_empty(self) -> None:
        tasks: list[TaskRunRecord] = [_make_task("build", status="Succeeded")]
        dag = PipelineDAGTracerService.build_dag("run-5", "default", "Succeeded", tasks)
        assert dag.cancelled_at_tasks == []

    def test_empty_task_list(self) -> None:
        dag = PipelineDAGTracerService.build_dag("run-6", "default", "Succeeded", [])
        assert dag.task_runs == []
        assert dag.critical_path == []
        assert dag.failed_tasks == []

    def test_longest_path_selected_as_critical(self) -> None:
        tasks = [
            _make_task("a", completion_time="2026-01-01T00:10:00Z"),
            _make_task("b", completion_time="2026-01-01T00:01:00Z", dependencies=["a"]),
            _make_task("c", completion_time="2026-01-01T00:50:00Z", dependencies=["a"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-7", "default", "Succeeded", tasks)
        assert dag.critical_path == ["a", "c"]

    def test_multiple_failures_skip_all_downstream(self) -> None:
        tasks = [
            _make_task("a", status="Failed"),
            _make_task("b", status="Failed"),
            _make_task("test-a", dependencies=["a"]),
            _make_task("test-b", dependencies=["b"]),
            _make_task("merge", dependencies=["test-a", "test-b"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-8", "default", "Failed", tasks)
        assert dag.failed_tasks == ["a", "b"]
        assert "test-a" in dag.skipped_tasks
        assert "test-b" in dag.skipped_tasks
        assert "merge" in dag.skipped_tasks

    def test_critical_path_picks_longest_chain(self) -> None:
        tasks = [
            _make_task("a", completion_time="2026-01-01T00:10:00Z"),
            _make_task("b", completion_time="2026-01-01T00:01:00Z"),
            _make_task("c", completion_time="2026-01-01T00:05:00Z", dependencies=["a", "b"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-9", "default", "Succeeded", tasks)
        assert dag.critical_path == ["a", "c"]

    def test_none_timestamps_in_tasks_handled(self) -> None:
        tasks = [
            _make_task("build", start_time=None, completion_time=None),
            _make_task("test", start_time=None, completion_time=None, dependencies=["build"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-10", "default", "Succeeded", tasks)
        assert len(dag.task_runs) == 2  # noqa: PLR2004
        for node in dag.task_runs:
            assert node.duration_seconds == 0.0


class TestComputeParallelGroups:
    def test_no_parallel_groups_when_all_sequential(self) -> None:
        dag = PipelineDAGTracerService.build_dag(
            "run-1",
            "default",
            "Succeeded",
            [
                _make_task("a"),
                _make_task("b", dependencies=["a"]),
                _make_task("c", dependencies=["b"]),
            ],
        )
        groups = PipelineDAGTracerService.compute_parallel_groups(dag)
        assert groups == []

    def test_detects_parallel_tasks_at_same_depth(self) -> None:
        tasks = [
            _make_task("build"),
            _make_task("lint"),
            _make_task("test-build", dependencies=["build"]),
            _make_task("test-lint", dependencies=["lint"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-2", "default", "Succeeded", tasks)
        groups = PipelineDAGTracerService.compute_parallel_groups(dag)
        assert ["build", "lint"] in groups
        assert ["test-build", "test-lint"] in groups

    def test_does_not_group_solitary_tasks(self) -> None:
        tasks = [
            _make_task("build"),
            _make_task("test", dependencies=["build"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-3", "default", "Succeeded", tasks)
        groups = PipelineDAGTracerService.compute_parallel_groups(dag)
        assert groups == []

    def test_multiple_same_level(self) -> None:
        tasks = [
            _make_task("a"),
            _make_task("b"),
            _make_task("c"),
        ]
        dag = PipelineDAGTracerService.build_dag("run-4", "default", "Succeeded", tasks)
        groups = PipelineDAGTracerService.compute_parallel_groups(dag)
        assert ["a", "b", "c"] in groups

    def test_failure_reason_in_nodes(self) -> None:
        tasks = [
            _make_task("build", failure_reason="timeout"),
            _make_task("test", dependencies=["build"]),
        ]
        dag = PipelineDAGTracerService.build_dag("run-5", "default", "Failed", tasks)
        for node in dag.task_runs:
            if node.name == "build":
                assert node.failure_reason == "timeout"
            else:
                assert node.failure_reason == ""

    def test_completion_time_without_trailing_z(self) -> None:
        result = _compute_duration("2026-01-01T00:00:00+00:00", "2026-01-01T01:00:00+00:00")
        assert result == 3600.0  # noqa: PLR2004

    def test_critical_path_handles_unknown_dependency(self) -> None:
        tasks = [
            _make_task("a", completion_time="2026-01-01T00:01:00Z", dependencies=["orphan"]),
            _make_task("b", completion_time="2026-01-01T00:05:00Z"),
        ]
        dag = PipelineDAGTracerService.build_dag("run-orphan", "default", "Succeeded", tasks)
        assert dag.critical_path is not None

from __future__ import annotations

from datetime import datetime

from hexawyn.domain.models.pipeline_dag import DAGEdge, PipelineDAG, TaskRunNode, TaskRunNodeDict


class TestTaskRunNodeDict:
    def test_create(self) -> None:
        d: TaskRunNodeDict = {
            "name": "build",
            "start_time": "2026-01-01T00:00:00Z",
            "duration_seconds": 45.0,
            "status": "Succeeded",
            "dependencies": [],
            "is_on_critical_path": True,
            "failure_reason": "",
        }
        assert d["name"] == "build"
        assert d["duration_seconds"] == 45.0  # noqa: PLR2004


class TestTaskRunNode:
    def test_create(self) -> None:
        n = TaskRunNode(name="build", status="Succeeded", duration_seconds=45.0)
        assert n.name == "build"
        assert n.dependencies == []
        assert not n.is_on_critical_path

    def test_with_deps(self) -> None:
        n = TaskRunNode(
            name="test",
            start_time=datetime(2026, 1, 1),
            duration_seconds=120.0,
            status="Failed",
            dependencies=["build"],
            is_on_critical_path=True,
            failure_reason="timeout",
        )
        assert n.dependencies == ["build"]
        assert n.is_on_critical_path
        assert n.failure_reason == "timeout"


class TestDAGEdge:
    def test_create(self) -> None:
        e = DAGEdge(source="build", target="test")
        assert e.source == "build"
        assert e.target == "test"


class TestPipelineDAG:
    def test_defaults(self) -> None:
        dag = PipelineDAG(pipeline_run_name="run-1", namespace="default")
        assert dag.pipeline_run_name == "run-1"
        assert dag.pipeline_status == ""
        assert dag.task_runs == []
        assert dag.critical_path == []
        assert dag.failed_tasks == []

    def test_with_tasks(self) -> None:
        n = TaskRunNode(name="build", status="Succeeded")
        dag = PipelineDAG(
            pipeline_run_name="run-2",
            namespace="ci",
            pipeline_status="completed",
            pipeline_ref="pipeline-xyz",
            task_runs=[n],
            critical_path=["build"],
            failed_tasks=[],
            skipped_tasks=["lint"],
            cancelled_at_tasks=[],
        )
        assert dag.pipeline_status == "completed"
        assert len(dag.task_runs) == 1
        assert dag.critical_path == ["build"]
        assert dag.skipped_tasks == ["lint"]

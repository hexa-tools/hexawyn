"""Unit tests for trace_pipeline_run_dag use case — TDD Red phase."""

from __future__ import annotations

import datetime as dt
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.pipeline_tracer_port import (
    PipelineRunRecord,
    PipelineTracerPort,
    TaskRunRecord,
)
from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_command import (
    TracePipelineRunDAGCommand,
)
from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_response import (
    TracePipelineRunDAGResponse,
)
from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_service_port import (
    TracePipelineRunDAGServicePort,
)
from hexawyn.application.service.trace_pipeline_run_dag_service import (
    TracePipelineRunDAGService,
)
from hexawyn.application.use_case.trace_pipeline_run_dag.trace_pipeline_run_dag_use_case import (
    TracePipelineRunDAGUseCase,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    PipelineNotFoundError,
    TektonNotInstalledError,
)
from hexawyn.domain.models.pipeline_dag import (
    DAGEdge,
    PipelineDAG,
    TaskRunNode,
)
from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
    PipelineDAGTracerService,
)

UTC = dt.UTC
_BASE = datetime(2026, 6, 15, 10, 0, 0, tzinfo=UTC)


# ── Helpers ────────────────────────────────────────────────────────────────


def _tr(
    name: str = "fetch-source",
    namespace: str = "ci",
    pipeline_run_name: str = "deploy-checkout-v5",
    start_time: datetime | None = None,
    completion_time: datetime | None = None,
    status: str = "Succeeded",
    run_after: list[str] | None = None,
    failure_reason: str = "",
) -> TaskRunRecord:
    start = start_time or _BASE
    end = completion_time or (start + timedelta(seconds=30))
    return TaskRunRecord(
        name=name,
        namespace=namespace,
        pipeline_run_name=pipeline_run_name,
        start_time=start.isoformat(),
        completion_time=end.isoformat(),
        status=status,
        run_after=run_after or [],
        failure_reason=failure_reason,
    )


def _pr(
    name: str = "deploy-checkout-v5",
    namespace: str = "ci",
    status: str = "Succeeded",
    start_time: str | None = None,
    completion_time: str | None = None,
    pipeline_ref: str = "deploy-pipeline",
) -> PipelineRunRecord:
    return PipelineRunRecord(
        name=name,
        namespace=namespace,
        status=status,
        start_time=start_time or _BASE.isoformat(),
        completion_time=completion_time or (_BASE + timedelta(minutes=4)).isoformat(),
        pipeline_ref=pipeline_ref,
    )


# ── Tests: Domain Models ───────────────────────────────────────────────────


class TestTaskRunNode:
    def test_creation_defaults(self) -> None:
        node = TaskRunNode(name="fetch-source")
        assert node.name == "fetch-source"
        assert node.status == ""
        assert node.duration_seconds == 0.0
        assert node.dependencies == []
        assert node.is_on_critical_path is False

    def test_with_all_fields(self) -> None:
        node = TaskRunNode(
            name="build-image",
            start_time=_BASE + timedelta(seconds=30),
            duration_seconds=130.0,
            status="Succeeded",
            dependencies=["fetch-source"],
            is_on_critical_path=True,
            failure_reason="",
        )
        assert node.name == "build-image"
        assert node.duration_seconds == 130.0
        assert node.is_on_critical_path is True

    def test_last_in_critical_chain(self) -> None:
        node = TaskRunNode(
            name="deploy",
            duration_seconds=45.0,
            status="Succeeded",
            dependencies=["build-image", "run-tests"],
        )
        assert len(node.dependencies) == 2


class TestPipelineDAG:
    def test_empty_dag(self) -> None:
        dag = PipelineDAG(pipeline_run_name="test-pr", namespace="ci")
        assert dag.pipeline_run_name == "test-pr"
        assert dag.namespace == "ci"
        assert dag.pipeline_status == ""
        assert dag.task_runs == []
        assert dag.critical_path == []
        assert dag.failed_tasks == []
        assert dag.skipped_tasks == []

    def test_with_tasks(self) -> None:
        nodes = [
            TaskRunNode(name="fetch-source", duration_seconds=30.0),
            TaskRunNode(name="build-image", duration_seconds=130.0),
        ]
        dag = PipelineDAG(
            pipeline_run_name="pr-1",
            namespace="ci",
            pipeline_status="Succeeded",
            task_runs=nodes,
            critical_path=["fetch-source", "build-image"],
        )
        assert len(dag.task_runs) == 2
        assert dag.critical_path == ["fetch-source", "build-image"]

    def test_failed_and_skipped(self) -> None:
        dag = PipelineDAG(
            pipeline_run_name="pr-fail",
            namespace="ci",
            failed_tasks=["run-tests"],
            skipped_tasks=["deploy"],
        )
        assert dag.failed_tasks == ["run-tests"]
        assert dag.skipped_tasks == ["deploy"]


class TestDAGEdge:
    def test_creation(self) -> None:
        edge = DAGEdge(source="fetch-source", target="build-image")
        assert edge.source == "fetch-source"
        assert edge.target == "build-image"


# ── Tests: Domain Service — PipelineDAGTracerService ────────────────────────


class TestPipelineDAGTracerService:
    def test_tc1_four_taskruns_correct_dag(self) -> None:
        task_runs = [
            _tr("fetch-source", start_time=_BASE, completion_time=_BASE + timedelta(seconds=30)),
            _tr(
                "build-image",
                start_time=_BASE + timedelta(seconds=30),
                completion_time=_BASE + timedelta(seconds=160),
                run_after=["fetch-source"],
            ),
            _tr(
                "run-tests",
                start_time=_BASE + timedelta(seconds=30),
                completion_time=_BASE + timedelta(seconds=135),
                run_after=["fetch-source"],
            ),
            _tr(
                "deploy",
                start_time=_BASE + timedelta(seconds=160),
                completion_time=_BASE + timedelta(seconds=205),
                run_after=["build-image", "run-tests"],
            ),
        ]
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name="deploy-checkout-v5",
            namespace="ci",
            pipeline_status="Succeeded",
            task_runs=task_runs,
        )
        assert dag.pipeline_run_name == "deploy-checkout-v5"
        assert len(dag.task_runs) == 4

        fetch = next(n for n in dag.task_runs if n.name == "fetch-source")
        assert fetch.dependencies == []
        assert fetch.duration_seconds == 30.0

        build = next(n for n in dag.task_runs if n.name == "build-image")
        assert build.dependencies == ["fetch-source"]
        assert build.duration_seconds == 130.0

        deploy = next(n for n in dag.task_runs if n.name == "deploy")
        assert sorted(deploy.dependencies) == ["build-image", "run-tests"]
        assert deploy.duration_seconds == 45.0

    def test_critical_path_identifies_longest_chain(self) -> None:
        task_runs = [
            _tr("fetch-source", start_time=_BASE, completion_time=_BASE + timedelta(seconds=30)),
            _tr(
                "build-image",
                start_time=_BASE + timedelta(seconds=30),
                completion_time=_BASE + timedelta(seconds=160),
                run_after=["fetch-source"],
            ),
            _tr(
                "run-tests",
                start_time=_BASE + timedelta(seconds=30),
                completion_time=_BASE + timedelta(seconds=135),
                run_after=["fetch-source"],
            ),
            _tr(
                "deploy",
                start_time=_BASE + timedelta(seconds=160),
                completion_time=_BASE + timedelta(seconds=205),
                run_after=["build-image", "run-tests"],
            ),
        ]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Succeeded", task_runs)
        assert dag.critical_path == ["fetch-source", "build-image", "deploy"]

    def test_parallel_tasks_detected(self) -> None:
        task_runs = [
            _tr("fetch-source"),
            _tr("build-image", run_after=["fetch-source"]),
            _tr("run-tests", run_after=["fetch-source"]),
        ]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Succeeded", task_runs)
        # build-image and run-tests are parallel (both depend only on fetch-source)
        parallel_groups = PipelineDAGTracerService.compute_parallel_groups(dag)
        parallel_names = [{n for n in group} for group in parallel_groups]
        assert {"build-image", "run-tests"} in parallel_names

    def test_tc2_failed_task_downstream_skipped(self) -> None:
        task_runs = [
            _tr("fetch-source", status="Succeeded"),
            _tr(
                "run-tests",
                status="Failed",
                failure_reason="TestSuiteTimeout",
                run_after=["fetch-source"],
            ),
            _tr("deploy", status="Succeeded", run_after=["run-tests"]),
        ]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Failed", task_runs)
        assert "run-tests" in dag.failed_tasks
        assert "deploy" in dag.skipped_tasks

    def test_skip_duration_zero_marked(self) -> None:
        task_runs = [
            _tr("fetch-source"),
            _tr(
                "lint",
                start_time=_BASE + timedelta(seconds=30),
                completion_time=_BASE + timedelta(seconds=30),
                status="Succeeded",
                run_after=["fetch-source"],
            ),
        ]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Succeeded", task_runs)
        lint_node = next(n for n in dag.task_runs if n.name == "lint")
        assert lint_node.duration_seconds == 0.0
        assert lint_node.status == "Succeeded"

    def test_tc3_all_succeeded_critical_path_correct(self) -> None:
        task_runs = [
            _tr("fetch-source"),
            _tr("build-image", run_after=["fetch-source"]),
            _tr("run-tests", run_after=["fetch-source"]),
            _tr("deploy", run_after=["build-image", "run-tests"]),
        ]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Succeeded", task_runs)
        assert dag.critical_path == ["fetch-source", "build-image", "deploy"]
        assert dag.failed_tasks == []
        assert dag.skipped_tasks == []

    def test_tc4_in_progress_partial_dag(self) -> None:
        task_runs = [
            _tr("fetch-source", status="Succeeded"),
            _tr("build-image", status="Running", completion_time=None, run_after=["fetch-source"]),
            _tr("run-tests", status="Running", completion_time=None, run_after=["fetch-source"]),
            _tr(
                "deploy",
                status="NotStarted",
                start_time=None,
                completion_time=None,
                run_after=["build-image", "run-tests"],
            ),
        ]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Running", task_runs)
        deploy = next(n for n in dag.task_runs if n.name == "deploy")
        assert deploy.status == "NotStarted"
        build = next(n for n in dag.task_runs if n.name == "build-image")
        assert build.status == "Running"

    def test_fan_in_handled(self) -> None:
        task_runs = [
            _tr("task-a"),
            _tr("task-b", run_after=["task-a"]),
            _tr("task-c", run_after=["task-a"]),
            _tr("task-d", run_after=["task-b", "task-c"]),
        ]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Succeeded", task_runs)
        d_node = next(n for n in dag.task_runs if n.name == "task-d")
        assert sorted(d_node.dependencies) == ["task-b", "task-c"]

    def test_cancelled_pipeline_point_identified(self) -> None:
        task_runs = [
            _tr("fetch-source", status="Succeeded"),
            _tr(
                "build-image",
                status="Cancelled",
                completion_time=None,
                run_after=["fetch-source"],
            ),
            _tr(
                "deploy",
                status="NotStarted",
                start_time=None,
                completion_time=None,
                run_after=["build-image"],
            ),
        ]
        dag = PipelineDAGTracerService.build_dag(
            "pr",
            "ci",
            "Cancelled",
            task_runs,
            cancelled_by="build-image",
        )
        assert "build-image" in dag.cancelled_at_tasks

    def test_large_pipeline_over_50_taskruns(self) -> None:
        task_runs = [_tr(f"task-{i}") for i in range(55)]
        for i in range(1, 55):
            task_runs[i]["run_after"] = [f"task-{i - 1}"]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Succeeded", task_runs)
        assert len(dag.task_runs) == 55

    def test_empty_taskruns_returns_empty_dag(self) -> None:
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Succeeded", [])
        assert len(dag.task_runs) == 0
        assert dag.critical_path == []

    def test_dependency_not_in_node_list_handled(self) -> None:
        task_runs = [
            _tr("task-a"),
            _tr("task-b", run_after=["non-existent-task"]),
        ]
        dag = PipelineDAGTracerService.build_dag("pr", "ci", "Succeeded", task_runs)
        assert len(dag.task_runs) == 2
        task_b = next(n for n in dag.task_runs if n.name == "task-b")
        assert "non-existent-task" in task_b.dependencies


# ── Tests: Driving Ports ───────────────────────────────────────────────────


class TestTracePipelineRunDAGCommand:
    def test_creation_frozen(self) -> None:
        cmd = TracePipelineRunDAGCommand(pipeline_run_name="deploy-checkout-v5", namespace="ci")
        assert cmd.pipeline_run_name == "deploy-checkout-v5"
        assert cmd.namespace == "ci"

    def test_frozen_prevents_mutation(self) -> None:
        cmd = TracePipelineRunDAGCommand(pipeline_run_name="pr-1", namespace="ci")
        with pytest.raises(Exception):
            cmd.pipeline_run_name = "pr-2"  # type: ignore[misc]


class TestTracePipelineRunDAGResponse:
    def test_creation_with_dag(self) -> None:
        dag = PipelineDAG(pipeline_run_name="pr-1", namespace="ci")
        response = TracePipelineRunDAGResponse(dag=dag)
        assert response.dag.pipeline_run_name == "pr-1"


class TestTracePipelineRunDAGServicePort:
    def test_is_abstract(self) -> None:
        assert TracePipelineRunDAGServicePort.__abstractmethods__ == {"trace_pipeline_run_dag"}


# ── Tests: Application Service ─────────────────────────────────────────────


class _StubPipelineTracerPort(PipelineTracerPort):
    def __init__(
        self,
        pipeline: PipelineRunRecord | None = None,
        task_runs: list[TaskRunRecord] | None = None,
        raise_exc: Exception | None = None,
    ) -> None:
        self._pipeline = pipeline or _pr()
        self._task_runs = task_runs or []
        self._raise_exc = raise_exc

    def get_pipeline_run(self, namespace: str, name: str) -> PipelineRunRecord:
        if self._raise_exc is not None:
            raise self._raise_exc
        return self._pipeline

    def list_task_runs_for_pipeline(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        if self._raise_exc is not None:
            raise self._raise_exc
        return self._task_runs


class TestTracePipelineRunDAGService:
    def test_happy_path_returns_dag(self) -> None:
        task_runs = [
            _tr("fetch-source"),
            _tr("build-image", run_after=["fetch-source"]),
            _tr("deploy", run_after=["build-image"]),
        ]
        port = _StubPipelineTracerPort(pipeline=_pr(), task_runs=task_runs)
        service = TracePipelineRunDAGService(port=port)
        response = service.trace_pipeline_run_dag(
            TracePipelineRunDAGCommand(pipeline_run_name="deploy-checkout-v5", namespace="ci")
        )
        assert response.dag.pipeline_run_name == "deploy-checkout-v5"
        assert len(response.dag.task_runs) == 3

    def test_pipeline_not_found_propagates(self) -> None:
        port = _StubPipelineTracerPort(raise_exc=PipelineNotFoundError("unknown"))
        service = TracePipelineRunDAGService(port=port)
        with pytest.raises(PipelineNotFoundError):
            service.trace_pipeline_run_dag(
                TracePipelineRunDAGCommand(pipeline_run_name="unknown", namespace="ci")
            )

    def test_rbac_error_propagates(self) -> None:
        port = _StubPipelineTracerPort(raise_exc=InsufficientPermissionsError("RBAC denied"))
        service = TracePipelineRunDAGService(port=port)
        with pytest.raises(InsufficientPermissionsError):
            service.trace_pipeline_run_dag(
                TracePipelineRunDAGCommand(pipeline_run_name="pr-1", namespace="ci")
            )

    def test_tekton_not_installed_propagates(self) -> None:
        port = _StubPipelineTracerPort(raise_exc=TektonNotInstalledError())
        service = TracePipelineRunDAGService(port=port)
        with pytest.raises(TektonNotInstalledError):
            service.trace_pipeline_run_dag(
                TracePipelineRunDAGCommand(pipeline_run_name="pr-1", namespace="ci")
            )

    def test_cluster_unreachable_propagates(self) -> None:
        port = _StubPipelineTracerPort(raise_exc=ClusterUnreachableError("timeout"))
        service = TracePipelineRunDAGService(port=port)
        with pytest.raises(ClusterUnreachableError):
            service.trace_pipeline_run_dag(
                TracePipelineRunDAGCommand(pipeline_run_name="pr-1", namespace="ci")
            )


# ── Tests: Use Case ────────────────────────────────────────────────────────


class TestTracePipelineRunDAGUseCase:
    def test_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=TracePipelineRunDAGServicePort)
        mock_service.trace_pipeline_run_dag.return_value = TracePipelineRunDAGResponse(
            dag=PipelineDAG(pipeline_run_name="pr-1", namespace="ci")
        )
        use_case = TracePipelineRunDAGUseCase(service=mock_service)
        command = TracePipelineRunDAGCommand(pipeline_run_name="pr-1", namespace="ci")
        response = use_case.execute(command)
        mock_service.trace_pipeline_run_dag.assert_called_once_with(command)
        assert isinstance(response, TracePipelineRunDAGResponse)


# ── Tests: TektonPipelineTracerAdapter ─────────────────────────────────────


class TestTektonPipelineTracerAdapter:
    def test_get_pipeline_run_happy_path(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()
        mock_custom_api.get_namespaced_custom_object.return_value = {
            "metadata": {"name": "deploy-checkout-v5", "namespace": "ci"},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True"}],
                "startTime": "2026-06-15T10:00:00Z",
                "completionTime": "2026-06-15T10:04:00Z",
            },
            "spec": {"pipelineRef": {"name": "deploy-pipeline"}},
        }

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            record = adapter.get_pipeline_run("ci", "deploy-checkout-v5")

        assert record["name"] == "deploy-checkout-v5"
        assert record["status"] == "Succeeded"
        assert record["pipeline_ref"] == "deploy-pipeline"

    def test_get_pipeline_run_404_raises_pipeline_not_found(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()

        class _NotFoundError(Exception):
            status = 404

        mock_custom_api.get_namespaced_custom_object.side_effect = _NotFoundError()

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            with pytest.raises(PipelineNotFoundError):
                adapter.get_pipeline_run("ci", "unknown-pr")

    def test_get_pipeline_run_403_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()

        class _ForbiddenError(Exception):
            status = 403

        mock_custom_api.get_namespaced_custom_object.side_effect = _ForbiddenError()

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.get_pipeline_run("ci", "pr-1")

    def test_list_task_runs_happy_path(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()
        mock_custom_api.list_namespaced_custom_object.return_value = {
            "items": [
                {
                    "metadata": {
                        "name": "fetch-source",
                        "namespace": "ci",
                        "labels": {"tekton.dev/pipelineRun": "deploy-checkout-v5"},
                    },
                    "status": {
                        "conditions": [{"type": "Succeeded", "status": "True"}],
                        "startTime": "2026-06-15T10:00:00Z",
                        "completionTime": "2026-06-15T10:00:30Z",
                    },
                    "spec": {"taskRef": {"name": "fetch-source"}},
                },
                {
                    "metadata": {
                        "name": "build-image",
                        "namespace": "ci",
                        "labels": {"tekton.dev/pipelineRun": "deploy-checkout-v5"},
                    },
                    "status": {
                        "conditions": [{"type": "Succeeded", "status": "True"}],
                        "startTime": "2026-06-15T10:00:30Z",
                        "completionTime": "2026-06-15T10:02:40Z",
                    },
                    "spec": {
                        "taskRef": {"name": "build-image"},
                        "runAfter": ["fetch-source"],
                    },
                },
            ]
        }

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            records = adapter.list_task_runs_for_pipeline("ci", "deploy-checkout-v5")

        assert len(records) == 2
        assert records[0]["name"] == "fetch-source"
        assert records[0]["run_after"] == []
        assert records[1]["name"] == "build-image"
        assert records[1]["run_after"] == ["fetch-source"]

    def test_list_task_runs_404_raises_tekton_not_installed(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()

        class _NotFoundError(Exception):
            status = 404

        mock_custom_api.list_namespaced_custom_object.side_effect = _NotFoundError()

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            with pytest.raises(TektonNotInstalledError):
                adapter.list_task_runs_for_pipeline("ci", "pr-1")

    def test_unknown_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()
        mock_custom_api.get_namespaced_custom_object.side_effect = RuntimeError(
            "connection refused"
        )

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.get_pipeline_run("ci", "pr-1")

    def test_pipeline_with_inline_spec(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()
        mock_custom_api.get_namespaced_custom_object.return_value = {
            "metadata": {"name": "inline-pr", "namespace": "ci"},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True"}],
                "startTime": "2026-06-15T10:00:00Z",
                "completionTime": "2026-06-15T10:01:00Z",
            },
            "spec": {"pipelineSpec": {"tasks": [{"name": "inline-task"}]}},
        }

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            record = adapter.get_pipeline_run("ci", "inline-pr")

        assert record["pipeline_ref"] == "inline"

    def test_pipeline_ref_missing_returns_unknown(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()
        mock_custom_api.get_namespaced_custom_object.return_value = {
            "metadata": {"name": "no-ref-pr", "namespace": "ci"},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True"}],
                "startTime": "2026-06-15T10:00:00Z",
                "completionTime": "2026-06-15T10:01:00Z",
            },
            "spec": {},
        }

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            record = adapter.get_pipeline_run("ci", "no-ref-pr")

        assert record["pipeline_ref"] == "unknown"

    def test_taskrun_with_finally_flag(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_custom_api = MagicMock()
        mock_custom_api.list_namespaced_custom_object.return_value = {
            "items": [
                {
                    "metadata": {
                        "name": "cleanup",
                        "namespace": "ci",
                        "labels": {
                            "tekton.dev/pipelineRun": "deploy-checkout-v5",
                            "tekton.dev/pipelineTask": "cleanup",
                        },
                    },
                    "status": {
                        "conditions": [{"type": "Succeeded", "status": "True"}],
                        "startTime": "2026-06-15T10:04:00Z",
                        "completionTime": "2026-06-15T10:04:15Z",
                    },
                    "spec": {},
                }
            ]
        }

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            adapter = TektonPipelineTracerAdapter()
            records = adapter.list_task_runs_for_pipeline("ci", "deploy-checkout-v5")

        assert len(records) == 1


# ── Tests: MCP Tool ────────────────────────────────────────────────────────


class TestTracePipelineRunDAGMCPTool:
    def test_happy_path_returns_expected_keys(self) -> None:
        from hexawyn.mcp.tools.trace_pipeline_run_dag import (
            trace_pipeline_run_dag,
        )

        task_runs = [
            _tr("fetch-source"),
            _tr("build-image", run_after=["fetch-source"]),
            _tr("deploy", run_after=["build-image"]),
        ]

        def _fake_build_adapter() -> PipelineTracerPort:
            return _StubPipelineTracerPort(pipeline=_pr(), task_runs=task_runs)

        with patch(
            "hexawyn.mcp.tools.trace_pipeline_run_dag._build_adapter",
            side_effect=_fake_build_adapter,
        ):
            result = trace_pipeline_run_dag(pipeline_run_name="deploy-checkout-v5", namespace="ci")

        assert result["pipeline_run_name"] == "deploy-checkout-v5"
        assert result["namespace"] == "ci"
        assert result["pipeline_status"] == "Succeeded"
        assert len(result["task_runs"]) == 3
        assert isinstance(result["critical_path"], list)
        assert result["error"] is None

    def test_error_returns_error_key(self) -> None:
        from hexawyn.mcp.tools.trace_pipeline_run_dag import (
            trace_pipeline_run_dag,
        )

        def _fail() -> PipelineTracerPort:
            raise PipelineNotFoundError("missing")

        with patch(
            "hexawyn.mcp.tools.trace_pipeline_run_dag._build_adapter",
            side_effect=_fail,
        ):
            result = trace_pipeline_run_dag(pipeline_run_name="missing", namespace="ci")

        assert result["error"] is not None
        assert "missing" in result["error"]
        assert result["task_runs"] == []

    def test_register_adds_tool_to_mcp(self) -> None:
        from hexawyn.mcp.tools.trace_pipeline_run_dag import register

        mock_mcp = MagicMock()
        register(mock_mcp)
        mock_mcp.tool.assert_called_once()


# ── Tests: Coverage gap fillers ─────────────────────────────────────────────


class TestComputeDuration:
    def test_invalid_date_returns_zero(self) -> None:
        from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
            _compute_duration,
        )

        assert _compute_duration("invalid", "also-invalid") == 0.0

    def test_partial_date_returns_zero(self) -> None:
        from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
            _compute_duration,
        )

        assert _compute_duration("2026-01-01T00:00:00Z", "") == 0.0
        assert _compute_duration("", "2026-01-01T00:00:00Z") == 0.0
        assert _compute_duration(None, None) == 0.0


class TestComputeDepth:
    def test_missing_node_returns_zero(self) -> None:
        from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
            _compute_depth,
        )

        result = _compute_depth("non-existent", [])
        assert result == 0

    def test_no_dependencies_returns_zero(self) -> None:
        from hexawyn.domain.models.pipeline_dag import TaskRunNode
        from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
            _compute_depth,
        )

        node = TaskRunNode(name="standalone")
        result = _compute_depth("standalone", [node])
        assert result == 0


class TestCollectDownstream:
    def test_collects_transitive_dependencies(self) -> None:
        from hexawyn.domain.models.pipeline_dag import TaskRunNode
        from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
            _collect_downstream,
        )

        nodes = [
            TaskRunNode(name="a"),
            TaskRunNode(name="b", dependencies=["a"]),
            TaskRunNode(name="c", dependencies=["b"]),
        ]
        result: set[str] = set()
        _collect_downstream("a", nodes, result)
        assert "b" in result
        assert "c" in result


class TestBuildAdapterTool:
    def test_returns_tracer_port(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )
        from hexawyn.mcp.tools.trace_pipeline_run_dag import _build_adapter

        with patch("kubernetes.client.CustomObjectsApi"):
            adapter = _build_adapter()
            assert isinstance(adapter, TektonPipelineTracerAdapter)


class TestAdapterEdgeCases:
    def test_list_task_runs_403_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_api = MagicMock()

        class _ForbiddenError(Exception):
            status = 403

        mock_api.list_namespaced_custom_object.side_effect = _ForbiddenError()

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = TektonPipelineTracerAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_task_runs_for_pipeline("ci", "pr-1")

    def test_list_task_runs_unknown_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            TektonPipelineTracerAdapter,
        )

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.side_effect = RuntimeError("boom")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            adapter = TektonPipelineTracerAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_task_runs_for_pipeline("ci", "pr-1")

    def test_extract_status_edge_cases(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            _extract_status,
        )

        assert _extract_status(None) == "Unknown"
        assert _extract_status([]) == "NotStarted"
        assert _extract_status([{"notSucceeded": True}]) == "NotStarted"
        assert _extract_status([{"type": "Succeeded", "status": "Unknown"}]) == "Running"

    def test_extract_failure_reason_with_no_conditions(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            _extract_failure_reason,
        )

        assert _extract_failure_reason({}) == ""
        assert _extract_failure_reason({"conditions": None}) == ""

    def test_to_iso_non_string_returns_none(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            _to_iso,
        )

        assert _to_iso(None) is None
        assert _to_iso(42) is None
        assert _to_iso({"key": "val"}) is None

    def test_extract_status_cancelled(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            _extract_status,
        )

        assert (
            _extract_status(
                [{"type": "Succeeded", "status": "False", "reason": "PipelineRunCancelled"}]
            )
            == "Cancelled"
        )

    def test_extract_status_failed(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            _extract_status,
        )

        assert (
            _extract_status([{"type": "Succeeded", "status": "False", "reason": "TaskRunTimeout"}])
            == "Failed"
        )

    def test_extract_status_non_dict_item_skipped(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            _extract_status,
        )

        assert (
            _extract_status(["not-a-dict", {"type": "Succeeded", "status": "True"}]) == "Succeeded"
        )

    def test_extract_failure_reason_non_dict_item(self) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
            _extract_failure_reason,
        )

        assert (
            _extract_failure_reason(
                {
                    "conditions": [
                        "not-a-dict",
                        {"type": "Succeeded", "status": "False", "message": "boo"},
                    ]
                }
            )
            == "boo"
        )

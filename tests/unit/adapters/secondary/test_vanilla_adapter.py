from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.domain.errors import ClusterUnreachableError, PipelineNotFoundError


class _ContainerStateWaiting:
    def __init__(self, reason: str) -> None:
        self.reason = reason


class _ContainerState:
    def __init__(self, waiting_reason: str | None = None) -> None:
        self.waiting = _ContainerStateWaiting(waiting_reason) if waiting_reason else None


class _ContainerStatus:
    def __init__(self, restart_count: int, waiting_reason: str | None = None) -> None:
        self.restart_count = restart_count
        self.state = _ContainerState(waiting_reason)


class _PodMetadata:
    def __init__(self, name: str, namespace: str) -> None:
        self.name = name
        self.namespace = namespace
        from datetime import UTC, datetime, timedelta

        self.creation_timestamp = datetime.now(UTC) - timedelta(days=3)


class _PodSpec:
    def __init__(self, node_name: str = "node-1") -> None:
        self.node_name = node_name


class _PodStatus:
    def __init__(
        self,
        phase: str,
        container_statuses: list[_ContainerStatus],
    ) -> None:
        self.phase = phase
        self.container_statuses = container_statuses


class _Pod:
    def __init__(  # noqa: PLR0913
        self,
        name: str,
        namespace: str,
        phase: str,
        restarts: int,
        waiting_reason: str | None = None,
        node_name: str = "node-1",
    ) -> None:
        self.metadata = _PodMetadata(name, namespace)
        self.spec = _PodSpec(node_name)
        self.status = _PodStatus(phase, [_ContainerStatus(restarts, waiting_reason)])


class _PodList:
    def __init__(self, items: list[_Pod]) -> None:
        self.items = items


class _NodeCondition:
    def __init__(self, condition_type: str, status: str) -> None:
        self.type = condition_type
        self.status = status


class _NodeMetadata:
    def __init__(self, name: str) -> None:
        self.name = name


class _NodeStatus:
    def __init__(self, allocatable: dict[str, str], conditions: list[_NodeCondition]) -> None:
        self.allocatable = allocatable
        self.conditions = conditions


class _Node:
    def __init__(self, name: str, allocatable: dict[str, str], ready: bool = True) -> None:
        self.metadata = _NodeMetadata(name)
        ready_status = "True" if ready else "False"
        self.status = _NodeStatus(allocatable, [_NodeCondition("Ready", ready_status)])


class _NodeList:
    def __init__(self, items: list[_Node]) -> None:
        self.items = items


class _NamespaceMetadata:
    def __init__(self, name: str) -> None:
        self.name = name
        from datetime import UTC, datetime, timedelta

        self.creation_timestamp = datetime.now(UTC) - timedelta(days=30)


class _NamespaceStatus:
    def __init__(self, phase: str) -> None:
        self.phase = phase


class _Namespace:
    def __init__(self, name: str, phase: str = "Active") -> None:
        self.metadata = _NamespaceMetadata(name)
        self.status = _NamespaceStatus(phase)


class _NamespaceList:
    def __init__(self, items: list[_Namespace]) -> None:
        self.items = items


class _CoreApi:
    def __init__(
        self,
        pods: list[_Pod],
        nodes: list[_Node] | None = None,
        namespaces: list[_Namespace] | None = None,
    ) -> None:
        self.pods = pods
        self.nodes = nodes or []
        self.namespaces = namespaces or []
        self.requested_namespace: str | None = None
        self.all_namespace_pod_calls = 0
        self.list_namespace_calls = 0

    def list_pod_for_all_namespaces(self, timeout_seconds: int) -> _PodList:
        self.all_namespace_pod_calls += 1
        return _PodList(self.pods)

    def list_namespaced_pod(self, namespace: str, timeout_seconds: int) -> _PodList:
        self.requested_namespace = namespace
        return _PodList(self.pods)

    def list_node(self, timeout_seconds: int) -> _NodeList:
        return _NodeList(self.nodes)

    def list_namespace(self, timeout_seconds: int) -> _NamespaceList:
        self.list_namespace_calls += 1
        return _NamespaceList(self.namespaces)


class _MetricsApi:
    def __init__(self, node_metrics: dict[str, object]) -> None:
        self.node_metrics = node_metrics

    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        return self.node_metrics


class TestVanillaAdapter:
    def test_is_k8s_port(self) -> None:
        adapter = VanillaAdapter("test-cluster")
        assert isinstance(adapter, K8sPort)

    def test_list_pods_returns_real_kubernetes_pods(self) -> None:
        api = _CoreApi(
            [
                _Pod("api-7f8d9c", "default", "Running", 1, node_name="node-a"),
                _Pod("worker-64d8b", "jobs", "Pending", 0, node_name="node-b"),
            ]
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        pods = adapter.list_pods(namespace="default")

        assert api.requested_namespace == "default"
        assert pods == [
            {
                "name": "api-7f8d9c",
                "namespace": "default",
                "status": "Running",
                "restarts": 1,
                "age": "3d",
                "node": "node-a",
                "cpu_request_millicores": 0,
                "memory_request_mib": 0,
            },
            {
                "name": "worker-64d8b",
                "namespace": "jobs",
                "status": "Pending",
                "restarts": 0,
                "age": "3d",
                "node": "node-b",
                "cpu_request_millicores": 0,
                "memory_request_mib": 0,
            },
        ]

    def test_list_pods_reuses_recent_all_namespace_result(self) -> None:
        api = _CoreApi([_Pod("api-7f8d9c", "default", "Running", 0)])
        adapter = VanillaAdapter("test-cluster", api=api)

        first_result = adapter.list_pods()
        second_result = adapter.list_pods()

        assert first_result == second_result
        assert api.all_namespace_pod_calls == 1

    def test_kind_context_reports_kind_provider(self) -> None:
        adapter = VanillaAdapter("kind-ecom-local", api=_CoreApi([]))

        context = adapter.get_cluster_context()

        assert context["provider"] == "kind"

    def test_cluster_metrics_returns_real_counts_and_usage(self) -> None:
        api = _CoreApi(
            pods=[
                _Pod("api-7f8d9c", "default", "Running", 0),
                _Pod("worker-64d8b", "jobs", "Running", 0),
            ],
            nodes=[_Node("node-a", {"cpu": "2", "memory": "4Gi"})],
        )
        metrics_api = _MetricsApi(
            {
                "items": [
                    {
                        "metadata": {"name": "node-a"},
                        "usage": {"cpu": "500m", "memory": "1Gi"},
                    }
                ]
            }
        )
        adapter = VanillaAdapter("test-cluster", api=api, metrics_api=metrics_api)

        metrics = adapter.get_cluster_metrics()

        assert metrics == {
            "cpu_usage_pct": 25.0,
            "memory_usage_pct": 25.0,
            "node_count": 1,
            "pod_count": 2,
        }

    def test_findings_are_derived_from_real_pods_and_nodes(self) -> None:
        api = _CoreApi(
            pods=[
                _Pod("api-7f8d9c", "default", "Running", 12),
                _Pod("worker-64d8b", "jobs", "Pending", 0),
                _Pod("payments-555", "default", "Running", 7, "CrashLoopBackOff"),
            ],
            nodes=[_Node("node-a", {"cpu": "2", "memory": "4Gi"}, ready=False)],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        findings = adapter.get_findings()

        assert findings == [
            {
                "severity": "warning",
                "message": "Pod default/api-7f8d9c restarted 12 times",
                "remediation": "Inspect recent logs and events for this pod.",
            },
            {
                "severity": "warning",
                "message": "Pod jobs/worker-64d8b is Pending",
                "remediation": "Check scheduling events, resource requests, and node capacity.",
            },
            {
                "severity": "critical",
                "message": "Pod default/payments-555 is CrashLoop",
                "remediation": "Inspect container logs, probes, image pull errors, and recent rollout changes.",  # noqa: E501
            },
            {
                "severity": "critical",
                "message": "Node node-a is NotReady",
                "remediation": "Inspect node conditions, kubelet status, and recent node events.",
            },
        ]

    def test_health_status_and_score_follow_real_findings(self) -> None:
        api = _CoreApi(
            pods=[_Pod("payments-555", "default", "Running", 7, "CrashLoopBackOff")],
            nodes=[],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        assert adapter.get_health_score() == 70  # noqa: PLR2004
        assert adapter.get_health_status() == "critical"

    def test_no_findings_when_cluster_objects_are_healthy(self) -> None:
        api = _CoreApi(
            pods=[_Pod("api-7f8d9c", "default", "Running", 0)],
            nodes=[_Node("node-a", {"cpu": "2", "memory": "4Gi"})],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        assert adapter.get_findings() == []
        assert adapter.get_health_score() == 100  # noqa: PLR2004
        assert adapter.get_health_status() == "healthy"


class TestVanillaAdapterListNamespaces:
    def test_list_namespaces_returns_namespace_info_list(self) -> None:
        api = _CoreApi(
            pods=[],
            namespaces=[
                _Namespace("default", "Active"),
                _Namespace("kube-system", "Active"),
                _Namespace("production", "Active"),
            ],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        namespaces = adapter.list_namespaces()

        assert len(namespaces) == 3  # noqa: PLR2004
        for ns in namespaces:
            assert ns["name"] in ("default", "kube-system", "production")
            assert ns["status"] == "Active"
            assert "d" in ns["age"]

    def test_list_namespaces_uses_k8s_api(self) -> None:
        api = _CoreApi(pods=[], namespaces=[])
        adapter = VanillaAdapter("test-cluster", api=api)

        adapter.list_namespaces()

        assert api.list_namespace_calls == 1

    def test_list_namespaces_terminating_status(self) -> None:
        api = _CoreApi(
            pods=[],
            namespaces=[_Namespace("old-ns", "Terminating")],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        namespaces = adapter.list_namespaces()

        assert namespaces[0]["status"] == "Terminating"

    def test_list_namespaces_empty_cluster(self) -> None:
        api = _CoreApi(pods=[], namespaces=[])
        adapter = VanillaAdapter("test-cluster", api=api)

        namespaces = adapter.list_namespaces()

        assert namespaces == []


class _CRDApi:
    """Fake KubernetesCRDApi that returns pre-built TaskRun dicts."""

    def __init__(self, items: list[dict[str, object]]) -> None:
        self._items = items
        self.last_label_selector: str = ""

    def list_namespaced_custom_object(  # noqa: PLR0913
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        label_selector: str = "",
    ) -> dict[str, object]:
        self.last_label_selector = label_selector
        return {"items": self._items}


def _make_task_run(  # noqa: PLR0913
    name: str,
    task_ref: str,
    succeeded: str,
    reason: str,
    start_time: str | None = None,
    completion_time: str | None = None,
    steps: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    conditions: list[dict[str, object]] = [
        {"type": "Succeeded", "status": succeeded, "reason": reason, "message": ""}
    ]
    status: dict[str, object] = {"conditions": conditions}
    if start_time:
        status["startTime"] = start_time
    if completion_time:
        status["completionTime"] = completion_time
    if steps:
        status["steps"] = steps
    return {
        "metadata": {"name": name, "labels": {"tekton.dev/pipeline": "build-deploy"}},
        "spec": {"taskRef": {"name": task_ref}},
        "status": status,
    }


class TestVanillaAdapterTektonPort:
    def test_implements_tekton_port(self) -> None:
        adapter = VanillaAdapter("test-cluster")
        assert isinstance(adapter, TektonPort)

    def test_list_task_runs_returns_succeeded_run(self) -> None:
        item = _make_task_run(
            name="build-deploy-clone-repo-abc",
            task_ref="clone-repo",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-01T10:00:00Z",
            completion_time="2024-01-01T10:00:12Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert len(result) == 1
        assert result[0]["name"] == "build-deploy-clone-repo-abc"
        assert result[0]["task_ref"] == "clone-repo"
        assert result[0]["status"] == "Succeeded"
        assert result[0]["start_time"] == "2024-01-01T10:00:00Z"
        assert result[0]["duration"] == "12s"
        assert result[0]["failing_step"] is None

    def test_list_task_runs_failed_exposes_step_and_error(self) -> None:
        steps: list[dict[str, object]] = [
            {
                "name": "run-tests",
                "terminated": {"exitCode": 1, "reason": "Error", "message": "exit code 1"},
            }
        ]
        item = _make_task_run(
            name="build-deploy-unit-tests-xyz",
            task_ref="unit-tests",
            succeeded="False",
            reason="Failed",
            start_time="2024-01-01T10:00:15Z",
            completion_time="2024-01-01T10:00:45Z",
            steps=steps,
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["status"] == "Failed"
        assert result[0]["failing_step"] == "run-tests"
        assert result[0]["failing_step_error"] == "exit code 1"

    def test_list_task_runs_timeout_step_shown_as_timeout(self) -> None:
        steps: list[dict[str, object]] = [
            {
                "name": "run-tests",
                "terminated": {"exitCode": 1, "reason": "DeadlineExceeded", "message": ""},
            }
        ]
        item = _make_task_run(
            name="build-deploy-unit-tests-timeout",
            task_ref="unit-tests",
            succeeded="False",
            reason="Failed",
            start_time="2024-01-01T10:00:00Z",
            steps=steps,
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["failing_step_error"] == "Timeout"

    def test_list_task_runs_running_has_no_duration(self) -> None:
        item = _make_task_run(
            name="build-deploy-lint-running",
            task_ref="lint",
            succeeded="Unknown",
            reason="Running",
            start_time="2024-01-01T10:01:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["status"] == "Running"
        assert result[0]["duration"] is None

    def test_list_task_runs_raises_pipeline_not_found_when_empty(self) -> None:
        crd_api = _CRDApi([])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(PipelineNotFoundError) as exc_info:
            adapter.list_task_runs("ghost-pipeline", "ci")

        assert exc_info.value.pipeline_name == "ghost-pipeline"

    def test_list_task_runs_raises_cluster_unreachable_on_api_error(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.side_effect = Exception("connection refused")
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_task_runs("build-deploy", "ci")

    def test_list_task_runs_filters_by_pipeline_label(self) -> None:
        item = _make_task_run(
            name="build-deploy-clone-repo",
            task_ref="clone-repo",
            succeeded="True",
            reason="Succeeded",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        adapter.list_task_runs("build-deploy", "ci")

        assert "tekton.dev/pipeline=build-deploy" in crd_api.last_label_selector

    def test_list_task_runs_duration_minutes(self) -> None:
        item = _make_task_run(
            name="build-deploy-build-image",
            task_ref="build-image",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-01T10:00:00Z",
            completion_time="2024-01-01T10:02:30Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["duration"] == "2m30s"

    def test_list_task_runs_duration_exact_minutes(self) -> None:
        item = _make_task_run(
            name="build-deploy-build-image",
            task_ref="build-image",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-01T10:00:00Z",
            completion_time="2024-01-01T10:02:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["duration"] == "2m"

    def test_list_task_runs_duration_invalid_timestamps_returns_unknown(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "run-abc", "labels": {}},
            "spec": {"taskRef": {"name": "build"}},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ],
                "startTime": "not-a-date",
                "completionTime": "also-not-a-date",
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["duration"] == "unknown"

    def test_list_task_runs_status_level_timeout_returns_timeout(self) -> None:
        item = _make_task_run(
            name="build-deploy-run-tests-timeout",
            task_ref="run-tests",
            succeeded="False",
            reason="DeadlineExceeded",
            start_time="2024-01-01T10:00:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["status"] == "Timeout"

    def test_list_task_runs_missing_spec_yields_unknown_task_ref(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "run-abc", "labels": {}},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ],
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["task_ref"] == "unknown"

    def test_list_task_runs_spec_without_task_ref_yields_unknown(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "run-abc", "labels": {}},
            "spec": {},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ],
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["task_ref"] == "unknown"

    def test_list_task_runs_failed_steps_not_list_returns_no_failing_step(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "run-abc", "labels": {}},
            "spec": {"taskRef": {"name": "build"}},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "False", "reason": "Failed", "message": ""}
                ],
                "steps": "not-a-list",
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["failing_step"] is None

    def test_list_task_runs_step_without_terminated_is_skipped(self) -> None:
        steps: list[dict[str, object]] = [
            {"name": "setup", "running": {}},
            {
                "name": "run-tests",
                "terminated": {"exitCode": 1, "reason": "Error", "message": "fail"},
            },
        ]
        item = _make_task_run(
            name="run-abc",
            task_ref="run-tests",
            succeeded="False",
            reason="Failed",
            steps=steps,
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["failing_step"] == "run-tests"

    def test_list_task_runs_step_error_without_message_uses_exit_code(self) -> None:
        steps: list[dict[str, object]] = [
            {"name": "run-tests", "terminated": {"exitCode": 2, "reason": "Error", "message": ""}},
        ]
        item = _make_task_run(
            name="run-abc",
            task_ref="run-tests",
            succeeded="False",
            reason="Failed",
            steps=steps,
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["failing_step_error"] == "exit code 2"

    def test_list_task_runs_invalid_crd_response_raises_pipeline_not_found(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.return_value = "not-a-dict"
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(PipelineNotFoundError):
            adapter.list_task_runs("build-deploy", "ci")


def _make_pipeline_run(  # noqa: PLR0913
    name: str,
    succeeded: str,
    reason: str,
    start_time: str | None = None,
    completion_time: str | None = None,
    annotations: dict[str, str] | None = None,
    labels: dict[str, str] | None = None,
) -> dict[str, object]:
    conditions: list[dict[str, object]] = [
        {"type": "Succeeded", "status": succeeded, "reason": reason, "message": ""}
    ]
    status: dict[str, object] = {"conditions": conditions}
    if start_time:
        status["startTime"] = start_time
    if completion_time:
        status["completionTime"] = completion_time
    metadata: dict[str, object] = {"name": name}
    if annotations:
        metadata["annotations"] = annotations
    if labels:
        metadata["labels"] = labels
    return {"metadata": metadata, "status": status}


class TestVanillaAdapterListPipelineRuns:
    def test_returns_succeeded_run(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-15T10:00:00Z",
            completion_time="2024-01-15T10:04:30Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert len(result) == 1
        assert result[0]["name"] == "payment-service-run-abc"
        assert result[0]["status"] == "Succeeded"
        assert result[0]["start_time"] == "2024-01-15T10:00:00Z"
        assert result[0]["duration"] == "4m30s"
        assert result[0]["duration_seconds"] == 270  # noqa: PLR2004

    def test_returns_failed_run(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-xyz",
            succeeded="False",
            reason="Failed",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "Failed"

    def test_returns_cancelled_run(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-cancel",
            succeeded="False",
            reason="PipelineRunCancelled",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "Cancelled"

    def test_returns_running_run(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-running",
            succeeded="Unknown",
            reason="Running",
            start_time="2024-01-15T10:00:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "Running"
        assert result[0]["duration"] is None
        assert result[0]["duration_seconds"] is None

    def test_triggered_by_from_pac_annotation(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
            annotations={"pipelinesascode.tekton.dev/sender": "john.doe"},
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["triggered_by"] == "john.doe"

    def test_triggered_by_falls_back_to_event_listener_label(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
            labels={"triggers.tekton.dev/eventlistener": "github-push"},
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["triggered_by"] == "github-push"

    def test_triggered_by_is_none_when_no_metadata(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["triggered_by"] is None

    def test_raises_service_not_found_when_empty(self) -> None:
        from hexawyn.domain.errors import ServiceNotFoundError

        crd_api = _CRDApi([])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(ServiceNotFoundError) as exc_info:
            adapter.list_pipeline_runs("ghost-service", "ci")

        assert exc_info.value.service_name == "ghost-service"

    def test_raises_cluster_unreachable_on_api_error(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.side_effect = Exception("connection refused")
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_pipeline_runs("payment-service", "ci")

    def test_filters_by_pipeline_label(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        adapter.list_pipeline_runs("payment-service", "ci")

        assert "tekton.dev/pipeline=payment-service" in crd_api.last_label_selector

    def test_duration_exact_minutes(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-15T10:00:00Z",
            completion_time="2024-01-15T10:03:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["duration"] == "3m"
        assert result[0]["duration_seconds"] == 180  # noqa: PLR2004

    def test_duration_under_sixty_seconds(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-fast",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-15T10:00:00Z",
            completion_time="2024-01-15T10:00:45Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["duration"] == "45s"
        assert result[0]["duration_seconds"] == 45  # noqa: PLR2004

    def test_invalid_timestamps_yield_none_duration(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "payment-run-bad"},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ],
                "startTime": "not-a-date",
                "completionTime": "also-invalid",
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["duration"] is None
        assert result[0]["duration_seconds"] is None

    def test_status_none_returns_not_started(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "payment-run-no-status"},
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "NotStarted"

    def test_empty_conditions_returns_not_started(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "payment-run-pending"},
            "status": {"conditions": []},
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "NotStarted"

    def test_non_mapping_condition_returns_not_started(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "payment-run-bad-cond"},
            "status": {"conditions": ["not-a-dict"]},
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "NotStarted"

    def test_unknown_status_non_running_reason_returns_not_started(self) -> None:
        item = _make_pipeline_run(
            name="payment-run-pending",
            succeeded="Unknown",
            reason="PipelineRunPending",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "NotStarted"

    def test_triggered_by_falls_back_to_label_when_annotation_empty(self) -> None:
        item = _make_pipeline_run(
            name="payment-run-abc",
            succeeded="True",
            reason="Succeeded",
            annotations={"pipelinesascode.tekton.dev/sender": ""},
            labels={"triggers.tekton.dev/eventlistener": "github-push"},
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["triggered_by"] == "github-push"


def _make_namespaced_pipeline_run(  # noqa: PLR0913
    name: str,
    succeeded: str,
    reason: str,
    start_time: str | None = None,
    completion_time: str | None = None,
    pipeline_ref_name: str | None = "deploy-payment",
) -> dict[str, object]:
    conditions: list[dict[str, object]] = [
        {"type": "Succeeded", "status": succeeded, "reason": reason, "message": ""}
    ]
    status: dict[str, object] = {"conditions": conditions}
    if start_time:
        status["startTime"] = start_time
    if completion_time:
        status["completionTime"] = completion_time
    spec: dict[str, object] = {}
    if pipeline_ref_name:
        spec["pipelineRef"] = {"name": pipeline_ref_name}
    return {"metadata": {"name": name}, "spec": spec, "status": status}


class TestVanillaAdapterListPipelineRunsInNamespace:
    def test_returns_empty_list_when_no_runs(self) -> None:
        crd_api = _CRDApi([])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

        assert result == []

    def test_returns_all_runs_with_fields(self) -> None:
        item = _make_namespaced_pipeline_run(
            name="deploy-payment-v3",
            succeeded="False",
            reason="Failed",
            start_time="2024-01-15T10:00:00Z",
            completion_time="2024-01-15T10:05:00Z",
            pipeline_ref_name="deploy-payment",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

        assert len(result) == 1
        assert result[0]["name"] == "deploy-payment-v3"
        assert result[0]["status"] == "Failed"
        assert result[0]["start_time"] == "2024-01-15T10:00:00Z"
        assert result[0]["duration"] == "5m"
        assert result[0]["pipeline_ref"] == "deploy-payment"

    def test_returns_running_and_succeeded_runs(self) -> None:
        items = [
            _make_namespaced_pipeline_run("run-running", "Unknown", "Running"),
            _make_namespaced_pipeline_run("run-ok", "True", "Succeeded"),
        ]
        crd_api = _CRDApi(items)
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

        statuses = {r["name"]: r["status"] for r in result}
        assert statuses["run-running"] == "Running"
        assert statuses["run-ok"] == "Succeeded"

    def test_pipeline_ref_inline_when_no_pipeline_ref(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "inline-run"},
            "spec": {"pipelineSpec": {}},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ]
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

        assert result[0]["pipeline_ref"] == "inline"

    def test_raises_insufficient_permissions_on_403(self) -> None:
        from hexawyn.domain.errors import InsufficientPermissionsError
        from kubernetes.client.exceptions import ApiException

        crd_api = MagicMock()
        exc = ApiException(status=403, reason="Forbidden")
        crd_api.list_namespaced_custom_object.side_effect = exc
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

    def test_raises_tekton_not_installed_on_404(self) -> None:
        from hexawyn.domain.errors import TektonNotInstalledError
        from kubernetes.client.exceptions import ApiException

        crd_api = MagicMock()
        exc = ApiException(status=404, reason="Not Found")
        crd_api.list_namespaced_custom_object.side_effect = exc
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(TektonNotInstalledError):
            adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

    def test_raises_cluster_unreachable_on_other_api_exception(self) -> None:
        from kubernetes.client.exceptions import ApiException

        crd_api = MagicMock()
        exc = ApiException(status=500, reason="Internal Server Error")
        crd_api.list_namespaced_custom_object.side_effect = exc
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

    def test_raises_cluster_unreachable_on_generic_exception(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.side_effect = Exception("connection refused")
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

    def test_queries_namespace_without_label_filter(self) -> None:
        crd_api = _CRDApi([])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        adapter.list_pipeline_runs_in_namespace("tekton", limit=100)

        assert crd_api.last_label_selector == ""


# ── Helpers for NamespaceWasteAnalysisPort tests ─────────────────


def _fake_pod(
    namespace: str,
    cpu_request: str | None = "500m",
    mem_request: str | None = "1Gi",
) -> MagicMock:
    pod = MagicMock()
    pod.metadata.namespace = namespace
    requests: dict[str, str] = {}
    if cpu_request:
        requests["cpu"] = cpu_request
    if mem_request:
        requests["memory"] = mem_request
    container = MagicMock()
    container.resources.requests = requests if requests else None
    pod.spec.containers = [container]
    return pod


def _fake_namespace_obj(name: str, age_hours: float = 48.0) -> MagicMock:
    from datetime import UTC, datetime, timedelta

    ns = MagicMock()
    ns.metadata.name = name
    ns.metadata.creation_timestamp = datetime.now(UTC) - timedelta(hours=age_hours)
    return ns


def _fake_core_api(
    pods: list[MagicMock] | None = None,
    namespaces: list[MagicMock] | None = None,
) -> MagicMock:
    api = MagicMock()
    pod_list = MagicMock()
    pod_list.items = pods or []
    api.list_pod_for_all_namespaces.return_value = pod_list
    ns_list = MagicMock()
    ns_list.items = namespaces or []
    api.list_namespace.return_value = ns_list
    return api


class TestVanillaAdapterNamespaceWastePort:
    def test_implements_namespace_waste_analysis_port(self) -> None:
        from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort

        adapter = VanillaAdapter("test-cluster")
        assert isinstance(adapter, NamespaceWasteAnalysisPort)

    def test_returns_raw_data_for_each_namespace(self) -> None:
        pods = [_fake_pod("dev"), _fake_pod("prod")]
        ns_objs = [_fake_namespace_obj("dev"), _fake_namespace_obj("prod")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        namespaces = {r["namespace"] for r in result}
        assert "dev" in namespaces
        assert "prod" in namespaces

    def test_cpu_request_parsed_from_millicores(self) -> None:
        pods = [_fake_pod("dev", cpu_request="500m", mem_request=None)]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["cpu_requested_cores"] == pytest.approx(0.5, abs=0.001)

    def test_memory_request_parsed_from_gi(self) -> None:
        pods = [_fake_pod("dev", cpu_request=None, mem_request="2Gi")]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["memory_requested_gb"] == pytest.approx(2.0, abs=0.001)

    def test_namespace_age_hours_set(self) -> None:
        pods = [_fake_pod("dev")]
        ns_objs = [_fake_namespace_obj("dev", age_hours=12.0)]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["age_hours"] == pytest.approx(12.0, abs=0.1)

    def test_has_resource_requests_true_when_pods_have_requests(self) -> None:
        pods = [_fake_pod("dev", cpu_request="100m")]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["has_resource_requests"] is True

    def test_cpu_actual_none_when_no_prometheus_url(self) -> None:
        pods = [_fake_pod("dev")]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api, prometheus_url="")

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["cpu_actual_avg_cores"] is None
        assert dev["memory_actual_avg_gb"] is None

    def test_prometheus_usage_returned_when_configured(self) -> None:
        pods = [_fake_pod("dev")]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api, prometheus_url="http://prometheus:9090")

        prometheus_response = {
            "status": "success",
            "data": {
                "resultType": "vector",
                "result": [
                    {"metric": {"namespace": "dev"}, "value": [1700000000, "0.45"]},
                ],
            },
        }

        with patch("httpx.get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.json.return_value = prometheus_response
            mock_resp.raise_for_status.return_value = None
            mock_get.return_value = mock_resp
            result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["cpu_actual_avg_cores"] == pytest.approx(0.45, abs=0.001)

    def test_raises_prometheus_unavailable_on_http_error(self) -> None:
        import httpx
        from hexawyn.domain.errors import PrometheusUnavailableError

        pods = [_fake_pod("dev")]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api, prometheus_url="http://prometheus:9090")

        with patch("httpx.get", side_effect=httpx.HTTPError("unreachable")):
            with pytest.raises(PrometheusUnavailableError):
                adapter.get_all_namespace_waste_data(window_days=7)

    def test_raises_cluster_unreachable_when_k8s_fails(self) -> None:
        api = MagicMock()
        api.list_namespace.side_effect = Exception("connection refused")
        adapter = VanillaAdapter("test-cluster", api=api)

        with pytest.raises(ClusterUnreachableError):
            adapter.get_all_namespace_waste_data(window_days=7)

    def test_aggregates_requests_across_multiple_pods_in_same_namespace(self) -> None:
        pods = [
            _fake_pod("dev", cpu_request="500m", mem_request=None),
            _fake_pod("dev", cpu_request="250m", mem_request=None),
        ]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["cpu_requested_cores"] == pytest.approx(0.75, abs=0.001)

    def test_namespace_without_metadata_is_skipped(self) -> None:
        ns_no_meta = MagicMock()
        ns_no_meta.metadata = None
        ns_with_meta = _fake_namespace_obj("dev")
        api = _fake_core_api(pods=[], namespaces=[ns_no_meta, ns_with_meta])
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        namespaces = {r["namespace"] for r in result}
        assert "dev" in namespaces

    def test_pod_without_namespace_is_skipped(self) -> None:
        pod = MagicMock()
        pod.metadata = None
        ns_obj = _fake_namespace_obj("dev")
        api = _fake_core_api(pods=[pod], namespaces=[ns_obj])
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next((r for r in result if r["namespace"] == "dev"), None)
        assert dev is not None
        assert dev["cpu_requested_cores"] is None

    def test_raises_cluster_unreachable_when_pod_list_fails(self) -> None:
        api = MagicMock()
        api.list_namespace.return_value = MagicMock(items=[_fake_namespace_obj("dev")])
        api.list_pod_for_all_namespaces.side_effect = Exception("forbidden")
        adapter = VanillaAdapter("test-cluster", api=api)

        with pytest.raises(ClusterUnreachableError):
            adapter.get_all_namespace_waste_data(window_days=7)

    def test_raises_prometheus_unavailable_on_generic_exception(self) -> None:
        from hexawyn.domain.errors import PrometheusUnavailableError

        pods = [_fake_pod("dev")]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api, prometheus_url="http://prometheus:9090")

        with patch("httpx.get", side_effect=RuntimeError("unexpected error")):
            with pytest.raises(PrometheusUnavailableError):
                adapter.get_all_namespace_waste_data(window_days=7)

    def test_cpu_request_parsed_as_whole_cores(self) -> None:
        pods = [_fake_pod("dev", cpu_request="2", mem_request=None)]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["cpu_requested_cores"] == pytest.approx(2.0, abs=0.001)

    def test_memory_request_parsed_from_mi(self) -> None:
        pods = [_fake_pod("dev", cpu_request=None, mem_request="512Mi")]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["memory_requested_gb"] == pytest.approx(0.5, abs=0.001)

    def test_memory_request_parsed_from_ki(self) -> None:
        pods = [_fake_pod("dev", cpu_request=None, mem_request="1048576Ki")]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=pods, namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["memory_requested_gb"] == pytest.approx(1.0, abs=0.01)

    def test_container_without_resources_contributes_no_request(self) -> None:
        pod = MagicMock()
        pod.metadata.namespace = "dev"
        container = MagicMock()
        container.resources = None
        pod.spec.containers = [container]
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=[pod], namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["cpu_requested_cores"] is None
        assert dev["has_resource_requests"] is False

    def test_pod_without_spec_contributes_no_containers(self) -> None:
        pod = MagicMock()
        pod.metadata.namespace = "dev"
        pod.spec = None
        ns_objs = [_fake_namespace_obj("dev")]
        api = _fake_core_api(pods=[pod], namespaces=ns_objs)
        adapter = VanillaAdapter("test-cluster", api=api)

        result = adapter.get_all_namespace_waste_data(window_days=7)

        dev = next(r for r in result if r["namespace"] == "dev")
        assert dev["cpu_requested_cores"] is None


class TestContainerRequest:
    def _call(self, container: object, resource: str) -> object:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import _container_request

        return _container_request(container, resource)

    def test_unknown_resource_returns_none(self) -> None:
        container = MagicMock()
        container.resources.requests = {"disk": "10Gi"}
        assert self._call(container, "disk") is None


class TestParseMemory:
    def _call(self, value: str) -> float:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import _parse_memory

        return _parse_memory(value)

    def test_raw_bytes_no_suffix(self) -> None:
        result = self._call("1073741824")
        assert result == pytest.approx(1.0, abs=0.001)


class TestParsePrometheusVector:
    def _call(self, payload: object) -> dict[str, float]:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
            _parse_prometheus_vector,
        )

        return _parse_prometheus_vector(payload)  # type: ignore[arg-type]

    def test_valid_payload_returns_namespace_values(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": {"namespace": "dev"}, "value": [0, "0.5"]},
                ]
            }
        }
        assert self._call(payload) == {"dev": 0.5}

    def test_non_dict_payload_returns_empty(self) -> None:
        assert self._call("not a dict") == {}

    def test_data_not_dict_returns_empty(self) -> None:
        assert self._call({"data": "bad"}) == {}

    def test_result_not_list_returns_empty(self) -> None:
        assert self._call({"data": {"result": "bad"}}) == {}

    def test_entry_not_dict_is_skipped(self) -> None:
        payload = {"data": {"result": ["not-a-dict"]}}
        assert self._call(payload) == {}

    def test_metric_not_dict_is_skipped(self) -> None:
        payload = {"data": {"result": [{"metric": "bad", "value": [0, "1.0"]}]}}
        assert self._call(payload) == {}

    def test_value_pair_not_list_is_skipped(self) -> None:
        payload = {"data": {"result": [{"metric": {"namespace": "dev"}, "value": "bad"}]}}
        assert self._call(payload) == {}

    def test_namespace_not_string_is_skipped(self) -> None:
        payload = {"data": {"result": [{"metric": {"namespace": 42}, "value": [0, "1.0"]}]}}
        assert self._call(payload) == {}

    def test_unparseable_value_is_skipped(self) -> None:
        payload = {"data": {"result": [{"metric": {"namespace": "dev"}, "value": [0, "NaN-bad"]}]}}
        assert self._call(payload) == {}


def _fake_deployment(
    name: str,
    namespace: str,
    cpu_request: str | None = "500m",
    mem_request: str | None = "1Gi",
    replicas: int = 1,
) -> MagicMock:
    dep = MagicMock()
    dep.metadata.name = name
    dep.metadata.namespace = namespace
    dep.spec.replicas = replicas
    container = MagicMock()
    requests: dict[str, str] = {}
    if cpu_request:
        requests["cpu"] = cpu_request
    if mem_request:
        requests["memory"] = mem_request
    container.resources.requests = requests or None
    dep.spec.template.spec.containers = [container]
    return dep


def _fake_pod_metric(
    name: str, namespace: str, cpu_nano: str = "400000000", mem_bytes: str = "2147483648"
) -> dict[str, object]:
    # Real K8s pod names: {deployment}-{rs-hash}-{pod-hash}
    # Using realistic format so workload extraction via rsplit("-", 2) works correctly
    return {
        "metadata": {"name": f"{name}-7d6b8-x4m2p", "namespace": namespace},
        "containers": [{"usage": {"cpu": cpu_nano, "memory": mem_bytes}}],
    }


def _fake_apps_api(deployments: list[MagicMock]) -> MagicMock:
    api = MagicMock()
    dep_list = MagicMock()
    dep_list.items = deployments
    api.list_deployment_for_all_namespaces.return_value = dep_list
    sts_list = MagicMock()
    sts_list.items = []
    api.list_stateful_set_for_all_namespaces.return_value = sts_list
    return api


def _fake_metrics_api(pod_metrics: list[dict[str, object]]) -> MagicMock:
    api = MagicMock()
    api.list_cluster_custom_object.return_value = {"items": pod_metrics}
    return api


class TestVanillaAdapterRightsizingPort:
    def test_implements_rightsizing_port(self) -> None:
        from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort

        assert isinstance(VanillaAdapter("test"), RightsizingPort)

    def test_returns_workload_for_each_deployment(self) -> None:
        deps = [_fake_deployment("ml-worker", "production")]
        apps_api = _fake_apps_api(deps)
        metrics_api = _fake_metrics_api([_fake_pod_metric("ml-worker-abc", "production")])
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        names = {r["resource_name"] for r in result}
        assert "ml-worker" in names

    def test_cpu_requested_parsed_from_millicores(self) -> None:
        deps = [_fake_deployment("svc", "ns", cpu_request="2000m", mem_request=None)]
        apps_api = _fake_apps_api(deps)
        metrics_api = _fake_metrics_api([])
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["cpu_requested_cores"] == pytest.approx(2.0, abs=0.001)

    def test_memory_requested_parsed_from_gi(self) -> None:
        deps = [_fake_deployment("svc", "ns", cpu_request=None, mem_request="4Gi")]
        apps_api = _fake_apps_api(deps)
        metrics_api = _fake_metrics_api([])
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["memory_requested_mi"] == pytest.approx(4096.0, abs=1.0)

    def test_actual_cpu_from_metrics_server(self) -> None:
        deps = [_fake_deployment("ml-worker", "production")]
        apps_api = _fake_apps_api(deps)
        # 400m = 400 millicores = 0.4 cores (metrics-server format)
        metrics_api = _fake_metrics_api(
            [_fake_pod_metric("ml-worker", "production", cpu_nano="400m")]
        )
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["cpu_actual_cores"] == pytest.approx(0.4, abs=0.001)

    def test_actual_memory_from_metrics_server_in_mi(self) -> None:
        deps = [_fake_deployment("ml-worker", "production")]
        apps_api = _fake_apps_api(deps)
        # 1073741824 bytes = 1024 Mi; pod name = "ml-worker-7d6b8-x4m2p"
        metrics_api = _fake_metrics_api(
            [_fake_pod_metric("ml-worker", "production", mem_bytes="1073741824")]
        )
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["memory_actual_mi"] == pytest.approx(1024.0, abs=1.0)

    def test_no_metrics_when_metrics_server_unavailable(self) -> None:
        deps = [_fake_deployment("svc", "ns")]
        apps_api = _fake_apps_api(deps)
        metrics_api = _fake_metrics_api([])
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["cpu_actual_cores"] is None
        assert result[0]["memory_actual_mi"] is None

    def test_raises_cluster_unreachable_on_k8s_error(self) -> None:
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.side_effect = Exception("forbidden")
        adapter = VanillaAdapter("test", apps_api=apps_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.get_workload_rightsizing_data()

    def test_kind_is_deployment(self) -> None:
        deps = [_fake_deployment("svc", "ns")]
        apps_api = _fake_apps_api(deps)
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=_fake_metrics_api([]))

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["kind"] == "Deployment"

    def test_metrics_api_exception_returns_no_actuals(self) -> None:
        deps = [_fake_deployment("svc", "ns")]
        apps_api = _fake_apps_api(deps)
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.side_effect = Exception(
            "metrics-server not installed"
        )
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["cpu_actual_cores"] is None
        assert result[0]["memory_actual_mi"] is None

    def test_non_dict_item_in_metrics_response_is_skipped(self) -> None:
        deps = [_fake_deployment("svc", "ns")]
        apps_api = _fake_apps_api(deps)
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.return_value = {"items": ["not-a-dict", None]}
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["cpu_actual_cores"] is None

    def test_non_dict_metadata_in_metrics_item_is_skipped(self) -> None:
        deps = [_fake_deployment("svc", "ns")]
        apps_api = _fake_apps_api(deps)
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.return_value = {"items": [{"metadata": "bad"}]}
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["cpu_actual_cores"] is None

    def test_multiple_pods_same_workload_metrics_are_averaged(self) -> None:
        deps = [_fake_deployment("api", "ns")]
        apps_api = _fake_apps_api(deps)
        # Two pods for the same workload: 400m + 800m = 1200m → avg 600m = 0.6 cores
        pod1 = {
            "metadata": {"name": "api-7d6b8-pod11", "namespace": "ns"},
            "containers": [{"usage": {"cpu": "400m", "memory": "0"}}],
        }
        pod2 = {
            "metadata": {"name": "api-7d6b8-pod22", "namespace": "ns"},
            "containers": [{"usage": {"cpu": "800m", "memory": "0"}}],
        }
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.return_value = {"items": [pod1, pod2]}
        adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)

        result = adapter.get_workload_rightsizing_data()

        assert result[0]["cpu_actual_cores"] == pytest.approx(0.6, abs=0.001)

    def test_apps_api_client_loads_kubeconfig_when_no_injected_api(self) -> None:
        with (
            patch(
                "hexawyn.adapters.secondary.vanilla.vanilla_adapter.load_kubeconfig"
            ) as mock_load,
            patch(
                "hexawyn.adapters.secondary.vanilla.vanilla_adapter.client.AppsV1Api"
            ) as mock_apps,
        ):
            adapter = VanillaAdapter("test")
            adapter._apps_api_client()

        mock_load.assert_called_once()
        mock_apps.assert_called_once()

    def test_sum_container_metrics_non_list_returns_zero(self) -> None:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
            _sum_container_metrics,
        )

        assert _sum_container_metrics("not-a-list") == (0.0, 0.0)

    def test_sum_container_metrics_non_dict_container_skipped(self) -> None:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
            _sum_container_metrics,
        )

        result = _sum_container_metrics(["not-a-dict", None])

        assert result == (0.0, 0.0)

    def test_sum_container_metrics_non_dict_usage_skipped(self) -> None:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
            _sum_container_metrics,
        )

        result = _sum_container_metrics([{"usage": "bad"}])

        assert result == (0.0, 0.0)

    def test_parse_nanocores_with_n_suffix(self) -> None:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import _parse_nanocores

        assert _parse_nanocores("400000000n") == pytest.approx(0.4, abs=0.001)

    def test_parse_memory_to_mi_ki_suffix(self) -> None:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import _parse_memory_to_mi

        assert _parse_memory_to_mi("1048576Ki") == pytest.approx(1024.0, abs=0.1)

    def test_parse_memory_to_mi_gi_suffix(self) -> None:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import _parse_memory_to_mi

        assert _parse_memory_to_mi("2Gi") == pytest.approx(2048.0, abs=0.1)

    def test_workload_key_from_pod_name_two_parts_returns_prefix(self) -> None:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
            _workload_key_from_pod_name,
        )

        # Pod with only one dash (no RS hash): "svc-abcde"
        result = _workload_key_from_pod_name("svc-abcde", "ns")

        assert result == "ns/svc"

    def test_workload_key_from_pod_name_no_dash_returns_none(self) -> None:
        from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
            _workload_key_from_pod_name,
        )

        result = _workload_key_from_pod_name("nodash", "ns")

        assert result is None
